# Review Plan

This section establishes explicit, numerically defined conditional gates and dependencies between critical pathways such as power commitment, tenant revenue achievement, land zoning finalization, and security compliance clearance, all of which function as hard non-linear inputs for schedule and cost simulation models.

## Numeric values
- Phase 2 power commitment trigger before Phase 1 financing: 3 GW — gates construction funding  [explicit | e=5 r=5 | quote: verified]
- Minimum take-or-pay commitment threshold for 1-3 GW expansion: 60% — financial gate for next tranche funding  [explicit | e=5 r=5 | quote: verified]
- Target operational PUE ceiling for Phase 1: 1.20 — engineering performance SLA  [explicit | e=5 r=5 | quote: verified]
- Initial commercial load target before sovereign review sign-off: 500 MW — defines Phase 1 security demarcation  [explicit | e=5 r=4 | quote: verified]
- Total project footprint target: 161 km² — physical constraint for modelling  [explicit | e=5 r=4 | quote: verified]
- Total project capacity goal: 9 GW — primary scale metric  [explicit | e=4 r=5 | quote: verified]

## Load-bearing assumptions
- Phase 1 scope limits must rely only on a non-binding RTE hosting consultation for power certainty.  [explicit | e=5 r=5 | quote: verified]
- The hyper-dense model requires 80% of the total footprint to be designated as permanent ecological buffer.  [explicit | e=5 r=5 | quote: verified]
- Phase 2 expansion FID depends on securing 60% take-or-pay commitments for the next tranche capacity.  [explicit | e=5 r=5 | quote: verified]
- Project viability requires sub-2ms round-trip time latency consistency between distributed campus clusters.  [explicit | e=4 r=4 | quote: verified]
- The initial 500 MW commercial load must employ commercially available hardware until sovereign AI partition protocols are signed.  [explicit | e=4 r=4 | quote: verified]
- Sovereign AI partition alignment must be signed before Phase 1 Power FID to unlock premium revenue streams.  [explicit | e=4 r=4 | quote: verified]

## Gates and thresholds
- If binding transmission allocation for Phase 2 (3 GW) is not secured before Phase 1 construction financing, then Phase 1 construction financing is blocked.  [explicit | e=5 r=5 | quote: verified]
- If take-or-pay commitments for the next tranche do not reach 60%, then Phase 2 expansion funding is blocked.  [explicit | e=5 r=5 | quote: verified]
- If Phase 1 proceeds by limiting scope to 500 MW with only a non-binding RTE consultation response, then transmission upgrade CAPEX is deferred until the 3 GW gate.  [explicit | e=5 r=4 | quote: verified]
- If Phase 1 utilization of 1 GW capacity is not guaranteed by three medium-sized cloud providers, then Phase 2 expansion is blocked.  [explicit | e=4 r=4 | quote: verified]
- If a formal, signed DGSI/ANSSI protocol is not executed, then the first 500 MW load remains restricted to commercial tenants.  [explicit | e=4 r=4 | quote: verified]
- If land assembly forces consolidation of the full 161 km², then schedule delays via local judicial review occur.  [inferred | e=4 r=4 | quote: verified]

## Risks and shocks
- Failure to secure land assembly consent for fragmented development risks 12–24 month delay to Phase 1 FID.  [stress_test | e=5 r=5 | quote: verified]
- Land assembly failure due to judicial challenges could cause €500M–€1B overrun and reduce buildable area to <15 km².  [stress_test | e=5 r=5 | quote: verified]
- Inability to secure binding 3 GW transmission allocation could strand €1B–€2B Phase 0/1 capital if tenants withdraw.  [stress_test | e=5 r=5 | quote: verified]
- PUE increase of 0.1 causes €5M–€10M annual energy cost increase at 1 GW load.  [stress_test | e=5 r=4 | quote: verified]
- Failure to secure DGSI/ANSSI protocols risks loss of premium domestic revenue stream of €10B–€20B long-term.  [stress_test | e=5 r=4 | quote: verified]
- Brownfield remediation costs could double or triple, increasing the budget by €500M–€2.25B, thereby delaying data hall construction start.  [stress_test | e=5 r=4 | quote: verified]

## Missing data to estimate
- Annual holding cost per hectare in EUR/ha/year for non-buildable land in Dunkirk/Cambrai zones — to budget 128.8 km² holding costs.  [missing | e=4 r=4 | quote: verified]
- Duration in months DGSI review for initial 500 MW isolation PoC — to schedule security sign-off gate.  [missing | e=3 r=4 | quote: verified]
- Required financial collateral amount in EUR demanded by RTE for Phase 2 (3 GW) interconnection initiation — scaling factor for grid investment collateral.  [missing | e=4 r=5 | quote: unverified]
- Duration in months RTE requires for network upgrade completion after Phase 2 funding commitment — to calculate grid latency offset.  [missing | e=4 r=5 | quote: unverified]
- Cost premium percentage added to civil construction due to 75% local workforce sourcing mandate — to price workforce risk.  [missing | e=3 r=4 | quote: unverified]
