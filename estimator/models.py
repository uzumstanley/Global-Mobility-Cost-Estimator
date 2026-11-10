from django.db import models


class CalculationRun(models.Model):
    """
    Audit log of cost calculations performed through the interface.
    Stores the key input parameters and high-level results for tracking.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    home_country = models.CharField(max_length=100, default='Switzerland')
    home_city = models.CharField(max_length=100, default='Zurich')
    host_country = models.CharField(max_length=100, default='United Kingdom')
    host_city = models.CharField(max_length=100, default='London')

    base_salary = models.DecimalField(max_digits=12, decimal_places=2)
    bonus = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    exchange_rate = models.DecimalField(max_digits=6, decimal_places=4, default=1.1000)

    total_y1_cost = models.DecimalField(max_digits=12, decimal_places=2)
    total_y2_cost = models.DecimalField(max_digits=12, decimal_places=2)
    total_assignment_cost = models.DecimalField(max_digits=12, decimal_places=2)
    cost_multiple = models.DecimalField(max_digits=6, decimal_places=3)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Estimate {self.id} ({self.created_at:%Y-%m-%d %H:%M}) - Total: £{self.total_assignment_cost:,.2f}"
