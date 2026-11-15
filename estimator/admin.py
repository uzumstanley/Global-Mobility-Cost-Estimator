from django.contrib import admin
from .models import CalculationRun

@admin.register(CalculationRun)
class CalculationRunAdmin(admin.ModelAdmin):
    # Show useful columns that actually exist on the model
    list_display = (
        'created_at',          # timestamp of the run
        'home_country',        # source country of the employee
        'host_country',        # destination country
        'base_salary',         # gross salary before any adjustments
        'total_assignment_cost',  # final cost for the assignment
    )
    readonly_fields = ('created_at',)
