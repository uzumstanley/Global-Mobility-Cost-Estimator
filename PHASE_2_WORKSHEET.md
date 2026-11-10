# Phase 2: Calculation Methodology and Mathematical Worksheet
**Global Mobility Cost Estimator (Switzerland → UK Assignment)**
**Case Study**: Swiss National, Single, 2-Year Assignment from Zurich to London (6 April 2026 to 5 April 2028)

---

## Overview & Core Principles

This worksheet sets out the complete, step-by-step mathematical model and figures for the test case, derived strictly from the statutory research verified in Phase 1. 

### Core Concepts Applied
1. **Tax Equalisation**: The employee pays only the hypothetical tax and social security they would have borne had they remained working in Zurich, Switzerland. The employer pays all UK host income taxes on the assignment earnings and benefits.
2. **Hypothetical Tax & Social Security**: Deducted from the employee's gross home pay to establish their net home pay, and deducted from the employer's assignment cost table.
3. **Tax on Tax (Gross-Up)**: UK tax paid by the employer on behalf of the employee is treated under UK tax law as taxable employment earnings (an economic benefit). It must be grossed up iteratively so that the grossed-up figure pays both the tax on the cash/benefits and the tax on the employer-paid tax itself.
4. **Social Security Certificate of Coverage**: Under Article 14(1) of the UK-Switzerland Social Security Coordination Convention, a 2-year assignment covered by a Swiss Certificate of Coverage (PDA1) is legally exempt from UK National Insurance for both employee and employer.

---

## Input Parameters (Test Case)

| Parameter | Value in Case Study | Notes / References |
| :--- | :--- | :--- |
| **Home Country / City** | Switzerland / City of Zurich | Canton of Zurich, Municipality BFS 261 |
| **Host Country / City** | United Kingdom / London | Resident for two UK tax years (2026/27 & 2027/28) |
| **Marital / Family Status** | Single, no children | Grundtarif (§ 35 StG ZH & Art. 36 DBG) |
| **Church Affiliation** | None (*konfessionslos*) | 0% church tax in Zurich |
| **Base Salary** | CHF 150,000.00 / year | Fixed for both years |
| **Annual Bonus** | CHF 20,000.00 / year | Fixed for both years |
| **Total Gross Remuneration** | **CHF 170,000.00 / year** | Base + Bonus |
| **London Housing** | £3,000.00 / month (£36,000.00 / year) | Rent paid directly to landlord by employer |
| **Relocation Allowance** | CHF 5,000.00 (Year 1 only) | Lump-sum cash paid directly to employee |
| **Moving Costs** | £6,000.00 (Year 1 only) | Flights and shipping of household goods |
| **Temporary Housing** | £4,000.00 (Year 1 only) | Serviced apartment for first 4 weeks |
| **Exchange Rate** | **£1.00 = CHF 1.10** | Fixed for both years (1 CHF = £0.9090909) |

---

## Step A: Hypothetical Swiss Deductions

Under tax equalisation, the employee is charged hypothetical Swiss income tax and social security contributions as if they had remained working in Zurich.

### 1. Swiss Social Security Contributions (Pillar 1)
Swiss social security contributions are mandatory and deductible in determining Swiss taxable income. (Occupational pension / BVG is excluded per brief instructions).

* **AHV / IV / EO (First Pillar)**:
  * Statutory rate: **5.30% employee share** (AHV 4.35%, IV 0.70%, EO 0.25%).
  * Ceiling: **No ceiling**.
  * Calculation: `CHF 170,000.00 * 5.30% = CHF 9,010.00`.
* **ALV (Unemployment Insurance)**:
  * Statutory rate: **1.10% employee share** up to maximum insurable earnings.
  * Statutory ceiling: **CHF 148,200.00 per year** (Art. 3 AVIG; solidarity surcharge abolished 1 Jan 2023).
  * Calculation: `CHF 148,200.00 * 1.10% = CHF 1,630.20`.
