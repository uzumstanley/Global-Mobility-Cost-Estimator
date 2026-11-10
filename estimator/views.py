from django.shortcuts import render
from .forms import CostEstimateForm
from .tax_calc import calculate_assignment_costs
from .models import CalculationRun


def estimator_view(request):
    """Handle display and processing of the cost estimator.
    On GET we pre‑populate the form with the test‑case defaults and display the calculated result.
    On POST we validate the form, perform the calculation, save a record, and redisplay.
    """
    if request.method == 'POST':
        form = CostEstimateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            result = calculate_assignment_costs(data)
            # Store summary in the audit model
            CalculationRun.objects.create(
                home_country=data['home_country'],
                home_city=data['home_city'],
                host_country=data['host_country'],
                host_city=data['host_city'],
                base_salary=data['base_salary'],
                bonus=data['bonus'],
                exchange_rate=data['exchange_rate'],
                total_y1_cost=result['summary']['cost_y1'],
                total_y2_cost=result['summary']['cost_y2'],
                total_assignment_cost=result['summary']['total_cost'],
                cost_multiple=result['summary']['mult_total'],
            )
            return render(request, 'estimator/estimator.html', {
                'form': form,
                'result': result,
                'show_result': True,
            })
        else:
            # Return form with errors
            return render(request, 'estimator/estimator.html', {
                'form': form,
                'result': None,
                'show_result': False,
            })
    else:
        # GET – initialise with defaults and compute once
        form = CostEstimateForm()
        if form.is_valid():
            data = form.cleaned_data
            result = calculate_assignment_costs(data)
        else:
            result = None
        return render(request, 'estimator/estimator.html', {
            'form': form,
            'result': result,
            'show_result': True,
        })
