from datetime import timezone
import math

import pytest

from evaluate_live_snapshot_20261023 import clean, finite, stats, timestamp


def test_profit_factor_is_not_win_rate():
    rows = [
        {"id": str(i), "pnl_pct": pnl, "closed_at": "2026-10-23T00:00:00Z",
         "source_system": "test", "exit_reason": "TIME_EXIT"}
        for i, pnl in enumerate([1.0, 1.0, -4.0, 0.0])
    ]
    result = stats(rows)
    assert result["positive"] == 2
    assert result["negative"] == 1
    assert result["zero"] == 1
    assert result["pf_published_pnl_only"] == .5
    assert result["distinct_close_dates"] == 1
    assert result["net_cost_populated"] == 0


def test_no_losses_is_undefined_not_infinity():
    result = stats([])
    assert result["pf_published_pnl_only"] is None
    assert result["pf_undefined_no_losses"] is True


def test_explicit_fixed_est_not_silently_utc():
    assert timestamp("2026-10-22T04:31:50 EST").astimezone(timezone.utc).hour == 9
    assert timestamp("2026-10-22T04:31:50Z").hour == 4


def test_naive_timestamp_assumption_is_explicitly_utc():
    assert timestamp("2026-10-22T04:31:50").tzinfo == timezone.utc


def test_nonfinite_export_does_not_manufacture_zero():
    assert clean({"x": [math.nan, math.inf, 0.0]}) == {"x": [None, None, 0.0]}
    assert finite(True) is False
    assert finite(math.nan) is False


def test_unknown_date_format_is_not_silently_accepted():
    with pytest.raises(ValueError):
        timestamp("not a timestamp")
