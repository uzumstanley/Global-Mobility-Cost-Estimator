The next step is a short practical project. In short, you'll build a small full-stack tool that estimates what it would cost, and how long it would take, to send an employee from Switzerland to work in the UK for two years.

The key points:

- Deadline: please submit by Monday 16 November 2026, 23:59 UK time.
- Tech: Python and Django on the back end.
- What to send as your submission is your GitHub repository and a 5 to 10 minute Loom video in which you walk through your code and explain how it works.

The brief also sets out exactly how your work will be checked, so you know what we're looking for from the start.

Assignment Cost Estimate: Candidate Pack

Company: TheCozm, thecozm.com
Switzerland → UK
Five days
Build a small full-stack tool that tells a company what it will cost, and how long it will take, to move an employee to another country. The case to build around: an employee sent from Switzerland to work in the UK for two years.
Deadline: five days from the day you receive this pack. The email this pack came with gives the exact date and time.
Questions: reply to the email this pack came with.
The brief
Tab 1, cost estimate: inputs for home and host country, salary, bonus and assignment benefits. The output is a table of the total cost to the employer when the employer pays the UK tax (method below).

Tab 2, immigration: the work permit the employee needs, whether a business visit before the assignment needs a visa, the passport requirements, what the company must do, and how long and how much it all takes. Researching this is part of the task.

Back end: Python and Django. If you pass, you will share your screen, walk through the back end and answer questions on it.

Front end: any framework. It should be easy to understand at a glance: not crowded, help text where something needs explaining, dropdowns for inputs, and tabs to separate concepts.

Sources: every tax rule and every immigration requirement the tool shows carries a link to the official page it came from.
AI tools: You may use AI tools such as Claude or ChatGPT to research the tax and immigration rules.

What to submit
Reply to the email this pack came with, and include two links:
1. Your GitHub repository. Your own repository, not a fork, built up over several commits. It can be public or private.

2. A Loom video of 5 to 10 minutes. Open the code and explain, in your own words, how it works and why you built it that way. Put the link in your README as well.
In the same reply, please also tell us:
* Your master’s subject and the year you finished or expect to finish.
* The country you would work from, and whether you have the right to work there.
* Optional: if you would like to be considered for work with our German clients, your level of German (for example B2, C1, or “business level”).
Your README needs the steps to install and run the tool (someone following them on a clean machine should get a cost estimate without editing any code), how to run your tests, and a section naming the AI tools you used for research and what for. “None” is a valid answer. Keep API keys, tokens and passwords out of every file and out of the commit history.

How your work is checked
Fifteen checks. Each one is answered yes or no, never with a number or a grade.
No.	Check	What counts as a yes	Who checks	Gate
1	The tool runs from the README steps	A clean install following the README produces a cost estimate with no edits to the code	Engineer	Gate
2	It covers work permit, business visa and passport	The immigration tab states a requirement for all three	Engineer	Gate
3	Every answer cites a source	Each tax rule and each immigration requirement carries a link to where it came from	Engineer	Gate
4	No secrets in the repository	No API keys, tokens or passwords in any file or in the commit history	Engineer	Gate
5	Original repository, not a fork	GitHub does not mark it as a fork, and the first commit is from your account	Engineer	Gate
6	Built over several commits	At least five commits from your account, on at least two different days	Engineer	
7	The README states which AI tools were used	A section names the tools used for research and says what for. “None” also counts	Engineer	
8	It takes the test case in this pack	The test-case inputs are accepted as given and produce a cost table for both years	Engineer	
9	Sources are official and the links open	Each link opens and points to a government, tax authority or regulator page	Engineer	
10	Python and Django back end	The back end is a Django project and its own logic is in Python	Engineer	
11	A test exists and passes	At least one automated test is in the repository and passes when run	Engineer	
12	Bad input gives a clear error	A missing or malformed field returns a readable message, not a crash	Engineer	
13	Submitted on time	The repository and video arrived within the five days	The Cozm	
14	You explain your own code	In a Loom of 5 to 10 minutes, you open the code and explain how it works	The Cozm	
15	One answer matches its source	For the test case, a stated figure or requirement agrees with the cited page	Engineer	Shortlist only
To pass. All five gates are yes, and at least 10 of checks 1 to 14 are yes.
People check your work. Engineers at The Cozm answer checks 1 to 12 and 15. The Cozm’s hiring team answers checks 13 and 14.
Every result can be explained. Each check is a fact anyone can verify. If you want a result explained, reply to the email this pack came with.
What is assessed. Your work: the repository and the video, against the fifteen checks above. Passing is decided by those checks alone. Separately, to be offered a role you must hold or be completing a master’s in computer science or a related subject (2024–2026), and be able to work legally from the UK or Germany. For roles serving our German clients, we also need spoken and written German at business level (CEFR C1 or equivalent), which we check in a short conversation in German. We do not assess your university, degree grade, name, photo, age, gender, nationality or any other protected characteristic.
What happens next. We reply to everyone who submits. If you pass, there is a short call, then a session where you show what you built.

