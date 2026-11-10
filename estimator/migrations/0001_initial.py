

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalculationRun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('home_country', models.CharField(default='Switzerland', max_length=100)),
                ('home_city', models.CharField(default='Zurich', max_length=100)),
                ('host_country', models.CharField(default='United Kingdom', max_length=100)),
                ('host_city', models.CharField(default='London', max_length=100)),
                ('base_salary', models.DecimalField(decimal_places=2, max_digits=12)),
                ('bonus', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('exchange_rate', models.DecimalField(decimal_places=4, default=1.1, max_digits=6)),
                ('total_y1_cost', models.DecimalField(decimal_places=2, max_digits=12)),
                ('total_y2_cost', models.DecimalField(decimal_places=2, max_digits=12)),
                ('total_assignment_cost', models.DecimalField(decimal_places=2, max_digits=12)),
                ('cost_multiple', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
