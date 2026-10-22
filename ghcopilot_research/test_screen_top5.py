import importlib.util
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location(
    "candidate_screen", Path(__file__).with_name("screen_top5.py"))
screen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(screen)
NOW = datetime(2026, 10, 22, tzinfo=timezone.utc)


def row(**overrides):
    result = {
        "id": 1, "asset_class": "CRYPTO", "source_system": "test_source",
        "strategy": "test_strategy", "symbol": "BTCUSDT", "direction": "LONG",
        "entry_price": 100, "take_profit": 105, "stop_loss": 97,
        "opened_at": NOW - timedelta(days=10),
        "intrabar_resolved_at": NOW - timedelta(days=7),
        "intrabar_pnl_pct": 1, "intrabar_status": "TIME_EXIT",
        "intrabar_ambiguous": 0, "reverse_split_affected": 0,
    }
    result.update(overrides)
    return result


@pytest.mark.parametrize("changes,reason", [
    ({"intrabar_ambiguous": None}, "ambiguous_or_unknown_flag"),
    ({"intrabar_ambiguous": 1}, "ambiguous_or_unknown_flag"),
    ({"intrabar_pnl_pct": float("nan")}, "Nonfinite numeric value"),
    ({"intrabar_resolved_at": None}, "missing_replay_timestamp"),
    ({"intrabar_resolved_at": NOW - timedelta(days=11)}, "invalid_replay_chronology"),
    ({"intrabar_status": "OPEN"}, "no_resolved_replay"),
    ({"stop_loss": 101}, "Invalid geometry"),
    ({"reverse_split_affected": 1}, "reverse_split"),
])
def test_bad_evidence_is_excluded(changes, reason):
    report = screen.analyze(NOW, [row(**changes)], [])
    assert not report["all_groups"]
    assert report["exclusions"] == {"CRYPTO:" + reason: 1}


def test_time_exit_and_zero_are_not_discarded():
    report = screen.analyze(NOW, [row(intrabar_pnl_pct=0)], [])
    assert report["all_groups"][0]["net_mean_pct"] == -0.30
    assert report["all_groups"][0]["n"] == 1


def test_identity_dedup_and_class_shortfall():
    report = screen.analyze(NOW, [row(), row(id=2)], [])
    assert report["all_groups"][0]["n"] == 1
    assert report["exclusions"]["CRYPTO:duplicate_identity"] == 1
    assert report["classes"]["PENNY_STOCK"]["research_shortfall"] == 5


def test_policy_exclusion(monkeypatch):
    monkeypatch.setattr(screen, "FLAT", {"test_source"})
    assert screen.analyze(NOW, [row()], [])["exclusions"] == {
        "CRYPTO:policy_excluded": 1}
