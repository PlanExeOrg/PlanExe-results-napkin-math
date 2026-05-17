# Premortem

This section defines nine critical decisions, each with numeric tripwires (like uptime percentages, review thresholds, unit counts, and potential cost overruns) that act as failure gates, explicitly linking strategic choices to quantified risks for Monte Carlo input simulation.

## Numeric values
- Equipment Uptime target greater than 90% — gates operational resilience KPI.  [explicit | e=5 r=5 | quote: verified]
- Mandatory human review watermark override of 15% on all AI flags — sets minimum safety buffer load.  [explicit | e=5 r=5 | quote: verified]
- Engineering staff commitment of 80% exclusively to in-residence training for the first five years — capacity throttle on deployment velocity.  [explicit | e=4 r=5 | quote: verified]
- Human review load threshold below 20% — capacity ceiling for compliance workflow.  [explicit | e=4 r=5 | quote: verified]
- Data escrow mandate: 75% of recovered data must reside on project-owned servers until the 10-year mark — compliance duration dependency.  [explicit | e=4 r=4 | quote: verified]
- Knowledge base completion target by year 10 — sets R&D project completion date.  [explicit | e=4 r=4 | quote: verified]

## Load-bearing assumptions
- Modular replacement MTBF must exceed original part MTBF by 30% within 18 months.  [inferred | e=5 r=5 | quote: verified]
- On-site maintenance engineers will achieve Level 1 Certification competence within six months of deployment commencement.  [inferred | e=4 r=5 | quote: verified]
- Archive partners will accept contractual liability for pre-treatment failures causing downtime exceeding 48 hours.  [inferred | e=4 r=5 | quote: verified]
- The combined weight/power of storage and hybrid power systems fits fixed container dimensions without structural redesign.  [inferred | e=4 r=5 | quote: verified]
- The 15% human review override applied to the expected AI flag rate keeps total review load below 17.5%.  [inferred | e=4 r=5 | quote: unverified]
- Sourcing 150 operational vintage units through auctions is feasible within the allocated $6M budget.  [inferred | e=4 r=5 | quote: unverified]

## Gates and thresholds
- If Equipment Uptime falls below 90%, then the project fails its primary operational metric.  [explicit | e=5 r=5 | quote: verified]
- If the human review load exceeds 20%, then throughput gains are nullified and reviewer burnout risks rise.  [explicit | e=4 r=5 | quote: verified]
- If the 'vintage knowledge base' is not completed by year 10, then expertise continuity assurance fails.  [explicit | e=4 r=4 | quote: verified]
- If archive pre-treatment reliability falls below 85% success rate, then partner archives must pay an augmentation fee.  [explicit | e=4 r=4 | quote: verified]
- If archive partners refuse the liability clause, then the reduced on-board crew size assumption is invalidated.  [inferred | e=3 r=5 | quote: verified]
- If AI sensitivity results in a human review load exceeding 17.5% safety buffer, then surge staffing is required.  [inferred | e=4 r=5 | quote: unverified]

## Risks and shocks
- Knowledge transfer failure increases Mean Time To Recovery by 50-100% on complex units.  [stress_test | e=4 r=5 | quote: verified]
- AI threshold strain requires a 100% staff increase for reviewers, causing 6-12 month delays across fleet scale-up.  [stress_test | e=4 r=5 | quote: verified]
- Annual operating cost per MIU exceeding $2-3M by a 20% OPEX increase consumes $6M-$9M of Phase 3 budget.  [stress_test | e=4 r=5 | quote: verified]
- Retrofitting incompatible power/dimensions for 40-foot container increases unit cost by $450k-1M (15-25% above baseline).  [stress_test | e=4 r=4 | quote: verified]
- Idle MIU costs $150k-$250k per month in unrecoverable standby costs if next site is inaccessible.  [stress_test | e=4 r=4 | quote: verified]
- Failure of cannibalization to yield parts results in 3-6 months downtime per MIU and $500k-1M cost overrun annually.  [stress_test | e=5 r=5 | quote: unverified]

## Missing data to estimate
- Target fleet size ceiling: 30 units — how many units are planned for full deployment by target?  [missing | e=1 r=5 | quote: unverified]
- Cost ceiling for forced long-term data migration at Year 10 in USD — bounds future liability shock analysis.  [missing | e=1 r=5 | quote: unverified]
- R&D cost budget cap for modular replacement assembly development in USD — defines Phase 1 engineering expenditure ceiling.  [missing | e=1 r=5 | quote: unverified]
- Target total recovered data volume in exabytes — required quantity to calculate true project ROI.  [missing | e=1 r=5 | quote: unverified]
- Annual fixed OpEx: USD per active MIU for core staffing outside of Flying QC/surge support — required for burn rate model.  [missing | e=1 r=5 | quote: unverified]
- Required data center throughput capacity in petabytes per year for escrow migration — needed for Data Destination Strategy simulation.  [missing | e=1 r=4 | quote: unverified]
