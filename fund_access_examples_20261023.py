"""Illustrative whole-unit access and reinvestment math; not broker certification."""
from decimal import Decimal, ROUND_FLOOR


def nonnegative(value, label):
    result = Decimal(str(value))
    if not result.is_finite() or result < 0:
        raise ValueError(f"{label} must be finite and nonnegative")
    return result


def whole_units(capital, price, commission=0):
    capital = nonnegative(capital, "capital")
    price = nonnegative(price, "price")
    commission = nonnegative(commission, "commission")
    if price == 0:
        raise ValueError("price must be positive")
    if capital < price + commission:
        return {"units": 0, "invested": Decimal(0), "commission": Decimal(0),
                "cash": capital}
    units = int(((capital - commission) / price).to_integral_value(rounding=ROUND_FLOOR))
    invested = price * units
    return {"units": units, "invested": invested, "commission": commission,
            "cash": capital - invested - commission}


def whole_unit_reinvestment(units, distribution_per_unit, reinvestment_price):
    count = nonnegative(units, "units")
    if count != count.to_integral_value():
        raise ValueError("units must be a whole-unit count")
    distribution = nonnegative(distribution_per_unit, "distribution")
    return whole_units(count * distribution, reinvestment_price)


def annual_expense_illustration(balance, expense_percent):
    return nonnegative(balance, "balance") * nonnegative(expense_percent, "expense") / 100
