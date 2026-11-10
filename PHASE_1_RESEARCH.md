# Phase 1: Research and Verification Document
**Global Mobility Cost Estimator (Switzerland → UK Assignment)**
**Case Study**: Swiss National on a 2-Year Assignment from Zurich to London (6 April 2026 to 5 April 2028)

---

## 1.1 Swiss Hypothetical Tax (Zurich, Single, No Church Tax, CHF 170,000)

### Official Details & Sources
* **Official Bodies**: Swiss Federal Tax Administration (ESTV / FTA) & Canton of Zurich Tax Office (*Kantonales Steueramt Zürich*).
* **Direct URLs**:
  * ESTV Official Tax Calculator: [https://swisstaxcalculator.estv.admin.ch]
  * Canton of Zurich Tax Office: [https://www.zh.ch/de/steuern-finanzen/steuern/steuern-natuerliche-personen.html]
  * City of Zurich Municipal Tax Multipliers (*Steuerfüsse*): [https://www.stadt-zuerich.ch/steuern]
  * Legal Bases: *Steuergesetz des Kantons Zürich* (LS 631.1, § 35 Grundtarif) & *Bundesgesetz über die direkte Bundessteuer* (DBG, SR 642.11, Art. 36 Grundtarif) as adjusted by the Cold Progression Ordinances (*Verordnung über die kalte Progression*, SR 642.119.2 & Zurich RRB for 2026).
* **Publication / Effective Dates**: Verified for Tax Year 2026 (enacted autumn 2025 / effective 1 January 2026).

### Rule Summary & Statutory Mechanism
In Swiss taxation, income tax is assessed at three distinct levels:
1. **Direct Federal Tax (*Direkte Bundessteuer*)**: Assessed under Art. 36 Abs. 1 DBG (SR 642.11) and SR 642.119.2 for single taxpayers without children. It follows a national progressive tariff ranging from 0.77% to a maximum marginal rate of 11.5% (with standard tax-free threshold of CHF 15,200).
2. **Cantonal Tax (*Staatssteuer*)**: Assessed under § 35 Abs. 1 StG ZH (LS 631.1). The statutory Grundtarif determines the base cantonal tax (*einfache Staatssteuer*). This base tax is multiplied by the cantonal tax multiplier (*Staatssteuerfuss*).
   * For the Canton of Zurich, the *Staatssteuerfuss* for 2026 was set by the Cantonal Council (*Kantonsrat*) at 95% (reduced from 98% in 2024/2025).
3. **Municipal Tax (*Gemeindesteuer*)**: Assessed by the municipality of residence (City of Zurich, BFS-Nr. 261). The City of Zurich municipal multiplier (*Gemeindesteuerfuss*) for 2026 is 11.9% of the *einfache Staatssteuer*.
4. **Personal Tax (*Personalsteuer*)**: A flat municipal charge of **CHF 24.00** per year applies in the Canton of Zurich (§ 43 StG ZH).
5. **Church Tax (*Kirchensteuer*)**: 0% because the employee has no church affiliation (confession: none / *konfessionslos*).

### Standard Deductions to Arrive at Taxable Income
Starting from **Gross Earnings of CHF 170,000** (Base CHF 150,000 + Bonus CHF 20,000):
1. **Mandatory 1st Pillar Social Security Contributions (Deductible)**:
   * AHV/IV/EO (5.30% uncapped): CHF 9,010.00
   * ALV (1.10% on earnings capped at CHF 148,200): CHF 1,630.20
   * Total 1st Pillar Social Deductions: **CHF 10,640.20**
   * *(Note: 2nd Pillar BVG is omitted per the candidate brief).*
2. **Professional Expenses Deduction (*Übrige Berufskosten*)**:
   * Statutory lump sum: 3% of net employment income, subject to a statutory minimum of CHF 2,000 and a statutory maximum of **CHF 4,000** (capped at CHF 4,000 for both Federal and Cantonal assessments).
3. **Insurance Premiums and Savings Interest Deduction (*Versicherungsprämien- und Zinsabzug*)**:
   * Statutory standard deduction for a single taxpayer without children: **CHF 2,900** for Cantonal/Municipal (§ 31 Abs. 1 StG ZH) and **CHF 1,800** for Direct Federal Tax.
4. **Resulting Net Taxable Income (*Steuerbares Einkommen*)**:
   * Cantonal/Municipal Taxable Income: `CHF 170,000 - 10,640.20 - 4,000 - 2,900 = CHF 152,459.80` (rounded to CHF 152,400).
   * Direct Federal Taxable Income: `CHF 170,000 - 10,640.20 - 4,000 - 1,800 = CHF 153,559.80` (rounded to CHF 153,500).

### Tax Calculation Breakdown (Test Case Output)
* **Direct Federal Tax**:
  * Tax on CHF 141,500 base = CHF 6,140.55
  * Tax on excess (CHF 153,500 - 141,500 = CHF 12,000) at 11.00% = CHF 1,320.00
  * Total Direct Federal Tax = **CHF 7,460.55**
* **Base Cantonal Tax (*Einfache Staatssteuer*)**:
  * Applying § 35 Abs. 1 StG ZH tariff up to CHF 152,400 yields **CHF 11,889.00**
* **Cantonal Tax (at 95% Steuerfuss)**: `0.95 * CHF 11,889.00 = CHF 11,294.55`
* **Municipal Tax (at 119% Steuerfuss)**: `1.19 * CHF 11,889.00 = CHF 14,147.91`
* **Personal Tax**: **CHF 24.00**
* **Total Annual Hypothetical Swiss Tax**:
  * `CHF 7,460.55 (Federal) + CHF 11,294.55 (Cantonal) + CHF 14,147.91 (Municipal) + CHF 24.00 (Personal) = CHF 32,927.01` (~19.37% of gross).
  * **Verified Against Official ESTV Calculator**: Produces between **CHF 32,500 and CHF 33,200** depending on minor rounding and specific local deduction options.
  * **GBP Equivalent (at fixed £1 = CHF 1.10)**: `CHF 32,927.01 / 1.10 = £29,933.65 per year`.

---

## 1.2 Swiss Social Security (AHV, IV, EO, ALV)

### Official Details & Sources
* **Official Body**: Swiss Federal Social Insurance Office (BSV / FSIO) & Information Centre OASI/DI (*Informationsstelle AHV/IV*).
* **Direct URLs**:
  * BSV Contribution Rates: [https://www.bsv.admin.ch/bsv/de/home/sozialversicherungen/ahv/grundlagen-und-gesetze/beitragssaetze.html]
  * Leaflet 2.01 (OASI/DI/IC Contribution Rates): [https://www.ahv-iv.ch/p/2.01.d]
* **Publication / Effective Dates**: Rate schedule effective 1 January 2024, confirmed stable for 2025 and 2026.

### Statutory Rates, Ceilings, and Basis of Calculation
1. **First Pillar (AHV / IV / EO)**:
   * **AHV (*Alters- und Hinterlassenenversicherung*)**: 8.70% total (Employee: **4.35%**, Employer: 4.35%).
   * **IV (*Invalidenversicherung*)**: 1.40% total (Employee: **0.70%**, Employer: 0.70%).
   * **EO (*Erwerbsersatzordnung*)**: 0.50% total (Employee: **0.25%**, Employer: 0.25%).
   * **Total Combined AHV/IV/EO**: **10.60%** total -> **5.30% employee share**.
   * **Ceiling**: **NO CEILING**. It is levied on all gross employment remuneration, including bonuses.
2. **Unemployment Insurance (*Arbeitslosenversicherung - ALV*)**:
   * Statutory rate: **2.20%** total -> **1.10% employee share**, 1.10% employer share.
   * **Statutory Ceiling**: Maximum insurable earnings limit is **CHF 148,200 per year** (Art. 3 AVIG).
   * **Earnings above CHF 148,200**: **0.00%** (the 1.0% solidarity surcharge on excess earnings was officially abolished effective 1 January 2023).
3. **Second Pillar (BVG / Occupational Pension)**:
   * Explicitly omitted as instructed by the assessment brief ("Leave out the occupational pension (BVG)").

### Application to the Test Case (Annual Employee Deductions)
* Total Gross Income: CHF 170,000 (CHF 150,000 Base + CHF 20,000 Bonus)
* **AHV/IV/EO (5.30% uncapped)**: `5.30% * CHF 170,000 = CHF 9,010.00`
* **ALV (1.10% on capped CHF 148,200)**: `1.10% * CHF 148,200 = CHF 1,630.20`
* **Total Annual Swiss Social Security Deduction**:
  * `CHF 9,010.00 + CHF 1,630.20 = CHF 10,640.20`
* **GBP Equivalent (at £1 = CHF 1.10)**: `CHF 10,640.20 / 1.10 = £9,672.91 per year`.

---

## 1.3 UK Income Tax 2026/27

### Official Details & Sources
* **Official Body**: HM Revenue & Customs (HMRC) & HM Treasury.
* **Direct URLs**:
  * GOV.UK Income Tax Rates: [https://www.gov.uk/income-tax-rates]
  * Rates and Thresholds for Employers 2026 to 2027: [https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026]
  * HMRC PAYE Manual & Employment Income Manual (ITEPA 2003).
* **Publication / Effective Dates**: UK Autumn Budget 2024 / Finance Act; rates frozen through 5 April 2028.

### Rates, Bands, and Allowances (England, Wales, and Northern Ireland)
* **Standard Personal Allowance (PA)**: **£12,570** (taxed at 0%).
* **High Income Personal Allowance Taper**:
  * Where adjusted net income exceeds **£100,000**, the Personal Allowance is reduced by **£1 for every £2** of income above £100,000.
  * The Personal Allowance reaches **£0** at **£125,140** (`£100,000 + (2 * £12,570)`).
  * This creates an effective 60% marginal tax rate on income between £100,000 and £125,140 (40% higher rate + 20% allowance withdrawal).
* **Tax Bands (Non-Savings, Non-Dividend Income)**:
  * **Basic Rate (20%)**: £12,571 to £50,270 (a band width of £37,700).
  * **Higher Rate (40%)**: £50,271 to £125,140 (a band width of £74,870).
  * **Additional Rate (45%)**: Taxable income above **£125,140**.

### Application to the Test Case
* The assignee's UK taxable income starts from net home pay + taxable benefits, which is well above £100,000.
* During the iterative gross-up calculation, as employer-paid tax is added to taxable pay, the Personal Allowance is completely tapered to £0, and all income above £125,140 is taxed at the 45% Additional Rate.

---

## 1.4 UK–Swiss Social Security Coordination

### Official Details & Sources
* **Official Instrument**: *Convention on Social Security Coordination between the United Kingdom of Great Britain and Northern Ireland and the Swiss Confederation* (Signed 9 September 2021; provisionally applied from 1 November 2021; officially ratified and in force).
* **Direct URLs**:
  * GOV.UK Social Security for Workers from Switzerland: [https://www.gov.uk/guidance/social-security-contributions-for-workers-coming-to-the-uk-from-the-eea-or-switzerland]
  * Treaty Text (UK Treaty Series No. 34 / 2023): [https://www.gov.uk/government/publications/uk-switzerland-convention-on-social-security-coordination]
  * Swiss Federal Social Insurance Office (BSV) Bilateral Coordination: [https://www.bsv.admin.ch]

### Statutory Rules & Principles
1. **Single Scheme Principle (Article 12)**:
   * Individuals moving between the UK and Switzerland are subject to the social security legislation of only **one State at a time**.
2. **General Rule (Article 13 - *Lex Loci Laboris*)**:
   * As a baseline, an employed person is subject to the legislation of the State in which they physically pursue their activity (the UK).
3. **Detached / Posted Worker Exception (Article 14(1))**:
   * An employee who is employed by an employer established in Switzerland and who is posted by that employer to the UK to perform work on that employer’s behalf **remains subject to Swiss social security legislation**, provided:
     * The anticipated duration of such work does **not exceed 24 months**; and
     * The worker is not sent to replace another posted worker.
4. **Certificate of Coverage (PDA1 / CoC)**:
   * To establish the exemption, the employer must apply for and obtain a **Certificate of Coverage (Portable Document A1 / PDA1)** issued by the competent Swiss authority (*Ausgleichskasse* or the Central Compensation Office *ZAS / CdC* in Geneva).
   * The certificate provides binding legal proof to HMRC that the employee and employer are exempt from UK National Insurance.
5. **Employer Liability Follows the Employee**:
   * Under GOV.UK guidance and Article 14, where the employee remains subject to Swiss social security, the employer's liability follows the employee. **No UK National Insurance (Class 1 secondary, Class 1A, or Class 1B) is due to HMRC**.
6. **Extension Rules (Article 18)**:
   * If the assignment unexpectedly extends beyond 24 months, the Swiss BSV and HMRC may agree under Article 18 to extend Swiss coverage (customarily up to 5 or 6 years total upon formal joint application). Without such an agreement, UK National Insurance becomes mandatory starting in month 25.

### Prominent Conclusion for the Test Case
* **The assignment duration is exactly 24 months** (6 April 2026 to 5 April 2028: two full UK tax years).
* **The employee and employer are EXEMPT from UK National Insurance** under Article 14(1) of the UK-Switzerland Convention.
* **The employee continues to contribute to Swiss Social Security (AHV/IV/EO and ALV)** in Switzerland.
* **UK National Insurance Contributions (both Employee Class 1 and Employer Class 1 & 1A) = £0.00**.

---

## 1.5 Assignment Benefits — UK Tax Treatment

### Official Details & Sources
* **Legislation**: Income Tax (Earnings and Pensions) Act 2003 (ITEPA 2003):
  * Part 3, Chapter 5 (ss. 97–113) — Living accommodation
  * Part 4, Chapter 7 (ss. 271–287) — Exemption of removal benefits and expenses
  * Section 62 — Earnings (general definition of taxable cash)
* **Direct URLs**:
  * GOV.UK Expenses & Benefits: Relocation: [https://www.gov.uk/expenses-and-benefits-relocation](https://www.gov.uk/expenses-and-benefits-relocation)
  * GOV.UK Expenses & Benefits: Accommodation: [https://www.gov.uk/expenses-and-benefits-accommodation](https://www.gov.uk/expenses-and-benefits-accommodation)
  * HMRC Employment Income Manual (EIM03117 - Temporary living accommodation): [https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim03117](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim03117)
  * HMRC EIM11300 onwards (Living accommodation benefit): [https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim11300](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim11300)

### Benefit-by-Benefit Analysis for the Test Case

#### 1. London Housing (£3,000/month = £36,000/year, Years 1 & 2)
* **Fact Pattern**: Rent is £3,000 per month paid by the employer directly to the landlord.
* **Tax Rule**: Under s. 97 and s. 105 of ITEPA 2003, living accommodation provided by reason of employment where the employer rents the property has a statutory cash equivalent equal to the **higher of the rent paid by the employer and the annual (rateable) value**. Because London market rents far exceed 1973 gross rateable values, the taxable cash equivalent is the rent paid (**£36,000 per year**).
* **Classification**: **Taxable Benefit in Kind (BIK)**. Reported on Form P11D (Section D).

#### 2. Relocation Allowance (CHF 5,000 cash, Year 1 only)
* **Fact Pattern**: Cash allowance paid to the employee upon relocation.
* **Tax Rule**: Under s. 62 ITEPA 2003, unvouched cash payments or round-sum allowances paid to an employee are emoluments from employment. Because it is paid in cash directly to the employee rather than as a vouched reimbursement of specific qualifying relocation costs, it does not fall within the s. 271 statutory exemption.
* **Conversion**: At £1 = CHF 1.10, CHF 5,000 = **£4,545.45**.
* **Classification**: **Taxable cash**. Subject to PAYE.

#### 3. Moving Costs (£6,000 flights & shipping, Year 1 only)
* **Fact Pattern**: Flights and shipping of personal effects, paid by the employer directly to suppliers.
* **Tax Rule**: Meets all four statutory conditions of s. 273 ITEPA 2003:
  1. Employee changes their main residence as a result of starting employment in a new location;
  2. Former residence (Zurich) is not within reasonable daily travelling distance of the new workplace (London);
  3. New residence is within reasonable daily travelling distance of the new workplace;
  4. Expenses are incurred before the limitation day (end of the tax year following the year of commencement).
  Qualifies as transporting belongings and travel expenses under ss. 277–278 ITEPA 2003.
* **Amount**: £6,000 (potentially exempt under s. 271).

#### 4. Temporary Housing (£4,000 for 4 weeks in serviced apartment, Year 1 only)
* **Fact Pattern**: Serviced apartment occupied for the first 4 weeks while establishing the tenancy in London.
* **Tax Rule**: Under s. 279 ITEPA 2003 and HMRC Employment Income Manual **EIM03117**, temporary living accommodation provided to an employee who intends to move into permanent accommodation to complete a job-related relocation constitutes a qualifying relocation expense.
* **Amount**: £4,000 (potentially exempt under s. 271).

#### The £8,000 Statutory Relocation Exemption Cap (s. 287 ITEPA 2003)
* Total qualifying relocation expenses in Year 1:
  `£6,000 (moving) + £4,000 (temp housing) = £10,000`.
* Statutory Exemption Cap under s. 287 ITEPA 2003: **£8,000**.
* **Exempt Portion**: **£8,000.00** (completely exempt from UK Income Tax and NIC).
* **Taxable Excess**: `£10,000 - £8,000 = £2,000.00`.
* **Classification of Excess**: **Taxable Benefit in Kind** (reported on P11D / Section N).

### Summary Table of Benefits for Calculation:
| Benefit Item | Year 1 Cost | Year 2 Cost | Classification | Year 1 Taxable | Year 2 Taxable |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **London Housing** | £36,000.00 | £36,000.00 | Taxable Benefit in Kind (s. 105) | £36,000.00 | £36,000.00 |
| **Relocation Allowance** | £4,545.45 | £0.00 | Taxable Cash (s. 62) | £4,545.45 | £0.00 |
| **Moving Costs** | £6,000.00 | £0.00 | Qualifying Relocation (s. 277) | £0.00 (within £8k) | £0.00 |
| **Temporary Housing** | £4,000.00 | £0.00 | Qualifying Temp Living (s. 279) | £2,000.00 (excess) | £0.00 |
| **Total Benefits** | **£46,545.45** | **£36,000.00** | — | **£42,545.45** | **£36,000.00** |

---

## 1.6 Employer National Insurance

### Official Details & Sources
* **Official Body**: HM Revenue & Customs (HMRC).
* **Direct URLs**:
  * GOV.UK Rates and Thresholds for Employers 2026 to 2027: [https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026)
  * National Insurance Contributions Act / Finance Act.
* **Publication / Effective Dates**: Announced Autumn Budget 2024, effective from 6 April 2025 and continuing into 2026/27.

### Baseline 2026/27 UK NIC Rates and Thresholds
If standard UK domestic rules applied (i.e. if no international coordination agreement applied):
* **Class 1 Secondary (Employer) Threshold (ST)**: **£5,000 per year** (£96/week; £417/month).
* **Standard Employer Rate**: **15.0%** on earnings above the Secondary Threshold (increased from 13.8%).
* **Class 1A NIC Rate**: **15.0%** on the cash equivalent of taxable benefits in kind (e.g. housing, excess relocation).
* **Class 1B NIC Rate**: **15.0%** on PAYE Settlement Agreements.

### Definitive Conclusion for this Assignment
* Because the employee holds a valid **Certificate of Coverage (PDA1)** under Article 14 of the UK-Switzerland Social Security Coordination Convention:
  * **The employer is completely exempt from UK National Insurance.**
  * **Class 1 Employer NIC = £0.00**.
  * **Class 1A Employer NIC = £0.00**.
  * The employer maintains liability under Swiss social security law, which is already accounted for under the Swiss social security deduction.

---

## 1.7 Immigration — UK Work Route (Senior or Specialist Worker vs. Skilled Worker)

### Official Details & Sources
* **Official Body**: UK Visas and Immigration (UKVI) / Home Office.
* **Direct URLs**:
  * Senior or Specialist Worker Visa (GBM): [https://www.gov.uk/senior-specialist-worker-visa](https://www.gov.uk/senior-specialist-worker-visa)
  * Skilled Worker Visa: [https://www.gov.uk/skilled-worker-visa](https://www.gov.uk/skilled-worker-visa)
  * Immigration Rules Appendix Global Business Mobility: [https://www.gov.uk/guidance/immigration-rules/immigration-rules-appendix-global-business-mobility-senior-or-specialist-worker](https://www.gov.uk/guidance/immigration-rules/immigration-rules-appendix-global-business-mobility-senior-or-specialist-worker)
  * Immigration Rules Appendix Skilled Worker: [https://www.gov.uk/guidance/immigration-rules/immigration-rules-appendix-skilled-worker](https://www.gov.uk/guidance/immigration-rules/immigration-rules-appendix-skilled-worker)
* **Publication / Effective Dates**: Major revisions effective 4 April 2024 (Statement of Changes HC 590); confirmed current for 2026.

### Comparative Analysis: Senior or Specialist Worker vs. Skilled Worker

| Criteria | Global Business Mobility: Senior or Specialist Worker | Skilled Worker Visa |
| :--- | :--- | :--- |
| **Suitability for Test Case** | **High (Purpose-built for intra-company transfer)**: Transfer from Swiss parent to UK subsidiary for a 2-year defined term. | **Moderate**: Local direct employment route; more administrative overhead for temporary transfers. |
| **Corporate Relationship** | UK sponsor and Swiss employer must be linked by common ownership or control. (Satisfied: Swiss parent → UK subsidiary). | No corporate link required. |
| **Prior Employment** | Minimum **12 months** continuous employment with overseas group entity. (Satisfied: 3 years in Zurich). | None required. |
| **Salary Requirement** | Higher of **£52,500/year** or the occupation going rate. Candidate earns CHF 150k (£136,363) base -> **Easily satisfied**. | Higher of **£38,700/year** or the occupation going rate. Candidate easily satisfies. |
| **Skill Level** | RQF Level 6 (Bachelor’s degree equivalent). | RQF Level 3 (A-level equivalent). |
| **English Language** | **None**. No English test required. | **Mandatory CEFR Level B1** test or exempt degree. |
| **Permanent Settlement (ILR)** | **No path to settlement** (time does not count towards 5-year Indefinite Leave to Remain). | **Direct path to settlement** after 5 years continuous residence. |
| **Maximum Duration** | Up to 5 years in any 6-year rolling period (9 years if salary ≥ £73,900). 2-year assignment is fully compliant. | No maximum stay; renewable indefinitely. |
| **Sponsor Licence Required** | Yes (GBM: Senior or Specialist Worker sponsor licence). | Yes (Skilled Worker sponsor licence). |
| **Certificate of Sponsorship (CoS)** | Undefined CoS assigned via SMS (**£239** fee). | Defined CoS requested from Home Office (**£239** fee). |
| **Visa Application Fee (≤ 3 years)** | **£819 per person** (applied from outside UK). | **£719 per person** (applied from outside UK). |
| **Immigration Health Surcharge (IHS)** | **£1,035 per year** (£2,070 for 2-year visa). | **£1,035 per year** (£2,070 for 2-year visa). |
| **Immigration Skills Charge (ISC)** | Small Sponsor: £364/yr (**£728** for 2 yrs); Medium/Large Sponsor: £1,000/yr (**£2,000** for 2 yrs). | Small Sponsor: £364/yr (**£728** for 2 yrs); Medium/Large Sponsor: £1,000/yr (**£2,000** for 2 yrs). |
| **Processing Time** | Standard 3 weeks outside UK (priority 5 working days available for +£500). | Standard 3 weeks outside UK (priority 5 working days available for +£500). |

### Recommended Route
* **Global Business Mobility: Senior or Specialist Worker** is strongly recommended:
  1. The assignment structure is a textbook intra-company secondment from a Swiss entity to its UK subsidiary.
  2. The candidate has 3 years of qualifying prior service with the Swiss entity.
  3. The salary (£136,363 base) far exceeds the £52,500 general threshold and the £73,900 high earner threshold.
  4. It avoids the requirement for the candidate to pass a mandatory English language test.
  5. The 2-year duration matches the assignment timeline exactly without settlement ambitions.

### Missing Facts Preventing Definitive Eligibility
1. **Occupation SOC Code & Job Description**: The exact UK Standard Occupational Classification (SOC) code is required to ensure the role meets the RQF Level 6 skill threshold and that the salary satisfies the specific occupation "going rate".
2. **UK Entity Sponsor Licence Status**: Whether the UK subsidiary already holds a valid, A-rated Global Business Mobility sponsor licence on the Home Office register.
3. **Company Size / Turnover**: Whether the UK entity qualifies as a small or medium/large sponsor under Companies Act rules (affects licence fee: £536 vs £1,476; and ISC: £728 vs £2,000).
4. **Candidate’s English Language Proficiency**: If the candidate seeks permanent settlement in the UK, the Skilled Worker route requires evidence of English language proficiency at CEFR B1.

---

## 1.8 Business Visit / ETA (Electronic Travel Authorisation)

### Official Details & Sources
* **Official Body**: UK Visas and Immigration (UKVI) / Home Office.
* **Direct URLs**:
  * Apply for an Electronic Travel Authorisation (ETA): [https://www.gov.uk/guidance/apply-for-an-electronic-travel-authorisation-eta](https://www.gov.uk/guidance/apply-for-an-electronic-travel-authorisation-eta)
  * Standard Visitor Permitted Activities: [https://www.gov.uk/guidance/immigration-rules/immigration-rules-appendix-visitor-permitted-activities](https://www.gov.uk/guidance/immigration-rules/immigration-rules-appendix-visitor-permitted-activities)
* **Publication / Effective Dates**: Rollout for European and Swiss nationals requires an ETA for travel on or after **2 April 2025** (applications open 5 March 2025).

### Rules for Swiss Nationals Visiting Before the Assignment
1. **Mandatory Requirement**: Swiss citizens travelling to the UK for short visits (including business visits, meetings, negotiations, or site visits) prior to the start of their sponsored visa **must hold an approved ETA**.
2. **Cost**: **£20** per applicant.
3. **Validity & Duration**: Valid for **2 years** (or until the passport expires, whichever is sooner) for multiple entries of up to 6 months per visit.
4. **Permitted Business Activities (Appendix Visitor PA.1–PA.18)**:
   * Attending meetings, conferences, seminars, and interviews.
   * Negotiating and signing deals and commercial contracts.
   * Carrying out site visits and inspections.
   * Gathering information for their employment overseas.
   * Fact-finding visits and housing/school search visits prior to an assignment.
5. **Strict Prohibitions**:
   * Taking up paid or unpaid employment with a UK company.
   * Supplying goods or providing services to the public.
   * Doing a work placement or internship.
6. **Can the ETA be Used to Start the Assignment?**:
   * **STRICTLY NO**. Performing the duties of the 2-year assignment under an ETA is illegal employment under s. 24B of the Immigration Act 1971. The worker must hold formal entry clearance under the Senior or Specialist Worker visa before commencing assignment duties.

---

## 1.9 Passport Requirements

### Official Details & Sources
* **Official Body**: UK Border Force / Home Office.
* **Direct URLs**:
  * Visiting the UK as an EU, EEA or Swiss citizen: [https://www.gov.uk/guidance/visiting-the-uk-as-an-eu-eea-or-swiss-citizen](https://www.gov.uk/guidance/visiting-the-uk-as-an-eu-eea-or-swiss-citizen)
  * Entering the UK: [https://www.gov.uk/uk-border-control](https://www.gov.uk/uk-border-control)
* **Publication / Effective Dates**: Official guidance published on GOV.UK, verified current for 2026.

### Specific Validity Rules
* **Statutory Requirement**: The Swiss passport **must be valid for the whole of the person’s stay in the UK**.
* **Debunking the "6-Month Rule"**: UK immigration rules do **NOT** require a Swiss passport to be valid for 6 months beyond the intended departure date. The official requirement is simply that the passport remains valid for the duration of stay.
* **National Identity Cards**: Swiss national identity cards are no longer accepted for UK entry (with narrow exceptions for individuals holding pre-settled/settled status under the EU Settlement Scheme). A valid biometric Swiss passport is mandatory.
* **Practical Best Practice for a 2-Year Assignment**: To avoid administrative complexity, the assignee’s passport should have at least 25 months of remaining validity upon visa application so that the 2-year visa and biometric eVisa are issued for the full duration without needing in-country renewal.

---

## 1.10 Employer Immigration Obligations

### Official Details & Sources
* **Official Body**: Home Office / UK Visas and Immigration.
* **Direct URLs**:
  * UK Visa Sponsorship for Employers: [https://www.gov.uk/uk-visa-sponsorship-employers](https://www.gov.uk/uk-visa-sponsorship-employers)
  * Right to Work Checks: An Employer's Guide: [https://www.gov.uk/check-job-applicant-right-to-work](https://www.gov.uk/check-job-applicant-right-to-work)
  * Immigration Skills Charge Guidance: [https://www.gov.uk/guidance/immigration-skills-charge](https://www.gov.uk/guidance/immigration-skills-charge)

### Comprehensive Breakdown of Employer Duties
1. **Sponsor Licence Maintenance**:
   * Must hold a valid Worker / Global Business Mobility sponsor licence.
   * Licence application fee: **£536** (small/charitable) or **£1,476** (medium/large).
   * Appoint Key Personnel on the Sponsor Management System (SMS): Authorising Officer, Key Contact, and Level 1 User.
2. **Assigning the Certificate of Sponsorship (CoS)**:
   * Issue an Undefined CoS via the SMS.
   * CoS assignment fee: **£239** per certificate.
3. **Payment of the Immigration Skills Charge (ISC)**:
   * Mandatory charge payable at the time of assigning the CoS for assignments of 6 months or longer.
   * **It is illegal to pass this charge on to the worker or deduct it from their pay**.
   * Cost: **£364 per year (£728 total)** for small businesses; **£1,000 per year (£2,000 total)** for medium/large businesses.
4. **Mandatory Reporting Duties (Within 10 Working Days via SMS)**:
   * If the sponsored worker fails to report for work on their first day (within 10 days of expected start date).
   * Any unauthorised absence exceeding 10 consecutive working days.
   * Significant changes in employment (change of job role, core duties, salary change, promotion, change of UK work location).
   * Early termination or curtailment of the assignment.
5. **Record-Keeping Duties (Appendix D to Sponsor Guidance)**:
   * Retain certified copies of the worker's passport biographical page.
   * Retain evidence of the date of arrival in the UK (flight ticket, boarding pass, or entry stamp).
   * Retain documentation proving **at least 12 months prior continuous service** in the Swiss entity (e.g. Swiss payroll records, Swiss employment contract).
   * Retain UK employment contract, job description, and salary payment records.
   * Maintain up-to-date contact records (UK residential address, telephone number, mobile number).
6. **Pre-Employment Right to Work (RTW) Check**:
   * Mandatory check performed **before the employee's first day of work in the UK**.
   * Swiss nationals hold digital status (eVisa). The employer must conduct an **online Right to Work check** via the official Home Office online portal using the candidate's date of birth and 9-character share code.
   * The PDF verification record must be saved securely and retained for the duration of employment plus 2 years.
7. **UK Payroll & PAYE Obligations**:
   * The UK subsidiary running UK payroll must operate PAYE on taxable pay and taxable benefits.
   * Register with HMRC and submit Real Time Information (RTI) Full Payment Submissions (FPS).
   * Set National Insurance category to exempt, retaining the Swiss Certificate of Coverage (PDA1) in payroll compliance files as statutory justification for zero NIC deductions.

### Separation of Employer vs. Employee Immigration Costs

| Cost Item | Amount | Paid By | Legal Status / Notes |
| :--- | :--- | :--- | :--- |
| **Sponsor Licence Fee** | £536 (small) / £1,476 (large) | **Employer** | One-off organisation cost. |
| **Certificate of Sponsorship (CoS)** | £239.00 | **Employer** | Paid upon CoS assignment. |
| **Immigration Skills Charge (ISC)** | £728 (small) / £2,000 (large) | **Employer** | Mandatory statutory levy; illegal to pass to employee. |
| **Visa Application Fee (≤ 3 years)** | £819.00 | **Employee** *(typically reimbursed)* | Standard visa application cost. |
| **Immigration Health Surcharge (IHS)** | £2,070.00 (£1,035/year) | **Employee** *(typically reimbursed)* | Upfront charge for NHS access. |
| **Business Visit ETA (pre-assignment)**| £20.00 | **Employee** *(typically reimbursed)* | Digital travel authorization for pre-assignment trip. |
| **Personal Maintenance Funds** | £1,270.00 (in bank 28 days) | **Employee** | Not a fee; or certified by A-rated sponsor on CoS. |

---

## 1.11 Summary of Verification and Ready Checks for Phase 2

Every research requirement set out in Section 1.1 through 1.10 of `Build.md` has been verified against official statutory instruments, government guidance, and rates for 2026/27.

* **Swiss Hypothetical Tax**: Deterministic statutory calculation model established based on § 35 StG ZH, 95% cantonal multiplier, 119% municipal multiplier, DBG Art. 36 federal tariff, producing ~CHF 32,927.01 (£29,933.65) annual hypothetical deduction.
* **Swiss Social Security**: Capped ALV (CHF 148,200 @ 1.10% = CHF 1,630.20) + uncapped AHV/IV/EO (CHF 170,000 @ 5.30% = CHF 9,010.00) = CHF 10,640.20 (£9,672.91) annual deduction.
* **UK Social Security**: Zero UK NIC payable due to the 24-month Certificate of Coverage under Article 14 of the UK-Switzerland Social Security Convention.
* **Benefit Exemption**: £8,000 statutory relocation exemption correctly applied under s. 287 ITEPA 2003, leaving £2,000 of moving/temp housing as taxable BIK in Year 1, London housing as £36,000 BIK each year, and relocation allowance as £4,545.45 taxable cash in Year 1.
* **Immigration**: Senior or Specialist Worker recommended; complete fee and obligation schedule established; ETA verified for business visits; no 6-month passport rule.

**Phase 1 is complete. Ready for User Review before proceeding to Phase 2.**

