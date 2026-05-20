# Review Plan

This section catalogs all critical decision points, the validation criteria (KPI thresholds) attached to them, and the assumptions flagged as unstable or mission-critical, providing the core variables and logical gates required for timeline and budget simulation, particularly concerning the integration risk of used hardware versus standardized control layers.

## Numeric values
- Mandatory on-site expert time for PLC stabilization: 1 week — gates Phase 2 completion.  [derived | e=4 r=5 | quote: verified]
- Manual intervention limit target: 2 hours per week — gates launch readiness.  [explicit | e=4 r=5 | quote: verified]
- Required expert budget allocation for OPC UA middleware: ~$50,000 USD — input to integration cost model.  [explicit | e=4 r=4 | quote: verified]
- Budget allocation for expert commissioning reserve: one-third of the remaining capital — sensitivity driver for integration risk.  [explicit | e=4 r=4 | quote: verified]
- Potential cost increase for used machinery integration issue: $15,000–$30,000 — stress test for custom driver budget.  [stress_test | e=3 r=4 | quote: verified]
- Minimum machinery acquisition budget: $150,000 USD — input to CAPEX model.  [derived | e=3 r=4 | quote: verified]

## Load-bearing assumptions
- Used wire bender must integrate smoothly with modern control systems using OPC UA.  [inferred | e=4 r=5 | quote: verified]
- Local regulatory bodies will approve permits without requiring costly facility upgrades.  [inferred | e=4 r=4 | quote: verified]
- The $300,000 to $500,000 budget covers all phases, including contingency costs.  [inferred | e=4 r=5 | quote: unverified]
- Carrier requirements allow staging parcels on fixed tables rather than dynamic conveyance.  [inferred | e=3 r=4 | quote: verified]
- The manual intervention target of under two hours per week is achievable.  [inferred | e=4 r=5 | quote: unverified]
- A used wire bender exists within the budget that supports a modern, documented fieldbus protocol.  [inferred | e=4 r=5 | quote: unverified]

## Gates and thresholds
- If manual intervention time exceeds 120 minutes across a standard operational week, then the end-to-end demo fails feasibility proof.  [explicit | e=4 r=5 | quote: verified]
- If the Commissioning Tester cannot secure firm contract under $25,000 by 21 days, then mandatory on-site support budget is breached.  [derived | e=3 r=4 | quote: verified]
- If the Automation Control Architect does not deliver the signed control choice by D+10, then control architecture scope creep results.  [derived | e=4 r=5 | quote: unverified]
- If the Control System Protocol Selection results in custom I/O mapping, then the Software Expertise Allocation is compromised.  [inferred | e=4 r=5 | quote: unverified]
- If the Logistics Specialist does not confirm carrier staging rules pre-Phase 5, then a total Phase 6 demonstration failure is possible.  [derived | e=3 r=4 | quote: unverified]
- If Regulatory Compliance Coordinator cannot secure CSP sign-off before rigging, then immediate stop-work orders risk 4-8 weeks delay.  [derived | e=3 r=4 | quote: unverified]

## Risks and shocks
- Regulatory/Permitting delays: 4 to 8 weeks delay — input to schedule contingency.  [stress_test | e=5 r=4 | quote: verified]
- Used wire bender technical integration issue: 4 to 6 weeks development time — input to integration schedule buffer.  [stress_test | e=5 r=4 | quote: verified]
- Budget overruns from unforeseen costs: $20,000 to $50,000 overrun — input to contingency spending model.  [stress_test | e=5 r=4 | quote: verified]
- Machinery/component delivery delays: 3 to 5 weeks project completion delay — input to overall timeline risk.  [stress_test | e=5 r=3 | quote: verified]
- Single internal developer bottleneck: 2 to 4 weeks software delay — input to Phase 4 schedule risk.  [stress_test | e=5 r=4 | quote: unverified]
- Environmental compliance fines due to improper waste disposal: $5,000 to $15,000 fines — input to operational risk cost.  [stress_test | e=5 r=2 | quote: verified]

## Missing data to estimate
- Total available capital budget for post-commissioning spare parts reserve in USD — needed to finalize maintenance OPEX.  [missing | e=1 r=4 | quote: unverified]
- Expected frequency of wire stock material variance exceeding the tight specification window per period — required for exception rate modelling.  [missing | e=1 r=4 | quote: unverified]
- Total weekly or monthly revenue exposure from the pilot line — input for calculating downtime cost impact.  [missing | e=1 r=3 | quote: unverified]
- Total hours staff are expected to work per period to calculate burden rate for internal resources — input for overhead cost calculation.  [missing | e=1 r=2 | quote: unverified]
- Total candidate pool size for the dedicated internal software developer's role — input for assessing hiring probability.  [missing | e=1 r=2 | quote: unverified]
- Total budget allocated for the Internal Systems Liaison role per period in USD — input for staffing cost burn rate.  [missing | e=1 r=2 | quote: unverified]
