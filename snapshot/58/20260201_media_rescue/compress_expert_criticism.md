# Expert Criticism

Expert criticism highlights quantitative dependencies and risks related to hardware supply chain volatility, the necessity of performance-based certification for maintenance knowledge transfer, and the operational sensitivity introduced by inadequate control over on-site media pre-treatment and AI review calibration thresholds.

## Numeric values
- Total project budget of $250 million over 10 years — constraint on total investment.  [explicit | e=5 r=5 | quote: verified]
- Human review reduction target of 80% — scaling factor for review bottleneck control.  [explicit | e=5 r=5 | quote: verified]
- Pre-treatment stabilization cycle time of 8 to 24 hours — input for processing time modelling.  [explicit | e=5 r=4 | quote: verified]
- Pilot MIU count of 3 units — readiness gate for Phase 1 completion.  [explicit | e=5 r=4 | quote: verified]
- Minimum annual operating cost per MIU of $2 million/MIU/annually — input to operational cash flow model.  [explicit | e=4 r=5 | quote: verified]
- Cost per digitized item range of $50 to $100/item — input for benefit calculation.  [explicit | e=5 r=4 | quote: verified]

## Load-bearing assumptions
- The maintenance program must sustain equipment uptime greater than 90%.  [explicit | e=5 r=5 | quote: verified]
- The required human review load must be kept below a 20% threshold.  [explicit | e=5 r=5 | quote: verified]
- The project relies on capturing institutional knowledge as the primary driver for 90% uptime.  [explicit | e=5 r=5 | quote: verified]
- The chosen Builder strategy prioritizes modular replacements over deep training knowledge capture.  [explicit | e=5 r=5 | quote: verified]
- The AI pre-screening system achieves at least an 80% reduction in human review load.  [inferred | e=4 r=5 | quote: verified]
- Pilot success for automated metadata accuracy must reach greater than 70%.  [explicit | e=5 r=4 | quote: verified]

## Gates and thresholds
- If content requiring human review exceeds 20%, then the review bottleneck target is failed.  [explicit | e=5 r=5 | quote: verified]
- If equipment uptime falls below 90%, then the maintenance program success metric is failed.  [explicit | e=5 r=5 | quote: verified]
- If the AI pre-screening sensitivity is too high, then the human review load exceeds the planned maximum.  [inferred | e=5 r=5 | quote: verified]
- If successful digitization rate falls below 95%, then Phase 2 funding/scaling is jeopardized.  [explicit | e=5 r=4 | quote: verified]
- If signal reconstruction accuracy falls below 80%, then the data quality goal is missed.  [explicit | e=5 r=4 | quote: verified]
- If automated metadata accuracy falls below 70%, then the AI validation target is missed.  [explicit | e=5 r=4 | quote: verified]

## Risks and shocks
- Cannibalization program fails to yield sufficient parts or knowledge transfer is too slow: prolonged downtimes below 90% uptime.  [stress_test | e=5 r=5 | quote: verified]
- Auction market tightens or desired unit types unavailable: Phase 1 construction stalls, causing budget overruns.  [stress_test | e=5 r=5 | quote: verified]
- Miscalibration of the AI pre-screening threshold leads to legal incidents or review capacity burnout.  [stress_test | e=5 r=5 | quote: verified]
- Failure to secure the initial inventory of 300-500 vintage digitization units needed for parts/operation.  [stress_test | e=5 r=4 | quote: verified]
- Failure to secure written contracts and funding commitment of $60M for Phase 1 drawdown.  [stress_test | e=5 r=4 | quote: verified]
- Archive staff outsourced pre-treatment quality failures cause hardware damage: increased Mean Time To Repair (MTTR).  [stress_test | e=4 r=5 | quote: verified]

## Missing data to estimate
- Total staff cost per MIU per year — needed to apply the $2-3M/MIU annual OpEx figure.  [missing | e=5 r=5 | quote: verified]
- Total number of years the initial $60M Phase 1 budget must sustain operations — needed for burn rate calculation.  [missing | e=5 r=5 | quote: verified]
- Total duration in months for Phase 2 scaling to 15 MIUs — needed to calculate average time-to-scale.  [missing | e=5 r=4 | quote: verified]
- Required engineering staff count for modular replacement R&D effort in Year 1 — needed to define engineering load division.  [missing | e=1 r=4 | quote: unverified]
- The number of high-failure vintage components per MIU line type (Tape, Film, Card) — needed for maintenance scheduling.  [missing | e=1 r=4 | quote: unverified]
- The absolute required revenue generated per year for the chosen Revenue Model Structure — needed to evaluate subscription/fee stability.  [missing | e=1 r=3 | quote: unverified]
