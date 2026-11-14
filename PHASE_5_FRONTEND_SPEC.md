# Phase 5: Frontend Specification
**Global Mobility Cost Estimator (Switzerland → UK Assignment)**

---

## 1. Design Philosophy & User Experience

The front-end design is clean, professional, intuitive, and uncluttered. It follows modern web design principles while adhering strictly to the brief requirements:
1. **Clarity at a Glance**: Clean card-based layout with high-contrast typography and clear visual hierarchy.
2. **Help Text Throughout**: Informative inline explanations for complex concepts (hypothetical tax, gross-up, benefit classifications, exchange rates).
3. **Tabbed Architecture**: Three dedicated tabs separating the **Cost Estimate**, **Immigration & Work Permits**, and **Assumptions & Sources**.
4. **No Framework Bloat**: Built using pure semantic HTML5, clean custom CSS, and lightweight vanilla JavaScript (~15 lines for tab switching). No npm, node_modules, or external script dependencies that could break during offline evaluation.
5. **Immediate Value on First Load**: Pre-populated with the test-case defaults so a visiting user or evaluating engineer sees the full cost estimate table immediately.

---

## 2. Global Layout & Navigation Wireframe

```
+-----------------------------------------------------------------------------------------+
|  [Logo] TheCozm | Global Mobility Cost Estimator                                        |
|  International Assignment Costing & Immigration Intelligence Engine                     |
+-----------------------------------------------------------------------------------------+
|  [ Tab 1: Cost Estimate ]   [ Tab 2: Immigration & Visas ]   [ Tab 3: Assumptions & Sources ] |
+-----------------------------------------------------------------------------------------+
|                                                                                         |
|  [ Active Tab Content Displays Here ]                                                   |
|                                                                                         |
+-----------------------------------------------------------------------------------------+
|  © 2026 TheCozm. Prepared for Global Mobility Technical Assessment. All sources verified.|
+-----------------------------------------------------------------------------------------+
```

---

## 3. Tab 1: Cost Estimate Specification

### 3.1 Wireframe Layout (Two-Column Responsive Grid)

```
+--------------------------------------------------+-------------------------------------------------------+
|  COLUMN 1: ASSIGNMENT INPUTS                     |  COLUMN 2: EMPLOYER COST ESTIMATE                     |
+--------------------------------------------------+-------------------------------------------------------+
|  [Card: Geography & Parameters]                  |  [Top Metrics Banner]                                 |
|  - Home: Switzerland (Zurich)                    |  Total 2-Yr Cost: £518,598.63 | Annual Home: £154,545 |
|  - Host: United Kingdom (London)                 |  Multiple: 1.68x Home Pay                            |
|  - Exchange Rate: 1.1000 [?]                     +-------------------------------------------------------+
|  - Dates: 2026-04-06 to 2028-04-05 [?]           |  [Four-Section Cost Table]                            |
|                                                  |                                                       |
|  [Card: Home Remuneration]                       |  SECTION 1: HOME PAY (CHF & GBP)                      |
|  - Base Salary: CHF 150,000 [?]                  |  - Base Salary: CHF 150,000.00 -> £136,363.64        |
|  - Annual Bonus: CHF 20,000 [?]                  |  - Annual Bonus: CHF 20,000.00 -> £18,181.82          |
|                                                  |  * Total Home Pay: CHF 170,000.00 -> £154,545.45      |
|  [Card: Assignment Benefits]                     |                                                       |
|  - London Monthly Rent: £3,000 [?]               |  SECTION 2: ASSIGNMENT BENEFITS (ACTUAL EXPENDITURE)  |
|  - Relocation Allowance: CHF 5,000 [?]           |  - London Housing: £36,000.00 (Both Y1 & Y2) [BIK]    |
|  - Moving Costs: £6,000 (Y1) [?]                 |  - Relocation Allowance: £4,545.45 (Y1) [Cash]        |
|  - Temp Housing: £4,000 (Y1) [?]                 |  - Moving Costs: £6,000.00 (Y1) [Qualifying]          |
|                                                  |  - Temporary Housing: £4,000.00 (Y1) [Qualifying]     |
|  [Button: Calculate Cost Estimate]               |  * £8,000 Relocation Exemption Applied: £2,000 Taxable |
|  [Button: Reset to Test Case Defaults]           |  * Total Benefits: Y1 £50,545.45 | Y2 £36,000.00     |
|                                                  |                                                       |
|                                                  |  SECTION 3: HOST TAX & EMPLOYER CHARGES               |
|                                                  |  - Grossed-Up UK Income Tax: Y1 £103,765 | Y2 £98,410 |
|                                                  |  - Employer Class 1 & 1A NIC: £0.00 [Exempt PDA1]     |
|                                                  |  * Total Host Tax: Y1 £103,765.37 | Y2 £98,410.01     |
|                                                  |                                                       |
|                                                  |  SECTION 4: DEDUCTIONS (HYPOTHETICAL SWISS TAXES)     |
|                                                  |  - Hypothetical Swiss Income Tax: -£29,933.65         |
|                                                  |  - Hypothetical Social Security: -£9,672.91           |
|                                                  |  * Total Deductions: -£39,606.55 (-CHF 43,567.21)     |
|                                                  |                                                       |
|                                                  |  TOTAL ANNUAL COST TO EMPLOYER                        |
|                                                  |  Year 1: £269,249.72 (1.74x)                          |
|                                                  |  Year 2: £249,348.91 (1.61x)                          |
|                                                  |                                                       |
|                                                  |  [Collapsible Details: Iterative Gross-Up Trace]      |
|                                                  |  > Click to view 20-step iteration convergence table  |
+--------------------------------------------------+-------------------------------------------------------+
```

