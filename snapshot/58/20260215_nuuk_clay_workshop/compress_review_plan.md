# Review Plan

This section details specific decision gates, KPI thresholds, and fragile assumptions that must be tracked for model inputs, particularly focusing on the financial consequences of labor contract legality, revenue stream viability against speculative rental uptake, and the financial impact of utility rate volatility and single-point operational failures.

## Numeric values
- Year 1 budget is 2,000,000 DKK total — explicit input to total initial capital model  [explicit | e=5 r=5 | quote: verified]
- Contingency for Year 1 budget is 15% commitment — scaling factor for financial shock absorption  [explicit | e=5 r=5 | quote: verified]
- Ring-fenced technical buffer for kiln spare parts is 20,000 DKK — input to maintenance failure cost model  [explicit | e=4 r=4 | quote: verified]
- Year 1 revenue mix estimate: 40% from courses — scaling factor for course revenue stream  [explicit | e=3 r=5 | quote: verified]
- Year 1 revenue mix estimate: 25% from drop-ins/rentals — scaling factor for speculative revenue stream  [explicit | e=3 r=5 | quote: verified]
- Expected material buffer inventory cost is 300,000-450,000 DKK — scaling input for capital lockup calculation  [stress_test | e=3 r=4 | quote: verified]

## Load-bearing assumptions
- The contractor staffing model is legally permissible under Greenlandic labor law without triggering employee rights.  [inferred | e=5 r=5 | quote: verified]
- Local users will accept the high, ad-hoc hourly rental rate for unscheduled studio access.  [inferred | e=5 r=5 | quote: verified]
- The preferred location near Katuaq is secured by the target date of 2026-July-01.  [explicit | e=3 r=4 | quote: verified]
- The lead instructor's absence will not cause service failure if backups are adequately compensated.  [inferred | e=3 r=5 | quote: verified]
- It is possible to negotiate a fixed or semi-fixed energy tariff for Year 1 in Nuuk.  [inferred | e=3 r=4 | quote: verified]
- The conversion rate from free Taster Sessions to paid enrollment must meet the 15% target.  [explicit | e=3 r=4 | quote: verified]

## Gates and thresholds
- If the commercial lease is not secured by 2026-07-01, then the operational readiness date will be threatened.  [explicit | e=5 r=5 | quote: verified]
- If utility variance approval is not granted by 2026-08-15, then the fit-out completion timeline is at risk.  [explicit | e=5 r=5 | quote: verified]
- If the written labor law opinion is not obtained by 2026-05-20, then contract finalization is halted.  [explicit | e=4 r=5 | quote: verified]
- If instructor absence causes service cancellation for 90 operational days, then the SMART goal for reliability fails.  [explicit | e=4 r=5 | quote: verified]
- If energy costs exceed 30% of variable operating expenses, then a conditional 5% utility surcharge triggers.  [explicit | e=3 r=4 | quote: verified]
- If Taster Session conversion rate falls below 12%, then resources redirect from local outreach to digital marketing.  [inferred | e=3 r=4 | quote: verified]

## Risks and shocks
- If instructor contracting is non-compliant, the fixed labor cost increases by 20-35%, potentially exhausting contingency.  [stress_test | e=3 r=5 | quote: verified]
- If DKK weakens 5-10% against USD/EUR, the material buffer supply shortfalls by 1-2 months.  [stress_test | e=3 r=4 | quote: verified]
- If local users reject the high hourly rental rate, revenue drops 150,000–250,000 DKK deficit in Year 1.  [stress_test | e=3 r=4 | quote: verified]
- If utility rates escalate by 10% annually, gross margin per piece declines by 6-9% in Year 2.  [stress_test | e=3 r=4 | quote: verified]
- If the lead instructor is unavailable for 1 to 4 weeks, core studio hours are cancelled.  [stress_test | e=3 r=4 | quote: verified]
- If formal partnership is bypassed, tourist revenue drops 20-30% during summer months.  [stress_test | e=3 r=3 | quote: verified]

## Missing data to estimate
- Cost per FTE salary equivalent per month for the four part-time instructors — estimate based on compliant labor model  [missing | e=1 r=5 | quote: unverified]
- Total DKK value of the 6-month rolling material buffer inventory — input for capital lockup at launch  [missing | e=1 r=4 | quote: unverified]
- Number of months the project must run to cover the required setup cost from operating profit — estimate for break-even duration  [missing | e=1 r=5 | quote: unverified]
- Total operating hours per month for off-peak rental revenue calculation — estimate based on opening schedule  [missing | e=1 r=4 | quote: unverified]
- Absolute DKK cost target per firing cycle required for profitability calculation — estimate based on utility/material costs  [missing | e=1 r=4 | quote: unverified]
- Total number of local community non-arts group attendees in Year 1 available for Taster Sessions — input for conversion rate  [missing | e=1 r=3 | quote: unverified]
