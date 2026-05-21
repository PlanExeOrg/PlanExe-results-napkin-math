# Selected Scenario

This chosen scenario, 'The Builder: Pragmatic Integration and Internalization,' commits to a specific complex flow automation project occurring in a 15,000 sq ft building, utilizing roughly 4,000 sq ft for the pilot line, with a hard constraint of $\le 2$ hr/week manual exception work, and a total budget envelope between $300,000 and $500,000. It dictates specific strategies regarding equipment commissioning, software expertise distribution, protocol selection (OPC UA), budget allocation for consultants, and the decision to develop a custom interface board rather than replacing existing proprietary PLCs. The viability gates are implicit in the successful completion of the six defined sequential phases leading to a fully autonomous end-to-end demo triggered by a single REST API call.

## Numeric values
- Total budget range lower bound: $300,000 — input to CAPEX model.  [explicit | e=5 r=5 | quote: verified]
- Total budget range upper bound: $500,000 — input to CAPEX model.  [explicit | e=5 r=5 | quote: verified]
- Wire bending machine budget range lower bound: $20,000 — CAPEX component.  [explicit | e=5 r=4 | quote: verified]
- Wire bending machine budget range upper bound: $40,000 — CAPEX component.  [explicit | e=5 r=4 | quote: verified]
- Paperclip packing machine budget range lower bound: $10,000 — CAPEX component.  [explicit | e=5 r=4 | quote: verified]
- Area reserved for pilot line: 2,000 sq ft — dimension for capacity planning.  [explicit | e=5 r=4 | quote: verified]

## Load-bearing assumptions
- The pilot system must achieve zero human intervention for standard orders.  [explicit | e=5 r=5 | quote: verified]
- The chosen scenario requires using OPC UA middleware for standardized protocol abstraction.  [explicit | e=5 r=5 | quote: verified]
- The project will replace the used machine's proprietary controller with an open industrial PC.  [explicit | e=5 r=5 | quote: verified]
- The new packing machine must automatically count exactly 100 paperclips per unit packaged.  [explicit | e=5 r=4 | quote: verified]
- Permits for building, electrical, and OSHA must be obtained before Phase 2 work begins.  [explicit | e=5 r=4 | quote: verified]
- The primary goal is a working, demonstrable autonomous flow, not revenue targeting.  [inferred | e=4 r=5 | quote: verified]

## Gates and thresholds
- If the total spending exceeds $500,000, then the project is over budget.  [explicit | e=5 r=5 | quote: verified]
- If manual exception work exceeds 2 hours per week, then the automation goal is breached.  [explicit | e=5 r=5 | quote: verified]
- If the total spending is less than $300,000, then the pilot scope may be overly constrained.  [explicit | e=5 r=4 | quote: verified]
- If API control of forming and packing is not verified by end of Phase 4, then system integration is delayed.  [explicit | e=4 r=5 | quote: verified]
- If the used wire bender commissioning does not stabilize production, then Phase 2 is blocked.  [explicit | e=4 r=5 | quote: verified]
- If the packaging machine counting precision fails, then sealed bags of 100 paperclips are not produced continuously.  [explicit | e=4 r=4 | quote: verified]

## Risks and shocks
- Using non-standard PLC programming increases risk that $\le 2$ hours exception limit is breached during diagnostics.  [inferred | e=5 r=4 | quote: verified]
- Acquiring the cheapest functional used wire bender risks significant custom sensor retrofitting and schedule extension.  [inferred | e=5 r=4 | quote: verified]
- Over-investing in the wire bender reduces funds available for Budget Allocation for Expert Commissioning support.  [inferred | e=5 r=4 | quote: verified]
- Reliance on proprietary Modbus RTU protocols risks complexity when integrating with custom software backend.  [inferred | e=4 r=4 | quote: verified]
- Forcing low-level I/O integration conflicts with Control System Protocol Selection, risking friction with custom backend.  [inferred | e=5 r=3 | quote: verified]

## Missing data to estimate
- Cost per hour for the temporary, on-site PLC/controls expert support — estimate consultant billing rate.  [missing | e=5 r=4 | quote: verified]
- Target paperclip production throughput per week — estimate based on max machinery speed.  [missing | e=5 r=4 | quote: verified]
- Required uptime percentage for the pilot line — estimate based on acceptable manual override fraction.  [missing | e=5 r=4 | quote: verified]
- Quality metrics threshold for paperclip production acceptance — estimate based on industry standard failure rate.  [missing | e=5 r=4 | quote: verified]
- Cost per hour for external consultants writing initial control code — estimate specialized integration services rate.  [missing | e=5 r=4 | quote: verified]
- Duration in weeks that the $300,000-$500,000 budget must cover — estimate based on project schedule phases.  [missing | e=5 r=5 | quote: unverified]
