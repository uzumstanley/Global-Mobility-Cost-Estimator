"""
Master calculation orchestrator for the Global Mobility Cost Estimator.
It combines Swiss hypothetical deductions, benefit classification, UK tax gross‑up, and employer NIC.
"""

from .swiss_tax import calc_hypo_deductions
from .benefits import process_benefits
from .gross_up import gross_up
from .uk_tax import calc_uk_tax


def get_assumptions_list():
    """Return a list of textual assumptions for the UI – this mirrors Phase 3 spec.
    The list is static for now; in a full product it could be generated dynamically.
    """
    return [
        "Exchange rate fixed at £1 = CHF 1.10",
        "Swiss Social Security rates: AHV/IV/EO 5.30%, ALV 1.10% (capped CHF 148,200)",
        "Zurich cantonal multiplier 95 % and municipal multiplier 119 %",
        "Personal tax CHF 24 per year",
        "UK personal allowance £12,570 with taper above £100,000",
        "UK tax bands 20 % up to £37,700 taxable, 40 % up to £125,140, 45 % above",
        "Statutory relocation exemption cap £8,000 (ITEPA s. 287)",
        "Employer NIC exempt under Article 14 Certificate of Coverage",
    ]


def calculate_assignment_costs(data: dict) -> dict:
    """Perform the full cost calculation.
    Returns a dictionary matching the structure described in Phase 4.
    """
    # 1. Basic inputs
    rate = float(data["exchange_rate"])
    salary_chf = float(data["base_salary"])
    bonus_chf = float(data["bonus"])
    total_home_chf = salary_chf + bonus_chf
    home_pay_gbp = round(total_home_chf / rate, 2)

    # 2. Swiss hypothetical deductions (converted to GBP)
    swiss = calc_hypo_deductions(salary_chf, bonus_chf, rate)
    total_deductions_gbp = swiss["total_deductions_gbp"]
    net_home_gbp = round(home_pay_gbp - total_deductions_gbp, 2)

    # 3. Benefits (actual cost and taxable value)
    b = process_benefits(data, rate)

    # 4. UK taxable pay before gross‑up (I)
    I_y1 = round(net_home_gbp + b["y1_taxable_value"], 2)
    I_y2 = round(net_home_gbp + b["y2_taxable_value"], 2)

    # 5. Iterative gross‑up to obtain host tax (T) and iteration trace
    T_y1, trace_y1 = gross_up(I_y1)
    T_y2, trace_y2 = gross_up(I_y2)

    # 6. Employer NIC – exempt under Certificate of Coverage
    host_charges_y1 = T_y1
    host_charges_y2 = T_y2

    # 7. Total employer cost per year
    cost_y1 = round(home_pay_gbp + b["y1_actual_cost"] + host_charges_y1 - total_deductions_gbp, 2)
    cost_y2 = round(home_pay_gbp + b["y2_actual_cost"] + host_charges_y2 - total_deductions_gbp, 2)
    total_assignment_cost = round(cost_y1 + cost_y2, 2)

    # 8. Summary multiples
    mult_y1 = round(cost_y1 / home_pay_gbp, 3)
    mult_y2 = round(cost_y2 / home_pay_gbp, 3)
    mult_total = round(total_assignment_cost / (home_pay_gbp * 2.0), 3)

    return {
        "section1": {
            "home_pay_gbp": home_pay_gbp,
            "total_deductions_gbp": total_deductions_gbp,
            "net_home_gbp": net_home_gbp,
        },
        "section2": b,
        "section3": {
            "taxable_income_y1": I_y1,
            "taxable_income_y2": I_y2,
            "host_tax_y1": T_y1,
            "host_tax_y2": T_y2,
            "employer_nic_class1": 0.0,
            "employer_nic_class1a": 0.0,
            "total_employer_nic": 0.0,
        },
        "section4": swiss,
        "summary": {
            "cost_y1": cost_y1,
            "cost_y2": cost_y2,
            "total_cost": total_assignment_cost,
            "home_pay_gbp": home_pay_gbp,
            "mult_y1": mult_y1,
            "mult_y2": mult_y2,
            "mult_total": mult_total,
        },
        "traces": {"y1": trace_y1, "y2": trace_y2},
        "assumptions": get_assumptions_list(),
    }

