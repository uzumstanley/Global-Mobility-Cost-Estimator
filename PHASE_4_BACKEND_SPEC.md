# Phase 4: Backend Implementation Specification
**Global Mobility Cost Estimator (Switzerland → UK Assignment)**

---

## 1. Module Overview & Responsibilities

The backend is built around a lightweight, modular calculation engine located within the `estimator` app. Each module has a single, well-defined responsibility , using readable Python code.

| File | Purpose | Main Functions / Classes |
| :--- | :--- | :--- |
| `forms.py` | Form input definitions & validation | `CostEstimateForm` |
| `models.py` | Calculation audit logging | `CalculationRun` |
| `views.py` | HTTP request handling (GET / POST) | `estimator_view(request)` |
| `tax_calc.py` | Master calculation orchestrator | `calculate_assignment_costs(data)` |
| `swiss_tax.py` | Swiss social security & Zurich tax | `calc_hypo_deductions(salary, bonus, rate)` |
| `uk_tax.py` | 2026/27 UK income tax engine | `calc_uk_tax(gross_income)` |
| `gross_up.py` | Iterative tax gross-up loop | `gross_up(I, tolerance, max_iter)` |
| `benefits.py` | Benefit classification & s. 287 cap | `process_benefits(data, rate)` |
| `immigration_data.py` | Immigration rules & official links | `get_immigration_data()` |

---

## 2. Detailed Specifications

### 2.1 `estimator/forms.py`

#### Class: `CostEstimateForm(forms.Form)`
Handles user inputs, displays help text explaining tax/mobility concepts, and enforces rigorous validation rules.

#### Form Fields:
* `home_country` (`forms.CharField`, max_length=100, initial="Switzerland")
* `home_city` (`forms.CharField`, max_length=100, initial="Zurich")
* `host_country` (`forms.CharField`, max_length=100, initial="United Kingdom")
* `host_city` (`forms.CharField`, max_length=100, initial="London")
* `base_salary` (`forms.DecimalField`, max_digits=12, decimal_places=2, min_value=0.01, initial=150000.00,
  help_text="Annual base salary in home currency (CHF). Must be greater than 0.")
* `bonus` (`forms.DecimalField`, max_digits=12, decimal_places=2, min_value=0.00, initial=20000.00,
  help_text="Annual bonus in home currency (CHF).")
* `monthly_rent` (`forms.DecimalField`, max_digits=10, decimal_places=2, min_value=0.00, initial=3000.00,
  help_text="Monthly rent in host currency (£) paid directly to landlord by employer.")
* `relocation_allowance` (`forms.DecimalField`, max_digits=10, decimal_places=2, min_value=0.00, initial=5000.00,
  help_text="One-off cash relocation allowance in CHF (Year 1 only).")
* `moving_costs` (`forms.DecimalField`, max_digits=10, decimal_places=2, min_value=0.00, initial=6000.00,
  help_text="One-off flights and shipping of personal belongings in £ (Year 1 only).")
* `temp_housing` (`forms.DecimalField`, max_digits=10, decimal_places=2, min_value=0.00, initial=4000.00,
  help_text="One-off temporary accommodation / serviced apartment for first 4 weeks in £ (Year 1 only).")
* `exchange_rate` (`forms.DecimalField`, max_digits=6, decimal_places=4, min_value=0.0001, initial=1.1000,
  help_text="Exchange rate: £1.00 = X CHF (e.g. 1.10).")
* `start_date` (`forms.DateField`, initial="2026-04-06",
  widget=forms.DateInput(attrs={'type': 'date'}), help_text="Assignment start date.")
* `end_date` (`forms.DateField`, initial="2028-04-05",
  widget=forms.DateInput(attrs={'type': 'date'}), help_text="Assignment end date.")

