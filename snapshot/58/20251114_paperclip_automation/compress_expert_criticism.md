# Expert Criticism

This section identifies critical technical trade-offs where strategic decisions create mutually exclusive control architectures, leading to high technical risk and guaranteed software customization effort if the pragmatic path is followed instead of the aggressive, standardized path; it also flags severe underestimation of sunk costs required for safety engineering and physical integration labor relative to the available budget.

## Numeric values
- Budget range is $300,000 to $500,000 USD — input to budget/CAPEX model.  [explicit | e=5 r=5 | quote: verified]
- Acceptable manual work is less than or equal to 2 hours per week — maximum allowable exception time.  [explicit | e=5 r=5 | quote: verified]
- Contingency budget reserve of $100,000 established — capital reserve placeholder for risk.  [stress_test | e=5 r=5 | quote: verified]
- Wire bending machine budget is $20,000 to $40,000 — CAPEX component for forming hardware.  [explicit | e=5 r=4 | quote: verified]
- Packing machine budget is $10,000 to $30,000 — CAPEX component for packaging hardware.  [explicit | e=5 r=4 | quote: verified]
- 4,000 sq ft reserved for pilot line — physical footprint constraint.  [explicit | e=5 r=4 | quote: verified]

## Load-bearing assumptions
- Manual intervention limit is achievable at less than two (2) hours per week.  [inferred | e=5 r=5 | quote: verified]
- Used machinery integrates smoothly with modern control systems like OPC UA.  [inferred | e=5 r=5 | quote: verified]
- The focus on automation balances product quality standards sufficiently to meet low exception targets.  [inferred | e=5 r=4 | quote: verified]
- The initial $300,000 to $500,000 budget covers all phases including contingency costs.  [inferred | e=4 r=4 | quote: verified]
- The physical interface between forming and packing cells will not experience chronic jamming.  [inferred | e=4 r=4 | quote: verified]
- Local regulatory bodies will approve necessary permits without demanding costly facility upgrades.  [inferred | e=5 r=3 | quote: verified]

## Gates and thresholds
- If documented manual intervention exceeds two (2) hours per week, then the automation goal is failed.  [explicit | e=5 r=5 | quote: verified]
- If the expert tuning period extends beyond two (2) weeks, then budget reserves for on-site experts will be overrun.  [stress_test | e=4 r=4 | quote: verified]
- If wire bender requires custom sensor retrofitting, then software development timeline will extend significantly.  [inferred | e=4 r=4 | quote: verified]
- If the project selects the cheapest used bender, then custom interface engineering will extend timeline.  [inferred | e=4 r=4 | quote: verified]
- If the control system relies on proprietary protocols, then maintaining the system imposes high customization cost.  [inferred | e=4 r=4 | quote: verified]
- If local server hardware purchase is made, then capital buffer for expert commissioning might be constrained.  [inferred | e=3 r=4 | quote: verified]

## Risks and shocks
- Failure to pre-engineer OSHA compliance results in immediate site shutdown and mandatory, expensive retrofitting.  [stress_test | e=5 r=5 | quote: verified]
- Used bender requiring custom sensor retrofitting leads to significant extension of Phase 4 software timeline.  [inferred | e=4 r=4 | quote: verified]
- Over-investing in a higher-cost wire bender constrains capital available for expert commissioning/tuning.  [inferred | e=4 r=4 | quote: verified]
- Ignoring community engagement may result in public opposition leading to regulatory delays and reputation damage.  [stress_test | e=5 r=3 | quote: verified]
- Outsourcing critical PLC integration accelerates timeline but significantly increases fixed software costs.  [inferred | e=4 r=3 | quote: verified]
- Mandating MQTT on old PLCs risks exceeding their limited computational budget, forcing expensive board upgrades.  [inferred | e=4 r=3 | quote: verified]

## Missing data to estimate
- Required throughput rate per hour — to scale production cycles and capacity planning.  [missing | e=5 r=4 | quote: verified]
- Required uptime percentage per operational period — to scale maintenance and reliability calculations.  [missing | e=5 r=4 | quote: verified]
- Duration in months for which the $300,000-$500,000 budget is expected to last — to calculate monthly burn.  [missing | e=1 r=4 | quote: unverified]
- Period revenue exposure per week — to calculate impact of shutdown duration stress tests.  [missing | e=1 r=4 | quote: unverified]
- Absolute value of remaining capital after wire bender purchase — needed to calculate expert commissioning ceiling.  [missing | e=1 r=4 | quote: unverified]
- Cost per specialist hour for remote PLC troubleshooting — to properly scope expert budgeting.  [missing | e=1 r=3 | quote: unverified]
