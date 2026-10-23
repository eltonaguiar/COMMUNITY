from decimal import Decimal

import pytest

from fund_access_examples_20261023 import (
    annual_expense_illustration, whole_unit_reinvestment, whole_units,
)


@pytest.mark.parametrize("capital,fee,units,cash", [
    (1000, 0, 5, "47.90"), (1000, 9.95, 5, "37.95"),
    (2000, 0, 10, "95.80"), (2000, 9.95, 10, "85.85"),
])
def test_whole_unit_budget_conservation(capital, fee, units, cash):
    result = whole_units(capital, "190.42", fee)
    assert result["units"] == units
    assert result["cash"] == Decimal(cash)
    assert result["invested"] + result["cash"] + result["commission"] == capital


def test_cannot_charge_fee_for_unaffordable_order():
    assert whole_units(10, 20, 9.95) == {
        "units": 0, "invested": 0, "commission": 0, "cash": 10,
    }


def test_small_distribution_stays_cash_in_whole_unit_plan():
    result = whole_unit_reinvestment(5, ".41", "190.42")
    assert result["units"] == 0
    assert result["cash"] == Decimal("2.05")


def test_reinvestment_conserves_distribution_and_excess_cash():
    result = whole_unit_reinvestment(1000, ".41", "190.42")
    assert result["units"] == 2
    assert result["cash"] == Decimal("29.16")


def test_expense_rate_is_percent_not_decimal_and_not_a_monthly_invoice():
    assert annual_expense_illustration(1000, ".08") == Decimal(".80")


@pytest.mark.parametrize("capital,price,fee", [
    (-1, 1, 0), (100, 0, 0), (100, "NaN", 0), (100, 1, -1),
])
def test_invalid_inputs_fail(capital, price, fee):
    with pytest.raises(ValueError):
        whole_units(capital, price, fee)
