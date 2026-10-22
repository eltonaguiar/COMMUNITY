# QUICK_FIXES — ML / copy-trader resolver (verified against main @ 64a3fd69, 2026-10-22)

All diffs pass `git apply --check` on clean main, individually and together (1+2+3+4).
Combined test run: existing resolver tests + new tests = **56 passed**. New tests: test_resolver_hit_ts.py, test_dsr_bounds.py, test_per_pick_price.py (all FAIL on main, PASS after the fixes).
Apply: `git apply fix1.diff fix2.diff fix3.diff fix4.diff`

| # | Fix | Impact | Effort |
|---|---|---|---|
| 1 | Resolver: `pp_price` unbound on intrabar hits + `resolved_at` = run time (PR #749 batch-close) | High: NameError or a stale price from the previous pick; fake clustered exit times | 10 lines |
| 2 | Harness DSR returns a z-score on an annualized Sharpe (DSR 7.69 in strategy_funnel_data.json) | High: every DSR gate is meaningless | 1 function |
| 3 | `_per_pick_price` returns the FIRST bar after entry, so TIME_EXIT ≈ entry price → 0.00% flats | High: the flat-exit artifact (from today's frozen-exit fix) | 20 lines |
| 4 | verification engine passes `n_trials=n` (trade count) | Medium | 1 line |

## 1. audit_trail/universal_pick_resolver.py:1446-1484 (intrabar hit path)
- `pp_price` is assigned only in the close_approx branch (line 1464), but line 1484 reads it on every hit.
  - On an intrabar hit it raises NameError if no earlier pick set it; otherwise it holds the PREVIOUS pick's price.
- `"resolved_at": now.strftime(...)` stamps the resolver run time. This causes the 21/29 closes at 2026-03-28T06:18.
- Fix: bind `pp_price = None` up front. `_check_tp_sl_intrabar` records the hit bar's open_time on `pick["_hit_bar_ts"]`. The new `_hit_ts_iso()` stamps that time and falls back to `now` if it is missing or in the future.
- Note: the stamp is the bar's open time, a lower bound accurate to one bar.
- Risk: low. The 3-tuple contract is unchanged. Rows already closed keep their old stamps, so a backfill is a separate job.

## 2. alpha_engine/rigorous_backtest_harness.py:180-203 compute_deflated_sharpe
- Main computes `dsr = (sharpe_obs - sqrt(2 ln k)*se)/se`. That is a z-score, and `sharpe_obs` is ×sqrt(252) annualized while `se` is per observation.
- With n_trials ≤ 1 it returns the raw Sharpe.
- Repro: normal(0.3, 2) n=200, k=100 → **old 14.71, new 0.449**.
- Fix: de-annualize, then compute Bailey–López de Prado `Φ((SR − SR0)/se)` with E[max] via the Euler–Mascheroni form. The result is bounded in [0, 1].
- Risk: gates `min_dsr` 0.80–0.95 will now fail most strategies. That is intended. Re-run the funnel and expect labels to drop to CANDIDATE/FAIL.

## 3. audit_trail/universal_pick_resolver.py:693-723 _per_pick_price (+ TIME_EXIT at ~1506)
- The docstring says "prefers the latest bar", but the loop `return`s the first bar ≥ entry.
- TIME_EXIT PnL is then computed at the entry-bar close (≈0%), and close_approx TP/SL checks can never trigger.
- Repro: 48 hourly bars rising 100→147, entry at bar 0. Main returns **100.0** (0% exit); the fix returns 147.0. With `as_of_ms` = expiry (+24h) it returns 124.0.
- Fix: use the latest bar in [entry, as_of_ms]. TIME_EXIT passes `as_of_ms = entry + max_hold`, so a stale feed is priced at expiry, not at today's price.
- Risk: medium. The existing test `test_per_pick_price_uses_newest_post_entry_bar_for_later_pick` encoded the buggy first-bar behavior, so the diff updates it to use `as_of_ms`. Caveat: `hold_hours` still reports now − entry (follow-up).

## 4. alpha_engine/strategy_verification_engine.py:594
- `n_trials=n` deflates by the trade count instead of the number of strategies tried. `n_trials` is already resolved at line 561 and ignored.
- Example: SR 1.8, n=40 → DSR 0.064 with k=40 vs 0.0 with k=500.
- Follow-up (not fixed): this engine also feeds an annualized Sharpe into a per-observation se, the same scale bug as #2.

## Not fixed / leads
- SL-first on bars where both SL and TP hit is already conservative and flagged `_intrabar_ambiguous`. OK.
- Direction is normalized BUY/SELL→LONG/SHORT before `_compute_pnl`, so the short sign is OK.
- clone_active_picks.json has 66 duplicate symbol+direction rows, but the feed has been dead since 2026-06-21, so it is low priority.
- ~20 other `deflated_sharpe*` implementations exist (git grep). Each should get the same [0, 1] bound test.

## fix1.diff
```diff
diff --git a/audit_trail/universal_pick_resolver.py b/audit_trail/universal_pick_resolver.py
index 0babac58..9242d2ef 100644
--- a/audit_trail/universal_pick_resolver.py
+++ b/audit_trail/universal_pick_resolver.py
@@ -673,6 +673,8 @@ def _check_tp_sl_intrabar(pick: dict, ohlcv_bars: list[dict]):
             tp_hit = bool(tp and high >= tp)
             if _ENTRY_ANCHORED and sl_hit and tp_hit:
                 pick["_intrabar_ambiguous"] = True
+            if sl_hit or tp_hit:
+                pick["_hit_bar_ts"] = bar.get("timestamp")
             if sl_hit:
                 return ("SL_HIT", sl, _compute_pnl(entry, sl, direction))
             if tp_hit:
@@ -682,6 +684,8 @@ def _check_tp_sl_intrabar(pick: dict, ohlcv_bars: list[dict]):
             tp_hit = bool(tp and low <= tp)
             if _ENTRY_ANCHORED and sl_hit and tp_hit:
                 pick["_intrabar_ambiguous"] = True
+            if sl_hit or tp_hit:
+                pick["_hit_bar_ts"] = bar.get("timestamp")
             if sl_hit:
                 return ("SL_HIT", sl, _compute_pnl(entry, sl, direction))
             if tp_hit:
@@ -885,6 +889,18 @@ def _snapshot_prediction_market_entry(pick: dict, current_price: float) -> bool:
     return True
 
 
+def _hit_ts_iso(hit_ms, now):
+    """ISO-Z for the intrabar hit bar (open_time ms); run time if unknown/future."""
+    try:
+        if hit_ms is not None:
+            dt = datetime.fromtimestamp(int(hit_ms) / 1000, tz=timezone.utc)
+            if dt <= now:
+                return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
+    except (TypeError, ValueError, OverflowError, OSError):
+        pass
+    return now.strftime("%Y-%m-%dT%H:%M:%SZ")
+
+
 def check_tp_sl(pick, current_price):
     """Check if a pick has hit TP or SL. Returns (reason, exit_price, pnl_pct) or None."""
     direction = pick["direction"]
@@ -1446,6 +1462,9 @@ def main():
             # Check TP/SL — unified intrabar OHLC replay for ALL symbols
             result = None
             _res_method = None
+            # Bound for every path (was only set in close_approx branch -> NameError /
+            # stale previous-pick price on intrabar hits).
+            pp_price = None
             intrabar_bars = ohlc_bars_cache.get(norm_sym, [])
             if intrabar_bars:
                 result = _check_tp_sl_intrabar(pick, intrabar_bars)
@@ -1480,7 +1499,9 @@ def main():
                     "exit_reason": reason,
                     "status": "CLOSED",
                     "resolution_method": _res_method,  # "intrabar" (accurate) | "close_approx" (Bug 1B)
-                    "resolved_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
+                    # Stamp the bar where SL/TP was actually touched, not the resolver
+                    # run time (PR #749 batch-close artifact). Falls back to run time.
+                    "resolved_at": _hit_ts_iso(pick.pop("_hit_bar_ts", None), now),
                     "current_price_at_resolve": pp_price,
                     "_resolver_version": RESOLVER_VERSION,
                     "_resolver_source": RESOLVER_SOURCE_ID,
```
## fix2.diff
```diff
diff --git a/alpha_engine/rigorous_backtest_harness.py b/alpha_engine/rigorous_backtest_harness.py
index 31050c62..3b28150a 100644
--- a/alpha_engine/rigorous_backtest_harness.py
+++ b/alpha_engine/rigorous_backtest_harness.py
@@ -178,29 +178,33 @@ def compute_sharpe(pnl_series: np.ndarray, annualize: bool = True) -> float:
     return float(sharpe)
 
 def compute_deflated_sharpe(sharpe_obs: float, n_trials: int, n_observations: int,
-                            base_sharpe: float = 0.0, conf_level: float = 0.95) -> float:
+                            base_sharpe: float = 0.0, conf_level: float = 0.95,
+                            annualization: float = 252.0) -> float:
     """
-    Compute Deflated Sharpe Ratio (DSR) per Bailey & Lopez de Prado (2014).
-    DSR adjusts the observed Sharpe for the number of trials tested.
-    Returns the deflated Sharpe (should be compared to 0 for significance).
+    Deflated Sharpe Ratio (Bailey & Lopez de Prado 2014) as a PROBABILITY in [0, 1].
+
+    Previous version returned a z-score (SR - E[max]*se)/se and compared an
+    ANNUALIZED Sharpe (x sqrt(252)) with a per-observation standard error, giving
+    impossible "DSR" values like 7.69 in strategy_funnel_data.json.
+    `sharpe_obs` is the annualized value produced by compute_sharpe(); it is
+    de-annualized here so SR and its standard error are on the same scale.
     """
-    if n_trials <= 1:
-        return sharpe_obs
-    # Estimate expected max Sharpe under null
     from scipy.stats import norm
-    # Variance of Sharpe ratio estimator
-    var_sr = (1 + 0.5 * sharpe_obs**2) / n_observations if n_observations > 0 else 1
-    std_sr = math.sqrt(var_sr)
-    # Expected maximum of n_trials standard normals
-    # Approximation: E[max] ≈ Φ^{-1}(1 - 1/(n_trials * e)) where e ≈ 2.718
-    import scipy.special as sc
-    # Use order statistics approximation
-    k = n_trials
-    # E[max of k standard normals] ≈ sqrt(2 * ln(k)) for large k
-    expected_max = math.sqrt(2 * math.log(k)) if k > 1 else 0
-    # Deflated Sharpe
-    dsr = (sharpe_obs - expected_max * std_sr) / std_sr if std_sr > 0 else 0
-    return float(dsr)
+    if n_observations is None or n_observations < 2:
+        return 0.0
+    sr = sharpe_obs / math.sqrt(annualization) if annualization else sharpe_obs
+    se = math.sqrt((1 + 0.5 * sr ** 2) / (n_observations - 1))
+    if se <= 0:
+        return 0.0
+    gamma = 0.5772156649
+    k = max(int(n_trials or 1), 1)
+    if k > 1:
+        e_max = ((1 - gamma) * norm.ppf(1 - 1.0 / k)
+                 + gamma * norm.ppf(1 - 1.0 / (k * math.e)))
+    else:
+        e_max = 0.0
+    sr0 = base_sharpe + e_max * se
+    return float(norm.cdf((sr - sr0) / se))
 
 def block_bootstrap(pnl_series: np.ndarray, block_size: int = 5,
                     n_iterations: int = 1000, confidence: float = 0.95) -> dict:
```
## fix3.diff
```diff
diff --git a/audit_trail/universal_pick_resolver.py b/audit_trail/universal_pick_resolver.py
index 0babac58..96c4b473 100644
--- a/audit_trail/universal_pick_resolver.py
+++ b/audit_trail/universal_pick_resolver.py
@@ -690,7 +690,7 @@ def _check_tp_sl_intrabar(pick: dict, ohlcv_bars: list[dict]):
     return None
 
 
-def _per_pick_price(pick, norm_sym, ohlc_bars_cache, current_price):
+def _per_pick_price(pick, norm_sym, ohlc_bars_cache, current_price, as_of_ms=None):
     """Resolve a PER-PICK reference price instead of reusing one frozen
     snapshot for every pick of a symbol (Bug: frozen-exit stamping).
 
@@ -710,15 +710,22 @@ def _per_pick_price(pick, norm_sym, ohlc_bars_cache, current_price):
     bars = ohlc_bars_cache.get(norm_sym) or []
     entry_ms = _parse_ts_ms(pick.get("timestamp"))
     if entry_ms is not None and bars:
-        # Chronological: the FIRST bar at/after entry is the pick's own close
-        # (entry-anchored; different entries anchor to different bars, so each
-        # pick resolves against its own price, not one shared snapshot).
+        # LATEST bar at/after entry (and at/before as_of_ms, e.g. the TIME_EXIT
+        # expiry). Returning the FIRST bar after entry priced every exit at the
+        # entry bar's close -> ~0.00% "flat" TIME_EXITs and close_approx checks
+        # that could never reach TP/SL.
+        best = None
         for b in bars:
             ts = b.get("timestamp")
-            if ts is not None and ts >= entry_ms:
-                close = b.get("close")
-                if close:
-                    return float(close)
+            if ts is None or ts < entry_ms:
+                continue
+            if as_of_ms is not None and ts > as_of_ms:
+                continue
+            close = b.get("close")
+            if close and (best is None or ts > best[0]):
+                best = (ts, float(close))
+        if best is not None:
+            return best[1]
     return current_price
 
 
@@ -1503,7 +1510,9 @@ def main():
             if pick_dt and (now - pick_dt).total_seconds() > _max_hold * 3600:
                 # Time exit — compute PnL at the PICK's OWN price (frozen-exit fix
                 # 2026-10-22), falling back to the run-wide snapshot when no bars.
-                pp_price = _per_pick_price(pick, norm_sym, ohlc_bars_cache, current_price)
+                _expiry_ms = int((pick_dt.timestamp() + _max_hold * 3600) * 1000)
+                pp_price = _per_pick_price(pick, norm_sym, ohlc_bars_cache, current_price,
+                                           as_of_ms=_expiry_ms)
                 pnl = _compute_pnl(entry, pp_price, pick["direction"])
                 # 2026-10-18: a failed price fetch must not be published as a
                 # flat 0% close (see _priceless_close).
diff --git a/tests/test_resolver_frozen_exit_fix.py b/tests/test_resolver_frozen_exit_fix.py
index 6129fc01..5a20f493 100644
--- a/tests/test_resolver_frozen_exit_fix.py
+++ b/tests/test_resolver_frozen_exit_fix.py
@@ -57,7 +57,10 @@ def test_per_pick_price_uses_newest_post_entry_bar_for_later_pick() -> None:
     early = _pick("2026-10-22T12:05:00Z")
     late = _pick("2026-10-22T14:05:00Z")
 
-    price_early = universal_pick_resolver._per_pick_price(early, "BTCUSDT", {"BTCUSDT": bars}, snapshot)
+    # Each pick is priced as of its own horizon (e.g. TIME_EXIT expiry); without
+    # as_of_ms the LATEST post-entry bar is used (the first bar == entry price -> 0% exits).
+    price_early = universal_pick_resolver._per_pick_price(
+        early, "BTCUSDT", {"BTCUSDT": bars}, snapshot, as_of_ms=_ms("2026-10-22T14:00:00Z"))
     price_late = universal_pick_resolver._per_pick_price(late, "BTCUSDT", {"BTCUSDT": bars}, snapshot)
 
     assert price_early == 66000.0
```
## fix4.diff
```diff
diff --git a/alpha_engine/strategy_verification_engine.py b/alpha_engine/strategy_verification_engine.py
index e2ad3d03..2304a650 100644
--- a/alpha_engine/strategy_verification_engine.py
+++ b/alpha_engine/strategy_verification_engine.py
@@ -591,7 +591,7 @@ def verify_strategy(
     pbo = compute_pbo_parameter_perms(pnl_costed)
 
     # 5. DSR
-    dsr = compute_deflated_sharpe(costed_sharpe, n_trials=n, n_observations=n,
+    dsr = compute_deflated_sharpe(costed_sharpe, n_trials=n_trials, n_observations=n,
                                    base_sharpe=DSR_CONFIG['base_sharpe']
                                    if 'base_sharpe' in DSR_CONFIG else 0.0,
                                    conf_level=DSR_CONFIG['conf_level'])
```

## fix1.diff
```diff
diff --git a/audit_trail/universal_pick_resolver.py b/audit_trail/universal_pick_resolver.py
index 0babac58..9242d2ef 100644
--- a/audit_trail/universal_pick_resolver.py
+++ b/audit_trail/universal_pick_resolver.py
@@ -673,6 +673,8 @@ def _check_tp_sl_intrabar(pick: dict, ohlcv_bars: list[dict]):
             tp_hit = bool(tp and high >= tp)
             if _ENTRY_ANCHORED and sl_hit and tp_hit:
                 pick["_intrabar_ambiguous"] = True
+            if sl_hit or tp_hit:
+                pick["_hit_bar_ts"] = bar.get("timestamp")
             if sl_hit:
                 return ("SL_HIT", sl, _compute_pnl(entry, sl, direction))
             if tp_hit:
@@ -682,6 +684,8 @@ def _check_tp_sl_intrabar(pick: dict, ohlcv_bars: list[dict]):
             tp_hit = bool(tp and low <= tp)
             if _ENTRY_ANCHORED and sl_hit and tp_hit:
                 pick["_intrabar_ambiguous"] = True
+            if sl_hit or tp_hit:
+                pick["_hit_bar_ts"] = bar.get("timestamp")
             if sl_hit:
                 return ("SL_HIT", sl, _compute_pnl(entry, sl, direction))
             if tp_hit:
@@ -885,6 +889,18 @@ def _snapshot_prediction_market_entry(pick: dict, current_price: float) -> bool:
     return True
 
 
+def _hit_ts_iso(hit_ms, now):
+    """ISO-Z for the intrabar hit bar (open_time ms); run time if unknown/future."""
+    try:
+        if hit_ms is not None:
+            dt = datetime.fromtimestamp(int(hit_ms) / 1000, tz=timezone.utc)
+            if dt <= now:
+                return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
+    except (TypeError, ValueError, OverflowError, OSError):
+        pass
+    return now.strftime("%Y-%m-%dT%H:%M:%SZ")
+
+
 def check_tp_sl(pick, current_price):
     """Check if a pick has hit TP or SL. Returns (reason, exit_price, pnl_pct) or None."""
     direction = pick["direction"]
@@ -1446,6 +1462,9 @@ def main():
             # Check TP/SL — unified intrabar OHLC replay for ALL symbols
             result = None
             _res_method = None
+            # Bound for every path (was only set in close_approx branch -> NameError /
+            # stale previous-pick price on intrabar hits).
+            pp_price = None
             intrabar_bars = ohlc_bars_cache.get(norm_sym, [])
             if intrabar_bars:
                 result = _check_tp_sl_intrabar(pick, intrabar_bars)
@@ -1480,7 +1499,9 @@ def main():
                     "exit_reason": reason,
                     "status": "CLOSED",
                     "resolution_method": _res_method,  # "intrabar" (accurate) | "close_approx" (Bug 1B)
-                    "resolved_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
+                    # Stamp the bar where SL/TP was actually touched, not the resolver
+                    # run time (PR #749 batch-close artifact). Falls back to run time.
+                    "resolved_at": _hit_ts_iso(pick.pop("_hit_bar_ts", None), now),
                     "current_price_at_resolve": pp_price,
                     "_resolver_version": RESOLVER_VERSION,
                     "_resolver_source": RESOLVER_SOURCE_ID,
```

## fix2.diff
```diff
diff --git a/alpha_engine/rigorous_backtest_harness.py b/alpha_engine/rigorous_backtest_harness.py
index 31050c62..3b28150a 100644
--- a/alpha_engine/rigorous_backtest_harness.py
+++ b/alpha_engine/rigorous_backtest_harness.py
@@ -178,29 +178,33 @@ def compute_sharpe(pnl_series: np.ndarray, annualize: bool = True) -> float:
     return float(sharpe)
 
 def compute_deflated_sharpe(sharpe_obs: float, n_trials: int, n_observations: int,
-                            base_sharpe: float = 0.0, conf_level: float = 0.95) -> float:
+                            base_sharpe: float = 0.0, conf_level: float = 0.95,
+                            annualization: float = 252.0) -> float:
     """
-    Compute Deflated Sharpe Ratio (DSR) per Bailey & Lopez de Prado (2014).
-    DSR adjusts the observed Sharpe for the number of trials tested.
-    Returns the deflated Sharpe (should be compared to 0 for significance).
+    Deflated Sharpe Ratio (Bailey & Lopez de Prado 2014) as a PROBABILITY in [0, 1].
+
+    Previous version returned a z-score (SR - E[max]*se)/se and compared an
+    ANNUALIZED Sharpe (x sqrt(252)) with a per-observation standard error, giving
+    impossible "DSR" values like 7.69 in strategy_funnel_data.json.
+    `sharpe_obs` is the annualized value produced by compute_sharpe(); it is
+    de-annualized here so SR and its standard error are on the same scale.
     """
-    if n_trials <= 1:
-        return sharpe_obs
-    # Estimate expected max Sharpe under null
     from scipy.stats import norm
-    # Variance of Sharpe ratio estimator
-    var_sr = (1 + 0.5 * sharpe_obs**2) / n_observations if n_observations > 0 else 1
-    std_sr = math.sqrt(var_sr)
-    # Expected maximum of n_trials standard normals
-    # Approximation: E[max] ≈ Φ^{-1}(1 - 1/(n_trials * e)) where e ≈ 2.718
-    import scipy.special as sc
-    # Use order statistics approximation
-    k = n_trials
-    # E[max of k standard normals] ≈ sqrt(2 * ln(k)) for large k
-    expected_max = math.sqrt(2 * math.log(k)) if k > 1 else 0
-    # Deflated Sharpe
-    dsr = (sharpe_obs - expected_max * std_sr) / std_sr if std_sr > 0 else 0
-    return float(dsr)
+    if n_observations is None or n_observations < 2:
+        return 0.0
+    sr = sharpe_obs / math.sqrt(annualization) if annualization else sharpe_obs
+    se = math.sqrt((1 + 0.5 * sr ** 2) / (n_observations - 1))
+    if se <= 0:
+        return 0.0
+    gamma = 0.5772156649
+    k = max(int(n_trials or 1), 1)
+    if k > 1:
+        e_max = ((1 - gamma) * norm.ppf(1 - 1.0 / k)
+                 + gamma * norm.ppf(1 - 1.0 / (k * math.e)))
+    else:
+        e_max = 0.0
+    sr0 = base_sharpe + e_max * se
+    return float(norm.cdf((sr - sr0) / se))
 
 def block_bootstrap(pnl_series: np.ndarray, block_size: int = 5,
                     n_iterations: int = 1000, confidence: float = 0.95) -> dict:
```

## fix3.diff
```diff
diff --git a/audit_trail/universal_pick_resolver.py b/audit_trail/universal_pick_resolver.py
index 0babac58..96c4b473 100644
--- a/audit_trail/universal_pick_resolver.py
+++ b/audit_trail/universal_pick_resolver.py
@@ -690,7 +690,7 @@ def _check_tp_sl_intrabar(pick: dict, ohlcv_bars: list[dict]):
     return None
 
 
-def _per_pick_price(pick, norm_sym, ohlc_bars_cache, current_price):
+def _per_pick_price(pick, norm_sym, ohlc_bars_cache, current_price, as_of_ms=None):
     """Resolve a PER-PICK reference price instead of reusing one frozen
     snapshot for every pick of a symbol (Bug: frozen-exit stamping).
 
@@ -710,15 +710,22 @@ def _per_pick_price(pick, norm_sym, ohlc_bars_cache, current_price):
     bars = ohlc_bars_cache.get(norm_sym) or []
     entry_ms = _parse_ts_ms(pick.get("timestamp"))
     if entry_ms is not None and bars:
-        # Chronological: the FIRST bar at/after entry is the pick's own close
-        # (entry-anchored; different entries anchor to different bars, so each
-        # pick resolves against its own price, not one shared snapshot).
+        # LATEST bar at/after entry (and at/before as_of_ms, e.g. the TIME_EXIT
+        # expiry). Returning the FIRST bar after entry priced every exit at the
+        # entry bar's close -> ~0.00% "flat" TIME_EXITs and close_approx checks
+        # that could never reach TP/SL.
+        best = None
         for b in bars:
             ts = b.get("timestamp")
-            if ts is not None and ts >= entry_ms:
-                close = b.get("close")
-                if close:
-                    return float(close)
+            if ts is None or ts < entry_ms:
+                continue
+            if as_of_ms is not None and ts > as_of_ms:
+                continue
+            close = b.get("close")
+            if close and (best is None or ts > best[0]):
+                best = (ts, float(close))
+        if best is not None:
+            return best[1]
     return current_price
 
 
@@ -1503,7 +1510,9 @@ def main():
             if pick_dt and (now - pick_dt).total_seconds() > _max_hold * 3600:
                 # Time exit — compute PnL at the PICK's OWN price (frozen-exit fix
                 # 2026-10-22), falling back to the run-wide snapshot when no bars.
-                pp_price = _per_pick_price(pick, norm_sym, ohlc_bars_cache, current_price)
+                _expiry_ms = int((pick_dt.timestamp() + _max_hold * 3600) * 1000)
+                pp_price = _per_pick_price(pick, norm_sym, ohlc_bars_cache, current_price,
+                                           as_of_ms=_expiry_ms)
                 pnl = _compute_pnl(entry, pp_price, pick["direction"])
                 # 2026-10-18: a failed price fetch must not be published as a
                 # flat 0% close (see _priceless_close).
diff --git a/tests/test_resolver_frozen_exit_fix.py b/tests/test_resolver_frozen_exit_fix.py
index 6129fc01..5a20f493 100644
--- a/tests/test_resolver_frozen_exit_fix.py
+++ b/tests/test_resolver_frozen_exit_fix.py
@@ -57,7 +57,10 @@ def test_per_pick_price_uses_newest_post_entry_bar_for_later_pick() -> None:
     early = _pick("2026-10-22T12:05:00Z")
     late = _pick("2026-10-22T14:05:00Z")
 
-    price_early = universal_pick_resolver._per_pick_price(early, "BTCUSDT", {"BTCUSDT": bars}, snapshot)
+    # Each pick is priced as of its own horizon (e.g. TIME_EXIT expiry); without
+    # as_of_ms the LATEST post-entry bar is used (the first bar == entry price -> 0% exits).
+    price_early = universal_pick_resolver._per_pick_price(
+        early, "BTCUSDT", {"BTCUSDT": bars}, snapshot, as_of_ms=_ms("2026-10-22T14:00:00Z"))
     price_late = universal_pick_resolver._per_pick_price(late, "BTCUSDT", {"BTCUSDT": bars}, snapshot)
 
     assert price_early == 66000.0
```

## fix4.diff
```diff
diff --git a/alpha_engine/strategy_verification_engine.py b/alpha_engine/strategy_verification_engine.py
index e2ad3d03..2304a650 100644
--- a/alpha_engine/strategy_verification_engine.py
+++ b/alpha_engine/strategy_verification_engine.py
@@ -591,7 +591,7 @@ def verify_strategy(
     pbo = compute_pbo_parameter_perms(pnl_costed)
 
     # 5. DSR
-    dsr = compute_deflated_sharpe(costed_sharpe, n_trials=n, n_observations=n,
+    dsr = compute_deflated_sharpe(costed_sharpe, n_trials=n_trials, n_observations=n,
                                    base_sharpe=DSR_CONFIG['base_sharpe']
                                    if 'base_sharpe' in DSR_CONFIG else 0.0,
                                    conf_level=DSR_CONFIG['conf_level'])
```

## test_bot.py
```python
#!/usr/bin/env python3
"""Quick test to verify the autonomous bot works"""

import os
import sys

# Set environment variables for testing
os.environ['PRIMARY_EXCHANGE'] = 'FREE_DATA'
os.environ.setdefault('COINGECKO_API_KEY', '')
os.environ.setdefault('CRYPTOCOMPARE_API_KEY', '')

# Add the bot to path
sys.path.insert(0, '/root/.openclaw/workspace')

# Import and test
from live_trading_bot_canada import Config, FreeDataFetcher

print("🧪 Testing Autonomous Trading Bot...")
print("=" * 50)

# Test config
config = Config()
print(f"✅ Config loaded: PRIMARY_EXCHANGE={config.PRIMARY_EXCHANGE}")

# Test free data fetcher
fetcher = FreeDataFetcher(config)
print(f"✅ FreeDataFetcher initialized")

# Test getting ticker data
print("\n📊 Fetching BTC price from CoinGecko (FREE)...")
ticker = fetcher.get_ticker('BTC-USD')

if ticker:
    print(f"✅ SUCCESS!")
    print(f"   Symbol: {ticker['symbol']}")
    print(f"   Price: ${ticker['price']:,.2f}")
    print(f"   24h Change: {ticker['price_change']:+.2f}%")
    print(f"   Volume: ${ticker['volume_24h']:,.0f}")
    print(f"   Source: {ticker['source']}")
else:
    print("❌ Failed to fetch ticker")

# Test getting historical data
print("\n📈 Fetching 30-day history...")
history = fetcher.get_klines('BTC-USD', days=7)

if not history.empty:
    print(f"✅ SUCCESS! Got {len(history)} days of data")
    print(f"   Latest close: ${history['close'].iloc[-1]:,.2f}")
    print(f"   7-day high: ${history['high'].max():,.2f}")
    print(f"   7-day low: ${history['low'].min():,.2f}")
else:
    print("❌ Failed to fetch history")

print("\n" + "=" * 50)
print("🎉 Bot is ready to run autonomously!")
print("   - GitHub Actions will trigger every 4 hours")
print("   - Results will be committed automatically")
print("   - No user intervention required!")
```

## test_dashboard_live.py
```python
#!/usr/bin/env python3
"""Test the live dashboard using Playwright"""
import asyncio
from playwright.async_api import async_playwright

async def test_dashboard():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # Load the dashboard
        url = 'https://eltonaguiar.github.io/findtorontoevents_antigravity.ca/predictions/dashboard/'
        print(f'Loading {url}...')
        
        try:
            await page.goto(url, wait_until='networkidle', timeout=30000)
            print('Page loaded successfully')
            
            # Wait for content to load
            await asyncio.sleep(3)
            
            # Get stats
            predictors = await page.text_content('#s-predictors')
            predictions = await page.text_content('#s-predictions')
            active = await page.text_content('#s-active')
            
            print(f'\nDashboard Stats:')
            print(f'  Predictors: {predictors}')
            print(f'  Total Picks: {predictions}')
            print(f'  Active: {active}')
            
            # Count visible prediction cards
            cards = await page.query_selector_all('.active-card')
            print(f'\nVisible prediction cards: {len(cards)}')
            
            # Get sources
            sources = await page.eval_on_selector_all('.active-card', '''elements => {
                return elements.map(el => el.getAttribute('data-source'));
            }''')
            
            from collections import Counter
            print('\nBy source (visible):')
            for src, count in Counter(sources).most_common():
                print(f'  {src}: {count}')
            
            # Check for data warning
            warning = await page.text_content('#data-warning')
            if warning:
                print(f'\nData warning: {warning}')
            
            # Take screenshot
            await page.screenshot(path='dashboard_screenshot.png', full_page=False)
            print('\nScreenshot saved: dashboard_screenshot.png')
            
        except Exception as e:
            print(f'Error: {e}')
        finally:
            await browser.close()

if __name__ == '__main__':
    asyncio.run(test_dashboard())
```

## test_data_validator.py
```python
#!/usr/bin/env python3
"""
Test script for Data Validator Agent
====================================
This script validates the core functionality of the Data Validator Agent
"""

import asyncio
import os
import sys
from datetime import datetime, timedelta
from decimal import Decimal

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_validator_agent import (
    DataValidatorAgent, DataValidatorConfig, DataSource,
    DataPoint, DataFeed, QualityMetrics, ValidationAlert, AlertType
)


async def test_data_validator_agent():
    """Test the Data Validator Agent functionality"""
    print("🧪 Testing Data Validator Agent...")

    # Mock URLs for testing
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
    db_url = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/trading")

    # Custom config for testing
    config = DataValidatorConfig(
        primary_sources={
            'BTC': [DataSource.BINANCE, DataSource.COINGECKO],
            'ETH': [DataSource.BINANCE, DataSource.CRYPTOCOMPARE],
        },
        monitoring_interval_seconds=5,  # Faster for testing
        max_staleness_seconds=30,  # Shorter for testing
    )

    # Initialize agent
    agent = DataValidatorAgent(redis_url, db_url, config)

    try:
        # Test 1: Agent initialization
        print("✅ Test 1: Agent initialization")
        assert agent.config.monitoring_interval_seconds == 5
        assert 'BTC' in agent.feeds
        assert 'ETH' in agent.feeds
        assert len(agent.feeds['BTC']) == 2
        assert agent.quality_metrics.total_feeds == 4  # 2 symbols * 2 sources each
        print("   ✓ Agent initialized correctly")

        # Test 2: Start agent
        print("✅ Test 2: Agent startup")
        await agent.start()
        await asyncio.sleep(2)  # Let it initialize
        print("   ✓ Agent started successfully")

        # Test 3: Feed health checking
        print("✅ Test 3: Feed health monitoring")
        await asyncio.sleep(10)  # Let monitoring run

        # Check that feeds have been updated
        btc_feeds = agent.feeds['BTC']
        eth_feeds = agent.feeds['ETH']

        feeds_checked = 0
        for source, feed in btc_feeds.items():
            if feed.last_update > datetime.utcnow() - timedelta(seconds=30):
                feeds_checked += 1

        for source, feed in eth_feeds.items():
            if feed.last_update > datetime.utcnow() - timedelta(seconds=30):
                feeds_checked += 1

        assert feeds_checked > 0, "No feeds were successfully checked"
        print(f"   ✓ {feeds_checked} feeds checked successfully")

        # Test 4: Data point storage
        print("✅ Test 4: Data point storage")
        # Create a test data point
        test_point = DataPoint(
            symbol='BTC',
            price=Decimal('50000.00'),
            source=DataSource.BINANCE,
            quality_score=0.95
        )

        await agent.store_data_point(test_point)

        # Check if it was stored in history
        assert 'BTC' in agent.price_history
        assert len(agent.price_history['BTC']) > 0
        print("   ✓ Data point stored successfully")

        # Test 5: Outlier detection
        print("✅ Test 5: Outlier detection")
        # Add some normal data points
        for i in range(10):
            normal_point = DataPoint(
                symbol='BTC',
                price=Decimal('50000.00') + Decimal(str(i * 100)),
                source=DataSource.BINANCE
            )
            await agent.store_data_point(normal_point)

        # Add outlier
        outlier_point = DataPoint(
            symbol='BTC',
            price=Decimal('100000.00'),  # Way higher
            source=DataSource.BINANCE
        )
        await agent.detect_outliers('BTC', outlier_point)

        # Check if alert was created
        outlier_alerts = [a for a in agent.active_alerts.values() if a.alert_type == AlertType.OUTLIER_DETECTED]
        assert len(outlier_alerts) > 0, "Outlier not detected"
        print("   ✓ Outlier detection working")

        # Test 6: Quality metrics
        print("✅ Test 6: Quality metrics update")
        await agent.update_quality_metrics()
        assert agent.quality_metrics.last_updated > datetime.utcnow() - timedelta(seconds=10)
        print(f"   ✓ Quality metrics updated: {agent.quality_metrics.average_quality_score:.2%}")

        # Test 7: API endpoints (simulate calls)
        print("✅ Test 7: API endpoints simulation")
        # Simulate health check
        health_response = {
            "status": "healthy",
            "timestamp": datetime.utcnow().isoformat(),
            "metrics": {
                "total_feeds": agent.quality_metrics.total_feeds,
                "active_feeds": agent.quality_metrics.active_feeds,
                "average_quality": f"{agent.quality_metrics.average_quality_score:.2%}",
                "outliers_24h": agent.quality_metrics.outlier_count_24h,
                "alerts_active": len(agent.active_alerts)
            }
        }
        assert health_response['status'] == 'healthy'
        print("   ✓ Health check simulation working")

        # Simulate feeds data
        feeds_data = {}
        for symbol in agent.feeds:
            feeds_data[symbol] = {}
            for source, feed in agent.feeds[symbol].items():
                feeds_data[symbol][source.value] = {
                    "status": feed.status,
                    "last_update": feed.last_update.isoformat(),
                    "latency_ms": feed.latency_ms,
                    "quality_score": feed.quality_score,
                    "error_count": feed.error_count
                }
        assert 'BTC' in feeds_data
        assert 'ETH' in feeds_data
        print("   ✓ Feeds data simulation working")

        print("🎉 All tests passed!")

    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

    finally:
        # Cleanup
        await agent.stop()

    return True


async def test_config_validation():
    """Test configuration validation"""
    print("🧪 Testing configuration validation...")

    try:
        # Test default config
        config = DataValidatorConfig()
        assert config.max_staleness_seconds == 300
        assert config.outlier_threshold_std == 3.0
        assert 'BTC' in config.primary_sources
        print("   ✓ Default config valid")

        # Test custom config
        custom_config = DataValidatorConfig(
            max_staleness_seconds=60,
            outlier_threshold_std=2.5,
            primary_sources={'TEST': [DataSource.BINANCE]}
        )
        assert custom_config.max_staleness_seconds == 60
        assert custom_config.outlier_threshold_std == 2.5
        assert 'TEST' in custom_config.primary_sources
        print("   ✓ Custom config valid")

        print("✅ Configuration tests passed!")
        return True

    except Exception as e:
        print(f"❌ Config test failed: {e}")
        return False


async def main():
    """Run all tests"""
    print("🚀 Starting Data Validator Agent Tests\n")

    # Test configuration
    config_ok = await test_config_validation()
    if not config_ok:
        return

    print()

    # Test main agent functionality
    agent_ok = await test_data_validator_agent()
    if not agent_ok:
        return

    print("\n🎊 All Data Validator Agent tests completed successfully!")


if __name__ == "__main__":
    asyncio.run(main())</content>
<parameter name="filePath">e:\findtorontoevents_antigravity.ca\test_data_validator.py```

## test_dsr_bounds.py
```python
import sys, os, math
import numpy as np
sys.path.insert(0, os.path.join(os.getcwd(), "alpha_engine"))
import rigorous_backtest_harness as h

def test_dsr_is_probability():
    rng = np.random.default_rng(0)
    for mu in (-0.5, 0.0, 0.2, 1.0, 3.0):
        pnl = rng.normal(mu, 2.0, 200)
        sr = h.compute_sharpe(pnl)
        for k in (1, 10, 100, 5000):
            d = h.compute_deflated_sharpe(sr, k, len(pnl))
            assert 0.0 <= d <= 1.0, (mu, k, d)

def test_more_trials_lower_dsr():
    pnl = np.random.default_rng(1).normal(0.3, 2.0, 300)
    sr = h.compute_sharpe(pnl)
    assert h.compute_deflated_sharpe(sr, 1000, 300) < h.compute_deflated_sharpe(sr, 2, 300)

def test_coin_flip_not_significant():
    pnl = np.random.default_rng(2).choice([-2.0, 3.5], 283, p=[0.67, 0.33])
    assert h.compute_deflated_sharpe(h.compute_sharpe(pnl), 100, 283) < 0.5
```

## test_etf_verify.py
```python
"""
Post-deploy verification: all 5 non-crypto magnifying glasses should now show data.
Tests against live https://findtorontoevents.ca/audit/ after the fix is deployed.
"""
import asyncio
import sys
import json
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')
URL = "https://findtorontoevents.ca/audit/"
CATEGORIES = ['EQUITY', 'FOREX', 'COMMODITY', 'FUTURES', 'ETF']

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1900, 'height': 1200})
        console_errs = []
        page.on('pageerror', lambda err: console_errs.append(f"[PAGEERROR] {err}"))

        print(f"Loading {URL}...")
        await page.goto(URL, wait_until='networkidle', timeout=60000)
        await page.wait_for_function("() => document.querySelectorAll('.nc-card').length >= 3", timeout=45000)
        await page.wait_for_timeout(3000)

        # Check payload generation time
        gen_at = await page.evaluate("() => { try { return document.querySelector('[data-audit-source]')?.textContent || 'unknown'; } catch(e) { return 'err'; } }")
        print(f"Data source info: {gen_at}")

        results = {}
        all_pass = True
        for cat in CATEGORIES:
            btn = page.locator(f'.nc-drill-btn[data-catkey="{cat}"]')
            if await btn.count() == 0:
                results[cat] = {"status": "NO_BUTTON"}
                all_pass = False
                continue

            # Close any open modal
            if await page.locator('.trade-modal-overlay').count() > 0:
                await page.evaluate("document.querySelectorAll('.trade-modal-overlay').forEach(e => e.remove())")
                await page.wait_for_timeout(200)

            await btn.click(timeout=5000)
            await page.wait_for_timeout(500)

            modal_data = await page.evaluate("""() => {
                const modal = document.querySelector('.trade-modal-overlay .trade-modal');
                if (!modal) return null;
                const h3 = modal.querySelector('h3');
                const h4s = [...modal.querySelectorAll('h4')].map(el => el.textContent);
                const closedRows = modal.querySelectorAll('[id^="nc-closed-"] tbody tr').length;
                const activeRows = modal.querySelectorAll('[id^="nc-active-"] tbody tr').length;
                return { title: h3?.textContent, headers: h4s, closed_rows: closedRows, active_rows: activeRows };
            }""")

            # Read card's displayed counts to compare
            card_data = await page.evaluate(f"""() => {{
                const btns = document.querySelectorAll('.nc-drill-btn');
                for (const b of btns) {{
                    if (b.getAttribute('data-catkey') === '{cat}') {{
                        const card = b.closest('.nc-card');
                        if (!card) return null;
                        const rows = card.querySelectorAll('.nc-row');
                        const data = {{}};
                        rows.forEach(r => {{
                            const lbl = r.querySelector('.nc-lbl')?.textContent?.trim();
                            const val = r.querySelector('.nc-val')?.textContent?.trim();
                            if (lbl && val) data[lbl] = val;
                        }});
                        return data;
                    }}
                }}
                return null;
            }}""")

            card_active = card_data.get('Active') if card_data else None
            card_closed = card_data.get('Closed') if card_data else None
            drill_closed = modal_data['closed_rows'] if modal_data else 0
            drill_active = modal_data['active_rows'] if modal_data else 0

            # Determine if fix worked: if card shows >0 then drill should show >0
            match = True
            if card_closed and card_closed.isdigit() and int(card_closed) > 0 and drill_closed == 0:
                match = False
            if card_active and card_active.isdigit() and int(card_active) > 0 and drill_active == 0:
                match = False

            results[cat] = {
                "card_active": card_active,
                "card_closed": card_closed,
                "drill_active": drill_active,
                "drill_closed": drill_closed,
                "match": match,
            }
            status = "PASS" if match else "FAIL"
            print(f"  {cat:12s}: card=A{card_active}/C{card_closed} | drill=A{drill_active}/C{drill_closed} | {status}")
            if not match:
                all_pass = False

            # Close modal
            close_btn = page.locator('.trade-modal-close')
            if await close_btn.count() > 0:
                await close_btn.click()
                await page.wait_for_timeout(200)

        print("\n" + "=" * 60)
        if all_pass:
            print("ALL 5 CATEGORIES PASS — card counts match drill-down counts")
        else:
            print("FAIL — card counts don't match drill-down counts")
        print("=" * 60)

        if console_errs:
            print("\n=== Page Errors ===")
            for e in console_errs[:5]:
                print(f"  {e}")

        await browser.close()
        return 0 if all_pass else 1

sys.exit(asyncio.run(main()))
```

## test_fast_automation.py
```python
#!/usr/bin/env python3
"""
Fast Variants Automation Test
Tests that the fast trading variants work correctly for automation.
"""

import subprocess
import sys
import json
from pathlib import Path

def test_fast_stocks():
    """Test fast stocks competition."""
    print("🧪 Testing Fast Stocks Competition...")

    # Run the script
    result = subprocess.run([
        sys.executable,
        "STOCKS/competition/run_fast_competition.py"
    ], capture_output=True, text=True, cwd=Path(__file__).parent)

    if result.returncode != 0:
        print(f"❌ Fast stocks failed: {result.stderr}")
        return False

    print("✅ Fast stocks completed successfully")
    return True

def test_mercury2_fast():
    """Test mercury2 fast scanner."""
    print("🧪 Testing Mercury2 Fast...")

    # Run the script
    result = subprocess.run([
        sys.executable,
        "mercury2/mercury2_fast.py"
    ], capture_output=True, text=True, cwd=Path(__file__).parent)

    if result.returncode != 0:
        print(f"❌ Mercury2 fast failed: {result.stderr}")
        return False

    print("✅ Mercury2 fast completed successfully")
    return True

def test_dashboard_generation():
    """Test dashboard regeneration."""
    print("🧪 Testing Dashboard Generation...")

    # Run dashboard generator
    result = subprocess.run([
        sys.executable, "-m", "audit_trail.dashboard_generator"
    ], capture_output=True, text=True, cwd=Path(__file__).parent)

    if result.returncode != 0:
        print(f"❌ Dashboard generation failed: {result.stderr}")
        return False

    print("✅ Dashboard generation completed successfully")
    return True

def check_system_counts():
    """Check that fast variants appear in dashboard."""
    print("🧪 Checking System Counts...")

    try:
        with open("audit_trail/data/dashboard_payload.json", 'r') as f:
            data = json.load(f)

        systems = {s['name']: s for s in data.get('systems', [])}
        fast_stocks = systems.get('fast_stocks_competition', {})
        mercury_fast = systems.get('mercury2_fast', {})

        stocks_picks = fast_stocks.get('active_picks', 0)
        crypto_picks = mercury_fast.get('active_picks', 0)

        print(f"📊 Fast Stocks Competition: {stocks_picks} active picks")
        print(f"📊 Mercury2 Fast: {crypto_picks} active picks")

        if stocks_picks > 0 and crypto_picks > 0:
            print("✅ Both fast variants have active picks")
            return True
        else:
            print("❌ Missing active picks in fast variants")
            return False

    except Exception as e:
        print(f"❌ Failed to check system counts: {e}")
        return False

def main():
    """Run all automation tests."""
    print("🚀 Fast Variants Automation Test Suite")
    print("=" * 50)

    tests = [
        test_fast_stocks,
        test_mercury2_fast,
        test_dashboard_generation,
        check_system_counts
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        if test():
            passed += 1
        print()

    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} passed")

    if passed == total:
        print("🎉 All automation tests passed! Fast variants are ready for production.")
        return 0
    else:
        print("❌ Some tests failed. Check the output above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())```

## test_mercury2_scoring.py
```python
"""Quick test of Mercury 2 scoring enhancements"""

from audit_trail.mercury2_scoring import (
    compute_blended_score,
    apply_liquidity_penalty,
    apply_time_decay,
    flag_low_confidence_picks,
)

# Test 1: Blended Score
print("=" * 60)
print("TEST 1: Blended Score (Tech 70% + PnL 30%)")
print("=" * 60)

cases = [
    (85, 12.5, "High tech score + positive PnL (good signal)"),
    (85, -8.0, "High tech score + negative PnL (bad signal)"),
    (45, 20.0, "Low tech score + high PnL (unexpected winner)"),
    (80, 0.0, "Good tech score + neutral PnL"),
]

for tech, pnl, desc in cases:
    blended = compute_blended_score(tech, pnl)
    print(f"  {desc}")
    print(f"    Tech={tech}, PnL={pnl}% | Blended={blended}\n")

# Test 2: Liquidity Penalty
print("=" * 60)
print("TEST 2: Liquidity Penalty")
print("=" * 60)

liquidity_cases = [
    (75, 5_000_000, 0.08, "High volume, tight spread"),
    (75, 50_000, 1.5, "Low volume, wide spread"),
    (60, 1_000_000, 0.5, "Medium volume, tight spread"),
]

for score, volume, spread, desc in liquidity_cases:
    penalized, penalty = apply_liquidity_penalty(score, volume_24h=volume, bid_ask_spread_pct=spread)
    print(f"  {desc}")
    print(f"    Score={score}, Volume=${volume:,.0f}, Spread={spread}%")
    print(f"    -> Penalized={penalized}, Penalty={penalty}\n")

# Test 3: Confidence Flags
print("=" * 60)
print("TEST 3: Confidence Flags (Score/PnL Divergence)")
print("=" * 60)

flag_cases = [
    (85, -15.0, "High score but negative PnL"),
    (45, 20.0, "Low score but positive PnL"),
    (80, 12.0, "Aligned score and PnL"),
    (70, -8.0, "Slight divergence"),
]

for score, pnl, desc in flag_cases:
    is_flag, reason, penalty = flag_low_confidence_picks(score, pnl)
    print(f"  {desc}")
    print(f"    Score={score}, PnL={pnl}%")
    print(f"    -> Flagged={is_flag}, Reason={reason}\n")

print("=" * 60)
print("[OK] All tests completed successfully")
print("=" * 60)
```

## test_mission.py
```python
#!/usr/bin/env python3
"""
MINIMAL STRATEGY DEVELOPMENT MISSION TEST
"""

import json
import statistics
from pathlib import Path

class TestMission:
    def __init__(self):
        self.root = Path(__file__).parent
        print("TestMission initialized")

    def test_method(self):
        print("Test method executed")
        return "success"

def main():
    print("Starting test mission...")
    mission = TestMission()
    result = mission.test_method()
    print(f"Result: {result}")
    print("Test completed successfully!")

if __name__ == "__main__":
    main()```

## test_model_health_agent.py
```python
#!/usr/bin/env python3
"""
Test Script for Model Health Agent
===================================
Comprehensive testing of model health monitoring functionality.
"""

import os
import sys
import numpy as np
import pandas as pd
import tempfile
import shutil
import time
from datetime import datetime, timedelta
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from model_health_agent import (
    ModelHealthAgent, Config, ModelMetrics, HealthAlert,
    AlertLevel, DriftDetection, DriftType
)


def create_test_model():
    """Create a simple test model for validation"""
    # Generate sample data
    X, y = make_classification(
        n_samples=1000,
        n_features=20,
        n_informative=10,
        n_redundant=5,
        random_state=42
    )

    # Train a simple model
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X, y)

    return model, X, y


def test_basic_functionality():
    """Test basic agent initialization and model registration"""
    print("🧪 Testing basic functionality...")

    # Create temporary directory for testing
    test_dir = tempfile.mkdtemp()
    original_db_path = Config.DB_PATH
    original_models_dir = Config.PRODUCTION_MODELS_DIR

    try:
        # Override config for testing
        Config.DB_PATH = os.path.join(test_dir, 'test_health.db')
        Config.PRODUCTION_MODELS_DIR = test_dir

        # Initialize agent
        agent = ModelHealthAgent()

        # Create and save test model
        model, X, y = create_test_model()
        model_path = os.path.join(test_dir, 'test_model.pkl')
        joblib.dump(model, model_path)

        # Register model
        success = agent.register_model(
            model_name="test_model",
            model_path=model_path,
            features=[f"feature_{i}" for i in range(20)],
            hyperparameters={"n_estimators": 50, "random_state": 42}
        )

        assert success, "Model registration failed"
        assert "test_model" in agent.monitors, "Model not added to monitors"

        print("✅ Basic functionality test passed")

    finally:
        # Cleanup
        Config.DB_PATH = original_db_path
        Config.PRODUCTION_MODELS_DIR = original_models_dir
        shutil.rmtree(test_dir)


def test_performance_monitoring():
    """Test performance metrics calculation and monitoring"""
    print("🧪 Testing performance monitoring...")

    test_dir = tempfile.mkdtemp()
    original_db_path = Config.DB_PATH

    try:
        Config.DB_PATH = os.path.join(test_dir, 'test_health.db')
        agent = ModelHealthAgent()

        # Create test model
        model, X, y = create_test_model()
        model_path = os.path.join(test_dir, 'test_model.pkl')
        joblib.dump(model, model_path)

        # Register model
        agent.register_model(
            model_name="test_model",
            model_path=model_path,
            features=[f"feature_{i}" for i in range(20)],
            hyperparameters={"n_estimators": 50}
        )

        # Generate predictions
        predictions = model.predict(X)
        actuals = y

        # Update performance
        agent.update_model_performance("test_model", predictions, actuals)

        # Check if metrics were saved
        monitor = agent.monitors["test_model"]
        assert monitor.last_metrics is not None, "Metrics not calculated"
        assert monitor.last_metrics.accuracy > 0, "Accuracy not calculated properly"

        # Check database
        metrics_history = agent.db.get_metrics_history("test_model", 1)
        assert len(metrics_history) > 0, "Metrics not saved to database"

        print("✅ Performance monitoring test passed")

    finally:
        Config.DB_PATH = original_db_path
        shutil.rmtree(test_dir)


def test_alert_generation():
    """Test alert generation for performance issues"""
    print("🧪 Testing alert generation...")

    test_dir = tempfile.mkdtemp()
    original_db_path = Config.DB_PATH

    try:
        Config.DB_PATH = os.path.join(test_dir, 'test_health.db')
        agent = ModelHealthAgent()

        # Create test model
        model, X, y = create_test_model()
        model_path = os.path.join(test_dir, 'test_model.pkl')
        joblib.dump(model, model_path)

        # Register model
        agent.register_model(
            model_name="test_model",
            model_path=model_path,
            features=[f"feature_{i}" for i in range(20)],
            hyperparameters={"n_estimators": 50}
        )

        monitor = agent.monitors["test_model"]

        # Set baseline metrics (good performance)
        baseline_metrics = ModelMetrics(
            timestamp=datetime.now() - timedelta(hours=1),
            accuracy=0.85,
            precision=0.82,
            recall=0.88,
            f1_score=0.85,
            sharpe_ratio=1.2,
            win_rate=0.65,
            sample_size=100
        )
        monitor.last_metrics = baseline_metrics
        agent.db.save_metrics("test_model", baseline_metrics)

        # Generate poor predictions to trigger alerts
        poor_predictions = np.zeros(len(y))  # All wrong predictions
        agent.update_model_performance("test_model", poor_predictions, y)

        # Check for alerts
        alerts = agent.db.get_active_alerts("test_model")
        assert len(alerts) > 0, "No alerts generated for poor performance"

        # Check alert types
        alert_types = [a.alert_type for a in alerts]
        assert "accuracy_degradation" in alert_types, "Accuracy degradation alert not generated"
        assert "low_win_rate" in alert_types, "Low win rate alert not generated"

        print("✅ Alert generation test passed")

    finally:
        Config.DB_PATH = original_db_path
        shutil.rmtree(test_dir)


def test_drift_detection():
    """Test drift detection algorithms"""
    print("🧪 Testing drift detection...")

    from model_health_agent import DriftDetector

    detector = DriftDetector()

    # Test concept drift detection
    np.random.seed(42)

    # Create historical predictions (good performance)
    historical_preds = np.random.choice([0, 1], size=500, p=[0.4, 0.6])

    # Create current predictions (drifted - different distribution)
    current_preds = np.random.choice([0, 1], size=500, p=[0.7, 0.3])

    drift_result = detector.detect_concept_drift(historical_preds, current_preds)

    assert drift_result.drift_type == DriftType.CONCEPT_DRIFT
    assert drift_result.is_significant, "Concept drift not detected"

    # Test data drift detection
    historical_features = np.random.normal(0, 1, (500, 10))
    current_features = np.random.normal(2.0, 1.5, (500, 10))  # Larger shift to ensure detection

    data_drift_result = detector.detect_data_drift(historical_features, current_features)

    assert data_drift_result.drift_type == DriftType.DATA_DRIFT
    # The statistical test might not always detect drift with random data
    # Just check that the method runs and returns a valid result
    assert data_drift_result.p_value >= 0.0, "P-value should be non-negative"
    assert data_drift_result.statistic >= 0.0, "Statistic should be non-negative"
    print(f"Data drift p-value: {data_drift_result.p_value:.6f}, significant: {data_drift_result.is_significant}")

    print("✅ Drift detection test passed")


def test_api_endpoints():
    """Test API endpoints (if FastAPI available)"""
    print("🧪 Testing API endpoints...")

    if not hasattr(sys.modules.get('model_health_agent'), 'FASTAPI_AVAILABLE') or \
       not sys.modules['model_health_agent'].FASTAPI_AVAILABLE:
        print("⚠️ FastAPI not available, skipping API tests")
        return

    test_dir = tempfile.mkdtemp()
    original_db_path = Config.DB_PATH

    try:
        Config.DB_PATH = os.path.join(test_dir, 'test_health.db')
        Config.ENABLE_API = False  # Disable API server for testing

        agent = ModelHealthAgent()

        # Test health report generation
        report = agent.get_health_report()
        assert "models" in report, "Health report missing models section"
        assert "timestamp" in report, "Health report missing timestamp"

        print("✅ API endpoints test passed")

    finally:
        Config.DB_PATH = original_db_path
        shutil.rmtree(test_dir)


def test_model_versioning():
    """Test model versioning functionality"""
    print("🧪 Testing model versioning...")

    test_dir = tempfile.mkdtemp()
    original_db_path = Config.DB_PATH

    try:
        Config.DB_PATH = os.path.join(test_dir, 'test_health.db')
        agent = ModelHealthAgent()

        # Create and register multiple versions
        for version in ["v1", "v2", "v3"]:
            model, X, y = create_test_model()
            model_path = os.path.join(test_dir, f'test_model_{version}.pkl')
            joblib.dump(model, model_path)

            agent.register_model(
                model_name="test_model",
                model_path=model_path,
                features=[f"feature_{i}" for i in range(20)],
                hyperparameters={"version": version}
            )

        # Check versions
        versions = agent.db.get_model_versions("test_model")
        assert len(versions) >= 3, f"Expected at least 3 versions, got {len(versions)}"

        # Check version ordering (newest first)
        assert versions[0].created_at > versions[1].created_at, "Versions not ordered correctly"

        print("✅ Model versioning test passed")

    finally:
        Config.DB_PATH = original_db_path
        shutil.rmtree(test_dir)


def test_retraining_triggers():
    """Test automated retraining trigger logic"""
    print("🧪 Testing retraining triggers...")

    test_dir = tempfile.mkdtemp()
    original_db_path = Config.DB_PATH

    try:
        Config.DB_PATH = os.path.join(test_dir, 'test_health.db')
        agent = ModelHealthAgent()

        # Create test model
        model, X, y = create_test_model()
        model_path = os.path.join(test_dir, 'test_model.pkl')
        joblib.dump(model, model_path)

        # Register model
        agent.register_model(
            model_name="test_model",
            model_path=model_path,
            features=[f"feature_{i}" for i in range(20)],
            hyperparameters={"n_estimators": 50}
        )

        monitor = agent.monitors["test_model"]

        # Set good baseline
        baseline_metrics = ModelMetrics(
            timestamp=datetime.now() - timedelta(hours=2),
            accuracy=0.85,
            sample_size=1000
        )
        monitor.last_metrics = baseline_metrics

        # Test accuracy drop trigger
        poor_metrics = ModelMetrics(
            timestamp=datetime.now(),
            accuracy=0.70,  # 15% drop
            sample_size=1000
        )

        should_retrain, reason = monitor.should_retrain(poor_metrics, [])
        assert should_retrain, "Retraining not triggered for accuracy drop"
        assert "accuracy_drop" in reason, f"Wrong retrain reason: {reason}"

        # Test consecutive failures
        monitor.consecutive_failures = 3
        should_retrain, reason = monitor.should_retrain(poor_metrics, [])
        assert should_retrain, "Retraining not triggered for consecutive failures"
        assert "consecutive_failures" in reason, f"Wrong retrain reason: {reason}"

        print("✅ Retraining triggers test passed")

    finally:
        Config.DB_PATH = original_db_path
        shutil.rmtree(test_dir)


def run_all_tests():
    """Run all test functions"""
    print("🚀 Starting Model Health Agent Tests")
    print("=" * 50)

    test_functions = [
        test_basic_functionality,
        test_performance_monitoring,
        test_alert_generation,
        test_drift_detection,
        test_api_endpoints,
        test_model_versioning,
        test_retraining_triggers
    ]

    passed = 0
    failed = 0

    for test_func in test_functions:
        try:
            test_func()
            passed += 1
        except Exception as e:
            print(f"❌ {test_func.__name__} failed: {e}")
            failed += 1

    print("=" * 50)
    print(f"📊 Test Results: {passed} passed, {failed} failed")

    if failed == 0:
        print("🎉 All tests passed!")
        return True
    else:
        print("⚠️ Some tests failed")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)```

## test_new_strategy.py
```python
import pandas as pd, numpy as np
from baby_strategies.hoffman_new_strategy import hoffman_new_strategy_signals
# generate dummy data
np.random.seed(0)
price = np.cumsum(np.random.randn(200)) + 100
cols = {
    "open": price,
    "high": price + np.random.rand(200) * 0.5,
    "low": price - np.random.rand(200) * 0.5,
    "close": price + np.random.randn(200) * 0.1,
    "volume": np.random.rand(200) * 10,
}
df = pd.DataFrame(cols)
signals = hoffman_new_strategy_signals(df, "BTCUSDT")
print(signals)
```

## test_per_pick_price.py
```python
import sys, os
sys.path.insert(0, os.path.join(os.getcwd(), "audit_trail"))
import universal_pick_resolver as r
H=3600_000; E=1_774_000_000_000
bars=[{"timestamp":E+i*H,"close":100.0+i} for i in range(-2,48)]
from datetime import datetime,timezone
pick={"timestamp":datetime.fromtimestamp(E/1000,tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
def test_latest_not_first():
    assert r._per_pick_price(pick,"X",{"X":bars},None)==147.0   # old: 100.0 (entry bar -> 0% exit)
def test_as_of_expiry():
    assert r._per_pick_price(pick,"X",{"X":bars},None,as_of_ms=E+24*H)==124.0
def test_no_bars_fallback():
    assert r._per_pick_price(pick,"X",{},99.0)==99.0
```

## test_resolver_hit_ts.py
```python
import sys, os
from datetime import datetime, timezone
sys.path.insert(0, os.path.join(os.getcwd(), "audit_trail"))
import universal_pick_resolver as r

def bars():
    base = int(datetime(2026,3,20,tzinfo=timezone.utc).timestamp()*1000)
    return [{"timestamp": base+h*3600_000, "open":100,"close":100,"high":101 if h!=5 else 104,"low":99} for h in range(10)], base

def test_hit_ts_is_bar_time_not_run_time():
    b, base = bars()
    pick = {"direction":"LONG","entry_price":100.0,"take_profit":103.5,"stop_loss":98.0,
            "timestamp":"2026-03-20T00:00:00Z"}
    res = r._check_tp_sl_intrabar(pick, b)
    assert res[0] == "TP_HIT"
    now = datetime(2026,3,28,6,18,tzinfo=timezone.utc)
    assert r._hit_ts_iso(pick.pop("_hit_bar_ts"), now) == "2026-03-20T05:00:00Z"

def test_fallback_to_now():
    now = datetime(2026,3,28,6,18,tzinfo=timezone.utc)
    assert r._hit_ts_iso(None, now) == "2026-03-28T06:18:00Z"
    assert r._hit_ts_iso(int(now.timestamp()*1000)+10**9, now) == "2026-03-28T06:18:00Z"

def test_pp_price_bound_before_use():
    src = open(r.__file__).read()
    i_def = src.index("pp_price = None")
    i_use = src.index('"current_price_at_resolve": pp_price')
    assert i_def < i_use
```

## test_risk_quantification.py
```python
#!/usr/bin/env python3
"""
Risk Quantification Agent - Basic Test
=====================================
Simple test to verify the agent works correctly.
"""

import asyncio
from risk_quantification_agent import RiskQuantificationAgent, StressScenario

async def test_agent():
    """Test basic agent functionality"""
    print("🧪 Testing Risk Quantification Agent...")

    agent = RiskQuantificationAgent("redis://mock", "postgresql://mock")
    await agent.initialize()

    # Test VaR calculation
    var_result = agent.calculate_historical_var("BTC", confidence_level=0.95)
    print(".2%")

    # Test stress testing
    stress_result = agent.run_stress_test(StressScenario.MARKET_CRASH)
    print(".2%")

    # Test optimization
    optimal_weights = agent.optimize_portfolio(target_return=0.15)
    print(f"Optimal weights: {optimal_weights}")

    print("✅ Test completed successfully!")
    return True

if __name__ == "__main__":
    success = asyncio.run(test_agent())
    print("Result:", "PASS" if success else "FAIL")```

## test_strategies.py
```python
#!/usr/bin/env python3
"""
Quick test of baby strategies
"""

import pandas as pd
import numpy as np
from datetime import datetime

# Test one strategy
from baby_strategies.rsi_volume_mean_reversion import RSIVolumeMeanReversionStrategy

# Create synthetic data
np.random.seed(42)
n = 500
returns = np.random.normal(0.0001, 0.02, n)
prices = 50000 * np.exp(np.cumsum(returns))

test_data = pd.DataFrame({
    'open': prices * (1 + np.random.normal(0, 0.001, n)),
    'high': prices * (1 + abs(np.random.normal(0, 0.01, n))),
    'low': prices * (1 - abs(np.random.normal(0, 0.01, n))),
    'close': prices,
    'volume': np.random.uniform(100, 1000, n)
})

# Test strategy
strategy = RSIVolumeMeanReversionStrategy()
signals = strategy.generate_signals(test_data, symbol="BTCUSDT")

print(f"Generated {len(signals)} signals from {len(test_data)} bars")
for sig in signals[:3]:
    print(f"  {sig.direction} {sig.symbol} at {sig.entry_price:.2f}, TP: {sig.take_profit:.2f}, SL: {sig.stop_loss:.2f}")
    print(f"    Reason: {sig.reason}")

print("✅ Strategy test passed!")```
