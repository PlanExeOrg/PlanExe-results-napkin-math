# Selected Scenario

This section locks in the 'The Builder: Pragmatic Integration and Internalization' scenario as the baseline plan to model, specifying the location, physical footprint, and ultimate functional goal of achieving zero human intervention for regular orders, constrained by the overall budget allowance.

## Numeric values
- Total project budget range minimum: $300,000 — input to financial model.  [explicit | e=5 r=5 | quote: verified]
- Total project budget range maximum: $500,000 — input to financial model.  [explicit | e=5 r=5 | quote: verified]
- Wire bending machine budget minimum: $20,000 — capital expenditure input.  [explicit | e=5 r=4 | quote: verified]
- Wire bending machine budget maximum: $40,000 — capital expenditure input.  [explicit | e=5 r=4 | quote: verified]
- Paperclip packing machine budget threshold: $10,000 minimum cost — capital expenditure input.  [explicit | e=5 r=4 | quote: verified]
- Paperclip packing machine budget cap: $30,000 maximum cost — capital expenditure input.  [explicit | e=5 r=4 | quote: verified]

## Load-bearing assumptions
- The primary goal is demonstrating a working, demonstrable autonomous flow, not revenue target achievement.  [explicit | e=5 r=5 | quote: verified]
- The chosen strategy relies on using OPC UA for pragmatic, standardized integration.  [explicit | e=5 r=5 | quote: verified]
- The internal software developer will focus on API and order queue management.  [explicit | e=5 r=4 | quote: verified]
- Manual intervention for system exceptions must not exceed two (2) hours per week.  [explicit | e=4 r=4 | quote: verified]
- The used wire bender acquisition assumes an expert tuning service for two (2) weeks.  [explicit | e=4 r=4 | quote: verified]
- The project requires obtaining building, electrical, and OSHA permits prior to Phase 2.  [explicit | e=4 r=4 | quote: verified]

## Gates and thresholds
- If manual work for exceptions exceeds two (2) hours per week, then the autonomy goal is breached.  [explicit | e=4 r=5 | quote: verified]
- If the API call successfully triggers the full flow, then Phase 6 end-to-end demo is complete.  [explicit | e=4 r=4 | quote: verified]
- If API command execution is not verified by the end of Phase 4, then software integration milestone is missed.  [explicit | e=4 r=4 | quote: verified]
- If the packaging machine counting mechanism fails to count exactly 100 paperclips, then Phase 3 commission fails.  [inferred | e=3 r=4 | quote: verified]
- If the used wire bender commission requires more than two (2) weeks of expert tuning, contractors must be retained for troubleshooting.  [inferred | e=3 r=4 | quote: verified]
- If permits are not obtained for building/electrical/OSHA by the start date, then Phase 1 is not complete.  [explicit | e=4 r=3 | quote: verified]

## Risks and shocks
- Failure of UPS/FedEx API integration during Phase 6: inability to generate labels or manifest shipments.  [explicit | e=4 r=4 | quote: verified]
- Failure of the used wire bender's I/O or PLC interface: extended commissioning and program tuning time.  [inferred | e=3 r=5 | quote: verified]
- Failure of the packing machine to count exactly 100 paperclips: unreliable bagging output quality.  [inferred | e=3 r=4 | quote: verified]
- Failure of custom control logic implementation by internal developer: slippage in Phase 4 software milestones.  [inferred | e=3 r=4 | quote: verified]
- Custom sensor retrofitting for the used wire bender: extension of the software development timeline.  [inferred | e=3 r=4 | quote: verified]
- Failure of mechanical integration between former and packer: blockage of the production flow.  [inferred | e=3 r=4 | quote: verified]

## Missing data to estimate
- Paperclip production throughput target clips/hour — required to assess utilization of the pilot line.  [missing | e=1 r=5 | quote: unverified]
- Projected revenue per period $ — required to scale manual exception hours threshold constraint.  [missing | e=1 r=4 | quote: unverified]
- Paperclip quality metric threshold failures/1000 units — required to stress test rework loop impact.  [missing | e=1 r=3 | quote: unverified]
- Uptime requirement percentage % — required to calculate capacity impacts of downtime shocks.  [missing | e=1 r=4 | quote: unverified]
- Expected weekly service cost for consultant support $ per week — required to model variable operational expenditure.  [missing | e=1 r=3 | quote: unverified]
- Paperclip packing machine counting error budget $ for replacement inventory — required to model material waste cost.  [missing | e=1 r=2 | quote: unverified]
