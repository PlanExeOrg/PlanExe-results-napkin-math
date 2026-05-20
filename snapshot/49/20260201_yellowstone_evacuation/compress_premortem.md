# Premortem

This premortem section identifies critical failure modes derived from mandatory assumptions, quantifying the immediate impact of assumed failures in logistics, command and control power resilience, regulatory compliance handover, and public communication efficacy, which directly translate into quantified loss of life or time-window failure for evacuation and stabilization phases.

## Load-bearing assumptions
- The decision threshold for the VEI-7 contingency trigger is sustained uplift exceeding 5cm per hour over three hours.  [explicit | e=5 r=5 | quote: verified]
- Immediate access to $500 million Disaster Relief Fund is available for life-saving logistics.  [inferred | e=4 r=5 | quote: verified]
- The target clearance time for Zone Zero is strictly T+6 hours based on contraflow enforcement.  [inferred | e=4 r=5 | quote: verified]
- The initial mandatory N95 distribution prioritizes giving 70% of stock to designated State Guard triage points.  [inferred | e=4 r=4 | quote: verified]
- Wyoming/Montana National Guard engineering troops are ready to mobilize heavy equipment by T+3 hours.  [inferred | e=4 r=4 | quote: verified]
- Internal breach/recovery assets are ready for a 90-minute response time within Zone Zero.  [inferred | e=4 r=4 | quote: verified]

## Gates and thresholds
- If the sustained uplift rate exceeds 5cm per hour measured over three consecutive hours, then Scenario Beta (VEI-7 contingency) is activated.  [explicit | e=5 r=5 | quote: verified]
- If Zone Zero vehicle exit compliance is less than 98% by T+6 hours, then the T+6 clearance metric fails.  [derived | e=4 r=5 | quote: verified]
- If a blockage on US-191 lasts longer than 25 minutes, then breach assets are deployed immediately to clear the road.  [derived | e=4 r=5 | quote: verified]
- If C2 external power source failure is verified at any remote node before T+60 hours, then decentralized command structure fails.  [derived | e=4 r=5 | quote: verified]
- If airborne visibility drops below 1.2 miles, then the authorized T+8 to T+16 aviation ingress window is grounded.  [derived | e=4 r=5 | quote: verified]
- If the final N95 allocation matrix is not ready by T+1 hour, then stakeholder coordination for initial distribution fails.  [explicit | e=4 r=4 | quote: verified]

## Risks and shocks
- Contraflow failure on US-191/US-20 prevents Zone Zero clearance by T+6, causing thousands of casualties and Phase 2 cascade failure.  [stress_test | e=5 r=5 | quote: verified]
- Distributed C2 satellite links fail due to ashfall, increasing decision latency by 30-60 minutes, risking premature VEI-7 trigger activation.  [stress_test | e=5 r=5 | quote: verified]
- Premature VEI-7 trigger depletes resources staged for VEI-6 response, increasing mortality estimates by 20% due to lack of life support.  [stress_test | e=5 r=4 | quote: verified]
- Poor public messaging compliance uncertainty causes evacuation delay of 8-10 hours, leading to bottlenecks at I-90/Bozeman staging.  [stress_test | e=5 r=4 | quote: verified]
- Pioneer strategy's zero inbound logistics until T+18 creates a gap causing mass casualties in Zone One from respiratory/dehydration issues, estimated cost over $500,000+ emergency mobilization.  [stress_test | e=5 r=5 | quote: unverified]
- Ashfall hardening efforts divert engineering assets from perimeter security, causing civil disorder/looting in Zone One communities between T+6 to T+12.  [stress_test | e=5 r=3 | quote: verified]

## Missing data to estimate
- Estimated average fuel consumption rate for decentralized C2 nodes operating at maximum load for 48 hours — required for cache sizing validation.  [missing | e=1 r=5 | quote: unverified]
- Cost per heavy-lift helicopter sortie used for emergency ingress — estimate based on military contract rates for CH-47 utilization.  [missing | e=1 r=5 | quote: unverified]
- Per-day sustained operational cost for a single decentralized C2 node at Ft. Harrison or Cheyenne — needed to test 72-hour cache adequacy.  [missing | e=1 r=4 | quote: unverified]
- Required duration of N95 protection for Zone One evacuees entering staging centers — estimate based on public health modeling for respiratory contamination risk.  [missing | e=1 r=4 | quote: unverified]
- Target metric for public compliance with evacuation orders in Zone One based on non-specific messaging — required to validate 95% goal.  [missing | e=1 r=4 | quote: unverified]
- The total expected operational duration for post-eruption infrastructure stabilization and recovery planning — impacts long-term budget assumptions.  [missing | e=1 r=3 | quote: unverified]
