from django import forms


class CostEstimateForm(forms.Form):
    """
    Form for international assignment parameters between Switzerland and the UK.
    Pre-populated with baseline scenario values.
    """
    home_country = forms.CharField(
        max_length=100,
        initial='Switzerland',
        help_text="Country of origin where employee is currently employed."
    )
    home_city = forms.CharField(
        max_length=100,
        initial='Zurich',
        help_text="City determining cantonal and municipal tax rates (e.g. Zurich 119% Steuerfuss)."
    )
    host_country = forms.CharField(
        max_length=100,
        initial='United Kingdom',
        help_text="Host assignment country."
    )
    host_city = forms.CharField(
        max_length=100,
        initial='London',
        help_text="Assignment work location (tax jurisdiction: England)."
    )

    base_salary = forms.DecimalField(
        max_digits=12,
        decimal_places=2,
        initial=150000.00,
        help_text="Annual base salary in home currency (CHF). Must be greater than zero."
    )
    bonus = forms.DecimalField(
        max_digits=12,
        decimal_places=2,
        min_value=0.00,
        initial=20000.00,
        help_text="Annual incentive bonus in home currency (CHF)."
    )
    monthly_rent = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=0.00,
        initial=3000.00,
        help_text="Monthly accommodation rent in GBP (£) paid by employer (taxable BIK under s. 105 ITEPA)."
    )
    relocation_allowance = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=0.00,
        initial=5000.00,
        help_text="One-off cash relocation allowance in CHF for Year 1 (taxable cash under s. 62 ITEPA)."
    )
    moving_costs = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=0.00,
        initial=6000.00,
        help_text="One-off flights and shipping of personal effects in GBP for Year 1 (s. 273 ITEPA)."
    )
    temp_housing = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=0.00,
        initial=4000.00,
        help_text="One-off temporary accommodation / serviced apartment in GBP for first 4 weeks (s. 279 ITEPA)."
    )
    exchange_rate = forms.DecimalField(
        max_digits=6,
        decimal_places=4,
        initial=1.1000,
        help_text="Fixed exchange rate: £1.00 = X CHF (e.g. 1.1000). Converts Swiss home pay and tax to GBP."
    )
    start_date = forms.DateField(
        initial='2026-04-06',
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Assignment start date (matches UK tax year start 6 April 2026)."
    )
    end_date = forms.DateField(
        initial='2028-04-05',
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Assignment end date (matches UK tax year end 5 April 2028, exactly 24 months)."
    )

    def clean_base_salary(self):
        salary = self.cleaned_data.get('base_salary')
        if salary is None or salary <= 0:
            raise forms.ValidationError("Base salary must be a positive number")
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

