# Premortem

This premortem section models potential failure pathways for critical decisions regarding evacuation speed, jurisdictional transfer, power hardening, and contingency activation, explicitly linking failure to breach asset readiness, C2 power loss, and jurisdictional disputes over engineering resources.

## Numeric values
- VEI-7 contingency trigger is sustained uplift rate exceeding 5cm per hour over three consecutive hours — trigger for Scenario Beta  [explicit | e=4 r=5 | quote: verified]
- logistical ingress is blocked until T+18 hours — capacity constraint for logistics  [explicit | e=4 r=5 | quote: verified]
- relief assets are blocked for the first 18 hours — duration of logistical gap  [explicit | e=4 r=5 | quote: verified]
- evacuation must clear Zone Zero by T+6 hours — gates launch readiness  [explicit | e=4 r=5 | quote: verified]
- Zone Zero contains 35,000 visitors and 800 essential staff — population size for evacuation scheduling  [explicit | e=4 r=4 | quote: verified]
- Zone One compliance target is 95% departure by T+12 hours — target compliance rate  [explicit | e=3 r=4 | quote: verified]

## Load-bearing assumptions
- Stafford Act declaration is assumed for immediate $500M DRF access.  [inferred | e=5 r=5 | quote: verified]
- Zone Zero clearance must achieve 98% vehicle exit success by T+6 hours.  [explicit | e=4 r=5 | quote: verified]
- National Guard engineers will be ready to mobilize heavy equipment by T+3 hours.  [inferred | e=4 r=4 | quote: verified]
- Limited aviation exemption allows ten heavy-lift helicopter sorties by T+8 hours.  [explicit | e=3 r=5 | quote: verified]
- USGS monitoring stations have 48-hour self-sufficient backup power before needing external cache fuel.  [explicit | e=4 r=4 | quote: verified]
- FEMA Incident Tracking System enables digital custodial transfer at egress points.  [inferred | e=4 r=4 | quote: verified]

## Gates and thresholds
- If uplift rate sustains exceeding 5cm per hour over three consecutive hours, then VEI-7 contingency triggers.  [explicit | e=4 r=5 | quote: verified]
- If evacuation egress time exceeds T+18 hours, then inbound logistics clearance is delayed past that point.  [explicit | e=4 r=5 | quote: verified]
- If the blockage duration on US-191 exceeds 15 minutes, then breach assets must be deployed.  [explicit | e=3 r=5 | quote: verified]
- If aviation visibility drops below 1.2 miles, then the emergency airlift window is grounded.  [stress_test | e=3 r=5 | quote: verified]
- If jurisdictional transfer authority is not signed by T+0, then NG engineering command conflicts arise.  [inferred | e=3 r=5 | quote: verified]
- If Zone Zero exit compliance drops below 95% by T+12 hours, then messaging policy needs revision.  [explicit | e=3 r=4 | quote: verified]

## Risks and shocks
- Premature VEI-7 trigger risks unsustainable resource expenditure due to false positives — drains VEI-6 resources  [stress_test | e=4 r=5 | quote: verified]
- Premature declaration of VEI-7 trigger could cause massive resource expenditure from a false alarm — drains VEI-6 budget  [stress_test | e=4 r=5 | quote: verified]
- Zero inbound logistical clearance for 18 hours risks resource failure once intake begins — impacts Zone One resupply  [stress_test | e=4 r=5 | quote: verified]
- Prioritizing hospital fuel denies supply to communications hubs, blinding the response within hours — command failure risk  [stress_test | e=4 r=5 | quote: verified]
- Fuel influx delay due to contraflow may starve generators at critical C2 nodes — impacts C2 resilience  [stress_test | e=4 r=4 | quote: verified]
- Diverting engineering assets for ash cleaning strands security assets, increasing civil disorder risk T+6 to T+12 — impacts security posture  [stress_test | e=4 r=4 | quote: verified]

## Missing data to estimate
- Target percentage of US-191 contraflow lanes required to be free of vehicles by T+6 hours — compliance target for throughput  [missing | e=1 r=5 | quote: unverified]
- Cost per heavy-lift helicopter sortie for emergency ingress — estimate based on known airlift rates  [missing | e=1 r=5 | quote: unverified]
- Total required N95 unit count for Zone One reception centers — estimate based on full Zone One population modeling  [missing | e=1 r=4 | quote: unverified]
- Lead time needed by State Directors to sign dual-hat MOU in hours — input for scheduling Decision 3 commencement  [missing | e=1 r=4 | quote: unverified]
- Maximum acceptable time delay for jurisdictional authority transfer in hours — estimate based on operational friction tolerance  [missing | e=1 r=4 | quote: unverified]
- Revenue exposure per week due to sustained regional power grid failure — input for stress-test cost modeling  [missing | e=1 r=3 | quote: unverified]