* **Total Annual Hypothetical Social Security**:
  * In CHF: `CHF 9,010.00 + CHF 1,630.20 = CHF 10,640.20`.
  * In GBP (at £1 = CHF 1.10): `CHF 10,640.20 / 1.10 = £9,672.91`.

### 2. Swiss Hypothetical Income Tax (Zurich City, Single, No Church Tax)
* **Gross Earnings**: CHF 170,000.00.
* **Standard Deductions**:
  * 1st Pillar Social Security: CHF 10,640.20.
  * Standard Professional Expenses (*Übrige Berufskosten*): 3% capped at **CHF 4,000.00**.
  * Insurance Premiums & Savings Interest (*Versicherungsprämienabzug*): **CHF 2,900.00** for Cantonal/Municipal (§ 31 Abs. 1 StG ZH); **CHF 1,800.00** for Direct Federal Tax.
* **Taxable Income (*Steuerbares Einkommen*)**:
  * Cantonal / Municipal: `CHF 170,000 - 10,640.20 - 4,000 - 2,900 = CHF 152,459.80` -> rounded to **CHF 152,400.00**.
  * Direct Federal: `CHF 170,000 - 10,640.20 - 4,000 - 1,800 = CHF 153,559.80` -> rounded to **CHF 153,500.00**.
* **Statutory Tax Calculations**:
  1. **Direct Federal Tax (*Direkte Bundessteuer*)**:
     * Base tax at CHF 141,500 = CHF 6,140.55.
     * Marginal rate between CHF 141,500 and CHF 185,900 = 11.00%.
     * Tax on excess: `(CHF 153,500 - 141,500) * 11.00% = CHF 12,000 * 11.00% = CHF 1,320.00`.
     * Total Direct Federal Tax = `CHF 6,140.55 + CHF 1,320.00 = CHF 7,460.55`.
  2. **Base Cantonal Tax (*Einfache Staatssteuer*)**:
     * Applying § 35 Abs. 1 StG ZH tariff up to CHF 152,400 = **CHF 11,889.00**.
  3. **Cantonal Tax (*Staatssteuer*)**:
     * Multiplier (*Staatssteuerfuss*) for 2026: **95%**.
     * `CHF 11,889.00 * 95% = CHF 11,294.55`.
  4. **Municipal Tax (*Gemeindesteuer Zürich Stadt*)**:
     * Multiplier (*Gemeindesteuerfuss*) for City of Zurich: **119%**.
     * `CHF 11,889.00 * 119% = CHF 14,147.91`.
  5. **Personal Tax (*Personalsteuer*)**: Flat fee of **CHF 24.00**.
  6. **Church Tax (*Kirchensteuer*)**: **CHF 0.00** (non-denominational).
* **Total Annual Hypothetical Swiss Income Tax**:
  * In CHF: `CHF 7,460.55 + CHF 11,294.55 + CHF 14,147.91 + CHF 24.00 = CHF 32,927.01`.
  * In GBP (at £1 = CHF 1.10): `CHF 32,927.01 / 1.10 = £29,933.65`.

### 3. Total Annual Hypothetical Deductions Summary
* **Total Deductions in CHF**: `CHF 32,927.01 (Tax) + CHF 10,640.20 (Social Security) = CHF 43,567.21`.
* **Total Deductions in GBP**: `£29,933.65 (Tax) + £9,672.91 (Social Security) = £39,606.55`.
* **Net Home Pay (GBP)**:
  * Gross Home Pay: `CHF 170,000 / 1.10 = £154,545.45`.
  * Deductions: `-£39,606.55`.
  * **Net Home Pay**: `£154,545.45 - £39,606.55 = £114,938.90` (equivalent to `CHF 126,432.79 / 1.10`).

---

## Step B: Assignment Benefits & UK Taxable Pay (I)

### Benefit Classification & Statutory Exemption Rules

1. **London Housing (£36,000.00 / year, Years 1 & 2)**:
   * Rent paid directly by employer to landlord.
   * Statutory rule: Living accommodation under s. 105 ITEPA 2003. Cash equivalent equals the rent paid (£36,000.00).
   * **Classification**: **Taxable Benefit in Kind (BIK)**.
   * **Employer Cost**: £36,000.00 / year.
   * **Taxable Value**: £36,000.00 / year.

