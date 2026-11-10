"""
Benefit classification and cost calculation.
Implements the £8,000 statutory relocation exemption cap.
"""

def process_benefits(cleaned_data: dict, exchange_rate: float) -> dict:
    """Classify benefits and compute employer cost vs taxable value.
    Returns a dict matching Phase 4 spec.
    """
    monthly_rent = float(cleaned_data.get('monthly_rent', 3000.0))
    annual_housing = monthly_rent * 12.0

    reloc_chf = float(cleaned_data.get('relocation_allowance', 5000.0))
    reloc_cash_gbp = round(reloc_chf / exchange_rate, 2)

    moving_costs = float(cleaned_data.get('moving_costs', 6000.0))
    temp_housing = float(cleaned_data.get('temp_housing', 4000.0))

    total_qualifying = moving_costs + temp_housing
    statutory_cap = 8000.0
    exempt_relocation = min(total_qualifying, statutory_cap)
    taxable_relocation_excess = max(0.0, total_qualifying - statutory_cap)

    # Year 1 calculations
    y1_employer_cost = annual_housing + reloc_cash_gbp + moving_costs + temp_housing
    y1_taxable_value = annual_housing + reloc_cash_gbp + taxable_relocation_excess

    # Year 2 (housing only)
    y2_employer_cost = annual_housing
    y2_taxable_value = annual_housing

    return {
        'housing_annual_cost': round(annual_housing, 2),
        'reloc_cash_gbp': reloc_cash_gbp,
        'moving_costs': moving_costs,
        'temp_housing': temp_housing,
        'total_qualifying_relocation': total_qualifying,
        'exempt_relocation': exempt_relocation,
        'taxable_relocation_excess': taxable_relocation_excess,
        'y1_actual_cost': round(y1_employer_cost, 2),
        'y1_taxable_value': round(y1_taxable_value, 2),
        'y2_actual_cost': round(y2_employer_cost, 2),
        'y2_taxable_value': round(y2_taxable_value, 2),
    }

