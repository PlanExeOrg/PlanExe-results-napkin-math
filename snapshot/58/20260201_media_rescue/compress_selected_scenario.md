# Selected Scenario

This section locks in the 'The Builder: Pragmatic Hardware Autonomy & Balanced Review' scenario as the operational baseline, directly selecting the specific mitigation choices made for hardware lifecycle maintenance, data archival security, workload distribution at partner sites, and AI validation sensitivity, thereby defining the parameters for subsequent financial and operational calculations.

## Numeric values
- Total project budget over 10 years: $250 million — absolute funding commitment.  [explicit | e=5 r=5 | quote: verified]
- Annual operating cost per mobile ingest unit range: $2-3 million/year — primary operational burn input scaling with fleet size.  [explicit | e=5 r=5 | quote: verified]
- Phase 1 budget commitment: $60 million — stage funding input.  [explicit | e=5 r=4 | quote: verified]
- Phase 2 budget commitment: $120 million — stage funding input.  [explicit | e=5 r=4 | quote: verified]
- Phase 3 budget commitment: $70 million — stage funding input.  [explicit | e=5 r=4 | quote: verified]
- Per mobile ingest unit cost range: $3-4 million — capital expenditure input per unit structure.  [explicit | e=5 r=4 | quote: verified]

## Gates and thresholds
- If successful digitization rate is less than 95%, then Phase 1 success is not met.  [explicit | e=5 r=5 | quote: verified]
- If signal reconstruction accuracy is less than 80%, then Phase 1 success is not met.  [explicit | e=5 r=5 | quote: verified]
- If automated metadata accuracy is less than 70%, then Phase 1 success is not met.  [explicit | e=5 r=5 | quote: verified]
- If content requiring human review exceeds 20%, then Phase 1 success and review bottleneck goal is failed.  [explicit | e=5 r=5 | quote: verified]
- If legal or privacy incidents occur, then legal goal is failed (Zero legal/privacy incidents).  [explicit | e=5 r=5 | quote: verified]
- If equipment uptime is less than 90%, then maintenance program success is not validated.  [explicit | e=5 r=4 | quote: verified]

## Risks and shocks
- Degradation of physical media before digitization window closes: permanent loss within 10-30 years.  [stress_test | e=5 r=5 | quote: verified]
- Failure of AI pre-screening to reduce human review load by 80% causes bottleneck overload.  [stress_test | e=4 r=4 | quote: verified]
- Failure to secure parts via cannibalization leads to equipment failure and lost uptime >10%.  [stress_test | e=4 r=4 | quote: verified]
- Catastrophic media damage during shipping (vibration, thermal shock) resulting in loss (mitigated by plan, but a baseline risk).  [stress_test | e=3 r=4 | quote: verified]
- Knowledge loss risk: failure to build the vintage knowledge base leads to operational failure.  [stress_test | e=3 r=4 | quote: verified]

## Missing data to estimate
- Total duration in years for Phase 1 deployment — needed to correctly apply phase funding and staff ramp-up models.  [missing | e=5 r=4 | quote: verified]
- Average operational duration for each site deployment in months — needed to calculate total fleet utilization time.  [missing | e=4 r=4 | quote: verified]
- Number of unique archive locations to be serviced across Phases 1, 2, and 3 — needed to scale deployment duration and staffing.  [missing | e=1 r=4 | quote: unverified]
- Total annual revenue target from cost-sharing partners over 10 years — needed to calculate partner revenue share percentage.  [missing | e=1 r=4 | quote: unverified]
- Annual cost escalation factor for operating cost range ($2-3M per MIU annually) — needed for future year OPEX projection.  [missing | e=1 r=3 | quote: unverified]
- Rate of knowledge loss (retirements per year) requiring immediate training coverage — needed to drive training investment sizing.  [missing | e=1 r=4 | quote: unverified]