2. **Relocation Allowance (CHF 5,000.00, Year 1 only)**:
   * Unvouched lump-sum cash allowance paid to employee.
   * Statutory rule: General earnings under s. 62 ITEPA 2003. Round-sum cash allowances do not qualify for the s. 271 removal exemption.
   * **Conversion**: `CHF 5,000.00 / 1.10 = £4,545.45`.
   * **Classification**: **Taxable cash**.
   * **Employer Cost**: £4,545.45.
   * **Taxable Value**: £4,545.45.

3. **Moving Costs (£6,000.00, Year 1 only)**:
   * Flights and shipping of personal belongings.
   * Statutory rule: Qualifying removal expense under ss. 273, 277, 278 ITEPA 2003.
   * **Employer Cost**: £6,000.00.

4. **Temporary Housing (£4,000.00, Year 1 only)**:
   * Serviced apartment for first 4 weeks while finding permanent home.
   * Statutory rule: Qualifying temporary living accommodation under s. 279 ITEPA 2003 & HMRC EIM03117.
   * **Employer Cost**: £4,000.00.

5. **Application of the £8,000 Statutory Relocation Exemption Cap (s. 287 ITEPA 2003)**:
   * Total qualifying relocation expenses: `£6,000.00 (moving) + £4,000.00 (temp housing) = £10,000.00`.
   * Statutory Cap: **£8,000.00**.
   * **Exempt Portion**: **£8,000.00** (Not taxable; £0 enters tax calculation).
   * **Taxable Excess**: `£10,000.00 - £8,000.00 = £2,000.00`.
   * **Classification of Excess**: **Taxable Benefit in Kind (BIK)**.

### No Double-Counting Rule
* **In the Cost Table**: Actual employer expenditure appears in Section 2 (Assignment Benefits):
  * Year 1 actual expenditure: `£36,000 + £4,545.45 + £6,000 + £4,000 = £50,545.45`.
  * Year 2 actual expenditure: `£36,000.00`.
* **In the Tax Calculation**: Only the **taxable value** of benefits enters UK Taxable Pay ($I$):
  * Year 1 taxable benefits: `£36,000 (housing) + £4,545.45 (cash reloc) + £2,000 (excess reloc) = £42,545.45`.
  * Year 2 taxable benefits: `£36,000.00 (housing)`.

### UK Taxable Pay Before Tax ($I$)
* Formula: `I = Net Home Pay + UK Taxable Benefits`.
* **Year 1**:
  $$I_1 = £114,938.90 + £42,545.45 = \mathbf{£157,484.35}$$
* **Year 2**:
  $$I_2 = £114,938.90 + £36,000.00 = \mathbf{£150,938.90}$$

---

## Step C: Iterative Gross-Up Calculation

The UK tax $T$ paid by the employer satisfies the non-linear equation:
$$T = \text{UKTax}(I + T)$$

Because UK tax rates progress across bands (20%, 40%, 45%) and the Personal Allowance (£12,570) tapers by £1 per £2 of income between £100,000 and £125,140, a single multiplication gives an erroneous answer. The gross-up must be solved by iteration.

### UK Tax Calculation Algorithm: $\text{UKTax}(G)$
For any total gross income $G$:
1. **Personal Allowance (PA)**:
   * If $G \le £100,000$: $\text{PA} = £12,570.00$.
   * If $£100,000 < G < £125,140$: $\text{PA} = £12,570.00 - \frac{G - £100,000}{2}$.
   * If $G \ge £125,140$: $\text{PA} = £0.00$.
