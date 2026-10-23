import importlib.util
import json
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("capital_replay", HERE / "fund_capital_replay_20261023.py")
replay = importlib.util.module_from_spec(spec)
spec.loader.exec_module(replay)


@pytest.mark.parametrize("capital", replay.CAPITALS)
def test_budget_scaling(capital):
    result = replay.dollars(capital, 0.75)
    assert result["ending_usd"] == pytest.approx(capital * .75)
    assert result["profit_usd"] == pytest.approx(-capital * .25)


def test_reject_invalid_capital():
    with pytest.raises(ValueError):
        replay.dollars(0, 1)
    with pytest.raises(ValueError):
        replay.dollars(100, -1)


def test_saved_replay_contract_and_no_future_rank_effect():
    data = json.loads((HERE / "GHCOPILOT_20261023_FUND_CAPITAL_CASE_STUDY.json").read_text())
    assert len(data["annual_selections"]) == 66
    assert data["future_perturbation_checks_passed"] == 66
    assert data["prior_trial_metric_reproductions_passed"] == 9
    assert data["future_eligibility_changed_selected_top_three"] is False
    assert data["survivorship_bias"] is True
    assert data["currency"] == "USD"
    assert len(data["input_hashes"]) == 24
    for row in data["annual_selections"]:
        assert row["signal_date"] < row["entry_date"] < row["exit_date"]
        assert len(row["selected"]) == 3
        assert len(row["capital_examples"]) == 5
        for c in row["capital_examples"]:
            assert c["ending_usd"] == pytest.approx(
                c["initial_usd"] * (1 + row["net_return_pct"] / 100))
        if row["partial_final_period"]:
            assert row["exit_date"] == "2026-10-21"
        for fact in row["selection_facts"]:
            assert fact["observations"] >= 700


def test_fresh_account_starts_after_signal_and_losses_are_retained():
    data = json.loads((HERE / "GHCOPILOT_20261023_FUND_CAPITAL_CASE_STUDY.json").read_text())
    for row in data["summaries"]:
        assert row["entry_date"] == "2016-01-04"
        assert row["metrics"]["mdd_pct"] > 20
    crisis = [r for r in data["annual_selections"] if r["entry_date"].startswith("2008")]
    assert len(crisis) == 3
    assert all(r["net_return_pct"] < 0 for r in crisis)
    text = replay.render(data)
    assert "UNKNOWN" in text
    assert "not a Canadian-dollar purchase plan" in text
    assert "no prospective" in text
