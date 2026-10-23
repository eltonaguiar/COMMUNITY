import numpy as np
import pandas as pd
import pytest

from rrsp_vehicle_comparison_20261023 import calendar_return, price_metrics


def test_drawdown_includes_starting_capital():
    prices = pd.Series([100, 50] + [75] * 251, index=pd.bdate_range("2020-01-01", periods=253))
    result = price_metrics(prices)
    assert result["max_drawdown_pct"] == pytest.approx(50)
    assert result["ending_10000_local_currency"] == pytest.approx(7500)
    assert result["total_return_pct"] == pytest.approx(-25)


def test_constant_prices():
    prices = pd.Series(100.0, index=pd.bdate_range("2020-01-01", periods=253))
    result = price_metrics(prices)
    assert result["cagr_pct"] == 0
    assert result["max_drawdown_pct"] == 0
    assert result["annualized_volatility_pct"] == 0


@pytest.mark.parametrize("bad", [0, -1, np.nan, np.inf])
def test_invalid_price_fails_explicitly(bad):
    prices = pd.Series(100.0, index=pd.bdate_range("2020-01-01", periods=253))
    prices.iloc[15] = bad
    with pytest.raises(ValueError):
        price_metrics(prices)


def test_calendar_includes_new_year_boundary():
    prices = pd.Series([100, 90, 80], index=pd.to_datetime(["2021-12-31", "2022-01-03", "2022-12-30"]))
    assert calendar_return(prices, 2022) == pytest.approx(-20)


def test_calendar_requires_prior_close():
    prices = pd.Series([100], index=pd.to_datetime(["2022-01-03"]))
    with pytest.raises(ValueError):
        calendar_return(prices, 2022)


def test_scale_does_not_change_return_or_drawdown():
    prices = pd.Series(np.linspace(100, 200, 253), index=pd.bdate_range("2020-01-01", periods=253))
    assert price_metrics(prices)["cagr_pct"] == pytest.approx(price_metrics(prices * 50)["cagr_pct"])
    assert price_metrics(prices)["max_drawdown_pct"] == price_metrics(prices * 50)["max_drawdown_pct"]