### 3.2 Form Fields & Explanatory Help Text Content

| Field Name | Type / Widget | Initial Value | Help Text Content |
| :--- | :--- | :---: | :--- |
| `home_country` | Select / Text | `Switzerland` | Home employment location where employee has worked for 3 years. |
| `home_city` | Text Input | `Zurich` | Used to determine cantonal and communal hypothetical income tax. |
| `host_country` | Select / Text | `United Kingdom` | Destination country for the 2-year assignment. |
| `host_city` | Text Input | `London` | Assignment work location (UK tax jurisdiction: England). |
| `exchange_rate` | Number (0.0001 step) | `1.1000` | Fixed exchange rate: £1.00 = X CHF. Converts Swiss home pay and deductions to GBP. |
| `start_date` | Date Input | `2026-04-06` | First day of assignment (aligned to UK tax year start). |
| `end_date` | Date Input | `2028-04-05` | Last day of assignment (exactly 24 months: 2 full UK tax years). |
| `base_salary` | Number (0.01 step) | `150000.00` | Annual gross base salary in Swiss Francs (CHF). |
| `bonus` | Number (0.01 step) | `20000.00` | Annual incentive bonus in Swiss Francs (CHF). Subject to AHV and tax. |
| `monthly_rent` | Number (0.01 step) | `3000.00` | Monthly rent in GBP paid directly to landlord. Treated as a Benefit in Kind (s. 105 ITEPA 2003). |
| `relocation_allowance` | Number (0.01 step) | `5000.00` | Lump-sum cash allowance in CHF (Year 1). Taxable cash earnings under s. 62 ITEPA 2003. |
| `moving_costs` | Number (0.01 step) | `6000.00` | Flights and shipping of household belongings (Year 1). Qualifying expense under s. 273 ITEPA. |
| `temp_housing` | Number (0.01 step) | `4000.00` | Serviced apartment for first 4 weeks (Year 1). Qualifying expense under s. 279 & EIM03117. |

### 3.3 Four-Section Output Table Elements
* **Section 1 (Home Pay)**: Displays Base Salary, Bonus, and Total in both CHF and GBP with the fixed rate indicator.
* **Section 2 (Assignment Benefits)**: Lists all 4 benefit items with badges:
  * `[Taxable BIK]` for London housing (£36k).
  * `[Taxable Cash]` for cash relocation allowance (£4,545.45).
  * `[Exempt under s. 287]` for qualifying moving & temporary housing up to the £8,000 cap.
  * `[Taxable BIK Excess]` for the £2,000 excess relocation cost in Year 1.
