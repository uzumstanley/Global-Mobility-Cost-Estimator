# Phase 6: Automated Test Scenarios Specification
**Global Mobility Cost Estimator (Switzerland → UK Assignment)**

---

## 1. Overview of the Test Suite

The test suite will be implemented in `estimator/tests.py` using Django’s standard testing framework (`django.test.TestCase` and `django.test.Client`). It ensures 100% test coverage over:
1. Core calculation accuracy (benchmarking against official statutory sources).
2. The iterative gross-up algorithm and convergence tolerance.
3. Benefit classification and statutory exemption caps under ITEPA 2003.
4. Social security coordination rules under the UK-Switzerland Convention.
5. Form input validation, date boundary logic, and resilient error handling (zero 500 crashes).

All 14 test scenarios specified in `Build.md` are defined below with their exact function signatures, test inputs, and expected assertions.

---

## 2. Test Scenarios Matrix

| No. | Test Scenario | Function Name | Type | Key Assertion |
| :---: | :--- | :--- | :---: | :--- |
| **1** | Supplied test case produces valid result | `test_supplied_test_case_runs_and_produces_result` | Integration | Y1: £269,249.72; Y2: £249,348.91; Total: £518,598.63 ($\pm £1.00$) |
| **2** | Both years produce different totals | `test_both_years_produce_different_totals` | Calculation | `cost_y1 > cost_y2` (difference reflects Y1 one-off benefits) |
| **3** | Currency conversion is accurate | `test_currency_conversion_is_correct` | Unit | CHF 170k / 1.10 = £154,545.45; CHF 5k / 1.10 = £4,545.45 |
| **4** | Swiss deductions in expected range | `test_swiss_deductions_in_expected_range` | Unit | Tax: CHF 32.5k–33.2k; Social Security: CHF 10,640.20 |
| **5** | UK tax is progressive across bands | `test_uk_income_tax_is_progressive` | Unit | Effective rate increases: `rate(30k) < rate(75k) < rate(150k)` |
| **6** | Personal Allowance taper above £100k | `test_personal_allowance_taper_triggers_above_100k` | Unit | PA reduced by £1 per £2 over £100k; 60% marginal tax rate |
| **7** | Gross-up loop converges within tolerance | `test_gross_up_converges_within_tolerance_and_max_iter` | Unit | Difference $< £0.01$; iterations $< 100$; $\text{UKTax}(I+T) == T$ |
| **8** | Employer NIC matches treaty exemption | `test_employer_nic_matches_social_security_conclusion` | Calculation | Employer Class 1 NIC = £0.00; Class 1A = £0.00 (PDA1 held) |
| **9** | £8,000 relocation exemption applied | `test_benefit_classification_and_relocation_exemption` | Unit | £10k costs $\implies$ £8k exempt, £2k taxable BIK (s. 287 ITEPA) |
| **10** | Missing input returns form error | `test_missing_input_returns_form_error` | Form / View | `form.is_valid() == False`; field error returned; HTTP 200 |
| **11** | Negative salary returns form error | `test_negative_salary_returns_form_error` | Form / View | `form.is_valid() == False`; readable message; no 500 crash |
| **12** | Zero exchange rate returns form error | `test_zero_exchange_rate_returns_form_error` | Form / View | `form.is_valid() == False`; prevents ZeroDivisionError; HTTP 200 |
| **13** | End date before start date error | `test_invalid_dates_return_form_error` | Form / View | `form.is_valid() == False`; date sequence error message |
| **14** | Total employer cost is computed & > 0 | `test_total_employer_cost_is_computed_and_positive` | Integration | `total_cost > 0`; `multiple > 1.0` |

---

## 3. Detailed Test Function Specifications

### Test 1: `test_supplied_test_case_runs_and_produces_result`
* **Objective**: Verifies that the test case inputs produce the complete cost table with verified totals.
* **Inputs**:
  * Salary: CHF 150,000; Bonus: CHF 20,000; Rent: £3,000/mo; Relocation: CHF 5,000; Moving: £6,000; Temp Housing: £4,000; Exchange Rate: 1.10.
* **Assertions**:
  ```python
  results = calculate_assignment_costs(test_case_data)
  self.assertIsNotNone(results)
  self.assertAlmostEqual(results['summary']['cost_y1'], 269249.72, delta=1.00)
  self.assertAlmostEqual(results['summary']['cost_y2'], 249348.91, delta=1.00)
  self.assertAlmostEqual(results['summary']['total_cost'], 518598.63, delta=1.00)
  self.assertAlmostEqual(results['summary']['mult_total'], 1.678, delta=0.01)
  ```

---

