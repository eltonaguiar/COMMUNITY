"""Bounded independent spot-vs-stored-path falsification; no mutations."""
import hashlib
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))
import pymysql
from tools.db_env import get_stocks_creds
from tools.ghcopilot_paper_monitor import market_bars, number, utc

OUT = Path(__file__).resolve().parent
now = datetime.now(timezone.utc)
args = get_stocks_creds()
args.update(cursorclass=pymysql.cursors.DictCursor, read_timeout=90)
connection = pymysql.connect(**args)
try:
    with connection.cursor() as cursor:
        cursor.execute("SET SESSION TRANSACTION READ ONLY")
        rows = []
        for strategy in ("adx_momentum", "triple_supertrend", "high_trust_momentum"):
            cursor.execute("""
                SELECT id,symbol,direction,entry_price,take_profit,stop_loss,
                  opened_at,intrabar_pnl_pct,intrabar_status,intrabar_horizon_bars,
                  strategy FROM at_signal_outcomes
                WHERE strategy=%s AND asset_class='CRYPTO'
                  AND opened_at BETWEEN UTC_TIMESTAMP()-INTERVAL 50 DAY
                                    AND UTC_TIMESTAMP()-INTERVAL 8 DAY
                  AND intrabar_status IN ('TP_HIT','SL_HIT','TIME_EXIT')
                  AND intrabar_ambiguous=0
                ORDER BY opened_at DESC,id LIMIT 4
            """, (strategy,))
            rows.extend(cursor.fetchall())
finally:
    connection.close()

results = []
for row in rows:
    result = {"strategy": row["strategy"], "symbol": row["symbol"],
              "id_hash": hashlib.sha256(str(row["id"]).encode()).hexdigest()[:20],
              "opened_at": utc(row["opened_at"]).isoformat(),
              "stored_status": row["intrabar_status"],
              "stored_pnl_pct": number(row["intrabar_pnl_pct"]),
              "direction": row["direction"],
              "entry": number(row["entry_price"]),
              "tp": number(row["take_profit"]), "sl": number(row["stop_loss"])}
    start = utc(row["opened_at"])
    hours = row["intrabar_horizon_bars"]
    if not hours or hours <= 0 or hours > 720:
        result["status"] = "UNVERIFIABLE_HORIZON"
        results.append(result)
        continue
    end = start + timedelta(hours=hours)
    try:
        bars = market_bars(row["symbol"], start, min(now, end + timedelta(hours=2)))
    except ValueError as exc:
        result.update(status="MARKET_DATA_UNAVAILABLE", error=str(exc))
        results.append(result)
        continue
    usable = [b for b in bars if utc(b["time"]) >= start and
              utc(b["time"]) + timedelta(hours=1) <= end]
    result["usable_completed_bars"] = len(usable)
    result["partial_entry_hour_excluded"] = start.minute != 0 or start.second != 0
    result["horizon_hours"] = hours
    result["hourly_gap"] = any(utc(b["time"]) - utc(a["time"]) != timedelta(hours=1)
                               for a, b in zip(usable, usable[1:]))
    result["status"] = "NO_TOUCH_IN_OBSERVED_COMPLETE_BARS"
    for bar in usable:
        long = row["direction"] == "LONG"
        stop = bar["low"] <= result["sl"] if long else bar["high"] >= result["sl"]
        target = bar["high"] >= result["tp"] if long else bar["low"] <= result["tp"]
        if stop or target:
            result["status"] = "BOTH_HIT_AMBIGUOUS" if stop and target else "SL_HIT" if stop else "TP_HIT"
            result["first_touch_bar"] = bar
            break
    result["caveat"] = "Yahoo USD spot vs USDT source; partial entry hour excluded; source observation/fill not authenticated. A witnessed difference requires venue-level adjudication, not automatic DB correction."
    results.append(result)
    print(row["strategy"], row["symbol"], result["stored_status"], result["status"])

doc = {"checked_at": now.isoformat(), "sampling": "Latest four available nonambiguous 50-to-8-day-old replay rows per named crypto candidate; no outcome-based sampling.",
       "results": results, "verdict": "Bounded falsification evidence only; not a full independent replay certificate."}
(OUT / "GHCOPILOT_TOP5_PRICE_CHECK_2026-10-22.json").write_text(
    json.dumps(doc, indent=2, allow_nan=False) + "\n")
print("Saved", len(results), "checks")
