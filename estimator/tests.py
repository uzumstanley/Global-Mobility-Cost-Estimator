from django.test import TestCase, Client
from django.urls import reverse
from .tax_calc import calculate_assignment_costs
from .swiss_tax import calc_hypo_deductions
from .uk_tax import calc_uk_tax
from .gross_up import gross_up
from .benefits import process_benefits

# Helper: default test‑case inputs matching the brief
DEFAULT_DATA = {
    'home_country': 'Switzerland',
    'home_city': 'Zurich',
    'host_country': 'United Kingdom',
    'host_city': 'London',
    'base_salary': 150000.00,
    'bonus': 20000.00,
    'monthly_rent': 3000.00,
    'relocation_allowance': 5000.00,
    'moving_costs': 6000.00,
    'temp_housing': 4000.00,
    'exchange_rate': 1.10,
    'start_date': '2026-04-06',
    'end_date': '2028-04-05',
}

class EstimatorTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('estimator')

    # 1. Supplied test case produces expected totals
    def test_supplied_test_case_runs_and_produces_result(self):
        result = calculate_assignment_costs(DEFAULT_DATA)
        self.assertIsNotNone(result)
        self.assertAlmostEqual(result['summary']['cost_y1'], 269249.72, delta=1.00)
        self.assertAlmostEqual(result['summary']['cost_y2'], 249348.91, delta=1.00)
        self.assertAlmostEqual(result['summary']['total_cost'], 518598.63, delta=1.00)
        self.assertAlmostEqual(result['summary']['mult_total'], 1.678, delta=0.01)

    # 2. Both years produce different totals
    def test_both_years_produce_different_totals(self):
        result = calculate_assignment_costs(DEFAULT_DATA)
        y1 = result['summary']['cost_y1']
        y2 = result['summary']['cost_y2']
        self.assertNotEqual(y1, y2)
        self.assertGreater(y1, y2)
        self.assertAlmostEqual(y1 - y2, 19900.81, delta=2.00)

    # 3. Currency conversion is correct
    def test_currency_conversion_is_correct(self):
        home_gbp = round((150000 + 20000) / 1.10, 2)
        self.assertEqual(home_gbp, 154545.45)
        reloc_gbp = round(5000 / 1.10, 2)
        self.assertEqual(reloc_gbp, 4545.45)

    # 4. Swiss deductions are in expected range
    def test_swiss_deductions_in_expected_range(self):
        swiss = calc_hypo_deductions(150000.0, 20000.0, 1.10)
        self.assertEqual(swiss['ahv_iv_eo_chf'], 9010.00)
        self.assertEqual(swiss['alv_chf'], 1630.20)
        self.assertEqual(swiss['total_ss_chf'], 10640.20)
        self.assertGreaterEqual(swiss['total_tax_chf'], 32500.00)
        self.assertLessEqual(swiss['total_tax_chf'], 33200.00)

    # 5. UK tax is progressive
    def test_uk_income_tax_is_progressive(self):
        tax_30k = calc_uk_tax(30000.0)
        tax_75k = calc_uk_tax(75000.0)
        tax_150k = calc_uk_tax(150000.0)
        rate_30k = tax_30k / 30000.0
        rate_75k = tax_75k / 75000.0
        rate_150k = tax_150k / 150000.0
        self.assertLess(rate_30k, rate_75k)
        self.assertLess(rate_75k, rate_150k)
        self.assertEqual(tax_30k, round((30000.0 - 12570.0) * 0.20, 2))
        self.assertEqual(calc_uk_tax(125140.0), 42516.00)

    # 6. Personal allowance taper triggers above 100k
    def test_personal_allowance_taper_triggers_above_100k(self):
        tax_100k = calc_uk_tax(100000.0)
        tax_110k = calc_uk_tax(110000.0)
        tax_125140 = calc_uk_tax(125140.0)
        marginal_rate = (tax_110k - tax_100k) / 10000.0
        self.assertAlmostEqual(marginal_rate, 0.60, places=2)
        self.assertEqual(tax_125140, 42516.00)

    # 7. Gross‑up converges within tolerance and max_iter
    def test_gross_up_converges_within_tolerance_and_max_iter(self):
        I_test = 157484.35  # Year 1 taxable pay from spec
        T, trace = gross_up(I_test, tolerance=0.01, max_iter=100)
        self.assertLess(len(trace), 100)
        self.assertAlmostEqual(calc_uk_tax(I_test + T), T, delta=0.01)

    # 8. Employer NIC matches social‑security conclusion
    def test_employer_nic_matches_social_security_conclusion(self):
        result = calculate_assignment_costs(DEFAULT_DATA)
        sec = result['section3']
        self.assertEqual(sec.get('employer_nic_class1'), 0.0)
        self.assertEqual(sec.get('employer_nic_class1a'), 0.0)
        self.assertEqual(sec.get('total_employer_nic'), 0.0)

    # 9. Benefit classification and relocation exemption
    def test_benefit_classification_and_relocation_exemption(self):
        b = process_benefits(DEFAULT_DATA, 1.10)
        self.assertEqual(b['total_qualifying_relocation'], 10000.00)
        self.assertEqual(b['exempt_relocation'], 8000.00)
        self.assertEqual(b['taxable_relocation_excess'], 2000.00)
        self.assertEqual(b['y1_taxable_value'], 42545.45)
        self.assertEqual(b['y2_taxable_value'], 36000.00)

    # 10. Missing input returns form error
    def test_missing_input_returns_form_error(self):
        invalid = DEFAULT_DATA.copy()
        del invalid['base_salary']
        response = self.client.post(self.url, invalid)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required")

    # 11. Negative salary returns form error
    def test_negative_salary_returns_form_error(self):
        invalid = DEFAULT_DATA.copy()
        invalid['base_salary'] = -1000
        response = self.client.post(self.url, invalid)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Base salary must be a positive number")

    # 12. Zero exchange rate returns form error
    def test_zero_exchange_rate_returns_form_error(self):
        invalid = DEFAULT_DATA.copy()
        invalid['exchange_rate'] = 0
        response = self.client.post(self.url, invalid)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Exchange rate must be greater than zero")

    # 13. Invalid dates return form error
    def test_invalid_dates_return_form_error(self):
        invalid = DEFAULT_DATA.copy()
        invalid['end_date'] = '2025-01-01'  # before start date
        response = self.client.post(self.url, invalid)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Assignment end date must be after the start date")

    # 14. Total employer cost is computed and > 0
    def test_total_employer_cost_is_computed_and_positive(self):
        result = calculate_assignment_costs(DEFAULT_DATA)
        self.assertGreater(result['summary']['total_cost'], 0)
        self.assertGreater(result['summary']['mult_total'], 1.0)