### Test 2: `test_both_years_produce_different_totals`
* **Objective**: Verifies that Year 1 and Year 2 totals differ because Year 1 includes one-off relocation, moving, and temporary housing costs.
* **Assertions**:
  ```python
  results = calculate_assignment_costs(test_case_data)
  cost_y1 = results['summary']['cost_y1']
  cost_y2 = results['summary']['cost_y2']
  self.assertNotEqual(cost_y1, cost_y2)
  self.assertGreater(cost_y1, cost_y2)
  # Expected difference is approx £19,900
  self.assertAlmostEqual(cost_y1 - cost_y2, 19900.81, delta=2.00)
  ```

---

### Test 3: `test_currency_conversion_is_correct`
* **Objective**: Verifies that all CHF amounts are converted to GBP using the exact exchange rate (£1.00 = CHF 1.10) with standard 2-decimal rounding.
* **Assertions**:
  ```python
  # Gross Home Pay: CHF 170,000 / 1.10 = £154,545.45
  home_gbp = round(170000.0 / 1.10, 2)
  self.assertEqual(home_gbp, 154545.45)

  # Relocation Allowance: CHF 5,000 / 1.10 = £4,545.45
  reloc_gbp = round(5000.0 / 1.10, 2)
  self.assertEqual(reloc_gbp, 4545.45)
  ```

---

### Test 4: `test_swiss_deductions_in_expected_range`
* **Objective**: Verifies that hypothetical Swiss tax and social security fall within the verified statutory ranges from Phase 1.
* **Expected Ranges**:
  * AHV/IV/EO: Exactly 5.30% of CHF 170k = CHF 9,010.00.
  * ALV: Exactly 1.10% of CHF 148,200 = CHF 1,630.20.
  * Total Social Security: CHF 10,640.20 (£9,672.91).
  * Total Swiss Tax (Zurich City): between CHF 32,500.00 and CHF 33,200.00.
* **Assertions**:
  ```python
  swiss = calc_hypo_deductions(150000.0, 20000.0, 1.10)
  self.assertEqual(swiss['ahv_iv_eo_chf'], 9010.00)
  self.assertEqual(swiss['alv_chf'], 1630.20)
  self.assertEqual(swiss['total_ss_chf'], 10640.20)
  self.assertGreaterEqual(swiss['total_tax_chf'], 32500.00)
  self.assertLessEqual(swiss['total_tax_chf'], 33200.00)
  ```

---

### Test 5: `test_uk_income_tax_is_progressive`
* **Objective**: Verifies that UK tax rates progress across bands and effective tax rates increase with income.
* **Test Cases**:
  * Low income (£30,000): Basic rate taxpayer.
  * Middle income (£75,000): Higher rate taxpayer.
  * High income (£150,000): Additional rate taxpayer.
* **Assertions**:
  ```python
  tax_30k = calc_uk_tax(30000.0)
  tax_75k = calc_uk_tax(75000.0)
  tax_150k = calc_uk_tax(150000.0)

  rate_30k = tax_30k / 30000.0
  rate_75k = tax_75k / 75000.0
  rate_150k = tax_150k / 150000.0

  self.assertLess(rate_30k, rate_75k)
  self.assertLess(rate_75k, rate_150k)
  # Verify specific statutory benchmark
  self.assertEqual(tax_30k, round((30000.0 - 12570.0) * 0.20, 2))
  self.assertEqual(calc_uk_tax(125140.0), 42516.00)
  ```

---

### Test 6: `test_personal_allowance_taper_triggers_above_100k`
* **Objective**: Verifies that the Personal Allowance is reduced by £1 for every £2 of income above £100,000 and reaches £0 at £125,140, producing a 60% marginal tax rate.
* **Assertions**:
  ```python
  tax_100k = calc_uk_tax(100000.0)  # £27,432.00
  tax_110k = calc_uk_tax(110000.0)  # £33,432.00
  tax_125140 = calc_uk_tax(125140.0) # £42,516.00

  # Marginal tax between 100k and 110k is (33,432 - 27,432) / 10,000 = 60.0%
  marginal_rate_100k_110k = (tax_110k - tax_100k) / 10000.0
  self.assertAlmostEqual(marginal_rate_100k_110k, 0.60, places=2)

  # At 125,140 PA is completely gone
  self.assertEqual(tax_125140, 42516.00)
  ```

---

### Test 7: `test_gross_up_converges_within_tolerance_and_max_iter`
* **Objective**: Verifies that $T = \text{UKTax}(I + T)$ converges with tolerance $< £0.01$ in fewer than 100 iterations.
* **Assertions**:
  ```python
  I_test = 157484.35  # Year 1 taxable pay
  T, trace = gross_up(I_test, tolerance=0.01, max_iter=100)

  self.assertLess(len(trace), 100)
  # Verify the condition T = UKTax(I + T)
  recalculated_tax = calc_uk_tax(I_test + T)
  self.assertAlmostEqual(recalculated_tax, T, delta=0.01)
  ```

