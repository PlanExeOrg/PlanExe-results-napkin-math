# Premortem

This section quantifies specific potential failure modes, identifying the contingent budget drawdown or recovery shortfall implied if critical performance tripwires are breached, such as exceeding incentive spending caps or failing to meet logistical throughput targets.

## Numeric values
- Maximum feasible donation incentive set at 5 DKK per crate — input to cash flow model and budget burn rate.  [explicit | e=4 r=5 | quote: verified]
- Projected volume of crates to be recovered annually set at 108,000 units — target volume for 40% goal.  [explicit | e=3 r=5 | quote: verified]
- Campaign total budget ceiling of 4 million DKK — hard constraint on total expenditure.  [explicit | e=3 r=5 | quote: verified]
- Target recovery volume specified as 40% of annual loss — primary project success metric.  [explicit | e=3 r=5 | quote: verified]
- Maximum donation outlay ceiling set at 1.35 million DKK — total financial constraint on consumer incentive.  [explicit | e=3 r=5 | quote: verified]
- Logistics budget allocation set at 1.65 million DKK — hard constraint on physical operational spend.  [explicit | e=3 r=5 | quote: verified]

## Load-bearing assumptions
- The aggressive 5 DKK incentive must balance against the 4 million DKK budget ceiling.  [explicit | e=4 r=5 | quote: verified]
- The core goal is recovering 40% of the annual loss volume within the 2026 timeline.  [explicit | e=3 r=5 | quote: verified]
- The pilot phase must rely solely on supermarket collection channels for initial logistical validation.  [explicit | e=3 r=5 | quote: verified]
- The marketing tone must be high-profile and slightly irreverent to spark conversation and virality.  [explicit | e=3 r=5 | quote: verified]
- The project goal requires generating a minimum of 20 million organic social media impressions.  [explicit | e=3 r=4 | quote: verified]
- Structural integrity assessment for reuse must be deferred to centralized hubs after receipt.  [explicit | e=3 r=4 | quote: verified]

## Gates and thresholds
- If consumer engagement fails to meet the 40% return target, then the environmental rationale is undermined.  [explicit | e=3 r=5 | quote: verified]
- If the pilot returns exceed 40,000 units, then the subsequent donation rate must drop to 3 DKK.  [explicit | e=3 r=4 | quote: verified]
- If if municipal channel cost per crate exceeds 25 DKK/unit, then it risks 700,000 DKK overrun on logistics budget.  [stress_test | e=3 r=4 | quote: verified]
- If the incentive structure sets the donation too low, then consumer engagement fails the 40% volume target.  [explicit | e=3 r=4 | quote: verified]
- If the fixed incentive is set too high, then the campaign may end prematurely before recovery stabilizes.  [explicit | e=3 r=4 | quote: verified]
- If the marketing budget is exhausted by paid media, then contingency funds are unavailable for logistical failures.  [derived | e=3 r=4 | quote: verified]

## Risks and shocks
- Premature budget exhaustion due to high participation risks a 500,000 DKK funding need or pre-term halt.  [stress_test | e=3 r=5 | quote: verified]
- Logistical bottleneck due to Pioneer strategy risks 4-8 week delay if capacity is underestimated by 50 percent.  [stress_test | e=3 r=4 | quote: verified]
- Irreverent marketing failure risks 50 percent reduction in organic impressions, requiring 500,000 DKK marketing cost increase.  [stress_test | e=3 r=4 | quote: verified]
- Municipal agreement failure threatens capacity curtailment, capping volume below 108,000 units if 30 percent fail Q3 agreement.  [stress_test | e=3 r=4 | quote: verified]
- Logistics consumption exceeding 60 percent of the 2.65 million DKK non-donation budget yields high net environmental cost.  [stress_test | e=3 r=4 | quote: verified]
- Failure to establish long-term habits post-campaign reverts 2027 recovery rates to baseline, reducing ROI by 15 to 25 percent.  [stress_test | e=3 r=4 | quote: verified]

## Missing data to estimate
- Municipal channel operational cost per crate in DKK — needed to model logistics budget viability against retail channel.  [missing | e=3 r=5 | quote: verified]
- Arla's internal procurement cost per new milk crate in DKK — needed to calculate true replacement cost ROI.  [missing | e=3 r=5 | quote: verified]
- Total duration in months/quarters for the Q3/Q4 rollout period — needed to scale logistics/marketing costs.  [missing | e=1 r=5 | quote: unverified]
- Total expected return volume in units for 2027 post-deceleration — needed to model long-term asset recovery success.  [missing | e=1 r=4 | quote: unverified]
- Initial adoption rate percentage for the Crate Passport system in Q3 — needed to model long-term habit formation lift.  [missing | e=1 r=4 | quote: unverified]
- Revenue impact loss per week if Crate Reintroduction Timelines delay asset recirculation — needed to quantify CO2 realization offset risk.  [missing | e=1 r=4 | quote: unverified]
