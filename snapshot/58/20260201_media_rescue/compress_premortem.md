# Premortem

This premortem details nine critical failure assumptions built into the project's hardware resilience, AI workflow balancing, and external partnership dependencies, each tied to specific numeric tripwires that, if tripped, initiate a documented response playbook to prevent catastrophic delays or budget overruns.

## Numeric values
- Equipment Uptime target greater than 90% — gates operational readiness metric  [explicit | e=5 r=5 | quote: verified]
- Engineering staff commitment to in-residence training of 80% for the first five years — driver for capacity throttle  [explicit | e=5 r=5 | quote: verified]
- Human review load threshold maximum of 20% — gates scalability throughput  [explicit | e=5 r=5 | quote: verified]
- Mandatory human review watermark override of 15% — compliance safety buffer input  [explicit | e=5 r=5 | quote: verified]
- Number of reviewers per MIU estimated between 12 and 15 — input for bottleneck capacity  [explicit | e=5 r=4 | quote: verified]
- Vintage knowledge base completion target by year 10 — gates long-term resilience  [explicit | e=5 r=4 | quote: verified]

## Load-bearing assumptions
- The success of the Vintage Pipeline is measured by Equipment Uptime greater than 90%.  [explicit | e=5 r=5 | quote: verified]
- The AI system must maintain a zero legal incidents metric across all operations.  [explicit | e=5 r=5 | quote: verified]
- The MIU crew size can be reliably reduced from four to two personnel with archive support.  [explicit | e=5 r=5 | quote: verified]
- The project's foundational premise relies on the sustainability of obsolete hardware.  [explicit | e=5 r=5 | quote: verified]
- Success rate for media stabilization by partner archives must meet the 85% success rate threshold for augmentation fee avoidance.  [explicit | e=5 r=4 | quote: verified]
- The AI pre-screening automatic rejection rate must aim for 90% to maximize throughput.  [explicit | e=5 r=4 | quote: verified]

## Risks and shocks
- Failure of cannibalization program to yield parts before knowledge transfer stabilizes causes 3-6 months downtime per grounded unit  [stress_test | e=5 r=5 | quote: verified]
- Slow knowledge transfer causes maintenance MTTR increase by 50-100% on complex units  [stress_test | e=5 r=5 | quote: verified]
- Strained review load due to low AI sensitivity requires 100% staff increase causing 6-12 month delays  [stress_test | e=5 r=5 | quote: verified]
- Annual operating cost per MIU underestimates by 20% OPEX increase consuming $6M-$9M of future budget  [stress_test | e=5 r=4 | quote: verified]
- Retrofit cost increases $450k - $1M per unit if vintage units lack compatible power/dimensions  [stress_test | e=5 r=4 | quote: verified]
- Idle MIU costs $150k-$250k per month due to gridlock on next site access  [stress_test | e=5 r=4 | quote: verified]

## Missing data to estimate
- Effective duration in months for the initial 18-month modular replacement R&D timeline — input for Phase 2 transition trigger  [missing | e=5 r=5 | quote: verified]
- Annual minimum revenue target in USD required to cover the high annual operating costs per unit — input for Revenue Model Structure viability  [missing | e=4 r=5 | quote: verified]
- Total project budget duration in years needed to monetize the $250M funding commitment — estimate based on 10-year plan horizon  [missing | e=1 r=5 | quote: unverified]
- Target cost per digitized item in USD needed to validate the $50-100 cost-effectiveness claim — input for ROI calculation  [missing | e=1 r=5 | quote: unverified]
- Required on-board MIU crew size in personnel count necessary to justify the reduced 2-person maintenance staffing level — input for OpEx calculation  [missing | e=1 r=5 | quote: unverified]
- The cost of exceeding the expected 20% human review load as a percentage of total project budget — input for stress testing review bottlenecks  [missing | e=1 r=4 | quote: unverified]
