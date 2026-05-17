# Review Plan

This section establishes multiple quantifiable, mutually exclusive trade-offs between evacuation speed and logistical readiness, providing the core success metrics (T+6 clearance, T+16 supply staging) against which scenario viability must be tested. It also defines crucial, high-stakes decision thresholds, particularly the sensitive VEI-7 escalation trigger and the quantified impact of resolving or ignoring jurisdictional friction on engineering timelines.

## Numeric values
- VEI-7 trigger uplift rate exceeding 5cm per hour over three consecutive hours — gates Scenario Beta activation.  [explicit | e=5 r=5 | quote: verified]
- Logistical ingress gap mitigation aim is staging 30% required N95/water supplies by T+16 hours — key performance indicator for mitigation success.  [derived | e=4 r=5 | quote: verified]
- Zero inbound logistical clearance for first 18 hours post-T+6 commitment — constraint on resource model.  [explicit | e=4 r=5 | quote: verified]
- Evacuation compliance goal is 95% Zone One compliance by T+12 hours — input for public response model.  [inferred | e=4 r=4 | quote: verified]
- Zone Zero clearance target time is T+6 hours — gates launch readiness.  [explicit | e=5 r=5 | quote: unverified]
- Critical window sacrifices logistical ingress capacity for first 18 hours — defines resource starvation period.  [inferred | e=3 r=4 | quote: verified]

## Load-bearing assumptions
- Zone Zero clearance is strictly targeted for T+6 hours due to mandatory contraflow implementation.  [explicit | e=5 r=5 | quote: verified]
- Stafford Act declaration is assumed, authorizing immediate mobilization of $500 million in Disaster Relief Funds.  [inferred | e=5 r=5 | quote: verified]
- Aviation exemption allows ten heavy-lift helicopter sorties for critical ingress between T+4 and T+8.  [inferred | e=4 r=4 | quote: verified]
- Two heavy wreckers and two breach vehicles are staged internally for rapid distress response.  [inferred | e=4 r=4 | quote: verified]
- USGS scientific monitoring stations have 48-hour self-sufficient backup power via UPS or solar.  [inferred | e=4 r=3 | quote: verified]
- National Guard engineering assets are ready to mobilize heavy equipment by T+3 hours.  [inferred | e=4 r=4 | quote: unverified]

## Gates and thresholds
- If ash uplift rate sustains over 5cm per hour for three consecutive hours, then Scenario Beta is triggered.  [explicit | e=5 r=5 | quote: verified]
- If Zone Zero vehicle exit compliance falls below 98%, then the VEI-7 contingency is immediately activated.  [inferred | e=4 r=5 | quote: verified]
- If a major contraflow blockage occurs, then breach assets must clear the blockage within 15 minutes.  [inferred | e=4 r=5 | quote: verified]
- If ashfall hardening is delayed 4-12 hours due to friction, then grid collapse likelihood increases by 25-50%.  [stress_test | e=4 r=4 | quote: verified]
- If C2 decision latency increases beyond 90 minutes, then Command Structure failure occurs.  [inferred | e=3 r=4 | quote: verified]
- If public panic causes compliance below 70%, then evacuation timeline loss is 8-10 hours.  [stress_test | e=4 r=3 | quote: verified]

## Risks and shocks
- Failure of mandatory contraflow on US-191/US-20 causes Zone Zero clearance failure by T+6, resulting in thousands of casualties.  [stress_test | e=5 r=5 | quote: verified]
- Premature VEI-7 trigger depletes resources needed for VEI-6 response, increasing mortality estimates by 20%.  [stress_test | e=5 r=4 | quote: verified]
- The Pioneer strategy's zero ingress constraint causes life support failure in Zone One, costing $500,000+ extra mobilization cost.  [stress_test | e=5 r=4 | quote: verified]
- C2 distributed node power failure causes decision latency increase of 30-60 minutes, delaying critical orders.  [stress_test | e=4 r=4 | quote: verified]
- Poor messaging transparency causes public non-compliance below 70%, leading to I-90 congestion and 8-10 hours lost time.  [stress_test | e=4 r=3 | quote: verified]
- Ashfall contamination of water sources strains regional hospitals, causing 15% critical care surge for non-respiratory cases.  [stress_test | e=4 r=3 | quote: verified]

## Missing data to estimate
- Target compliance rate needed to reduce public panic risk (percent) — estimate based on modeling of Decision 8 messaging scenarios.  [missing | e=4 r=4 | quote: verified]
- Per-head monthly cost for embedded full-time employee staff at decentralized Command Nodes (USD/FTE/month) — estimate based on comparable FEMA Region VIII pay grades.  [missing | e=4 r=4 | quote: verified]
- Maximum acceptable cost for temporary construction contracts to secure C2 backup fuel caches (USD) — estimate based on prevailing local contractor rates.  [missing | e=4 r=3 | quote: verified]
- Required volume of JP-8/Diesel fuel for 72-hour sustainment per Command Node (Liters) — estimate based on C2 Systems Architect power consumption reports.  [missing | e=4 r=5 | quote: unverified]
- Days of post-eruption operational capacity sustained by N95 storage caches (Days) — required to validate hospital surge assumptions.  [missing | e=3 r=3 | quote: verified]
- Required operational cost for the 'Operational Status Dashboard' Killer Application (USD) — estimate via detailed software contracting quotes.  [missing | e=4 r=4 | quote: unverified]
