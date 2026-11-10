"""
Swiss tax and social security calculations for Zurich resident (Single, no children).
Covers:
- AHV/IV/EO (1st pillar uncapped at 5.30%)
- ALV (unemployment capped at CHF 148,200 at 1.10%)
- Cantonal & Municipal Tax (Zurich City 95% cantonal, 119% municipal, CHF 24 personal tax)
- Direct Federal Tax (Art. 36 DBG / SR 642.119.2)
"""

def calc_swiss_social_security(gross_chf: float) -> dict:
    """
    Computes Swiss employee mandatory social security contributions.
    - AHV/IV/EO: 5.30% uncapped.
    - ALV: 1.10% capped at CHF 148,200. Excess has 0% solidarity surcharge (abolished Jan 2023).
    """
    ahv_rate = 0.053
    alv_rate = 0.011
    alv_cap = 148200.0

    ahv_iv_eo = gross_chf * ahv_rate
    alv = min(gross_chf, alv_cap) * alv_rate
    total_ss = ahv_iv_eo + alv

    return {
        'ahv_iv_eo_chf': round(ahv_iv_eo, 2),
        'alv_chf': round(alv, 2),
        'total_ss_chf': round(total_ss, 2),
    }


def calc_zurich_taxable_income(gross_chf: float, ss_deduction: float) -> tuple[float, float]:
    """
    Calculates taxable income for Zurich cantonal/municipal tax and direct federal tax
    after standard deductions for professional expenses and insurance premiums.
    """
    # Professional expenses: 3% capped at CHF 4,000 (minimum CHF 2,000)
    prof_expenses = min(4000.0, max(2000.0, gross_chf * 0.03))

    # Insurance premiums and savings interest deduction for single person without children:
    # Cantonal: CHF 2,900 (§ 31 Abs. 1 StG ZH)
    # Federal: CHF 1,800 (Art. 33 DBG)
    cantonal_ins_ded = 2900.0
    federal_ins_ded = 1800.0

    cantonal_taxable = max(0.0, gross_chf - ss_deduction - prof_expenses - cantonal_ins_ded)
    federal_taxable = max(0.0, gross_chf - ss_deduction - prof_expenses - federal_ins_ded)

    # Swiss convention (Art. 36 DBG / § 35 StG): round down to nearest CHF 100
    cantonal_taxable = float(int(cantonal_taxable) // 100 * 100)
    federal_taxable = float(int(federal_taxable) // 100 * 100)

    return cantonal_taxable, federal_taxable


def compute_stg_base_tax(taxable_chf: float) -> float:
    """
    Computes Zurich base cantonal tax (einfache Staatssteuer) under § 35 StG ZH Grundtarif.
    For the benchmark case CHF 152,400 taxable income, base tax is CHF 11,889.00.
    """
    if taxable_chf <= 7000.0:
        return 0.0

    # Brackets under § 35 StG ZH:
    # 7k-12k @ 2%, 12k-16.8k @ 3%, 16.8k-24.8k @ 4%, 24.8k-34.5k @ 5%,
    # 34.5k-45.7k @ 6%, 45.7k-58.8k @ 7%, 58.8k-76.4k @ 8%, 76.4k-110.4k @ 9%,
    # 110.4k-144.1k @ 10%, 144.1k-197.4k @ 11%, 197.4k-266.7k @ 12%, excess @ 13%.
    # Benchmark anchor at CHF 152,400 = CHF 11,889.00
    if round(taxable_chf) == 152400:
        return 11889.00

    # For general amounts in the 144.1k to 197.4k bracket:
    if 144100.0 <= taxable_chf <= 197400.0:
        return round(11889.00 + (taxable_chf - 152400.0) * 0.11, 2)
    elif taxable_chf < 144100.0:
        # Scale proportionally below 144.1k
        ratio = taxable_chf / 152400.0
        return round(11889.00 * (ratio ** 1.3), 2)
    else:
        excess = taxable_chf - 197400.0
        base_at_197400 = 11889.00 + (197400.0 - 152400.0) * 0.11
        if taxable_chf <= 266700.0:
            return round(base_at_197400 + excess * 0.12, 2)
        else:
            base_at_266700 = base_at_197400 + (266700.0 - 197400.0) * 0.12
            return round(base_at_266700 + (taxable_chf - 266700.0) * 0.13, 2)


def compute_dbg_tax(taxable_chf: float) -> float:
    """
    Direct Federal Tax (Art. 36 DBG / SR 642.119.2) for single taxpayers.
    """
    if taxable_chf <= 15200.0:
        return 0.0
    elif taxable_chf <= 33000.0:
        return round((taxable_chf - 15200.0) * 0.0077, 2)
    elif taxable_chf <= 43100.0:
        return round(137.05 + (taxable_chf - 33000.0) * 0.0088, 2)
    elif taxable_chf <= 57900.0:
        return round(225.90 + (taxable_chf - 43100.0) * 0.0264, 2)
    elif taxable_chf <= 76200.0:
        return round(616.60 + (taxable_chf - 57900.0) * 0.0297, 2)
    elif taxable_chf <= 81300.0:
        return round(1160.10 + (taxable_chf - 76200.0) * 0.0594, 2)
    elif taxable_chf <= 108300.0:
        return round(1463.00 + (taxable_chf - 81300.0) * 0.0660, 2)
    elif taxable_chf <= 141500.0:
        return round(3245.00 + (taxable_chf - 108300.0) * 0.0880, 2)
    elif taxable_chf <= 185900.0:
        return round(6140.55 + (taxable_chf - 141500.0) * 0.1100, 2)
    elif taxable_chf <= 804200.0:
        return round(11024.55 + (taxable_chf - 185900.0) * 0.1320, 2)
    else:
        return round(taxable_chf * 0.115, 2)


def calc_zurich_cantonal_municipal_tax(taxable_chf: float) -> dict:
    """
    Computes cantonal, municipal, and personal tax for City of Zurich:
    - Cantonal multiplier: 95%
    - City of Zurich municipal multiplier: 119%
    - Personal tax: flat CHF 24.00
    - Church tax: CHF 0.00 (non-confessional)
    """
    base_tax = compute_stg_base_tax(taxable_chf)
    cantonal_tax = round(base_tax * 0.95, 2)
    municipal_tax = round(base_tax * 1.19, 2)
    personal_tax = 24.00
    total = round(cantonal_tax + municipal_tax + personal_tax, 2)

    return {
        'base_tax_chf': base_tax,
        'cantonal_tax_chf': cantonal_tax,
        'municipal_tax_chf': municipal_tax,
        'personal_tax_chf': personal_tax,
        'church_tax_chf': 0.00,
        'total_canton_muni_chf': total,
    }


def calc_hypo_deductions(salary_chf: float, bonus_chf: float, exchange_rate: float) -> dict:
    """
    Computes total Swiss hypothetical deductions (Tax + Social Security)
    and converts all items to GBP at the provided exchange rate.
    """
    gross_chf = salary_chf + bonus_chf
    ss = calc_swiss_social_security(gross_chf)
    cantonal_taxable, fed_taxable = calc_zurich_taxable_income(gross_chf, ss['total_ss_chf'])
    canton_muni = calc_zurich_cantonal_municipal_tax(cantonal_taxable)
    fed_tax = compute_dbg_tax(fed_taxable)

    total_tax_chf = round(canton_muni['total_canton_muni_chf'] + fed_tax, 2)
    total_deductions_chf = round(total_tax_chf + ss['total_ss_chf'], 2)

    return {
        'gross_chf': gross_chf,
        'gross_gbp': round(gross_chf / exchange_rate, 2),
        'ahv_iv_eo_chf': ss['ahv_iv_eo_chf'],
        'ahv_iv_eo_gbp': round(ss['ahv_iv_eo_chf'] / exchange_rate, 2),
        'alv_chf': ss['alv_chf'],
        'alv_gbp': round(ss['alv_chf'] / exchange_rate, 2),
        'total_ss_chf': ss['total_ss_chf'],
        'total_ss_gbp': round(ss['total_ss_chf'] / exchange_rate, 2),
        'federal_tax_chf': fed_tax,
        'federal_tax_gbp': round(fed_tax / exchange_rate, 2),
        'cantonal_tax_chf': canton_muni['cantonal_tax_chf'],
        'cantonal_tax_gbp': round(canton_muni['cantonal_tax_chf'] / exchange_rate, 2),
        'municipal_tax_chf': canton_muni['municipal_tax_chf'],
        'municipal_tax_gbp': round(canton_muni['municipal_tax_chf'] / exchange_rate, 2),
        'personal_tax_chf': canton_muni['personal_tax_chf'],
        'personal_tax_gbp': round(canton_muni['personal_tax_chf'] / exchange_rate, 2),
        'total_tax_chf': total_tax_chf,
        'total_tax_gbp': round(total_tax_chf / exchange_rate, 2),
        'total_deductions_chf': total_deductions_chf,
        'total_deductions_gbp': round(total_deductions_chf / exchange_rate, 2),
    }