2. **Taxable Income**: $\text{Taxable} = \max(0, G - \text{PA})$.
3. **Application of Bands (England / NI 2026/27)**:
   * **Basic Rate (20%)**: First £37,700 of taxable income $\to$ maximum tax £7,540.00.
   * **Higher Rate (40%)**:
     * If $G \le £125,140$: applied to taxable income above £37,700.
     * If $G > £125,140$: applied to the fixed slice of £87,440 (from £37,700 to £125,140) $\to$ tax £34,976.00.
   * **Additional Rate (45%)**: Applied to all income exceeding **£125,140.00**.
4. **Cumulative Benchmark (for $G \ge £125,140$)**:
   $$\text{UKTax}(G) = £7,540.00 + £34,976.00 + 0.45 \times (G - £125,140.00) = £42,516.00 + 0.45 \times (G - £125,140.00)$$

### Iteration Protocol
* Start with initial estimate: $T_0 = \text{UKTax}(I)$.
* At each iteration $k \ge 1$:
  $$T_k = \text{UKTax}(I + T_{k-1})$$
* Stop when $|T_k - T_{k-1}| < £0.01$ (tolerance 1 penny) or iteration count reaches 100.

---

### Year 1 Iteration Trace ($I_1 = £157,484.35$)

* Initial seed: $T_0 = \text{UKTax}(£157,484.35) = £42,516.00 + 0.45 \times (£157,484.35 - £125,140.00) = £57,070.96$.

| Iteration ($k$) | $T_{k-1}$ (Old Tax) | Gross Pay ($I + T_{k-1}$) | $T_k = \text{UKTax}(I + T_{k-1})$ | Absolute Difference |
| :---: | :---: | :---: | :---: | :---: |
| **0 (Seed)** | £0.00 | £157,484.35 | £57,070.96 | — |
| **1** | £57,070.96 | £214,555.31 | £82,752.89 | £25,681.93 |
| **2** | £82,752.89 | £240,237.24 | £94,309.76 | £11,556.87 |
| **3** | £94,309.76 | £251,794.11 | £99,510.35 | £5,200.59 |
| **4** | £99,510.35 | £256,994.70 | £101,850.61 | £2,340.27 |
| **5** | £101,850.61 | £259,334.96 | £102,903.73 | £1,053.12 |
| **6** | £102,903.73 | £260,388.08 | £103,377.64 | £473.90 |
| **7** | £103,377.64 | £260,861.99 | £103,590.89 | £213.26 |
| **8** | £103,590.89 | £261,075.24 | £103,686.86 | £95.97 |
| **9** | £103,686.86 | £261,171.21 | £103,730.04 | £43.18 |
| **10** | £103,730.04 | £261,214.39 | £103,749.48 | £19.43 |
| **11** | £103,749.48 | £261,233.83 | £103,758.22 | £8.74 |
| **12** | £103,758.22 | £261,242.57 | £103,762.16 | £3.94 |
| **13** | £103,762.16 | £261,246.51 | £103,763.93 | £1.77 |
| **14** | £103,763.93 | £261,248.28 | £103,764.73 | £0.80 |
| **15** | £103,764.73 | £261,249.08 | £103,765.08 | £0.36 |
| **16** | £103,765.08 | £261,249.43 | £103,765.25 | £0.16 |
| **17** | £103,765.25 | £261,249.60 | £103,765.32 | £0.07 |
| **18** | £103,765.32 | £261,249.67 | £103,765.35 | £0.03 |
| **19** | £103,765.35 | £261,249.70 | £103,765.37 | £0.01 |
| **20 (Converged)** | **£103,765.37** | **£261,249.72** | **£103,765.37** | **£0.007 < £0.01** |

* **Year 1 UK Tax Result ($T_1$)**: **£103,765.37**
* **Total Grossed-Up Taxable Pay ($I_1 + T_1$)**: **£261,249.72**
* **Verification**:
  * First £37,700 @ 20% = £7,540.00
  * Next £87,440 (up to £125,140) @ 40% = £34,976.00
  * Excess above £125,140 (£136,109.72) @ 45% = £61,249.37
  * Total Tax = `£7,540.00 + £34,976.00 + £61,249.37 = £103,765.37`. Matches to the exact penny.

---

### Year 2 Iteration Trace ($I_2 = £150,938.90$)