* **Section 3 (Host Tax & Charges)**: Displays the grossed-up UK Income Tax ($T_1 = £103,765.37$, $T_2 = £98,410.01$) and a prominent badge `[Exempt: Art. 14 Convention]` showing £0.00 for Employer Class 1 and Class 1A NIC.
* **Section 4 (Deductions)**: Displays the hypothetical Swiss Income Tax (-£29,933.65) and hypothetical Swiss Social Security (-£9,672.91) as negative values.
* **Section 5 (Summary & Metrics)**: Total Employer Cost for Year 1, Year 2, and the full assignment, accompanied by the cost multiples of home pay (1.74x and 1.61x).
* **Collapsible Iteration Trace**: An expandable `<details>` section rendering the full 20-step iteration table for technical verification.

---

## 4. Tab 2: Immigration & Work Permits Specification

### 4.1 Wireframe Layout (Structured Cards)

```
+-----------------------------------------------------------------------------------------+
|  TAB 2: UK IMMIGRATION & REGULATORY COMPLIANCE                                          |
+-----------------------------------------------------------------------------------------+
|  [Card 1: Recommended Visa Route: Global Business Mobility (Senior or Specialist Worker)]|
|  - Rationale: Purpose-built for intra-company secondments from Swiss parent to UK sub.  |
|  - Key Criteria Met: Corporate link, 3 years prior service in Zurich, salary £136k > £52.5k|
|  - Key Advantage: No mandatory English language testing required.                       |
|  - Alternative Route: Skilled Worker (direct UK employment; leads to ILR; B1 test req.) |
+-----------------------------------------------------------------------------------------+
|  [Card 2: Business Visits Prior to Assignment & Electronic Travel Authorisation (ETA)]   |
|  - Requirement: Swiss nationals need an ETA for pre-assignment business trips (£20 fee).|
|  - Permitted Activities: Meetings, conferences, contract negotiations, housing search.   |
|  - Strict Warning: ETA cannot be used for productive work or to start the assignment.   |
+-----------------------------------------------------------------------------------------+
|  [Card 3: Swiss Passport Validity Requirements]                                         |
|  - Official Rule: Must be valid for the whole duration of the stay in the UK.           |
|  - Myth Debunked: No 6-month validity rule exists under UK law for Swiss citizens.      |
|  - Practical Advice: Passport should ideally have 25+ months validity upon visa filing. |
+-----------------------------------------------------------------------------------------+
|  [Card 4: Employer Sponsor Obligations & Compliance Duties]                             |
|  - Sponsor Licence: Must hold A-rated Worker / GBM licence (£536 small / £1,476 large). |
|  - Certificate of Sponsorship: Assign Undefined CoS via SMS (£239 fee).                 |
|  - Immigration Skills Charge: £728 small / £2,000 large (mandatory employer levy).       |
|  - Digital Right to Work Check: Pre-employment online verification using eVisa share code|
|  - Reporting Duties: SMS reports within 10 days for non-attendance, absences, changes.  |
|  - UK Payroll: PAYE RTI setup with NIC category set to exempt (Certificate of Coverage).|
+-----------------------------------------------------------------------------------------+
|  [Card 5: Complete Fee Breakdown & Cost Separation Table]                                |
|  - Table clearly dividing Employer-Borne Costs vs Employee-Borne (Reimbursable) Costs.   |
+-----------------------------------------------------------------------------------------+
|  [Card 6: Official Government Citations & Direct Links]                                 |
|  - Working links to official GOV.UK guidance and immigration legislation.               |
+-----------------------------------------------------------------------------------------+
```

### 4.2 Exact Content Structure for Tab 2

#### 1. Route Comparison
* **Senior or Specialist Worker (GBM)**: Recommended route. RQF Level 6, salary threshold £52,500, no English test, maximum 5 years, no direct settlement.
* **Skilled Worker**: Alternative route. RQF Level 3, salary threshold £38,700, mandatory B1 English test, leads to permanent settlement (ILR) after 5 years.
* **Missing Eligibility Facts**: SOC occupation code (to verify going rate) and UK entity sponsor licence tier.

#### 2. Business Visit / ETA Rules
* **Mandatory ETA from 2 April 2025**: Cost **£20**, valid for 2 years.
* **Permitted Activities**: Business meetings, contract negotiations, fact-finding, housing visits.
* **Prohibited**: Productive employment, providing services. Cannot start assignment on an ETA.

#### 3. Passport Rules
* Must be valid for the whole of the stay in the UK.
* UK law does **not** enforce a 6-month rule for Swiss passport holders.