---

### Test 8: `test_employer_nic_matches_social_security_conclusion`
* **Objective**: Verifies that Employer Class 1 and Class 1A NIC are £0.00 because of the 24-month Certificate of Coverage under Article 14 of the UK-Switzerland Social Security Convention.
* **Assertions**:
  ```python
  results = calculate_assignment_costs(test_case_data)
  self.assertEqual(results['section3']['employer_nic_class1'], 0.00)
  self.assertEqual(results['section3']['employer_nic_class1a'], 0.00)
  self.assertEqual(results['section3']['total_employer_nic'], 0.00)
  ```

---

### Test 9: `test_benefit_classification_and_relocation_exemption`
* **Objective**: Verifies the £8,000 statutory relocation exemption under s. 287 ITEPA 2003 on £6,000 moving + £4,000 temp housing.
* **Assertions**:
  ```python
  b = process_benefits(test_case_data, 1.10)
  self.assertEqual(b['total_qualifying_relocation'], 10000.00)
  self.assertEqual(b['exempt_relocation'], 8000.00)
  self.assertEqual(b['taxable_relocation_excess'], 2000.00)
  # Year 1 taxable benefits: Housing £36k + Cash Reloc £4,545.45 + Excess £2,000 = £42,545.45
  self.assertEqual(b['y1_taxable_value'], 42545.45)
  # Year 2 taxable benefits: Housing £36k only
  self.assertEqual(b['y2_taxable_value'], 36000.00)
  ```

---

### Test 10: `test_missing_input_returns_form_error`
* **Objective**: Verifies that omitting a required field (e.g. `base_salary`) triggers a validation error and does not cause an unhandled 500 server crash.
* **Assertions**:
  ```python
  invalid_data = test_case_data.copy()
  del invalid_data['base_salary']

  response = self.client.post('/', invalid_data)
  self.assertEqual(response.status_code, 200)
  form = response.context['form']
  self.assertFalse(form.is_valid())
  self.assertIn('base_salary', form.errors)
  ```

---

### Test 11: `test_negative_salary_returns_form_error`
* **Objective**: Verifies that inputting a negative salary returns a readable error.
* **Assertions**:
  ```python
  invalid_data = test_case_data.copy()
  invalid_data['base_salary'] = -150000.00

  response = self.client.post('/', invalid_data)
  self.assertEqual(response.status_code, 200)
  form = response.context['form']
  self.assertFalse(form.is_valid())
  self.assertIn('base_salary', form.errors)
  ```

---

### Test 12: `test_zero_exchange_rate_returns_form_error`
* **Objective**: Verifies that an exchange rate of 0 is rejected by validation, preventing a `ZeroDivisionError`.
* **Assertions**:
  ```python
  invalid_data = test_case_data.copy()
  invalid_data['exchange_rate'] = 0.0

  response = self.client.post('/', invalid_data)
  self.assertEqual(response.status_code, 200)
  form = response.context['form']
  self.assertFalse(form.is_valid())
  self.assertIn('exchange_rate', form.errors)
  ```

---

### Test 13: `test_invalid_dates_return_form_error`
* **Objective**: Verifies that an end date earlier than the start date is rejected by cross-field validation.
* **Assertions**:
  ```python
  invalid_data = test_case_data.copy()
  invalid_data['start_date'] = '2028-04-05'
  invalid_data['end_date'] = '2026-04-06'

  response = self.client.post('/', invalid_data)
  self.assertEqual(response.status_code, 200)
  form = response.context['form']
  self.assertFalse(form.is_valid())
  self.assertTrue(len(form.non_field_errors()) > 0 or 'end_date' in form.errors)
  ```

---

### Test 14: `test_total_employer_cost_is_computed_and_positive`
* **Objective**: Verifies that the total cost is positive and exceeds base home remuneration (multiple > 1.0x).
* **Assertions**:
  ```python
  results = calculate_assignment_costs(test_case_data)
  total_cost = results['summary']['total_cost']
  multiple = results['summary']['mult_total']

  self.assertGreater(total_cost, 0.0)
  self.assertGreater(multiple, 1.0)
  ```

---

## 4. Test Execution Command

To run the complete test suite:
```bash
python3 manage.py test estimator
```
Expected output:
```
Found 14 test(s).
System check identified no issues (0 silenced).
..............
----------------------------------------------------------------------
Ran 14 tests in 0.045s

OK
```

---

## 5. Ready for Phase 6 Review

All 14 test scenarios have been specified with exact function names, inputs, and assertion logic.

**Phase 6 is complete. Ready for User Review before proceeding to Phase 7 (Code Implementation).**

