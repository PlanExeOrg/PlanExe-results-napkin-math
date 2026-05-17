# Premortem

This section quantifies specific failure modes by defining external tripwires and associated contingent financial impacts, allowing quantification of the downside risk to the 2M DKK budget under various operational failures. It identifies key performance indicator thresholds, such as minimum acceptable conversion rates and maximum allowable utility cost breaches, which directly gate the necessity of drawing down the contingency fund or reducing initial CAPEX allocations.

## Load-bearing assumptions
- The project goal is to achieve operational readiness by 2026-09-15 to capture peak Q3 revenue.  [explicit | e=4 r=5 | quote: verified]
- It is possible to secure a fixed or semi-fixed energy tariff in Nuuk for Year 1.  [inferred | e=4 r=5 | quote: verified]
- The Year 1 revenue mix target is 40% courses, 35% memberships, and 25% drop-ins/rentals.  [explicit | e=3 r=5 | quote: verified]
- Local Taster Sessions must convert at a 15% target rate to paying customers.  [explicit | e=4 r=4 | quote: verified]
- The 6-month bulk material buffer inventory cost is within the initial budget allocation.  [explicit | e=3 r=4 | quote: verified]
- The four part-time instructors can be managed effectively as two FTE capacity.  [explicit | e=3 r=4 | quote: verified]

## Gates and thresholds
- If utility invoices exceed 30% of variable operating expenses for any given month, then a 5% utility surcharge trigger mechanism must activate.  [derived | e=4 r=5 | quote: verified]
- If the contingency fund reserve falls below 50% of initial allocation due to non-capital expenditure, then all non-essential CAPEX spending must cease immediately.  [stress_test | e=4 r=5 | quote: verified]
- If the utility variance application approval is delayed past 2026-09-15, then fit-out must stop to avoid rework costs.  [explicit | e=4 r=4 | quote: verified]
- If the conversion rate from Taster Sessions falls below 10% after the first 90 days, then ongoing Taster Sessions must be canceled.  [inferred | e=3 r=4 | quote: verified]
- If the blended off-peak utilization revenue covers less than 60% of direct utility overhead for two consecutive months, then speculative hourly rentals must cease.  [derived | e=4 r=5 | quote: unverified]
- If the single electric kiln fails requiring parts with lead time greater than 10 business days, then the response playbook triggers immediate revenue stopping measures.  [stress_test | e=4 r=5 | quote: unverified]

## Risks and shocks
- Reliance on high hourly rental rate model failing causes a deficit of 100,000–300,000 DKK by Q3.  [stress_test | e=5 r=5 | quote: verified]
- Exchange rate variance of 5-10% causes a 1-2 months material shortfall, delaying courses.  [stress_test | e=5 r=5 | quote: verified]
- Centralizing drying/firing may trigger unbudgeted mandates, causing up to 6 weeks delay to full capacity and 150,000 DKK in lost revenue.  [stress_test | e=5 r=5 | quote: verified]
- Single kiln breakdown halts all instructional revenue for 4-8 weeks, costing approximately 200,000 DKK.  [stress_test | e=5 r=5 | quote: verified]
- Bypassing formal Katuaq partnership risks a 20-30% tourist revenue drop during summer, challenging winter salary coverage.  [stress_test | e=5 r=4 | quote: verified]
- Potential labor law misclassification error could increase fixed labor cost by 20-35% in Year 1.  [stress_test | e=4 r=5 | quote: verified]

## Missing data to estimate
- The absolute DKK cost of the highest-risk modeling assumption (Labor Law non-compliance) is missing — estimate based on 4 instructors' 3-month salary commitment.  [missing | e=1 r=5 | quote: unverified]
- The total budgeted Year 1 revenue required to cover fixed expenses is missing — estimate based on required break-even point.  [missing | e=1 r=5 | quote: unverified]
- The total expected revenue generated from tourist drop-ins and workshops per operating month is missing — estimate based on 25% of total Year 1 revenue target.  [missing | e=1 r=4 | quote: unverified]
- The DKK/kWh price for commercial electricity in Nuuk is missing — estimate based on published Greenlandic commercial tariff indices.  [missing | e=1 r=5 | quote: unverified]
- The maximum acceptable duration of kiln downtime in weeks before operational pivot is missing — estimate based on material buffer depletion timeline.  [missing | e=1 r=4 | quote: unverified]
- The total number of potential local community groups available for Taster Sessions is missing — estimate based on local community registry counts.  [missing | e=1 r=3 | quote: unverified]
