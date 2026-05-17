# Premortem

This section identifies fourteen critical project decisions, their corresponding trade-offs, and potential resource impacts, serving as the core parameter space for scenario analysis regarding technical pacing, financial risk allocation, and commercial friction points. It explicitly defines several high-stakes assumptions that, if invalidated, lead directly to documented failure modes with defined consequences, such as the achievable T+5 technical latency benchmark or the legal viability of the chosen liability model.

## Load-bearing assumptions
- The strict tiered liability model will be legally sound and defensible against operator challenge.  [inferred | e=4 r=5 | quote: verified]
- National operators will provide auditable records for IT operational costs to verify the royalty cap.  [inferred | e=3 r=5 | quote: verified]
- Total capacity building allocation for IT grants and testing support will be €900M, sixty percent of the total budget.  [explicit | e=3 r=4 | quote: verified]
- The T+5 minute real-time latency benchmark will be achievable for 95% of endpoints.  [inferred | e=4 r=5 | quote: unverified]
- The Binding Standard Adoption Timeline will achieve provisional status within six months.  [explicit | e=3 r=4 | quote: verified]
- The current strict enforcement posture will be successfully applied against major operators without political intervention.  [inferred | e=3 r=4 | quote: verified]

## Gates and thresholds
- If cross-border through-ticket adoption falls below 40%, then the five-year target is missed.  [explicit | e=4 r=5 | quote: verified]
- If OSDM core standards binding status is not achieved by eighteen months, then technical development stalls.  [explicit | e=4 r=5 | quote: verified]
- If distributor complaints are not reduced by 50%, then the relevance metric is not met by 2029-05-14.  [explicit | e=4 r=4 | quote: verified]
- If API exposure completion falls below 100% across priority corridors, then the KPI is missed by 2028-05-14.  [explicit | e=4 r=4 | quote: verified]
- If PRM data schema conformance testing is not completed by 2028-12-31, then the accessibility integration goal is missed.  [explicit | e=4 r=4 | quote: verified]
- If the liquidity buffer falls below 150% of peak daily obligation, then the Emergency Float Reserve is triggered.  [explicit | e=3 r=5 | quote: verified]

## Risks and shocks
- Inability to enforce 'Three Strikes' policy against major operators without Council approval leads to political friction.  [stress_test | e=4 r=5 | quote: verified]
- Unstable OSDM real-time data layer causes operator compliance delays of 2–3 months on initial four corridors.  [stress_test | e=3 r=5 | quote: verified]
- Transactional fee model under-capitalization causes settlement delays, requiring EU budget support of €50–€200 million in working capital.  [stress_test | e=4 r=5 | quote: unverified]
- Distributor failure to adopt new system results in only twenty percent adoption, diminishing ROI justification.  [stress_test | e=3 r=4 | quote: verified]
- Operator lobbying weakens the tiered liability framework, pushing liability to distributors/passengers and threatening adoption targets.  [stress_test | e=3 r=4 | quote: verified]
- Overly ambitious non-core mode integration diverts resources, delaying core rail API stabilization by nine to twelve months.  [stress_test | e=3 r=3 | quote: verified]

## Missing data to estimate
- Total baseline cross-border rail ticket revenue per fiscal year needed to project the 40% adoption target — estimate based on current market segmentation.  [missing | e=1 r=5 | quote: unverified]
- Average transaction value for calculating clearing mechanism velocity — estimate based on historical Euro-denominated rail sales data.  [missing | e=1 r=5 | quote: unverified]
- Average monthly operating cost for the Public Reference Distributor to establish fixed budget needs — estimate based on comparative EU agency overhead.  [missing | e=1 r=4 | quote: unverified]
- Cost of delay per week for core API exposure delay impacting distributor adoption — estimate based on distributor lost sales opportunity cost.  [missing | e=1 r=4 | quote: unverified]
- The implied percentage of IT operational expenditure that national operators will attempt to inflate during cost auditing — estimate based on FinTech audit precedents.  [missing | e=1 r=4 | quote: unverified]
- The percentage of required OSDM IT CAPEX covered by the capacity building grants — estimate based on operator IT modernization planning.  [missing | e=1 r=4 | quote: unverified]
