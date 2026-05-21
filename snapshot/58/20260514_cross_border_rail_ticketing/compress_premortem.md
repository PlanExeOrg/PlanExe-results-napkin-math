# Premortem

This section details the specific quantitative tripwires and financial consequences associated with the failure of critical underlying assumptions regarding operator compliance with liability frameworks, technical latency mandates, and commercial data access auditability, serving as direct input gates for Monte Carlo simulation regarding project timeline and budget overruns.

## Numeric values
- Initial clearing mechanism float: €200 million — input for liquidity stress testing  [explicit | e=5 r=5 | quote: verified]
- Emergency Float Reserve for clearing mechanism: 20% of the €1.5B budget — contingency funding buffer  [derived | e=4 r=5 | quote: verified]
- Commission coordination budget for clearing float capitalization: €1.5 billion — input for initial financial state model  [explicit | e=4 r=5 | quote: verified]
- Settlement reconciliation duration target: T+3 — gates cash flow model input for liquidity lag  [explicit | e=5 r=4 | quote: verified]
- Mandatory real-time latency benchmark: T+5 minutes — gates technical readiness milestone  [explicit | e=5 r=4 | quote: verified]
- Cost recovery royalty rate capped at 5% of attributable IT O&M expenditure — input for distributor cost model scaling  [explicit | e=4 r=4 | quote: verified]

## Load-bearing assumptions
- The builder scenario's pragmatic timeline avoids aggressive adoption timelines for standards.  [explicit | e=5 r=5 | quote: verified]
- Core API exposure deadlines are set such that stability testing completes before final binding rules are established.  [explicit | e=5 r=5 | quote: verified]
- The EU backstop limits compensation to failures between the first and last known connection segments.  [explicit | e=5 r=5 | quote: verified]
- API access fees are strictly cost-recovery for national carriers, overseen by regulators.  [explicit | e=5 r=4 | quote: verified]
- Initial distributor API access will be free for two years, burdening the public budget.  [inferred | e=5 r=4 | quote: verified]
- Consumer protection threshold for continuity protection is defined as service cancellation exceeding ninety minutes.  [explicit | e=5 r=4 | quote: verified]

## Gates and thresholds
- If the OSDM data exchange and transaction processing standards do not achieve provisional binding status by six months, then core development speed is jeopardized.  [explicit | e=5 r=5 | quote: verified]
- If the operator's segment caused the failure, then that carrier bears one hundred percent of compensation costs unless distributor negligence is proven.  [explicit | e=5 r=5 | quote: verified]
- If distributor API access is offered free for two years, then the cost is shifted entirely onto the €1.5 billion public budget.  [explicit | e=5 r=4 | quote: verified]
- If core OSDM data exchange and transaction processing standards do not achieve formal binding status by eighteen months, then initial corridor access is delayed.  [derived | e=4 r=5 | quote: verified]
- If the standard adoption is deferred until the full TEN-T network integration phase, then reduction card and accessibility harmonization is delayed.  [explicit | e=5 r=4 | quote: verified]
- If a carrier exceeds the imposed maximum commercial fee threshold for inventory access, then they face temporary barring from the clearing settlement mechanism.  [explicit | e=5 r=4 | quote: verified]

## Risks and shocks
- Political resistance leads to 6–12 month delay on key routes, jeopardizing 40% through-ticket target.  [stress_test | e=4 r=5 | quote: verified]
- Technical integration challenges causing unstable OSDM data layer results in 2–3 month delay in commercial rollout on initial four corridors.  [stress_test | e=4 r=5 | quote: verified]
- Under-capitalization/insufficient liquidity in clearing/settlement causes EU budget gap of €50–€200 million in working capital support.  [stress_test | e=4 r=5 | quote: verified]
- Failure to integrate accessibility or reduction cards limits modal shift gain by 10–15% and causes mandatory compliance failure.  [stress_test | e=4 r=4 | quote: verified]
- Overly complex governance structure leads to security patches or functional improvements taking 6–9 months versus expected rapid response.  [stress_test | e=4 r=4 | quote: verified]
- Lobbying by operators weakens the tiered liability framework, pushing liability to distributor/passenger, threatening 40% adoption target.  [stress_test | e=4 r=4 | quote: verified]

## Missing data to estimate
- Total eligible cross-border journeys per year — required to convert the 40% adoption target into an absolute ticket count.  [missing | e=1 r=5 | quote: unverified]
- Average working cost of a required IT modification per carrier — needed to scope the total usage of the capacity building grants.  [missing | e=1 r=4 | quote: unverified]
- Average revenue per cross-border ticket sold — needed to convert adoption targets into revenue projections.  [missing | e=1 r=4 | quote: unverified]
- Contracted monthly salary cost for the three (3) Interoperability Standards Lead FTE equivalents — needed to calculate internal staffing burn rate.  [missing | e=1 r=3 | quote: unverified]
- Duration in months the transactional fee model will apply for the clearing mechanism capitalization — required to project total fee revenue.  [missing | e=1 r=4 | quote: unverified]
- Annual duration in years the public reference distributor will be funded directly by the EU Program Budget — required for long-term cost projection.  [missing | e=1 r=3 | quote: unverified]
