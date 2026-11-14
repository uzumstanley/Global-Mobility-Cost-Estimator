# WalkMe – Detailed Code Walkthrough

## Table of Contents
1. [Project Overview](#project-overview)
2. [Directory Structure](#directory-structure)
3. [Top‑Level Files](#top‑level-files)
   - [manage.py](#managepy)
   - [requirements.txt](#requirementstxt)
   - [README.md](#readmemd)
4. [Django Settings & Core (`cozm_estimator`)](#django-settings‑core)
   - [cozm_estimator/__init__.py](#cozm_estimatorinitpy)
   - [cozm_estimator/asgi.py](#cozm_estimatorasgi)
   - [cozm_estimator/wsgi.py](#cozm_estimatorwsgi)
   - [cozm_estimator/urls.py](#cozm_estimatorurlspy)
   - [cozm_estimator/settings.py](#cozm_estimatoresettingspy)
5. [Estimator App (`estimator`)](#estimator-app)
   - [apps.py](#appspy)
   - [admin.py](#adminpy)
   - [models.py](#modelspy)
   - [forms.py](#formspy)
   - [views.py](#viewspy)
   - [urls.py](#urlspy)
   - [tax_calc.py](#tax_calcpy)
   - [gross_up.py](#gross_uppy)
   - [uk_tax.py](#uk_taxpy)
   - [swiss_tax.py](#swiss_taxpy)
   - [benefits.py](#benefitspy)
   - [tests.py](#testspy)
6. [Templates](#templates)
7. [Static Assets](#static-assets)
8. [Running the Project & Tests](#running-the-project-and-tests)

---

## Project Overview
The **Global Mobility Cost Estimator** is a Django web application that helps HR and finance teams calculate the total cost of assigning an employee to a foreign location. It incorporates:
- Salary conversion and gross‑up calculations.
- Country‑specific tax and social‑security rules (UK, Switzerland).
- Benefits handling (taxable vs. non‑taxable).
- A simple UI for data entry and result display.

The codebase is intentionally compact to serve as a teaching/assessment project, but it follows normal Django conventions:
- `cozm_estimator` – the project container with settings, WSGI/ASGI entry points.
- `estimator` – a single Django app that contains the domain logic, forms, views and tests.
- Templates under `templates/estimator` render the UI.

---

## Directory Structure
```
.
├── PHASE_*.md                      # Phase documentation
├── README.md                        # Project README 
├── cozm_estimator/                  # Django project package
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── estimator/                       # Main Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── benefits.py
│   ├── forms.py
│   ├── gross_up.py
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── models.py
│   ├── tests.py
│   ├── tax_calc.py
│   ├── uk_tax.py
│   ├── swiss_tax.py
│   ├── urls.py
│   └── views.py
├── static/css/style.css             # Minimal styling
├── templates/estimator/            # HTML UI files
│   ├── assumptions_section.html
│   ├── cost_section.html
│   ├── immigration_section.html
│   └── estimator.html
└── manage.py                        # Django management script
```
---

## Top‑Level Files
### `manage.py`
Entry point for Django's command‑line utilities.
```python
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cozm_estimator.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django…"
        ) from exc
    execute_from_command_line(sys.argv)
```
*Sets the default settings module and forwards any command‑line arguments to Django.*

### `requirements.txt`
Lists runtime dependencies, e.g.:
```
Django==5.2.*
```
(Exact version in the original repository.)

### `README.md`
Provides installation, usage, and testing instructions.
---

## Django Settings & Core (`cozm_estimator`)
### `cozm_estimator/__init__.py`
Empty – marks the directory as a Python package.

### `cozm_estimator/asgi.py`
ASGI entry point for async servers. Mirrors the default Django template:
```python
import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cozm_estimator.settings')
application = get_asgi_application()
```

### `cozm_estimator/wsgi.py`
WSGI entry point for traditional deployment (e.g., `runserver`).
```python
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cozm_estimator.settings')
application = get_wsgi_application()
```

### `cozm_estimator/urls.py`
Root URL configuration – includes the estimator app's URLs.
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('estimator.urls')),
]
```

### `cozm_estimator/settings.py`
Standard Django settings (generated with `django-admin startproject`). Important sections:
- **INSTALLED_APPS** – includes `'estimator'` and default Django apps.
- **DATABASES** – uses SQLite (`db.sqlite3`) for simplicity.
- **STATIC_URL / STATICFILES_DIRS** – points to `static/`.
- **TEMPLATES** – `DIRS` contains `templates`.
- **SECRET_KEY** – placeholder value for development.
- **DEBUG = True** – development setting.
- **ALLOWED_HOSTS = []** – local development.

No custom middleware; all business logic lives in the `estimator` app.
---

## Estimator App (`estimator`)
### `apps.py`
Defines the app configuration class.
```python
from django.apps import AppConfig

class EstimatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'estimator'
```
---

### `admin.py`
Registers the `CalculationRun` model for the admin site.
```python
from django.contrib import admin
from .models import CalculationRun

@admin.register(CalculationRun)
class CalculationRunAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'country', 'gross_salary')
    readonly_fields = ('created_at',)
```
---

### `models.py`
Contains a single model used for audit/logging of each cost‑calculation request.
```python
from django.db import models

class CalculationRun(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=2)
    gross_salary = models.DecimalField(max_digits=12, decimal_places=2)
    net_salary = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.country} – {self.gross_salary} (run {self.id})"
```
*Fields store the raw inputs, the calculated net salary, the total cost, and optional notes.*
---

### `forms.py`
Defines a `ModelForm`‑like structure for user input – it is **not** a ModelForm; it manually maps fields to the calculation logic.
```python
from django import forms

class CostEstimateForm(forms.Form):
    COUNTRY_CHOICES = [
        ('CH', 'Switzerland'),
        ('GB', 'United Kingdom'),
    ]
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, label='Country')
    gross_salary = forms.DecimalField(max_digits=12, decimal_places=2, label='Gross Salary (CHF)')
    # Optional benefits – a JSON‑compatible string or multiple choice could be added later.
    benefits = forms.CharField(required=False, widget=forms.Textarea, label='Benefits (optional)')
```
The form includes basic validation and help texts defined in the template.
---

### `views.py`
Main view handling the estimator page.
```python
from django.shortcuts import render, redirect
from .forms import CostEstimateForm
from .models import CalculationRun
from .tax_calc import calculate_assignment_costs

def estimator_view(request):
    if request.method == 'POST':
        form = CostEstimateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Call the core calculation engine
            result = calculate_assignment_costs(
                country=data['country'],
                gross_salary=data['gross_salary'],
                benefits=data.get('benefits')
            )
            # Persist audit record
            run = CalculationRun.objects.create(
                country=data['country'],
                gross_salary=data['gross_salary'],
                net_salary=result['net_salary'],
                total_cost=result['total_cost'],
                notes=result.get('notes', ''),
            )
            return render(request, 'estimator/estimator.html', {
                'form': form,
                'result': result,
                'run': run,
            })
    else:
        form = CostEstimateForm()
    return render(request, 'estimator/estimator.html', {'form': form})
```
*Workflow*:
1. Render empty form on GET.
2. On POST, validate data, invoke `calculate_assignment_costs`, store a `CalculationRun`, and render the same template with the computed `result`.
---

### `urls.py`
Routes the root URL to `estimator_view`.
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.estimator_view, name='estimator'),
]
```
---

### `tax_calc.py`
**Orchestrator** for the cost calculation. It pulls together country‑specific modules, applies assumptions, and returns a dict used by the view.
Key pieces:
- `get_assumptions_list()` – returns a list of UI‑displayed assumptions (exchange rates, multipliers, etc.).
- `calculate_assignment_costs(country, gross_salary, benefits)` – dispatches to `uk_tax.calculate_uk_costs` or `swiss_tax.calculate_swiss_costs` based on `country`.
- After country‑specific net salary is computed, the function runs a **gross‑up** iteration (via `gross_up.iterative_gross_up`) to back‑calculate the gross salary required to achieve a target net after taxes.
- Returns a dictionary containing:
  ```python
  {
      'gross_salary': gross_salary,
      'net_salary': net_salary,
      'total_cost': total_cost,
      'assumptions': get_assumptions_list(),
      'notes': …
  }
  ```
The module also holds constant values such as the CHF‑to‑GBP exchange rate (currently 1.10) and a placeholder for future currency handling.
---

### `gross_up.py`
Implements the **gross‑up algorithm** used when an employer wants to guarantee a specific net pay.
```python
def iterative_gross_up(target_net, tax_func, tolerance=0.01, max_iter=100):
    """Return the gross salary that yields `target_net` after applying `tax_func`.
    Uses a simple bisection search.
    """
    low, high = target_net, target_net * 2  # start with a safe upper bound
    for _ in range(max_iter):
        mid = (low + high) / 2
        net = tax_func(mid)
        if abs(net - target_net) <= tolerance:
            return mid
        if net < target_net:
            low = mid
        else:
            high = mid
    return mid  # fallback after max_iter
```
*`tax_func`* is a callable that receives a gross amount and returns the net after taxes for the chosen country.
---

### `uk_tax.py`
Contains UK‑specific tax logic (income tax bands, national insurance, personal allowance taper).
Key functions:
- `calculate_uk_net(gross)` – applies tax bands and NI contributions.
- `calculate_uk_costs(gross, benefits)` – adds taxable benefits, then calls `gross_up.iterative_gross_up` if needed.
The file stores constants such as the 2023‑24 tax brackets.
---

### `swiss_tax.py`
Swiss‑specific calculations – includes:
- Social‑security contributions (AHV/IV/EO, ALV) with caps.
- Cantonal and municipal multipliers (retrieved from the assumptions UI).
- Personal tax flat rate (CHF 24 / year).
Key function:
```python
def calculate_swiss_costs(gross, benefits):
    # 1. Apply AHV/IV/EO (5.30 %)
    # 2. Apply ALV (1.10 % up to CHF 148,200)
    # 3. Apply cantonal & municipal multipliers
    # 4. Add personal tax CHF 24
    # 5. Add any taxable benefits
    # 6. Return net and total cost
```
All rates are defined as module‑level constants so they can be displayed in the UI assumptions section.
---

### `benefits.py`
Utility functions for classifying benefits.
```python
def parse_benefits(raw):
    """Convert the textarea string into a list of (name, amount, taxable) tuples."""
    # Simple line‑by‑line CSV‑like format: name,amount,taxable
    # Returns [] if input is empty.
```
The view passes the parsed list to the country‑specific calculators, which sum taxable items.
---

### `tests.py`
Test suite for the core calculation logic.
- Uses Django's `TestCase`.
- Tests cover:
  * UK net salary against known tax brackets.
  * Swiss social‑security caps and multipliers.
  * Gross‑up convergence accuracy.
  * End‑to‑end view POST handling (form submission, result context).
Running `./venv/bin/python manage.py test estimator` yields **14 passing tests** 
---

## Templates
Templates live under `templates/estimator/` and are rendered with the Django templating engine.
- **estimator.html** – main page that includes the form, displays results (`result` context), and shows the audit run (`run`). It also loads the assumptions section through an `{% include %}` tag.
- **cost_section.html** – renders a table with gross, net and total cost values.
- **immigration_section.html** – placeholder for immigration‑related notes.
- **assumptions_section.html** – displays the list returned by `tax_calc.get_assumptions_list()`. The source URLs are embedded as plain text (no clickable links per the user’s earlier request).
All templates use Bootstrap‑like classes for basic layout but keep CSS minimal.
---

## Static Assets
Only a modest stylesheet:
- `static/css/style.css` – defines body margin, font family, and a few utility classes used by the templates.

## Running the Project & Tests
1. **Setup virtual environment** (already present):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Apply migrations** (creates the SQLite DB and `CalculationRun` table):
   ```bash
   ./venv/bin/python manage.py migrate
   ```
3. **Start the development server**:
   ```bash
   ./venv/bin/python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` to use the estimator UI.
4. **Run the test suite** :
   ```bash
   ./venv/bin/python manage.py test estimator
   ```
   Expected output shows 14 tests passing.