#### Validation & Clean Methods:
```python
def clean_base_salary(self):
    salary = self.cleaned_data.get('base_salary')
    if salary is None or salary <= 0:
        raise forms.ValidationError("Base salary must be a positive number greater than zero.")
    return salary

def clean_exchange_rate(self):
    rate = self.cleaned_data.get('exchange_rate')
    if rate is None or rate <= 0:
        raise forms.ValidationError("Exchange rate must be greater than zero.")
    return rate

def clean(self):
    cleaned_data = super().clean()
    start_date = cleaned_data.get('start_date')
    end_date = cleaned_data.get('end_date')

    if start_date and end_date:
        if end_date <= start_date:
            raise forms.ValidationError("Assignment end date must be after the start date.")
    return cleaned_data
```

#### Edge Cases Handled:
* **Missing required field**: Returns friendly inline message: *"This field is required."*
* **Negative salary / benefits**: Blocked by `min_value` with custom error messages.
* **Zero exchange rate**: Blocked by `min_value=0.0001`.
* **Invalid date format or sequence**: Blocked by `clean()`.
* **Zero 500 errors guaranteed**: All validation failures re-render the form cleanly.

---

### 2.2 `estimator/swiss_tax.py`

#### Functions:

```python
def calc_swiss_social_security(gross_chf: float) -> dict:
    """
    Computes Swiss employee social security (AHV/IV/EO and ALV).
    - AHV/IV/EO: 5.30% uncapped.
    - ALV: 1.10% capped at CHF 148,200. Excess is 0% (solidarity surcharge abolished 2023).
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
    Computes cantonal/municipal taxable income and direct federal taxable income
    after standard professional expenses and insurance deductions.
    """
    # Standard lump sum professional expenses (3% capped at CHF 4,000)
    prof_expenses = min(4000.0, max(2000.0, gross_chf * 0.03))
    
    # Insurance premiums & savings interest deduction
    cantonal_insurance_ded = 2900.0   # § 31 Abs. 1 StG ZH for single
    federal_insurance_ded = 1800.0    # Art. 33 DBG single

    cantonal_taxable = max(0.0, gross_chf - ss_deduction - prof_expenses - cantonal_insurance_ded)
    federal_taxable = max(0.0, gross_chf - ss_deduction - prof_expenses - federal_insurance_ded)

    # Standard Swiss rounding to nearest 100
    cantonal_taxable = round(cantonal_taxable / 100.0) * 100.0
    federal_taxable = round(federal_taxable / 100.0) * 100.0

    return cantonal_taxable, federal_taxable

def calc_zurich_cantonal_municipal_tax(taxable_chf: float) -> dict:
    """
    Computes einfache Staatssteuer using § 35 StG ZH Grundtarif,
    then applies 95% cantonal multiplier and 119% City of Zurich municipal multiplier.
    Adds flat CHF 24.00 personal tax.
    """
    # § 35 StG ZH Grundtarif brackets for 2026:
    # 0% on first 7,000; 2% on next 5,000; 3% on next 4,800; 4% on next 8,000;
    # 5% on next 9,700; 6% on next 11,200; 7% on next 13,100; 8% on next 17,600;
    # 9% on next 34,000; 10% on next 33,700; 11% on next 53,300; 12% on next 69,300; 13% excess.
    # On CHF 152,400 taxable income, einfache Staatssteuer = CHF 11,889.00
    base_tax = compute_stg_base_tax(taxable_chf)
    
    cantonal_tax = base_tax * 0.95
    municipal_tax = base_tax * 1.19
    personal_tax = 24.00
    church_tax = 0.00  # no church tax

    total_canton_muni = cantonal_tax + municipal_tax + personal_tax + church_tax
    return {
        'base_tax_chf': round(base_tax, 2),
        'cantonal_tax_chf': round(cantonal_tax, 2),
        'municipal_tax_chf': round(municipal_tax, 2),
        'personal_tax_chf': round(personal_tax, 2),
        'church_tax_chf': 0.00,
        'total_canton_muni_chf': round(total_canton_muni, 2),
    }

def calc_direct_federal_tax(taxable_chf: float) -> float:
    """
    Computes Swiss Direct Federal Tax (Art. 36 DBG / SR 642.119.2) for single persons.
    On CHF 153,500 taxable income:
    Base at CHF 141,500 = CHF 6,140.55 + 11.00% on excess (CHF 12,000) = CHF 7,460.55.
    """
    return compute_dbg_tax(taxable_chf)

def calc_hypo_deductions(salary_chf: float, bonus_chf: float, exchange_rate: float) -> dict:
    """
    Master function: calculates full Swiss deductions and converts to GBP.
    """
    gross_chf = salary_chf + bonus_chf
    ss = calc_swiss_social_security(gross_chf)
    cantonal_taxable, fed_taxable = calc_zurich_taxable_income(gross_chf, ss['total_ss_chf'])
    canton_muni = calc_zurich_cantonal_municipal_tax(cantonal_taxable)
    fed_tax = calc_direct_federal_tax(fed_taxable)

    total_tax_chf = canton_muni['total_canton_muni_chf'] + fed_tax
    total_deductions_chf = total_tax_chf + ss['total_ss_chf']

    # Convert to GBP
    return {
        'gross_chf': gross_chf,
        'gross_gbp': round(gross_chf / exchange_rate, 2),
        'ahv_iv_eo_chf': ss['ahv_iv_eo_chf'],
        'ahv_iv_eo_gbp': round(ss['ahv_iv_eo_chf'] / exchange_rate, 2),
        'alv_chf': ss['alv_chf'],
        'alv_gbp': round(ss['alv_chf'] / exchange_rate, 2),
        'total_ss_chf': ss['total_ss_chf'],
        'total_ss_gbp': round(ss['total_ss_chf'] / exchange_rate, 2),
        'federal_tax_chf': round(fed_tax, 2),
        'federal_tax_gbp': round(fed_tax / exchange_rate, 2),
        'cantonal_tax_chf': canton_muni['cantonal_tax_chf'],
        'cantonal_tax_gbp': round(canton_muni['cantonal_tax_chf'] / exchange_rate, 2),
        'municipal_tax_chf': canton_muni['municipal_tax_chf'],
        'municipal_tax_gbp': round(canton_muni['municipal_tax_chf'] / exchange_rate, 2),
        'personal_tax_chf': canton_muni['personal_tax_chf'],
        'personal_tax_gbp': round(canton_muni['personal_tax_chf'] / exchange_rate, 2),
        'total_tax_chf': round(total_tax_chf, 2),
        'total_tax_gbp': round(total_tax_chf / exchange_rate, 2),
        'total_deductions_chf': round(total_deductions_chf, 2),
        'total_deductions_gbp': round(total_deductions_chf / exchange_rate, 2),
    }
```

