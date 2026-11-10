"""
UK income tax calculation for 2026/27 tax year.
Implements personal allowance taper and progressive rates.
"""

def calc_uk_tax(gross_income: float) -> float:
    """Calculate UK income tax payable for a given gross income.
    Applies 2026/27 rates:
    - Personal Allowance (PA) £12,570, tapered £1 per £2 over £100,000.
    - Basic rate 20% on first £37,700 of taxable income.
    - Higher rate 40% on taxable income up to £125,140 total income.
    - Additional rate 45% above £125,140.
    """
    # Personal Allowance calculation
    if gross_income <= 12570.0:
        return 0.0

    if gross_income <= 100000.0:
        pa = 12570.0
    elif gross_income >= 125140.0:
        pa = 0.0
    else:
        pa = 12570.0 - (gross_income - 100000.0) / 2.0

    taxable = max(0.0, gross_income - pa)

    # Basic rate band (first £37,700 of taxable income)
    basic_band = 37700.0
    if taxable <= basic_band:
        return round(taxable * 0.20, 2)

    basic_tax = basic_band * 0.20
    remaining = taxable - basic_band

    # Higher rate up to total income £125,140 (i.e., taxable up to £125,140 - pa)
    higher_limit_income = 125140.0
    higher_limit_taxable = max(0.0, higher_limit_income - pa - basic_band)
    if gross_income <= higher_limit_income:
        return round(basic_tax + remaining * 0.40, 2)

    higher_tax = higher_limit_taxable * 0.40
    # Additional rate for any remaining taxable income above higher limit
    additional_taxable = taxable - basic_band - higher_limit_taxable
    additional_tax = additional_taxable * 0.45
    return round(basic_tax + higher_tax + additional_tax, 2)