* Initial seed: $T_0 = \text{UKTax}(£150,938.90) = £42,516.00 + 0.45 \times (£150,938.90 - £125,140.00) = £54,125.50$.

| Iteration ($k$) | $T_{k-1}$ (Old Tax) | Gross Pay ($I + T_{k-1}$) | $T_k = \text{UKTax}(I + T_{k-1})$ | Absolute Difference |
| :---: | :---: | :---: | :---: | :---: |
| **0 (Seed)** | £0.00 | £150,938.90 | £54,125.50 | — |
| **1** | £54,125.50 | £205,064.40 | £78,481.98 | £24,356.48 |
| **2** | £78,481.98 | £229,420.88 | £89,442.40 | £10,960.41 |
| **3** | £89,442.40 | £240,381.30 | £94,374.58 | £4,932.19 |
| **4** | £94,374.58 | £245,313.48 | £96,594.07 | £2,219.48 |
| **5** | £96,594.07 | £247,532.97 | £97,592.84 | £998.77 |
| **6** | £97,592.84 | £248,531.74 | £98,042.28 | £449.45 |
| **7** | £98,042.28 | £248,981.18 | £98,244.53 | £202.25 |
| **8** | £98,244.53 | £249,183.43 | £98,335.54 | £91.01 |
| **9** | £98,335.54 | £249,274.44 | £98,376.50 | £40.96 |
| **10** | £98,376.50 | £249,315.40 | £98,394.93 | £18.43 |
| **11** | £98,394.93 | £249,333.83 | £98,403.22 | £8.29 |
| **12** | £98,403.22 | £249,342.12 | £98,406.96 | £3.73 |
| **13** | £98,406.96 | £249,345.86 | £98,408.64 | £1.68 |
| **14** | £98,408.64 | £249,347.54 | £98,409.39 | £0.76 |
| **15** | £98,409.39 | £249,348.29 | £98,409.73 | £0.34 |
| **16** | £98,409.73 | £249,348.63 | £98,409.88 | £0.15 |
| **17** | £98,409.88 | £249,348.78 | £98,409.95 | £0.07 |
| **18** | £98,409.95 | £249,348.85 | £98,409.98 | £0.03 |
| **19** | £98,409.98 | £249,348.88 | £98,410.00 | £0.01 |
| **20 (Converged)** | **£98,410.00** | **£249,348.90** | **£98,410.01** | **£0.006 < £0.01** |

* **Year 2 UK Tax Result ($T_2$)**: **£98,410.01**
* **Total Grossed-Up Taxable Pay ($I_2 + T_2$)**: **£249,348.91**
* **Verification**:
  * First £37,700 @ 20% = £7,540.00
  * Next £87,440 (up to £125,140) @ 40% = £34,976.00
  * Excess above £125,140 (£124,208.91) @ 45% = £55,894.01
  * Total Tax = `£7,540.00 + £34,976.00 + £55,894.01 = £98,410.01`. Matches to the exact penny.

---

## Step D: Employer National Insurance (NIC)

* **Statutory Analysis**:
  * As verified in Phase 1 (Section 1.4 & 1.6), under **Article 14(1) of the UK-Switzerland Convention on Social Security Coordination**, an employee posted from Switzerland to the UK for up to 24 months holding a valid Swiss Certificate of Coverage (PDA1) remains subject exclusively to Swiss social security legislation.
  * Employer liability strictly follows employee liability under GOV.UK guidance and bilateral treaty rules.
* **Liability**:
  * **Class 1 Secondary (Employer) NIC on cash earnings**: **£0.00**
  * **Class 1A NIC on taxable benefits in kind**: **£0.00**
  * **Class 1B NIC on gross-up tax**: **£0.00**
* *(Note: If no Certificate of Coverage were held, secondary Class 1 NIC at 15.0% above £5,000 threshold and Class 1A NIC at 15.0% on £42,545.45 of benefits would have added over £35,000 per year to employer costs. The Certificate of Coverage saves the employer substantial cost).*

---

