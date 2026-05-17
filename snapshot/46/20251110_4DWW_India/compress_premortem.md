# Premortem

This section lists critical assumptions and detailed failure modes, providing the structure for defining probabilistic inputs (assumption failure likelihoods) and quantifying the associated financial and operational impact (tripwires and response costs like sunk cost or budget overrun estimates) necessary for risk simulation.

## Numeric values
- SME cohort minimum representation mandate: 50% employees — input for selection bias modeling.  [explicit | e=5 r=5 | quote: verified]
- Mandatory observation window for negative metric trends before rollback execution: 30-day window — duration input for adaptive management.  [explicit | e=5 r=5 | quote: verified]
- Pilot period for primary measurement: 48 months — total pilot duration for Monte Carlo simulation horizon.  [explicit | e=5 r=5 | quote: verified]
- Incentive budget allocation toward productivity-sharing grants: 80% of budget — input for incentive mix simulation.  [explicit | e=4 r=4 | quote: verified]
- Pilot duration for assessing findings: three-year window — time horizon for longitudinal analysis.  [explicit | e=4 r=4 | quote: verified]
- Pilot period for legislative negotiation timeline: 36 months — time constraint on regulatory amendment depth.  [explicit | e=4 r=3 | quote: verified]

## Load-bearing assumptions
- State Labor Departments will agree to a binding PMO tie-breaking vote on core KPI adherence despite political pressure.  [inferred | e=5 r=5 | quote: verified]
- Compliance with low-friction data entry linking directly to incentive tranche unlocks must drive sustained behavioral adoption.  [inferred | e=5 r=5 | quote: verified]
- The identified partner companies' internal SME classifications align with the established definition for pilot selection.  [inferred | e=4 r=5 | quote: verified]
- The proposed performance-linked grant structure will catalyze structural process changes rather than temporary boosts.  [inferred | e=4 r=5 | quote: verified]
- The administrative simplicity goal of two worker-hours per week for SME compliance is achievable without sacrificing data quality.  [inferred | e=4 r=4 | quote: verified]
- Unionized firms will remain compliant and cooperative during the forty-eight month period.  [inferred | e=4 r=4 | quote: verified]

## Risks and shocks
- Pilot delay due to regulatory friction: 3–6 month pilot delay, INR 150–300 crore sunk cost.  [stress_test | e=5 r=5 | quote: verified]
- Data quality degradation risks 50% reduction in productivity attribution confidence and INR 50 crore evaluation loss.  [stress_test | e=5 r=5 | quote: verified]
- Widespread adoption failure post-incentive causes up to 15% budget overrun, INR 300 crore, perceived as subsidy sink.  [stress_test | e=5 r=5 | quote: verified]
- If 50% SME mandate causes high small-firm failure, rollout toolkit becomes unusable, costing INR 400 crore re-design.  [stress_test | e=5 r=5 | quote: verified]
- Localized infrastructure failures cause simultaneous failure threshold breaches in two (2) to three (3) cities, leading to 6-week delay.  [stress_test | e=5 r=4 | quote: verified]
- Unplanned legal review due to notification ambiguity causes INR 5 crore unplanned legal cost and four-week data collection pause.  [stress_test | e=5 r=4 | quote: unverified]

## Missing data to estimate
- Baseline administrative time spent per week per SME employee on pilot compliance — estimate via pre-pilot time-and-motion study.  [missing | e=1 r=5 | quote: unverified]
- Total annual revenue target for pilot firms to calculate incentive dependency impact — estimate based on industry benchmarks.  [missing | e=1 r=4 | quote: unverified]
- Average revenue lost per week for manufacturing sites if machinery uptime data fails verification — estimate based on facility cost structure.  [missing | e=1 r=4 | quote: unverified]
- The specific required political capital expenditure amount required to overcome a State Labor Department block by executive mandate — estimate required legal/bureaucratic overhead cost in INR.  [missing | e=1 r=4 | quote: unverified]
- Total number of eligible external firms for voluntary paid adoption trials of the scheduling optimizer post-Month 24 — estimate based on industry outreach capacity.  [missing | e=1 r=3 | quote: unverified]
- Cost per FTE employee for PMO staffing across the forty-eight month pilot duration — estimate based on government pay scales.  [missing | e=1 r=3 | quote: unverified]
