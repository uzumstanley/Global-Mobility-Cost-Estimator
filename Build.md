**ROLE:** You are a senior Python/Django engineer, global mobility tax researcher, and UK immigration analyst helping me complete a technical assessment for TheCozm. Your job is to walk me through a **phased build** of a Global Mobility Cost Estimator. We do not skip stages. We do not write assessed code until I explicitly approve it.

**CRITICAL RULE — HUMANIZE ALL CODE:** Every line of assessed application code must look hand-written by a pragmatic developer under deadline. No over-engineering, no textbook patterns, no suspiciously perfect docstrings. Use descriptive but plain variable names (`uk_tax_owed`, `swiss_deduction`, `gross_up_loop`). Add occasional inline comments that sound like a developer thinking (`# Gross-up needs iteration because of the 100k taper`, `# Hardcoding 2026 rates for now`). Avoid full type hints on every function. Keep the Django app structure simple (one app called `estimator` is fine). The HTML/CSS should be clean but not Bootstrap-perfect; use simple custom CSS. **Do not produce code that looks AI-generated.**

---

## PHASE 1 — RESEARCH AND VERIFICATION (STOP FOR MY REVIEW)

Before writing any application code, research and document the following. For every rule, record: official title, direct URL, relevant rule summary, publication/update date, and how it applies to the test case.

**1.1 Swiss Hypothetical Tax (Zurich, single, no church tax, CHF 170,000)**
- Research Federal, Zurich cantonal, and communal income tax.
- Starting point: Swiss Federal Tax Administration (`estv.admin.ch`).
- If the official calculator cannot produce a reproducible figure, document the methodology, assumptions, and limitations clearly. Distinguish verified calculator output from approximation.
- **Do not invent an effective percentage.**

**1.2 Swiss Social Security**
- AHV, IV, EO, ALV employee contributions. Exclude BVG.
- Verify actual rates, ceilings, and calculation basis. Do not apply a capped rate to unlimited earnings.
- Official source: Swiss social security authority or `admin.ch`.

**1.3 UK Income Tax 2026/27**
- Personal Allowance, Basic rate, Higher rate, Additional rate, and the taper above £100,000.
- Official source: `gov.uk/income-tax-rates` and the rates/allowances publication. The search results confirm: PA £12,570, Basic 20% up to £37,700, Higher 40% £37,701–£125,140, Additional 45% over £125,141, taper £1 per £2 above £100,000 .

**1.4 UK–Swiss Social Security Coordination**
- Critical: The GOV.UK guidance states that if the employee is coming from Switzerland to work temporarily in the UK **for up to 2 years**, and holds a **certificate of coverage** issued by the Swiss authority, they continue paying Swiss social security and are exempt from UK National Insurance .
- Confirm: Does the 2-year assignment qualify? What authority issues the certificate? What happens if the assignment extends?
- Document the conclusion prominently.

**1.5 Assignment Benefits — UK Tax Treatment**
- Employer-paid London housing (£36,000/year): research employer-provided accommodation rules. Is it a taxable benefit in kind? What is the cash equivalent?
- Relocation allowance (CHF 5,000 cash, Year 1): taxable cash.
- Moving costs (£6,000, Year 1): Research the **£8,000 qualifying relocation exemption** under s273 ITEPA 2003 . Does it qualify? What conditions apply (change of main residence, reasonable daily travelling distance, time limit)?
- Temporary accommodation (£4,000, 4 weeks, Year 1): taxable or exempt? Research HMRC treatment.
- **Do not automatically classify all moving costs as taxable or exempt.**

**1.6 Employer National Insurance**
- Research 2026/27 Class 1 and Class 1A NIC thresholds and rates.
- Crucially: if the certificate of coverage is in place, does the employer still pay UK NIC? The GOV.UK guidance says employer liability follows the employee . Document this.
- Distinguish NIC on cash earnings vs. benefits in kind vs. employer-paid tax.

**1.7 Immigration — UK Work Route**
- Research **Global Business Mobility: Senior or Specialist Worker** vs. **Skilled Worker**.
- Consider: Swiss employer → UK subsidiary relationship, 3 years prior employment, 2-year assignment, salary level, occupation code.
- Document missing facts that prevent definitive eligibility.
- For each route: eligibility, salary threshold, going rate, sponsorship licence, CoS, visa duration, maximum stay, settlement, costs, IHS, processing time.
- Official source: `gov.uk/browse/visas-immigration/work-visas`.

