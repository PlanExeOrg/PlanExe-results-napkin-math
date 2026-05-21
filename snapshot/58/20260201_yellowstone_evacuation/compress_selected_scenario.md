# Selected Scenario

This section fixes the chosen baseline plan ('The Pioneer: Maximum Throughput First') by selecting specific resource allocation levers, thereby determining the modeled parameters for immediate evacuation throughput prioritization, the timing of jurisdictional handoffs, the front-loaded effort for infrastructure hardening versus security, and the trigger sensitivity for escalating to the catastrophic VEI-7 contingency.

## Numeric values
- Evacuate tourists target: 35,000 people — input to evacuation volume model.  [explicit | e=5 r=5 | quote: verified]
- Evacuate staff target: 800 people — input to evacuation volume model.  [explicit | e=5 r=5 | quote: verified]
- Probability of VEI-6 or higher eruption: 40% — input to success probability distribution.  [explicit | e=5 r=5 | quote: verified]
- Evacuation window for Zone Zero: 6 Hours — duration constraint for Phase 1 evacuation.  [explicit | e=5 r=5 | quote: verified]
- Vulnerability zone radius for evacuation Zone One: 100km radius — parameter for hazard footprint.  [explicit | e=5 r=5 | quote: verified]
- Eruption severity modeled: VEI-6 or higher — primary scenario intensity.  [explicit | e=5 r=5 | quote: verified]

## Load-bearing assumptions
- Full contraflow on US-191/US-20 blocks all inbound logistics for 18 hours post-T+0.  [explicit | e=5 r=5 | quote: verified]
- The primary evacuation strategy must be maximum throughput via contraflow on US-191 for Zone Zero egress.  [explicit | e=5 r=5 | quote: verified]
- Unified Command must maintain authority over evacuees until they check in at designated intake centers.  [explicit | e=5 r=4 | quote: verified]
- The contingency trigger for VEI-7 escalation is sustained uplift exceeding 5cm per hour over three hours.  [explicit | e=4 r=4 | quote: verified]
- Respiratory protection for 100,000 people as N95 minimum must be pre-staged for Zone One.  [explicit | e=4 r=4 | quote: verified]
- Bottled water convoys from Salt Lake City will arrive within 12 hours to meet demand.  [explicit | e=4 r=4 | quote: verified]

## Gates and thresholds
- If uplift rate exceeds 5cm per hour for three consecutive hours, then trigger VEI-7 expansion (Scenario Beta).  [explicit | e=4 r=5 | quote: verified]
- If US-89/191/287 remains blocked by landslide, then traffic must route solely North and West.  [explicit | e=4 r=5 | quote: verified]
- If evacuation is not complete by T+6 Hours, then Phase 2 external evacuation scope is compromised.  [explicit | e=3 r=5 | quote: verified]
- If commercial and private aviation remains operational past T+0, then the risk of silicate ash ingestion is too high.  [explicit | e=4 r=4 | quote: verified]
- If VCM reading exceeds its pre-determined threshold, then the VEI-7 contingency is not initiated.  [explicit | e=4 r=4 | quote: verified]

## Risks and shocks
- VEI-6/7 eruption risk: 40% probability in the next 72 hours triggers main plan.  [explicit | e=5 r=5 | quote: verified]
- VEI-7 Supereruption risk: Requires immediate expansion of evacuation zone to 500km radius.  [stress_test | e=4 r=5 | quote: verified]
- Logistical ingress failure risk: Full contraflow blocks inbound logistics for 18 hours post-T+0.  [stress_test | e=4 r=5 | quote: verified]
- Phreatic explosion risk: Compromised section of the Grand Loop Road occurred before T+0 planning began.  [explicit | e=5 r=4 | quote: verified]
- Unprecedented ground uplift risk: Uplift exceeding 20cm in 6 hours indicates impending major event.  [explicit | e=4 r=4 | quote: verified]
- Seismic swarm risk: Unprecedented activity (Mag 4.5+) indicates magma ascension to shallow depths.  [explicit | e=4 r=4 | quote: verified]

## Missing data to estimate
- Duration of inbound logistics blockage in hours by T+18 — determined by time required for evacuation wave to clear contraflow US-191.  [missing | e=1 r=5 | quote: unverified]
- Total population within 500km buffer zone count — needed to scale evacuation volume if VEI-7 is triggered.  [missing | e=1 r=4 | quote: unverified]
- Average per-person lodging/care cost per day $ — input for mass casualty intake center models.  [missing | e=1 r=4 | quote: unverified]
- Average monthly or annual cost per deployed National Guard or State Patrol unit $ — needed for security mobilization burn.  [missing | e=1 r=4 | quote: unverified]
- Cost per unit of bottled water mobilized from Salt Lake City $ — needed to total logistics water cost.  [missing | e=1 r=3 | quote: unverified]
- Total available regional generator fuel supply in gallons/liters — needed for grid failure prioritization burn model.  [missing | e=1 r=3 | quote: unverified]
