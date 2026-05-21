# Review Plan

This review document identifies specific, high-stakes gates, validation failures, and evidence requirements tied to core decisions, particularly focusing on the conflict arising from prioritizing immediate evacuation speed over logistical ingress capacity and the need to formally validate C2 power resilience and jurisdictional handoff protocols before launch. The section locks down decision paths that create high-severity, quantified risks, such as the failure to bridge the T+6 to T+18 supply gap or the premature activation of the VEI-7 contingency.

## Numeric values
- Logistical ingress viability metric of 30% staging by T+16 hours — input to resource supply model  [derived | e=5 r=5 | quote: verified]
- VEI-7 trigger uplift rate of 5cm per hour sustained over three consecutive hours — threshold for catastrophic event escalation  [explicit | e=5 r=5 | quote: verified]
- Zone Zero population clear by T+6 hours deadline — gates launch readiness  [explicit | e=5 r=5 | quote: verified]
- Inbound logistical clearance rejection window of zero inbound logistical clearance until T+18 hours — duration of ingress denial  [explicit | e=5 r=5 | quote: verified]
- Zone Zero clearance success metric of 98% of registered vehicles exiting — gates launch readiness  [explicit | e=5 r=5 | quote: verified]
- Zone Zero staff count target is 800 essential staff — input to throughput model  [explicit | e=4 r=4 | quote: verified]

## Load-bearing assumptions
- Mandatory immediate contraflow on US-191 and US-20 accepts zero inbound logistics until T+18 hours.  [explicit | e=5 r=5 | quote: verified]
- VEI-7 contingency trigger activates upon uplift rate exceeding 5cm per hour over three consecutive hours.  [explicit | e=5 r=5 | quote: verified]
- Stafford Act declaration provides immediate access to $500M DRF ceiling for expenditure.  [inferred | e=5 r=5 | quote: verified]
- Formal transfer of custodial authority occurs the moment the first vehicular convoy clears egress control points.  [explicit | e=5 r=5 | quote: verified]
- National Guard engineers immediately conduct prophylactic ash washing on high-voltage substation components first.  [explicit | e=5 r=5 | quote: verified]
- Unified Command function distributes across three geographically separated, hardened federal facilities requiring remote coordination.  [explicit | e=5 r=5 | quote: verified]

## Gates and thresholds
- If inbound logistical clearance is zero until T+18 hours, then relief assets cannot stage until T+18.  [explicit | e=5 r=5 | quote: verified]
- If sustained uplift rate exceeds 5cm per hour for three consecutive hours, then trigger VEI-7 Scenario Beta.  [explicit | e=5 r=5 | quote: verified]
- If Zone Zero clearance is not met by T+6 hours, then the Pioneer Strategy fails its Phase 1 objective.  [explicit | e=4 r=5 | quote: verified]
- If Zone One compliance goal is below 95% by T+12 hours, then secondary gridlock risk increases.  [explicit | e=4 r=4 | quote: verified]
- If full transparency of VEI-6 threat is released, then uncontrolled mass exodus risks overwhelming unprepared contraflow routes.  [explicit | e=4 r=4 | quote: verified]
- If Authority Transfer is established early, then immediate shelter intake processes subordinate to potentially slower federal structures.  [explicit | e=4 r=4 | quote: verified]

## Risks and shocks
- Mandatory full contraflow sacrifices all logistical ingress capacity for a critical window of 18 hours — creating a logistical gap post-T+6.  [stress_test | e=5 r=5 | quote: verified]
- Risk of resource failure once mandated shelter intake begins if logistical ingress capacity is sacrificed for evacuation speed.  [stress_test | e=5 r=5 | quote: verified]
- Grid failure due to ash flashovers starves generators at critical C2 nodes due to delayed fuel influx post-evacuation.  [stress_test | e=4 r=5 | quote: verified]
- Delaying perimeter security allows opportunistic civil disorder and looting in Zone One towns between T+6 and T+12 hours.  [stress_test | e=4 r=4 | quote: verified]
- Sacrificing power hardening buys long-term stability but strains engineering against immediate perimeter security needs T+6 to T+12 — increasing civil disorder risk.  [stress_test | e=4 r=4 | quote: verified]
- Premature VEI-7 trigger risks massive resource expenditure and public panic if magma reservoir stabilizes after initial surge.  [stress_test | e=4 r=4 | quote: verified]

## Missing data to estimate
- Required duration for C2 node power cache sustainment in hours — factor for multiplying the C2 72-hour burn rate  [missing | e=3 r=5 | quote: verified]
- Cost per sortie for emergency helicopter ingress in USD — required to calculate total cost of T+8 to T+16 airlift.  [missing | e=3 r=5 | quote: verified]
- Total number of staff requiring N95 PPE at egress checkpoints — factor for allocating egress-based PPE cache.  [missing | e=3 r=4 | quote: verified]
- Duration in days for which the Stage 1 security lockdown on evacuated Zone One communities is planned — factor for looting damage projection.  [missing | e=3 r=3 | quote: verified]
- Total period cost rate for running decentralized C2 nodes in USD/hour — required to project total C2 operational burn.  [missing | e=1 r=5 | quote: unverified]
- Time duration in hours for which the aviation grounding constraint (Decision 7) is active — factor for scaling readiness cost.  [missing | e=1 r=4 | quote: unverified]