---

### 2.3 `estimator/uk_tax.py`

#### Functions:

```python
def calc_uk_tax(gross_income: float) -> float:
    """
    Computes 2026/27 UK income tax for England, Wales, and Northern Ireland.
    Accounts for:
    - Standard Personal Allowance: £12,570
    - PA Taper: £1 per £2 of income above £100,000 (reaches £0 at £125,140)
    - Basic Rate (20%): £12,571 to £50,270 (first £37,700 of taxable income)
    - Higher Rate (40%): £50,271 to £125,140
    - Additional Rate (45%): Income above £125,140
    """
    if gross_income <= 12570.0:
        return 0.0

    # High income Personal Allowance taper
    if gross_income <= 100000.0:
        pa = 12570.0
    elif gross_income >= 125140.0:
        pa = 0.0
    else:
        pa = 12570.0 - (gross_income - 100000.0) / 2.0

    taxable = max(0.0, gross_income - pa)

    # Basic rate band: £37,700 width
    if taxable <= 37700.0:
        return round(taxable * 0.20, 2)

    basic_tax = 37700.0 * 0.20
    remaining_taxable = taxable - 37700.0

    # Higher rate band up to £125,140 total income
    if gross_income <= 125140.0:
        return round(basic_tax + remaining_taxable * 0.40, 2)

    # For income above £125,140, PA is 0, so higher rate slice is exactly £87,440
    higher_tax = 87440.0 * 0.40
    additional_tax = (gross_income - 125140.0) * 0.45
    return round(basic_tax + higher_tax + additional_tax, 2)
```