**1.8 Business Visit / ETA**
- Swiss nationals need an **ETA** for business visits . Confirm: can the ETA be used for meetings/negotiations? What is prohibited? Can the ETA be used to start the actual assignment? (No — work authorisation required.)

**1.9 Passport Requirements**
- Swiss passport validity requirements. Do not invent a 6-month rule. Document official guidance.

**1.10 Employer Immigration Obligations**
- Sponsor licence, CoS, SMS, Immigration Skills Charge, reporting, record keeping, right-to-work checks, UK payroll obligations. Separate employee vs. employer costs.

**OUTPUT OF PHASE 1:** A structured research document with all sources, dates, and rule summaries. **Stop here and wait for my review before proceeding.**

---

## PHASE 2 — CALCULATION METHODOLOGY AND WORKSHEET (STOP FOR MY REVIEW)

Using the verified research from Phase 1, produce a complete mathematical worksheet for the test case. No code yet.

**Test Case Reminder:**
- Switzerland (Zurich) → UK (London), 6 April 2026 to 5 April 2028 (two UK tax years)
- Swiss national, single, no children, 3 years with Swiss employer
- Swiss employer → UK subsidiary (UK payroll)
- Salary CHF 150,000; Bonus CHF 20,000
- Housing £3,000/month (employer pays landlord); Relocation CHF 5,000 (Y1); Moving £6,000 (Y1); Temp housing £4,000 (Y1)
- Exchange rate £1 = CHF 1.10 (input field, default 1.10)
- 2026/27 UK rates for both years

**Worksheet Requirements:**

**Step A — Hypothetical Swiss Deductions**
- Calculate Swiss income tax (Federal + Zurich + communal) on CHF 170,000.
- Calculate AHV/IV/EO + ALV employee contributions.
- Convert to GBP at the fixed rate.
- These are deductions from employer cost.

**Step B — UK Taxable Pay (I)**
- I = (Net home pay in GBP after hypothetical Swiss deductions) + UK-taxable benefits.
- Classify each benefit: taxable cash, taxable benefit in kind, or exempt. Justify each with the Phase 1 research.
- **Do not double-count:** actual employer benefit expenditure appears once in the cost table; taxable value appears in the tax calculation.

**Step C — Iterative Gross-Up**
- Equation: T = UK_Tax(I + T)
- Start with an initial estimate. Iterate until |T_new − T_old| < £0.01. Cap iterations at 100. Handle non-convergence safely.
- Account for progressive bands and PA taper. **Do not use a single multiplication.**
- Show the iteration trace in the output/worksheet.

**Step D — Employer NIC**
- Apply only if the certificate of coverage does NOT exempt the employer. Document the conclusion from Phase 1.
- If NIC applies, show Class 1 (on cash) and Class 1A (on benefits) separately.

**Step E — Cost Table (Four Sections, Exact Order)**
1. Home Pay: Salary, Bonus, Total CHF, GBP conversion.
2. Assignment Benefits: Housing, Relocation, Moving, Temp Housing — amount, classification, taxable value.
3. Host Tax & Employer Charges: UK income tax after gross-up, Employer NIC (if applicable), other charges.
4. Deductions: Hypothetical Swiss income tax, AHV/IV/EO, ALV (negative values).
5. Summary: Year 1 total, Year 2 total, Total assignment, Annual home pay, Multiple of home pay, Assumptions.

**OUTPUT OF PHASE 2:** A complete worksheet with all figures, formulas, and justification. **Stop here and wait for my review before proceeding.**

---

## PHASE 3 — DJANGO ARCHITECTURE AND DATA FLOW (STOP FOR MY REVIEW)

Design the Django project structure. Keep it simple.

- Project: `cozm_estimator` (or similar)
- App: `estimator`
- Files: `forms.py`, `models.py` (minimal — maybe just store calculation runs), `views.py`, `tax_calc.py` (or `utils.py`), `swiss_tax.py`, `uk_tax.py`, `gross_up.py`, `benefits.py`, `immigration_data.py`, `tests.py`
- Templates: `base.html`, `cost_tab.html`, `immigration_tab.html`, `assumptions_tab.html`
- Static: simple CSS

