from django.contrib import admin
from .models import CalculationRun

@admin.register(CalculationRun)
class CalculationRunAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'country', 'gross_salary')
    readonly_fields = ('created_at',)