Four ideas to understand first
Tax equalisation. The employee should be no better and no worse off than if they had stayed at home. The employer pays whatever tax the host country charges.
Hypothetical tax. The tax and social security the employee would have paid at home. The employer deducts it from their pay, so they still bear their usual home tax.
Tax on tax. The host tax the employer pays for the employee is itself taxable income. It has to be grossed up, which is why the employer’s tax bill is higher than a normal tax calculation.
Social security. In the UK this is National Insurance. In Switzerland it is AHV/IV/EO and unemployment insurance. Which country’s system applies during the assignment depends on the agreement between the two countries.

What the cost tab should show
The output answers one question: what does this assignment cost the employer each year? Lay the table out in four sections, in this order:

1. Home pay. Salary and bonus, as if the employee had stayed in Switzerland.

2. Assignment benefits. For example housing, relocation and moving costs. Tag each one as taxable cash, a taxable benefit in kind, or not taxable in the UK.

3. Host tax and charges paid by the employer. UK income tax on the assignment pay, including the tax on tax, plus any employer charges that apply.

4. Deductions. Hypothetical Swiss income tax and hypothetical Swiss social security, which reduce the employer’s cost.

Then show the total employer cost per year and over the whole assignment, as a figure and as a multiple of home pay, and list the assumptions the figure depends on.
The gross-up starts from I, the UK taxable pay before any tax: net home pay after the hypothetical deductions, plus the taxable benefits. The UK tax T paid by the employer is the value that satisfies:
T = UKTax(I + T)
Solve it by iteration, not one multiplication. UK rates change between bands as income rises, and the personal allowance is withdrawn above £100,000, so a single multiplication gives the wrong answer.

Test case: Switzerland to UK, two years
Your tool must accept these inputs as given. We do not supply the answer: your figures are checked against the official sources you cite, so show your working in the output.

Test case inputs
Input	Value
Home → host	Switzerland (city of Zurich) → UK (London), 6 April 2026 to 5 April 2028: two full UK tax years
Employee	Swiss national, single, no children. Has worked for the employer in Zurich for 3 years
Employer	A Swiss company, sending the employee to its UK subsidiary, which runs a UK payroll
Base salary	CHF 150,000 a year
Bonus	CHF 20,000 a year
Housing in London	£3,000 a month, rent paid by the employer directly to the landlord
Relocation allowance	CHF 5,000 cash, year 1 only
Moving costs (flights, shipping)	£6,000, paid by the employer, year 1 only
Temporary housing	£4,000: a serviced apartment for the first 4 weeks, year 1 only
Exchange rate	£1 = CHF 1.10 (fixed for both years; make it an input)
Assumptions you may make
Hypothetical Swiss tax is the federal, cantonal and communal income tax a single person living in the city of Zurich would pay on the same salary and bonus, with no church tax. You may check your figure against the Swiss Federal Tax Administration’s calculator.
Hypothetical Swiss social security covers the employee’s AHV/IV/EO and unemployment insurance contributions. Leave out the occupational pension (BVG).
The employee is UK tax resident in both years and leaves Swiss tax residence for the assignment. Use 2026/27 UK rates for both years.
Decide which country’s social security applies during the assignment, show it in the output, and explain the rule you applied.
This is an exercise, not tax advice.
Where to start
These are starting points, not the full list. Researching the rest is part of the task.
* GOV.UK: Income Tax rates and Personal Allowances and Rates and thresholds for employers 2026 to 2027
* HMRC: Tax equalisation (HS212) and PAYE72028: how to gross up
* GOV.UK: Social security contributions for workers coming to the UK from Switzerland
* Swiss Federal Tax Administration: tax calculator