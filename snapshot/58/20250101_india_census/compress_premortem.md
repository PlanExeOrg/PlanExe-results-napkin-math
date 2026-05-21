# Premortem

This section quantifies specific failure modes by identifying the exact assumptions, or tripwires, that, if breached, trigger predefined, numerically impacted response playbooks including resource reallocation, timeline adjustments, or specific financial drawdown limits; failure responses are tied directly to metrics like time to system restoration, cost overrun percentages, and target coverage rates.

## Numeric values
- target coverage rate of 99%+ — input to coverage model  [explicit | e=5 r=5 | quote: verified]
- device failure rate of 10% causing cost overrun of ₹400–600 crore — maximum financial impact of supply chain failure  [stress_test | e=4 r=5 | quote: verified]
- isolated 10% of enumeration blocks requiring satellite hubs — scale factor for high-cost redundancy  [explicit | e=4 r=5 | quote: verified]
- 50% of enumerator payment contingent upon validation acceptance — multiplier for quality-dependent HR cost  [explicit | e=4 r=5 | quote: verified]
- secondary paper audit within 72 hours trigger — gate for coverage remediation  [explicit | e=4 r=4 | quote: verified]
- field supervisors dedicate 15% of required weekly check-ins — minimum effort allocation for nomadic enumeration  [explicit | e=4 r=4 | quote: verified]

## Load-bearing assumptions
- Digital submission failure must automatically trigger an independent paper audit within 72 hours to secure coverage.  [explicit | e=5 r=5 | quote: verified]
- Phase 2 data collection must include provisional, anonymized self-declared caste categories for public review.  [explicit | e=4 r=5 | quote: verified]
- Election Commission must be satisfied with the fast track release of Phase 1 population data before caste data is finalized.  [explicit | e=4 r=5 | quote: verified]
- Fifty percent of enumerator payment is contingent on data blocks passing validation within seven days.  [explicit | e=4 r=5 | quote: verified]
- Field supervisors must dedicate fifteen percent of weekly check-ins to documenting temporary housing sites for migrants.  [explicit | e=4 r=4 | quote: verified]
- The final caste methodology, including linkage rules, must be locked down by Q4 2025 before mass training.  [inferred | e=3 r=5 | quote: verified]

## Gates and thresholds
- If Enumeration Coverage drops below 99% target, then the data reliability gap may exacerbate political friction.  [inferred | e=4 r=4 | quote: verified]
- If Phase 2 caste data collection is selected, then a three-month public review period must precede final linkage.  [explicit | e=4 r=4 | quote: verified]
- If enumerator pay is performance structured, then fifty percent of payment hinges on successful validation acceptance.  [explicit | e=4 r=4 | quote: verified]
- If caste data release is delayed past delimitation stabilization, then accusations of manipulation are guaranteed.  [inferred | e=4 r=4 | quote: verified]
- If digital submission failure occurs, then an independent paper audit must be triggered immediately by local revenue staff.  [explicit | e=4 r=4 | quote: verified]
- If population totals are released first, then delimitation boundaries use only the initial housing frame documentation.  [explicit | e=4 r=4 | quote: verified]

## Risks and shocks
- Failure of satellite hubs causes enumeration coverage to drop 2-5%, risking Phase 1 slip of 4-6 weeks due to attrition.  [stress_test | e=4 r=5 | quote: verified]
- Administrative delays in key states cause Phase 2 aggregation delay of 2 to 3 months if Judicial Review Board arbitration fails on provisional totals.  [stress_test | e=4 r=5 | quote: verified]
- Fabrication due to contingent pay pressure causes salary payouts to delay 1-2 months for over 100,000 personnel.  [stress_test | e=4 r=4 | quote: verified]
- Monsoon disruption grounds enumerators for 3-5 weeks in affected states, threatening continuity and slipping timeline by 4-8 weeks.  [stress_test | e=4 r=4 | quote: verified]
- Loss of 10% devices requires emergency procurement costing ₹400–600 crore, causing localized halts.  [stress_test | e=4 r=4 | quote: verified]
- Undercounting of fluid populations leads to 5-10% undercount of vulnerable groups, causing resource allocation errors.  [stress_test | e=4 r=4 | quote: verified]

## Missing data to estimate
- Total budget duration in months for the main census execution period — estimate based on Phase 1/2 dates.  [missing | e=1 r=5 | quote: unverified]
- Absolute period revenue target to apply the 50% contingent pay multiplier against — estimate based on project financial planning cycles.  [missing | e=1 r=4 | quote: unverified]
- Absolute cost of the total project excluding the 5% contingency fund — needed to calculate the contingency percentage impact.  [missing | e=1 r=4 | quote: unverified]
- Maximum acceptable enumerated error rate (%) across all data collection phases — defines the threshold for dataset rejection.  [missing | e=1 r=4 | quote: unverified]
- Cost per unit for the secondary paper audit materials and logistics per block — needed to calculate total paper audit burden.  [missing | e=1 r=4 | quote: unverified]
- Total number of enumeration blocks requiring the satellite hub contingency — needed to scale the satellite OpEx.  [missing | e=1 r=3 | quote: unverified]