## Step E: Complete Cost Table (Four Sections, Exact Order)

The brief requires the output to answer one central question: **What does this assignment cost the employer each year?**

### Section 1: Home Pay (As If Employee Had Stayed in Switzerland)
| Component | Amount in CHF | Exchange Rate | Amount in GBP |
| :--- | :---: | :---: | :---: |
| **Base Salary** | CHF 150,000.00 | £1 = CHF 1.10 | £136,363.64 |
| **Annual Bonus** | CHF 20,000.00 | £1 = CHF 1.10 | £18,181.82 |
| **Total Section 1 (Home Pay)** | **CHF 170,000.00** | **£1 = CHF 1.10** | **£154,545.45** |

---

### Section 2: Assignment Benefits (Actual Employer Expenditure)
| Benefit Item | Year 1 (GBP) | Year 2 (GBP) | Classification (UK Tax) | Taxable Value (Y1) | Taxable Value (Y2) |
| :--- | :---: | :---: | :--- | :---: | :---: |
| **London Housing** | £36,000.00 | £36,000.00 | Taxable Benefit in Kind (s. 105) | £36,000.00 | £36,000.00 |
| **Relocation Allowance** | £4,545.45 | £0.00 | Taxable Cash (s. 62) | £4,545.45 | £0.00 |
| **Moving Costs** | £6,000.00 | £0.00 | Qualifying Relocation (s. 273) | £0.00 | £0.00 |
| **Temporary Housing** | £4,000.00 | £0.00 | Qualifying Temp Housing (s. 279) | £2,000.00 | £0.00 |
| *Exempt Relocation (s. 287)*| *(£8,000.00)* | *—* | *Statutory Exemption Cap* | *Exempt* | *—* |
| **Total Section 2 (Benefits)** | **£50,545.45** | **£36,000.00** | — | **£42,545.45** | **£36,000.00** |

*(Note: Moving £6,000 + Temp Housing £4,000 = £10,000. Under s. 287 ITEPA 2003, £8,000 is tax-exempt and £2,000 is taxable BIK in Year 1).*

---

### Section 3: Host Tax and Employer Charges Paid by Employer
| Charge Component | Year 1 (GBP) | Year 2 (GBP) | Authority / Rule Reference |
| :--- | :---: | :---: | :--- |
| **UK Income Tax (Grossed-Up)** | £103,765.37 | £98,410.01 | HMRC PAYE72028 (T = UKTax(I + T)) |
| **Employer Class 1 NIC** | £0.00 | £0.00 | Exempt: Art. 14 UK-Swiss Convention |
| **Employer Class 1A NIC** | £0.00 | £0.00 | Exempt: Art. 14 UK-Swiss Convention |
| **Total Section 3 (Host Tax & Charges)** | **£103,765.37** | **£98,410.01** | — |

---

### Section 4: Deductions (Hypothetical Swiss Taxes Retained by Employer)
These amounts reduce the employer's net assignment cost, as the employee bears their home tax via payroll deduction.

| Deduction Component | Year 1 (CHF) | Year 1 (GBP) | Year 2 (CHF) | Year 2 (GBP) |
| :--- | :---: | :---: | :---: | :---: |
| **Hypothetical Swiss Income Tax** | -CHF 32,927.01 | -£29,933.65 | -CHF 32,927.01 | -£29,933.65 |
| **Hypothetical AHV/IV/EO (5.30%)** | -CHF 9,010.00 | -£8,190.91 | -CHF 9,010.00 | -£8,190.91 |
| **Hypothetical ALV (1.10% capped)**| -CHF 1,630.20 | -£1,482.00 | -CHF 1,630.20 | -£1,482.00 |
| **Total Section 4 (Deductions)** | **-CHF 43,567.21** | **-£39,606.55** | **-CHF 43,567.21** | **-£39,606.55** |

---

### Section 5: Cost Summary & Assignment Multiples

$$\text{Total Employer Cost} = \text{Section 1 (Home Pay)} + \text{Section 2 (Benefits)} + \text{Section 3 (Host Tax)} + \text{Section 4 (Deductions)}$$