#### 4. Employer Immigration Obligations
* Sponsor Licence, CoS assignment (£239), Immigration Skills Charge (£728 small / £2,000 large).
* Mandatory SMS reporting within 10 working days.
* Pre-employment online Right-to-Work verification using share code.
* Operating UK PAYE payroll with NIC category set to exempt based on the Swiss Certificate of Coverage.

#### 5. Cost Separation Table
| Expense Item | Amount | Borne By | Statutory Nature |
| :--- | :---: | :---: | :--- |
| **Sponsor Licence Fee** | £536 (small) / £1,476 (large) | **Employer** | Institutional licensing fee |
| **CoS Assignment Fee** | £239.00 | **Employer** | Mandatory certificate fee |
| **Immigration Skills Charge (2 yrs)** | £728 (small) / £2,000 (large) | **Employer** | Mandatory levy (illegal to pass to worker) |
| **Visa Application Fee (≤ 3 yrs)** | £819.00 | **Employee** *(reimbursed)* | Individual entry clearance fee |
| **Immigration Health Surcharge (2 yrs)**| £2,070.00 (£1,035/yr) | **Employee** *(reimbursed)* | Mandatory NHS access charge |
| **Business Visit ETA** | £20.00 | **Employee** *(reimbursed)* | Pre-assignment travel authorization |
| **Maintenance Savings** | £1,270.00 | **Employee** | Proof of funds (or employer certified) |

---

## 5. Tab 3: Assumptions & Sources Specification

### 5.1 Content Layout
Tab 3 provides full transparency into the tax, legal, and operational assumptions underlying the tool, ensuring every figure can be verified by an auditor or engineer.

#### Group A: Tax Equalisation & Swiss Tax Assumptions
1. **Tax Equalisation Policy**: The employee bears hypothetical Swiss home tax and social security. The employer covers all UK host taxes on assignment earnings.
2. **Swiss Jurisdiction**: Canton of Zurich, City of Zurich (BFS 261), non-denominational (no church tax).
3. **Statutory Tax Tariffs**: Direct Federal Tax computed under Art. 36 DBG / SR 642.119.2. Cantonal Tax computed under § 35 StG ZH Grundtarif with a 95% cantonal multiplier and 119% City of Zurich multiplier, plus CHF 24 personal tax.
4. **Standard Deductions**: Mandatory Pillar 1 social security, capped professional expenses (CHF 4,000), and insurance deductions (CHF 2,900 cantonal / CHF 1,800 federal).
5. **Swiss Social Security**: Employee AHV/IV/EO @ 5.30% (uncapped); employee ALV @ 1.10% capped at CHF 148,200 (solidarity surcharge abolished 1 Jan 2023). BVG pension excluded per brief.

#### Group B: UK Tax & Benefit Treatment Assumptions
1. **Tax Residency**: Employee is UK tax resident and leaves Swiss tax residence for both full UK tax years (6 April 2026 to 5 April 2028).
2. **UK Rates & Allowances (2026/27)**: Personal Allowance £12,570; £1 per £2 taper on income between £100,000 and £125,140; Basic Rate 20% (£37,700 band); Higher Rate 40% (up to £125,140); Additional Rate 45% (above £125,140).
3. **London Housing**: Living accommodation under s. 105 ITEPA 2003; cash equivalent equals rent paid (£36,000/yr). Taxable BIK.
4. **Relocation Cash Allowance**: Round-sum unvouched cash allowance under s. 62 ITEPA 2003. Fully taxable cash.
5. **Moving & Temporary Housing**: Qualifying relocation expenses under ss. 273, 277, 279 ITEPA 2003 and HMRC EIM03117. The £8,000 statutory cap (s. 287 ITEPA) exempts £8,000, leaving £2,000 as taxable BIK in Year 1.
6. **Iterative Gross-Up**: UK tax solved iteratively ($T = \text{UKTax}(I + T)$) until $|T_{\text{new}} - T_{\text{old}}| < £0.01$ (converges in 20 iterations).

#### Group C: Social Security Coordination & NIC Assumptions
1. **Bilateral Convention**: Article 14(1) of the UK-Switzerland Social Security Coordination Convention applies to assignments up to 24 months.
2. **Certificate of Coverage (PDA1)**: Held by the employee, exempting employee and employer from UK National Insurance.
3. **UK Employer NIC**: £0.00 Class 1 secondary NIC and £0.00 Class 1A NIC.

