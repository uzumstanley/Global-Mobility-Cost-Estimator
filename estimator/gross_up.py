"""
Iterative gross‑up calculation for UK tax.
Returns the converged tax amount and a trace list for debugging.
"""

def gross_up(I: float, tolerance: float = 0.01, max_iter: int = 100):
    """Solve T = UKTax(I + T) by fixed‑point iteration.
    Args:
        I: Taxable income before gross‑up (GBP).
        tolerance: Convergence tolerance for the tax amount.
        max_iter: Maximum iterations.
    Returns:
        (converged_tax, trace) where trace is a list of dicts describing each step.
    """
    from .uk_tax import calc_uk_tax

    T = calc_uk_tax(I)  # initial seed
    trace = []
    # Record initial step
    trace.append({
        "iteration": 0,
        "old_tax": round(T, 2),
        "gross_pay": round(I + T, 2),
        "new_tax": round(calc_uk_tax(I + T), 2),
        "diff": round(abs(calc_uk_tax(I + T) - T), 4),
    })

    for k in range(1, max_iter + 1):
        new_T = calc_uk_tax(I + T)
        diff = abs(new_T - T)
        trace.append({
            "iteration": k,
            "old_tax": round(T, 2),
            "gross_pay": round(I + T, 2),
            "new_tax": round(new_T, 2),
            "diff": round(diff, 4),
        })
        if diff < tolerance:
            return round(new_T, 2), trace
        T = new_T
    # Return best estimate after max_iter
    return round(T, 2), trace

