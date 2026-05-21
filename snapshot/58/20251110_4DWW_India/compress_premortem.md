# Premortem

This section defines specific, quantifiable assumptions about political cooperation, data collection feasibility, incentive dependency, and infrastructure readiness that, if violated, trigger defined failure modes with high organizational impact. It provides the specific failure triggers and associated tripwires necessary to parameterize Monte Carlo simulations modeling project timeline and budget viability under execution risk.

## Numeric values
- SME participation mandate must be 50% of participating companies — explicit — scales cohort composition assumptions  [explicit | e=5 r=5 | quote: verified]
- Rigorous quantitative threshold for immediate rollback: 10% drop in first-pass yield sustained over two consecutive months — stress_test — scales rollback execution uncertainty  [stress_test | e=4 r=5 | quote: verified]
- Mandatory observation window for negative metric trends toward threshold: 30-day — stress_test — scales delay before rollback execution  [explicit | e=4 r=5 | quote: verified]
- Incentive budget allocation toward productivity-sharing grants contingent exclusively on hitting efficiency increases within nine months — 80% — scales incentive mix upon grant uptake  [explicit | e=4 r=4 | quote: verified]
- Duration for low-profile internal reporting before public visibility: 18 months — inferred — scales political risk exposure  [inferred | e=3 r=4 | quote: verified]
- Informal sector track budget allocation relative to formal track budget: 30% — inferred — scales resource allocation for parallel track  [inferred | e=3 r=4 | quote: verified]

## Load-bearing assumptions
- Pilot cohorts must mandate 50% participation from SMEs below one hundred employees.  [explicit | e=5 r=5 | quote: verified]
- Rollback execution must include a mandatory 30-day observation window before committee sign-off.  [explicit | e=5 r=5 | quote: verified]
- The central PMO structure requires joint sign-off on quarterly decision-gate thresholds by key state labor departments.  [explicit | e=4 r=5 | quote: verified]
- Centralized decision making power must enforce standardization without alienating State Labor Departments leading to passive resistance.  [inferred | e=4 r=5 | quote: verified]
- The formal sector pilot must test administrative simplicity among SMEs while ensuring stability for large firms for measurement.  [explicit | e=4 r=5 | quote: verified]
- High-frequency, granular data collection must be achieved without imposing intense administrative burden on participating SMEs.  [explicit | e=4 r=5 | quote: verified]

## Gates and thresholds
- If SME count falls below 50% of participating companies, then the cohort selection criteria fails representativeness.  [explicit | e=5 r=5 | quote: verified]
- If a metric trends negatively toward a threshold, then a mandatory 30-day observation window must proceed execution.  [explicit | e=5 r=5 | quote: verified]
- If state labor departments do not agree to joint co-chair sign-off on quarterly gates, then centralized enforcement is blocked.  [explicit | e=4 r=5 | quote: verified]
- If incentive uptake relies only on efficiency improvements and not documented gender diversity metrics, then the incentive structure is not tiered.  [explicit | e=4 r=4 | quote: verified]
- If productivity dips below the ten percent threshold sustained over two consecutive months, then rollback must instantly execute.  [stress_test | e=3 r=5 | quote: verified]
- If the PMO grants absolute decision authority over cohort selection, then state labor departments may resist compliance verification.  [explicit | e=4 r=4 | quote: verified]

## Risks and shocks
- Selection bias against typical SMEs from prioritizing large unionized manufacturing risks complicating transferability findings.  [stress_test | e=4 r=5 | quote: verified]
- High-granularity data demands risk significant SME burnout and non-compliance due to administrative overhead.  [stress_test | e=4 r=5 | quote: verified]
- Excluding marginal firms needing baseline support due to performance-linked grants narrows pilot representation of national landscape.  [stress_test | e=4 r=4 | quote: verified]
- Heavy centralization of PMO decision-making risks alienating powerful State Labor Departments causing passive resistance.  [stress_test | e=4 r=4 | quote: verified]
- Inflexibility from rigid quantitative rollback triggers sacrifices diagnostic depth, potentially forcing premature termination of volatile pilots.  [stress_test | e=4 r=4 | quote: verified]
- Pursuing comprehensive legislative amendment increases political risk and timeline dependencies halting immediate pilot initiation.  [stress_test | e=4 r=4 | quote: verified]

## Missing data to estimate
- Absolute cost in INR of the INR four hundred crore SME re-design if selection bias occurs — scales failure cost magnitude  [missing | e=1 r=5 | quote: verified]
- Maximum permissible political risk escalation fund expenditure in INR — total contingency budget — scales risk-modeling ceiling  [missing | e=1 r=5 | quote: verified]
- Average weekly administrative overhead work hours for SMEs before pilot implementation — baseline for ASI calculation — scales SME burnout risk  [missing | e=2 r=5 | quote: unverified]
- Total operational duration for the pilot in months — how long the UMF monitoring must run — scales data collection cost  [missing | e=1 r=5 | quote: unverified]
- Required minimum percentage of productivity retention post-incentive expiration — expected decay rate — scales long-term ROI estimate  [missing | e=1 r=5 | quote: unverified]
- Total estimated value of the incentive budget allocated for the formal sector track in INR — scales uptake probability  [missing | e=1 r=5 | quote: unverified]
