import pytest

from peer_lag_review_20261023 import bucket, summarize


@pytest.mark.parametrize("hours,expected", [
    (0, "<=48h"), (48, "<=48h"), (48.001, "2-7d"), (168, "2-7d"),
    (168.001, "7-30d"), (720, "7-30d"), (720.001, ">30d"),
])
def test_boundaries(hours, expected):
    assert bucket(hours) == expected


def test_negative_interval_is_not_a_short_hold():
    with pytest.raises(ValueError):
        bucket(-.1)


def row(identifier, closed_at, pnl, start="2026-10-01T00:00:00Z"):
    return {"id": identifier, "timestamp": start, "closed_at": closed_at,
            "pnl_pct": pnl, "source_system": "test", "strategy": "test",
            "direction": "LONG", "trade_timeframe": "SWING", "exit_reason": "TP_HIT"}


def test_partition_and_no_loss_undefined():
    output = summarize([row("a", "2026-10-02T00:00:00Z", 1),
                        row("b", "2026-10-05T00:00:00Z", -2)])
    assert sum(v["records"] for v in output.values()) == 2
    assert output["<=48h"]["pf_published_pnl_only"] is None
    assert output["2-7d"]["pf_published_pnl_only"] == 0


def test_exclusion_removes_exact_batch_not_all_same_day_rows():
    a, b = "2026-10-02T00:00:00Z", "2026-10-02T00:01:00Z"
    output = summarize([row("a", a, 1), row("b", b, -2)], excluded_batch=a)
    assert output["<=48h"]["records"] == 1


def test_timezone_sensitivity_can_change_boundary():
    sample = row("a", "2026-10-02T19:30:00 EST", 1)
    assert summarize([sample])["2-7d"]["records"] == 1
    assert summarize([sample], est_as_daylight=True)["<=48h"]["records"] == 1