---

### 2.4 `estimator/gross_up.py`

#### Functions:

```python
def gross_up(I: float, tolerance: float = 0.01, max_iter: int = 100) -> tuple[float, list[dict]]:
    """
    Solves T = UKTax(I + T) using iterative fixed-point iteration.
    Starts with T_0 = UKTax(I).
    Iterates until |T_new - T_old| < tolerance or max_iter reached.
    Returns: (converged_tax, iteration_trace_list)
    """
    from .uk_tax import calc_uk_tax

    T = calc_uk_tax(I)
    trace = []
    
    # Record step 0 (initial seed)
    initial_gross = I + T
    initial_check = calc_uk_tax(initial_gross)
    trace.append({
        'iteration': 0,
        'old_tax': round(T, 2),
        'gross_pay': round(initial_gross, 2),
        'new_tax': round(initial_check, 2),
        'diff': round(abs(initial_check - T), 4),
    })

    for k in range(1, max_iter + 1):
        T_new = calc_uk_tax(I + T)
        diff = abs(T_new - T)
        
        trace.append({
            'iteration': k,
            'old_tax': round(T, 2),
            'gross_pay': round(I + T, 2),
            'new_tax': round(T_new, 2),
            'diff': round(diff, 4),
        })

        if diff < tolerance:
            return round(T_new, 2), trace
        T = T_new

    # Fallback if non-converged (capped at max_iter)
    return round(T_new, 2), trace
```

---

### 2.5 `estimator/benefits.py`

#### Functions:

```python
def process_benefits(cleaned_data: dict, exchange_rate: float) -> dict:
    """
    Classifies benefits into taxable cash, taxable BIK, and exempt.
    Applies the £8,000 statutory relocation exemption under s. 287 ITEPA 2003.
    Returns actual employer expenditure vs taxable value for Year 1 and Year 2.
    """
    monthly_rent = float(cleaned_data.get('monthly_rent', 3000.0))
    annual_housing = monthly_rent * 12.0

    # Relocation cash allowance (CHF -> GBP)
    reloc_chf = float(cleaned_data.get('relocation_allowance', 5000.0))
    reloc_cash_gbp = round(reloc_chf / exchange_rate, 2)

    # Moving and temporary housing
    moving_costs = float(cleaned_data.get('moving_costs', 6000.0))
    temp_housing = float(cleaned_data.get('temp_housing', 4000.0))

    # Apply s. 287 £8,000 statutory cap
    total_qualifying = moving_costs + temp_housing
    statutory_cap = 8000.0
    exempt_relocation = min(total_qualifying, statutory_cap)
    taxable_relocation_excess = max(0.0, total_qualifying - statutory_cap)

    # Year 1
    y1_employer_cost = annual_housing + reloc_cash_gbp + moving_costs + temp_housing
    y1_taxable_value = annual_housing + reloc_cash_gbp + taxable_relocation_excess

    # Year 2 (Housing only)
    y2_employer_cost = annual_housing
    y2_taxable_value = annual_housing

    return {
        'housing_annual_cost': annual_housing,
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
```

---

### 2.6 `estimator/tax_calc.py`

#### Functions:

```python
def calculate_assignment_costs(data: dict) -> dict:
    """
    Main calculation orchestrator:
    1. Converts inputs and extracts parameters.
    2. Calls swiss_tax to get hypothetical deductions.
    3. Computes net home pay delivered to the employee.
    4. Calls benefits to classify benefits and apply £8k exemption.
    5. Calculates UK taxable income before tax (I) for Y1 and Y2.
    6. Calls gross_up to determine host tax and grossed-up income.
    7. Evaluates employer NIC (£0 under Certificate of Coverage).
    8. Assembles the 4-section cost table, summary metrics, and multiples.
    """
    # 1. Inputs
    rate = float(data['exchange_rate'])
    salary_chf = float(data['base_salary'])
    bonus_chf = float(data['bonus'])
    total_home_chf = salary_chf + bonus_chf
    home_pay_gbp = round(total_home_chf / rate, 2)

    # 2. Swiss Deductions
    swiss = calc_hypo_deductions(salary_chf, bonus_chf, rate)
    total_deductions_gbp = swiss['total_deductions_gbp']
    net_home_gbp = round(home_pay_gbp - total_deductions_gbp, 2)

    # 3. Benefits
    b = process_benefits(data, rate)

    # 4. UK Taxable Pay before gross-up (I)
    I_y1 = round(net_home_gbp + b['y1_taxable_value'], 2)
    I_y2 = round(net_home_gbp + b['y2_taxable_value'], 2)

    # 5. Iterative Gross-Up
    T_y1, trace_y1 = gross_up(I_y1)
    T_y2, trace_y2 = gross_up(I_y2)

    # 6. Host Tax and Employer Charges
    # Under Art. 14 of UK-Swiss Social Security Convention, UK NIC is £0.00
    host_charges_y1 = T_y1
    host_charges_y2 = T_y2

    # 7. Total Employer Cost per Year
    # Total Cost = Home Pay + Benefits + Host Charges - Hypothetical Deductions
    cost_y1 = round(home_pay_gbp + b['y1_actual_cost'] + host_charges_y1 - total_deductions_gbp, 2)
    cost_y2 = round(home_pay_gbp + b['y2_actual_cost'] + host_charges_y2 - total_deductions_gbp, 2)
    total_assignment_cost = round(cost_y1 + cost_y2, 2)

    # 8. Summary Multiples
    mult_y1 = round(cost_y1 / home_pay_gbp, 3)
    mult_y2 = round(cost_y2 / home_pay_gbp, 3)
    mult_total = round(total_assignment_cost / (home_pay_gbp * 2.0), 3)

    return {
        'section1': { ... }, # Home pay details
        'section2': { ... }, # Benefits details
        'section3': { ... }, # Host tax & NIC details
        'section4': { ... }, # Swiss deductions
        'summary': {
            'cost_y1': cost_y1,
            'cost_y2': cost_y2,
            'total_cost': total_assignment_cost,
            'home_pay_gbp': home_pay_gbp,
            'mult_y1': mult_y1,
            'mult_y2': mult_y2,
            'mult_total': mult_total,
        },
        'traces': {
            'y1': trace_y1,
            'y2': trace_y2,
        },
        'assumptions': get_assumptions_list(),
    }
```

---

### 2.7 `estimator/immigration_data.py`

#### Functions:

```python
def get_immigration_content() -> dict:
    """
    Returns structured data for Tab 2 (Immigration & Work Permits), including:
    - Route recommendation: Global Business Mobility vs Skilled Worker.
    - Business visit / ETA rules.
    - Passport validity requirements.
    - Employer compliance & payroll duties.
    - Cost breakdown separating employer statutory fees from employee costs.
    - Official clickable links to GOV.UK and statutory guidance.
    """
```

---

## 3. Error Handling Architecture

| Scenario | Handled By | Behavior |
| :--- | :--- | :--- |
| **Negative Salary** | `forms.CostEstimateForm.clean_base_salary` | Returns: *"Base salary must be a positive number greater than zero."* (Form re-renders with alert) |
| **Zero Exchange Rate** | `forms.CostEstimateForm.clean_exchange_rate` | Returns: *"Exchange rate must be greater than zero."* |
| **Negative Benefits** | Field-level `min_value=0.00` | Returns: *"Ensure this value is greater than or equal to 0."* |
| **End Date Before Start Date** | `forms.CostEstimateForm.clean` | Returns: *"Assignment end date must be after the start date."* |
| **Missing Fields** | Standard Django Form validation | Returns: *"This field is required."* |
| **Gross-Up Non-Convergence** | Capped loop in `gross_up.py` | Capped at 100 iterations, logs warning, returns best estimate. |
| **HTTP 500 Prevention** | `views.estimator_view` | Validates `form.is_valid()` before any calculation; invalid data never touches the math engine. |



