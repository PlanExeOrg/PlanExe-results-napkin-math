# Review Plan

This section specifies validation checks, mandatory deadlines, and quantified thresholds that must be met or failed for the primary and secondary decisions selected under the Pioneer strategy, providing essential quantitative gates for Monte Carlo simulation inputs like budget burnout thresholds and operational capacity failures.

## Numeric values
- Target volume recovery of 40% (40%) — gates primary volume success metric.  [explicit | e=5 r=5 | quote: verified]
- Maximum feasible financial incentive of 5 DKK per crate — drives initial consumer action.  [explicit | e=5 r=5 | quote: verified]
- Total program budget ceiling of 4 million DKK — financial constraint for all activities.  [explicit | e=5 r=5 | quote: verified]
- Target recovery volume of 108,000 crates — minimum threshold for success.  [explicit | e=5 r=5 | quote: verified]
- Maximum donation outlay budget of 1.35 million DKK — maximum spend on consumer incentive.  [explicit | e=5 r=4 | quote: verified]
- Estimated annual loss volume of 270,000 units — source population for recovery target.  [explicit | e=5 r=4 | quote: verified]

## Load-bearing assumptions
- The campaign requires a critical volume return rate of at least 40% to meet the environmental rationale.  [explicit | e=5 r=5 | quote: verified]
- The Pioneer strategy requires routing all returned crates to centralized hubs for ultrasonic cleaning first.  [explicit | e=5 r=5 | quote: verified]
- The Pioneer strategy commits to designating supermarkets as the sole collection point during the initial pilot phase.  [explicit | e=5 r=4 | quote: verified]
- The primary marketing posture will utilize a slightly irreverent narrative centered on the crates' secret lives.  [explicit | e=5 r=4 | quote: verified]
- The quality protocol must ensure high reuse rates, realizing an estimated 106 tonnes of CO2 avoided.  [explicit | e=5 r=3 | quote: verified]
- The primary incentive of 5 DKK must not exhaust the 4 million DKK budget ceiling prematurely.  [inferred | e=3 r=5 | quote: verified]

## Gates and thresholds
- If premature budget exhaustion if high volume exceeds 1.35M DKK donation budget, then risking 500,000 DKK funding need.  [stress_test | e=5 r=5 | quote: verified]
- If consumer engagement fails to meet the 40% return minimum, then the entire environmental rationale fails.  [explicit | e=5 r=5 | quote: verified]
- If the first tier incentive runs out at 50,000 returns, then subsequent returns drop to 3 DKK.  [explicit | e=5 r=4 | quote: verified]
- If the return volume target of 40% fails, then the charitable donation mechanism's justification is undermined.  [derived | e=3 r=5 | quote: verified]
- If the financial incentive is set too high, then budget exhaustion may require the campaign to end prematurely.  [inferred | e=4 r=4 | quote: verified]
- If municipal channel integration is not proven robust, then municipal intake is deferred past the initial pilot phase.  [explicit | e=4 r=4 | quote: verified]

## Risks and shocks
- Logistical bottleneck at hubs due to Pioneer strategy: throughput less than 7,000 crates/week stalls assets.  [stress_test | e=5 r=5 | quote: verified]
- Irreverent marketing alienates partners, potentially causing 50% reduction in organic impressions or requiring 500,000 DKK marketing cost increase.  [stress_test | e=5 r=4 | quote: verified]
- If 30% of municipalities fail Q3 agreement, volume capacity is curtailed below 108,000 units.  [stress_test | e=5 r=4 | quote: verified]
- Inconsistent quality grading leading to expedited reintroduction of poor inventory increases 2027 replacement production costs by 15%.  [stress_test | e=5 r=4 | quote: verified]
- Logistics costs consuming greater than 60% of the 2.65 million DKK non-donation budget threatens economic viability.  [stress_test | e=5 r=4 | quote: verified]
- Inaccurate returns tracking at high-volume stores loses 10,000 DKK in tracking value.  [stress_test | e=5 r=3 | quote: verified]

## Missing data to estimate
- The cost per recovered crate for the supermarket channel (DKK/crate) — needed to calculate logistics budget impact.  [missing | e=2 r=5 | quote: unverified]
- The cost per recovered crate for the municipal channel (DKK/crate) — needed to compare channel efficiency.  [missing | e=2 r=5 | quote: unverified]
- The absolute annual revenue/cost exposure (DKK/week) if logistical throughput stalls for one week — needed to quantify Risk 2 impact.  [missing | e=2 r=4 | quote: unverified]
- The average time in minutes for a consumer transaction at supermarket collection points (minutes/transaction) — needed for operational burden budgeting.  [missing | e=2 r=3 | quote: unverified]
- The required percentage of Arla QA staff trained in food-grade handling (percent/total QA staff) — needed to size the specialized inspection team.  [missing | e=1 r=3 | quote: unverified]
- The average cost per week of maintaining a position on the external industrial plastics recycling market (DKK/week) — needed to budget delayed off-take holding costs.  [missing | e=1 r=3 | quote: unverified]
