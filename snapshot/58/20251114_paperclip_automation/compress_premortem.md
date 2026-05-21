# Premortem

This section outlines specific, actionable failure scenarios rooted in core project assumptions that, if triggered, will necessitate drawdown from contingency funds or cause schedule delays, providing quantified tripwires for risk probability assessment. Each scenario details a specific failure mode, its measurable trigger points, and the required response to limit schedule impact or financial exposure. The critical pathways for failure center on integrating used machinery, maintaining budget for expert consultation, and meeting the strict manual intervention threshold.

## Numeric values
- Project budget range is $300,000 to $500,000 USD — sets total capital expenditure ceiling.  [explicit | e=5 r=5 | quote: verified]
- Expert engagement budget recommended minimum of $15,000 for 1 week on-site — scales mandatory expert time.  [inferred | e=5 r=5 | quote: verified]
- Manual intervention limit is less than 2 hours per week — gates feasibility demonstration.  [explicit | e=5 r=5 | quote: verified]
- Potential delay impact from regulatory compliance risk is 4 to 8 weeks — quantifies lead-time shock.  [stress_test | e=5 r=4 | quote: verified]
- OPC UA middleware development budget assumption is ~$50,000 — scales specialized software integration cost.  [explicit | e=5 r=4 | quote: verified]
- Pilot line footprint is 4,000 sq ft — sets physical capacity constraint.  [explicit | e=5 r=3 | quote: verified]

## Load-bearing assumptions
- The project needs to allocate emergency funds to secure 1 week of on-site expert time post-rigging.  [inferred | e=5 r=5 | quote: verified]
- The used wire bender must possess a documented modern fieldbus protocol within budget.  [inferred | e=5 r=5 | quote: verified]
- The chosen final control architecture will successfully support required low-latency edge compute implementation.  [inferred | e=5 r=5 | quote: verified]
- The specialized OPC UA middleware development cost must not exceed $75,000.  [stress_test | e=5 r=4 | quote: verified]
- Specialized PLC on-site integration expertise can be contracted for under $30,000 total for the first engagement.  [inferred | e=5 r=4 | quote: verified]
- Carrier staging protocols will allow for collection of parcels on fixed tables or pallets.  [inferred | e=5 r=4 | quote: verified]

## Gates and thresholds
- If manual intervention time exceeds 120 minutes across a standard week, the end-to-end automation feasibility fails.  [explicit | e=5 r=5 | quote: verified]
- If relying on legacy PLC programming increases risk of breaching the $\le 2$ hours exception limit, flexibility is constrained.  [inferred | e=5 r=5 | quote: verified]
- If external consultant integration costs exceed ~$50,000, the middleware budget is breached.  [explicit | e=5 r=4 | quote: verified]
- If the required network latency for edge compute is not achieved by local hosting, control loop reliability fails.  [inferred | e=4 r=5 | quote: verified]
- If custom driver development requires more than Phase 4 software risk mitigation, the integration strategy fails.  [inferred | e=4 r=4 | quote: verified]
- If the custom API command execution time exceeds installation to verified time, Phase 4 speed fails.  [inferred | e=4 r=4 | quote: verified]

## Risks and shocks
- Integration issues with used wire bender cause 4 to 6 weeks development time delay and $15,000 to $30,000 extra cost.  [stress_test | e=5 r=5 | quote: verified]
- Regulatory/Permitting delays cause 4 to 8 weeks delay and $10,000 to $20,000 cost increase.  [stress_test | e=5 r=5 | quote: verified]
- Relying on legacy PLC programming creates a hard dependency on obscure vendor knowledge, escalating risk to the $\le 2$ hours exception limit.  [inferred | e=5 r=5 | quote: verified]
- Budget overruns due to unforeseen commissioning/integration costs could range from $20,000 to $50,000.  [stress_test | e=5 r=4 | quote: verified]
- Reliance on single internal developer causes 2 to 4 weeks software delay and $5,000 to $10,000 extra cost.  [stress_test | e=5 r=4 | quote: verified]
- Delays in critical machinery supply cause 3 to 5 weeks project completion delay and $10,000 to $15,000 in rescheduling/storage costs.  [stress_test | e=5 r=4 | quote: verified]

## Missing data to estimate
- Total expected person-weeks for the internal developer to complete API development (Decision 2) — needed to budget for Risk 4 delays.  [missing | e=1 r=4 | quote: unverified]
- Required throughput (units/hour) for Phase 2/3 boundary check — needed to normalize stability metrics.  [missing | e=1 r=4 | quote: unverified]
- Total capital budget duration (months) — needed to convert fixed budget to average monthly burn rate.  [missing | e=1 r=5 | quote: unverified]
- Required usage duration (weeks) for initial expert commissioning — needed to scale weekly expert cost.  [missing | e=1 r=5 | quote: unverified]
- Total planned duration (weeks) for stabilization testing — needed to scale the consumption rate assumption A8.  [missing | e=1 r=4 | quote: unverified]
- Cost per week for consultant engaging in regulatory permit expediting — needed to scale Phase 1 delay cost impact.  [missing | e=1 r=4 | quote: unverified]
