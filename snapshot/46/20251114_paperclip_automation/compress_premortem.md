# Premortem

This section documents critical failure hypotheses for the project, detailing the underlying assumptions whose invalidation acts as a potential threat, and provides quantified tripwires that signal when a discrete failure scenario has been triggered, alongside the immediate impact pathway that justifies model contingency planning.

## Load-bearing assumptions
- The project assumes the budget is sufficient for all phases, including contingency for unexpected costs.  [inferred | e=5 r=5 | quote: verified]
- The assumption of reliable modern interfaces on used machinery must hold true for OPC UA integration.  [inferred | e=5 r=5 | quote: verified]
- The assumed allocation split favors machinery acquisition at 50% of the total budget.  [inferred | e=4 r=5 | quote: verified]
- The budget must cover specialty PLC expert engagement, estimated around $50,000 for the middleware abstraction layer.  [inferred | e=4 r=4 | quote: verified]
- A used wire bender exists within budget that supports at least one modern, documented fieldbus protocol.  [inferred | e=5 r=5 | quote: unverified]
- The $\le 2$ hours per week manual intervention limit is achievable with robust exception handling.  [inferred | e=5 r=4 | quote: unverified]

## Gates and thresholds
- If documented manual intervention time exceeds 120 minutes across a standard operational week, then achieving the feasibility demonstration is failed.  [explicit | e=5 r=5 | quote: verified]
- If the 99th percentile API job queue latency exceeds 100ms during stress testing, then the project pivots to HMI-controlled demonstration.  [stress_test | e=4 r=4 | quote: verified]
- If the lowest qualified bid for OPC UA middleware exceeds $75,000, then the project reverts to the high-risk custom I/O translator model.  [stress_test | e=5 r=5 | quote: unverified]
- If the commission expert requires an extension beyond 4 weeks total engagement time, then the project sponsor must inject $50,000 in new capital or be canceled.  [stress_test | e=5 r=4 | quote: unverified]
- If carrier staging requirements necessitate capital expenditure greater than $40,000 for mechanical redesign, then the project pivots to a B2B volume shipment model only.  [stress_test | e=4 r=4 | quote: unverified]
- If initial permit feedback requires electrical remediation exceeding $25,000, then contingency funds allocated for spares must be re-allocated to cover the deficit.  [stress_test | e=4 r=3 | quote: unverified]

## Risks and shocks
- Regulatory delays from permitting issues: 4–8 weeks of schedule delay.  [stress_test | e=5 r=5 | quote: verified]
- Budget overruns due to commissioning or compliance issues: $20,000–$50,000 overrun magnitude.  [stress_test | e=5 r=4 | quote: verified]
- Security breach downtime: 1–2 weeks of operational shutdown.  [stress_test | e=5 r=4 | quote: verified]
- Environmental compliance fines from waste disposal or emissions: $5,000–$15,000 potential fines.  [stress_test | e=5 r=3 | quote: verified]
- Integration issues with used wire bender causing debugging delays: 4–6 weeks development time impact.  [stress_test | e=5 r=5 | quote: unverified]
- Delays in critical machinery delivery: 3–5 weeks project completion delay.  [stress_test | e=5 r=3 | quote: unverified]

## Missing data to estimate
- Maximum acceptable post-commissioning engineering support cost buffer in USD — how to estimate from Review 11.1.  [missing | e=1 r=4 | quote: unverified]
- Total planned expenditure on middleware development in USD for stress testing budget sensitivity — needed for FM5 analysis.  [missing | e=1 r=4 | quote: unverified]
- Total weekly operating revenue exposure in USD for scheduling delay simulation — required for quantifying schedule delay impact.  [missing | e=1 r=4 | quote: unverified]
- Total cost for the replacement control board for the used wire bender in USD — required for spare parts scenario modeling.  [missing | e=1 r=4 | quote: unverified]
- Maximum allowed variance percentage for raw wire stock quality before requiring a system re-tune — required for Decision 13 sensitivity.  [missing | e=1 r=3 | quote: unverified]
- The dollar value of equipment to be purchased for staging/palletizing conveyors if carrier rejection occurs in USD — required for FM6 response funding.  [missing | e=1 r=3 | quote: unverified]
