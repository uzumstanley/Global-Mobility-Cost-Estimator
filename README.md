# Global Mobility Cost Estimator

## Installation

```bash
# Clone the repository (you will do this yourself)
# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
./venv/bin/pip install -r requirements.txt
```

## Running the application

```bash
# Apply migrations
./venv/bin/python manage.py migrate

# Start the development server
./venv/bin/python manage.py runserver
```

Open your browser at `http://127.0.0.1:8000/`. The cost estimator loads with the test‑case defaults and displays the full cost table immediately.

## Tests

```bash
# Run the test suite
./venv/bin/python manage.py test estimator
```

All 14 tests should pass.

## AI tools used

- **Research**: Google Gemini, ChatGPT – used only to look up tax legislation and immigration rules.
- **Code generation**: None – the code was written manually following the specification.

## Loom video

A short (5‑10 min) walkthrough video will be added here once recorded.

## Methodology & assumptions

- Exchange rate is a fixed input (default £1 = CHF 1.10).
- Swiss social security rates: AHV/IV/EO 5.30 %; ALV 1.10 % capped at CHF 148,200.
- Zurich cantonal multiplier 95 % and municipal multiplier 119 %.
- Personal tax CHF 24 per year.
- UK personal allowance £12,570 with taper above £100,000.
- UK tax bands 20 % up to £37,700 taxable, 40 % up to £125,140, 45 % above.
- Statutory relocation exemption cap £8,000 (ITEPA s. 287).
- Employer NIC is £0.00 under Article 14 Certificate of Coverage.

## Sources

- **Swiss Federal Tax Administration** – tax calculator and rates.
- **Zurich Cantonal Tax Office** – cantonal and municipal multipliers.
- **BSV (Swiss Social Insurance)** – AHV/IV/EO and ALV contribution rates.
- **GOV.UK** – UK income‑tax rates, personal allowance, NIC rates, immigration rules.
- **ITEPA 2003** – relocation benefit exemption rules.
- **UK‑Switzerland Social Security Convention** – Certificate of Coverage exemption.