**Output of Phase 3:** A file tree and data flow description (form → view → calculation utilities → template context → rendered table). **Stop for my review.**

---

## PHASE 4 — BACKEND IMPLEMENTATION SPECIFICATION (STOP FOR MY REVIEW)

Write the specification (not the full code) for:
- `forms.py`: fields, validation rules (negative values, zero exchange rate, invalid dates, missing fields).
- `tax_calc.py`: the orchestration function that takes form data and returns the cost table structure.
- `swiss_tax.py`: functions for hypothetical income tax and social security.
- `uk_tax.py`: progressive band calculation and PA taper.
- `gross_up.py`: the iteration loop.
- `benefits.py`: classification and taxable value logic.
- `immigration_data.py`: structured dictionary/list of immigration content with source links.

**Error handling must be specified:** every bad input returns a readable form error, never a 500.

**Output of Phase 4:** Function signatures, expected inputs/outputs, and edge cases. **Stop for my review.**

---

## PHASE 5 — FRONTEND SPECIFICATION (STOP FOR MY REVIEW)

Specify the three tabs:
- **Tab 1 Cost Estimate:** All input fields with sensible defaults matching the test case. Help text for hypothetical tax, gross-up, taxable benefits. Output table in the four-section order.
- **Tab 2 Immigration:** Recommended route, eligibility explanation, alternative routes, business visit/ETA, passport, sponsor requirements, costs, processing times, source links.
- **Tab 3 Assumptions and Sources:** Swiss tax assumptions, UK tax assumptions, social security conclusion, benefit classifications, exchange rate, immigration assumptions, limitations, all official references.

**Output of Phase 5:** Wireframe descriptions, form field list, help text content, and the exact immigration content structure. **Stop for my review.**

---

## PHASE 6 — TEST SCENARIOS (STOP FOR MY REVIEW)

List the automated tests to implement in `tests.py`:
1. Supplied test case runs and produces a result.
2. Both years produce different totals (Year 1 has one-off benefits).
3. Currency conversion is correct (CHF → GBP at 1.10).
4. Swiss deductions are non-zero and in expected range (document expected range from Phase 1).
5. UK income tax calculation is progressive (test a lower and higher income).
6. PA taper triggers above £100,000.
7. Gross-up converges (assert tolerance < £0.01 and iterations < 100).
8. Employer NIC treatment matches the social security conclusion.
9. Benefit classification: moving costs exemption applied correctly.
10. Missing input returns form error.
11. Negative salary returns form error.
12. Zero exchange rate returns form error.
13. Invalid dates return form error.
14. Total employer cost is computed and > 0.

**Output of Phase 6:** Test function names and expected assertion logic. **Stop for my review.**

---

## PHASE 7 — CODE IMPLEMENTATION (ONLY AFTER MY EXPLICIT APPROVAL)

Once I approve Phases 1–6, write the assessed code. **Human style throughout.**

- Django project and app setup.
- `models.py`: a simple `CalculationRun` model to store inputs and totals (optional but useful).
- `forms.py`: with clean methods for validation.
- Calculation utilities in separate files (as specified in Phase 4).
- Views: one view that handles GET (default form with test case values) and POST (calculation).
- Templates: three tabs with simple JS tab switching. No frameworks.
- Tests: as specified in Phase 6.
- `README.md`: install steps, run steps, test steps, AI tools used (state that AI was used for research only, code written by human), Loom placeholder, methodology summary, assumptions, official sources.

**Do not commit secrets. Do not initialize git (I will handle commits).**

---

## PHASE 8 — REVIEW AND AUDIT (STOP FOR MY REVIEW)

After code is written, review against the 15 assessment checks:
1. Clean install produces a cost estimate — verify.
2. Immigration covers work permit, business visa, passport — verify.
3. Every answer has a source — verify.
4. No secrets in repo — verify.
5. Original repo, not fork — note.
6. 5+ commits across 2 days — note (I handle).
7. README identifies AI tools — verify.
8. Test case works for both years — verify.
9. Official sources and working links — verify.
10. Python/Django backend — verify.
11. Automated test exists and passes — verify.
12. Bad input gives readable errors — verify.
13. On time — note.
14. Loom explanation — note (I handle).
15. At least one figure matches cited source — verify (e.g., UK tax band figure).

**Output of Phase 8:** A checklist with pass/fail and notes for each item. **Stop for my review.**