#### Group D: Verified Official Sources Table (Every Rule Linked)
| Subject | Official Title / Legislation | Issuing Body | Direct URL |
| :--- | :--- | :--- | :--- |
| **Swiss Tax Calculator** | Official Swiss Tax Calculator | ESTV / FTA | [swisstaxcalculator.estv.admin.ch](https://swisstaxcalculator.estv.admin.ch) |
| **Zurich Cantonal Tax** | Steuergesetz des Kantons Zürich (LS 631.1) | Canton of Zurich | [zh.ch/steuern-finanzen](https://www.zh.ch/de/steuern-finanzen/steuern/steuern-natuerliche-personen.html) |
| **City of Zurich Tax** | Steuerfüsse der Stadt Zürich 2026 | City of Zurich | [stadt-zuerich.ch/steuern](https://www.stadt-zuerich.ch/steuern) |
| **Direct Federal Tax** | Bundesgesetz über die direkte Bundessteuer (DBG) | Fedlex / EFD | [fedlex.admin.ch (SR 642.11)](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| **Swiss Social Security** | Beitragssätze AHV, IV, EO und ALV | BSV / FSIO | [bsv.admin.ch/beitragssaetze](https://www.bsv.admin.ch/bsv/de/home/sozialversicherungen/ahv/grundlagen-und-gesetze/beitragssaetze.html) |
| **UK Income Tax Rates** | Income Tax rates and Personal Allowances | HMRC / GOV.UK | [gov.uk/income-tax-rates](https://www.gov.uk/income-tax-rates) |
| **UK Employer Rates** | Rates and thresholds for employers 2026 to 2027 | HMRC / GOV.UK | [gov.uk/rates-and-thresholds-for-employers](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026) |
| **UK-Swiss Coordination** | Social security for workers from Switzerland | GOV.UK | [gov.uk/social-security-workers-switzerland](https://www.gov.uk/guidance/social-security-contributions-for-workers-coming-to-the-uk-from-the-eea-or-switzerland) |
| **Bilateral Treaty** | UK-Switzerland Social Security Convention | UK Parliament | [gov.uk/uk-switzerland-convention](https://www.gov.uk/government/publications/uk-switzerland-convention-on-social-security-coordination) |
| **Relocation Expenses** | Expenses and benefits: relocation costs | HMRC / GOV.UK | [gov.uk/expenses-and-benefits-relocation](https://www.gov.uk/expenses-and-benefits-relocation) |
| **Accommodation Benefit**| Expenses and benefits: accommodation | HMRC / GOV.UK | [gov.uk/expenses-and-benefits-accommodation](https://www.gov.uk/expenses-and-benefits-accommodation) |
| **Temp Accommodation** | EIM03117: Temporary living accommodation | HMRC Manuals | [gov.uk/hmrc-manuals/eim03117](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim03117) |
| **GBM Work Visa** | Senior or Specialist Worker visa | Home Office | [gov.uk/senior-specialist-worker-visa](https://www.gov.uk/senior-specialist-worker-visa) |
| **Skilled Worker Visa** | Skilled Worker visa overview | Home Office | [gov.uk/skilled-worker-visa](https://www.gov.uk/skilled-worker-visa) |
| **Electronic Authorisation**| Apply for an Electronic Travel Authorisation (ETA) | Home Office | [gov.uk/apply-for-an-eta](https://www.gov.uk/guidance/apply-for-an-electronic-travel-authorisation-eta) |
| **Visitor Activities** | Appendix Visitor: Permitted Activities | Home Office | [gov.uk/immigration-rules-visitor](https://www.gov.uk/guidance/immigration-rules/immigration-rules-appendix-visitor-permitted-activities) |
| **Passport Requirements** | Visiting the UK as an EU, EEA or Swiss citizen | Home Office | [gov.uk/visiting-the-uk-swiss-citizen](https://www.gov.uk/guidance/visiting-the-uk-as-an-eu-eea-or-swiss-citizen) |
| **Sponsorship Guidance** | UK visa sponsorship for employers | Home Office | [gov.uk/uk-visa-sponsorship-employers](https://www.gov.uk/uk-visa-sponsorship-employers) |
| **Right to Work Checks** | Check a job applicant's right to work | Home Office | [gov.uk/check-job-applicant-right-to-work](https://www.gov.uk/check-job-applicant-right-to-work) |