| Summary Metric | Year 1 | Year 2 | Total 2-Year Assignment |
| :--- | :---: | :---: | :---: |
| **Section 1: Home Pay** | £154,545.45 | £154,545.45 | £309,090.91 |
| **Section 2: Assignment Benefits** | £50,545.45 | £36,000.00 | £86,545.45 |
| **Section 3: Host Tax & Charges** | £103,765.37 | £98,410.01 | £202,175.38 |
| **Section 4: Hypothetical Deductions** | -£39,606.55 | -£39,606.55 | -£79,213.11 |
| **TOTAL EMPLOYER COST** | **£269,249.72** | **£249,348.91** | **£518,598.63** |
| **Annual Home Pay Benchmark** | £154,545.45 | £154,545.45 | £309,090.91 |
| **Cost Multiple of Home Pay** | **1.742x** *(1.74x)* | **1.613x** *(1.61x)* | **1.678x** *(1.68x)* |

---

## Reconciliation & Mathematical Proof

1. **Year 1 Reconciliation**:
   * Net Home Pay delivered to employee: `£154,545.45 - £39,606.55 = £114,938.90`
   * Plus actual benefits paid: `£50,545.45`
   * Plus UK tax paid to HMRC: `£103,765.37`
   * Sum of actual cash outflows: `£114,938.90 + £50,545.45 + £103,765.37 = £269,249.72`. Exactly ties to Total Employer Cost.
   * Tax reconciliation: Taxable pay $I_1 + T_1 = £157,484.35 + £103,765.37 = £261,249.72$. Total cost = $I_1 + T_1 + £8,000$ (exempt relocation) = £269,249.72. Exactly ties.

2. **Year 2 Reconciliation**:
   * Net Home Pay delivered to employee: `£114,938.90`
   * Plus actual benefits paid: `£36,000.00`
   * Plus UK tax paid to HMRC: `£98,410.01`
   * Sum of actual cash outflows: `£114,938.90 + £36,000.00 + £98,410.01 = £249,348.91`. Exactly ties to Total Employer Cost.
   * Tax reconciliation: All Year 2 benefits are taxable, so $I_2 + T_2 = £150,938.90 + £98,410.01 = £249,348.91$. Exactly ties.

---

## Assumptions List (Required in Output)

1. **Exchange Rate**: Fixed at £1.00 = CHF 1.10 throughout the 2-year assignment period.
2. **Tax Residency**: The employee is non-resident in Switzerland and UK tax resident for both full UK tax years (6 April 2026 to 5 April 2028).
3. **UK Rates**: Standard 2026/27 England & Northern Ireland income tax rates apply to both assignment years (Personal Allowance £12,570, Basic 20%, Higher 40%, Additional 45%, PA taper between £100k and £125,140).
4. **Swiss Hypothetical Tax**: Calculated under Canton of Zurich Tax Law (§ 35 StG ZH) and Federal Direct Tax (Art. 36 DBG) for a single taxpayer residing in the City of Zurich with no church affiliation, taking standard lump-sum professional and insurance deductions.
5. **Swiss Hypothetical Social Security**: Includes employee AHV/IV/EO (5.30% uncapped) and ALV (1.10% capped at CHF 148,200). Second pillar occupational pension (BVG) is omitted per instruction.
6. **Social Security Coordination**: A valid Swiss Certificate of Coverage (PDA1) is issued under Article 14(1) of the UK-Switzerland Social Security Coordination Convention, exempting employee and employer from UK National Insurance for the entire 24-month duration.
7. **Relocation Exemption**: Flights, shipping, and temporary living accommodation meet the conditions of s. 273 ITEPA 2003, with the £8,000 statutory cap applied under s. 287 ITEPA 2003. Round-sum cash relocation allowance is fully taxable.
8. **Immigration Route**: Sponsored under Global Business Mobility: Senior or Specialist Worker visa, incurring employer-borne sponsorship and Immigration Skills Charge obligations.

