Sections come in two forms.

Compressed sections (Selected Scenario, Review Plan, Premortem, Expert
Criticism). Each bullet carries an inline tag of the form
``[<source_status> | e=N r=N | quote: verified|unverified]``:

- ``explicit``    — the plan commits directly to this value
- ``derived``     — calculable from one or more ``explicit`` values
- ``inferred``    — source-stated non-binding claim, or a model-added
                    plausible guess
- ``stress_test`` — a downside-scenario magnitude, not a plan fact
- ``missing``     — a primitive input the source does not supply

- ``e=N`` — source evidence (1-5)
- ``r=N`` — modelling relevance (1-5)
- ``quote: verified|unverified`` — independent substring check of the
  source_quote against the original section text

Raw sections (Executive Summary, Project Plan, Assumptions, Data
Collection). These carry no inline tags. Apply general parameter-extraction
triage to them: prefer plan commitments, numeric anchors, denominators,
and missing inputs over narrative framing.

When extracting parameters from the compressed sections, prefer
``explicit`` and ``derived`` items with ``quote: verified``. Treat
``stress_test`` items as downside-scenario inputs rather than baseline
plan facts. Items in ``Missing data to estimate`` are the ones to surface
as ``missing_values_to_estimate`` in the output.

---

# Executive Summary

## Focus and Context
How will a multi-billion Euro commitment overcome the French infrastructure triad of Power, Land, and Sovereignty? This plan outlines the 'Pragmatic Scale-Up' strategy to build the 9 GW Sovereign AI Engine in Hauts-de-France by systematically de-risking capacity scaling against external regulatory and revenue validation gates.

## Purpose and Goals
The primary goal is successfully completing Phase 1 (1 GW operational within 3 years at PUE <=1.20) while achieving two critical prerequisites for subsequent scaling: securing binding power commitment for the 3 GW expansion from RTE and achieving 60% tenant revenue commitment before Phase 1 construction FID.

## Key Deliverables and Outcomes
Phase 1 build completion (1 GW) within 36 months; Formal DGSI sign-off on Phase 1 security isolation; Budget finalized and funded for 18-month land-holding costs for the 80% buffer zone; Binding RTE commitment secured for post-Phase 1 transmission capacity.

## Timeline and Budget
Phase 1: 3 years (36 months) CAPEX estimated at €5B–€10B. Long-term 9 GW footprint development spans 10–15 years (€100B+ total). Initial Phase 0 budget must include funding for uncosted land holding reserves and workforce academy development.

## Risks and Mitigations
The three critical risks are: 1) Regulatory Delays caused by judicial challenge to the hyper-dense land model (Mitigated by dedicating 30% buffer as permanent ecological offset). 2) RTE/Grid Confirmation Failure contingent on external timeline (Mitigated by strictly linking Phase 2 FID to both tenant revenue *and* binding RTE contract). 3) Failure to Monetize Local Benefit (Mitigated by immediately funding the skills academy and heat reuse feasibility).

## Audience Tailoring
The summary is tailored for senior investors, government partners (DGSI/Prefectures), and key infrastructure executives (RTE/EDF), adopting a rigorous, skeptical, and condition-heavy tone suitable for high-CAPEX, multi-year industrial strategy.

## Action Orientation
Immediate action is required across three vectors: The Grid Specialist must engage RTE to finalize the 36-month infrastructure completion buffer; the Land Modeler/CFO must finalize and budget the €1.3B holding cost for the 80% land reserve by Q3 2026; and the Regulatory Lead must secure written DGSI acknowledgement of Phase 1 isolation feasibility by Q1 2027.

## Overall Takeaway
The 'Pragmatic Scale-Up' provides a controlled, skeptical path to unlock the 9 GW potential by enforcing stringent revenue and regulatory validation gates, transforming critical infrastructure dependencies into manageable, sequenced financial decisions.

## Feedback
Strengthen the summary by explicitly quantifying the financial impact of the deferred RTE timeline (36+ months) on the overall 15-year NPV, and provide a firm budgetary allocation for the residual, unhedged USD hardware exposure to demonstrate comprehensive financial control over currency volatility.

---

# Project Plan

**Goal Statement:** Successfully complete Phase 1 (500 MW–1 GW buildout) of the Hauts-de-France AI data center campus within 3 years, achieving operational PUE of 1.20, securing 500 MW-1 GW in non-classified commercial capacity, and obtaining legally binding grid commitment for the subsequent 2 GW expansion tranche prior to Phase 1 construction financing FID.

## SMART Criteria

- **Specific:** Successfully build, commission, and operate a functionally and contractually validated 500 MW to 1 GW segment of the hyperscale AI data center campus in Hauts-de-France, focusing on liquid cooling and strict power segregation until national security clearance for sovereign zones is finalized.
- **Measurable:** Phase 1 completion is measured by successful operation at target PUE (<=1.20), verified contractual commitment for 60% of the next 2 GW expansion tranche (Decision 4), and a binding RTE allocation contract for new transmission capacity required for Phase 2.
- **Achievable:** Achievable by adhering to the Pragmatic Scale-Up strategy, which intentionally limits initial power commitment to non-binding consultation for Phase 1, reducing immediate CAPEX exposure, and focusing on hyper-dense construction within a pre-defined 32.2 km² buildable area.
- **Relevant:** This phase validates the core technical and financial assumptions required to pursue the full 9 GW long-term goal, specifically testing grid coordination feasibility, tenant demand thresholds, and social license viability in the chosen region.
- **Time-bound:** 3 Years (End of Phase 1)

## Dependencies

- Completion of Phase 0 Feasibility, Site Control, and Land Assembly Agreements.
- Successful execution of pre-paid RTE grid impact studies for initial 1 GW load (Decision 1, Choice 2).
- Securing preliminary right-of-way easements for Phase 2 transmission upgrades (Assumptions Q8).
- Formal agreement on physical and logical isolation protocols for the future sovereign compute zone (Decision 3).
- Securing initial, binding contracts covering 30-50% of the next 2 GW expansion tranche (Decision 4).

## Resources Required

- Land control documentation for 161 km² area, primarily for 32.2 km² buildable zone and 128.8 km² buffer.
- EUR denominated financing (€5B–€10B) for Phase 1 CAPEX.
- Direct-to-chip liquid cooling components (pumps, piping, heat rejection equipment).
- Hardware Procurement Contracts denominated in EUR or covered by 70% forward hedging (for initial 1 GW compute).
- Specialized environmental remediation contractors for brownfield sites.
- Local workforce development program funding (~€12.5M–€37.5M initial allocation).

## Related Goals

- Finalize 9 GW Power Procurement Strategy (Post-Phase 1)
- Achieve DGSI/ANSSI Sign-off for Sovereign AI Partitioning (Post-Phase 1)
- Establish Full Multi-Route Fiber Network to Core European Hubs (Phase 2)

## Tags

- Hyperscale
- Hauts-de-France
- AI Data Center
- 9GW
- Liquid Cooling
- Grid Feasibility
- Skepticism

## Risk Assessment and Mitigation Strategies


### Key Risks

- Regulatory Delays: Judicial challenges to the fragmented, hyper-dense land assembly plan (80% buffer).
- RTE/Grid Confirmation Failure: Inability to secure binding 3 GW capacity allocation before Phase 1 construction FID.
- Failure to Monetize Local Benefit: Inability to secure binding Heat Reuse contracts or meet workforce quotas, eroding social license.

### Diverse Risks

- Technical: Inability to consistently maintain PUE <=1.20 in brownfield deployment under liquid cooling load.
- Financial: Budget overrun (€1.3B+) due to uncosted holding costs for permanent and reserve buffer land.
- Operational/Security: Failure to physically isolate Phase 1 commercial load from future sovereign zone, jeopardizing premium revenue.

### Mitigation Plans

- For Regulatory Delays: Proactively designate 30% of the buffer as legally binding 'Permanent Ecological Offset' in Phase 0 (Decision 10, Choice 2) to preempt litigation regarding long-term land use.
- For RTE/Grid Confirmation Failure: Adhere strictly to 'No Grid Pre-Commitment' for upgrade capital (Decision 1, Choice 2), making Phase 2 expansion FID contingent on 60% signed tenant capacity (Decision 4) *and* a formal RTE contract for transmission upgrades.
- For Failure to Monetize Local Benefit: Immediately budget and execute the initial skill academy funding commitment (€12.5M minimum) and formalize feasibility studies for heat reuse partners in Phase 0 (Assumptions Q3, Decision 6).
- For Technical PUE Risk: Mandate dry-cooling only for Phase 1 heat rejection, setting operational PUE tolerance ceiling at 1.20 (Assumptions Q4) to manage water scarcity risks.
- For Land Holding Cost: Explicitly budget holding costs for the 128.8 km² buffer for 18 months upfront, ring-fenced from infrastructure CAPEX (Review Issue 2).
- For Operational/Security Isolation: Contractually and physically separate Substation 1 for initial 500 MW load from all future sovereign zone connection points, using dedicated feeders (Pre-Project Q4).

## Stakeholder Analysis


### Primary Stakeholders

- Project Development Team (Plan Execution)
- Anchor Tenants (Post-FID capacity purchasers)
- EPC/Construction Managers (Delivery of 1 GW physical build)

### Secondary Stakeholders

- RTE / EDF (Grid Access and Power Contracts)
- DGSI / ANSSI (National Security Vetting & Sovereignty Alignment)
- DREAL / Prefectural Authorities (Land Zoning, Environmental Permits)
- Local Municipalities (Cambrai, Valenciennes, Dunkirk - Social License/Workforce)

### Engagement Strategies

- Project Team: Weekly progress reviews and formal decision gate submissions for all planning milestones.
- Anchor Tenants: Quarterly confidential updates on power reliability verification and security status, linking Phase 2 expansion FID directly to their commitment thresholds.
- RTE/EDF: Utilize pre-paid studies to force high-priority review slots; provide necessary collateral estimations contingent on binding capacity confirmation.
- Regulatory Authorities (DGSI/ANSSI): Proactive, front-loaded engagement in Phase 0/1 with isolation schematics to accelerate security review timelines for the non-classified initial load.
- Local Municipalities: Implement mandatory 75% local hiring clause (Decision 8) and commence immediate funding for the regional skills academy to secure social license over buffer land usage.

## Regulatory and Compliance Requirements


### Permits and Licenses

- Land Use Zoning Approvals for Fragmented Parcels (DREAL/Local Authorities)
- Environmental Impact Assessment (EIA) Approvals across multiple zones
- Water Usage Permits (Given ultra-low/zero-water cooling preference)
- Electrical Connection Permit for 1 GW capacity (RTE/Enedis)

### Compliance Standards

- French National Security Requirements (DGSI/ANSSI) for Data Center Classification
- EU GDPR and Data Sovereignty Requirements
- PUE and Efficiency Standards (Related to PPA terms)
- Brownfield Remediation Standards (ICPE classifications if applicable)

### Regulatory Bodies

- Direction régionale de l'environnement, de l'aménagement et du logement (DREAL)
- Direction Départementale des Territoires et de la Mer (DDETSPP)
- Réseau de Transport d'Électricité (RTE)
- Direction Générale de la Sécurité Intérieure (DGSI)

### Compliance Actions

- Submit formal request for expedited review of the hyper-dense land use model under the local planning authority (Phase 0).
- Schedule DGSI checkpoint meeting (Q4 2026) to review physical segregation plans between commercial and sovereign clusters.
- Implement compliance plan for brownfield remediation based on Phase 0 environmental baseline testing.
- Execute initial PPA template negotiations requiring EDF/EDF-backed green energy sources for the 1 GW commitment.

---

# Selected Scenario

This section selects the 'The Builder: Pragmatic Scale-Up' plan, establishing the baseline scenario committed to a 9 GW full buildout in Hauts-de-France. Key operational commitments involve a phased approach tied to specific validation gates, including limiting Phase 1 power commitment to non-binding agreements while mandating a high 60% take-or-pay threshold for anchor tenants before committing to the 1-3 GW expansion tranche.

## Numeric values
- Fixed total physical area: 161 km² — capacity ceiling.  [explicit | e=5 r=5 | quote: verified]
- Fixed notional footprint dimension: 12.7 km — input to land use model.  [explicit | e=5 r=4 | quote: verified]
- Phase 1 power target range minimum: 500 MW — Phase 1 commencement trigger.  [explicit | e=5 r=5 | quote: unverified]
- Phase 1 power target range maximum: 1 GW — Phase 1 commencement trigger.  [explicit | e=5 r=5 | quote: unverified]
- Full buildout power target: 9 GW — capacity ceiling.  [explicit | e=5 r=5 | quote: unverified]
- Power Usage Effectiveness PUE target range minimum: 1.15 — operational cost driver.  [explicit | e=5 r=4 | quote: unverified]

## Load-bearing assumptions
- Phase 1 expansion requires anchor tenants with commitments for 30% to 50% capacity.  [explicit | e=5 r=5 | quote: verified]
- Phase 2 expansion requires tenant capacity commitments greater than or equal to 60% of the tranche.  [explicit | e=5 r=5 | quote: verified]
- Phase 1 power commitment is based only on a non-binding hosting consultation response from RTE.  [explicit | e=5 r=5 | quote: verified]
- Sovereign AI partition compliance requires a formal signed agreement with national authorities before scaling load.  [explicit | e=5 r=5 | quote: verified]
- The project requires obtaining a credible social license before proceeding beyond Phase 0 feasibility.  [explicit | e=5 r=4 | quote: verified]
- The default cooling strategy must target ultra-low-water usage or zero-water consumption to manage risk.  [explicit | e=5 r=4 | quote: verified]

## Gates and thresholds
- If Phase 1 feasibility criteria are not proven credible, then the project does not proceed past Gate 0.  [explicit | e=5 r=5 | quote: verified]
- If creditworthy anchor tenants have not signed for 30% to 50% of the next tranche, then FID for expansion is blocked.  [explicit | e=5 r=5 | quote: verified]
- If power reliability, PUE, water, security, and community targets are not met after Phase 1, then expansion is blocked.  [explicit | e=5 r=5 | quote: verified]
- If demand, grid capacity, financing, permits, and social license are not strong in Year 7, then 9 GW is not reached.  [explicit | e=5 r=4 | quote: unverified]
- If the required national security review is not completed, then the project cannot proceed past Phase 0.  [inferred | e=4 r=4 | quote: unverified]

## Risks and shocks
- Failure to secure anchor tenants leads to no FID for the 1-3 GW expansion tranche.  [stress_test | e=5 r=4 | quote: verified]
- Grid commitment failure: schedule delay/cost overrun tied to RTE transmission upgrades.  [stress_test | e=4 r=5 | quote: verified]
- Failure of DGSI/ANSSI alignment results in inability to implement dedicated sovereign AI partition post-Phase 1.  [stress_test | e=4 r=5 | quote: verified]
- Inability to host 9 GW without overwhelming the French grid: feasibility failure.  [stress_test | e=5 r=5 | quote: unverified]
- Environmental/Water failure leads to mandatory prohibition of high-risk evaporative cooling systems.  [stress_test | e=5 r=3 | quote: verified]
- Local litigation delays land aggregation for the 161 km² footprint by years.  [stress_test | e=3 r=4 | quote: verified]

## Missing data to estimate
- Total Phase 1 operational expenditure excluding initial CAPEX for Years 1 through 3 — estimate using labor and operational contracts.  [missing | e=1 r=4 | quote: unverified]
- Cost metric for land assembly premiums paid to accelerate consolidation (EUR per km²) — required to calculate Phase 0/1 land budget overrun risk.  [missing | e=1 r=4 | quote: unverified]
- Annual revenue per MW sold in Euros for tenant contract baseline — estimate based on comparable regional data.  [missing | e=1 r=5 | quote: unverified]
- Average daily revenue exposure for 1 GW of capacity in EUR per day — needed to quantify downtime risk.  [missing | e=1 r=4 | quote: unverified]
- Duration of potential litigation delay for 161 km² contiguous land assembly in years — needed for schedule impact analysis.  [missing | e=1 r=4 | quote: unverified]
- Conversion rate from LOI to signed take-or-pay contract for expansion tranches (percent) — estimate based on competitive conversion velocity.  [missing | e=1 r=4 | quote: unverified]

---

# Assumptions

# Purpose
# Project Plan Summary

## Purpose

- Business: Strategic planning and feasibility assessment.

## Topic

- Development of an intentionally extreme hyperscale AI data center campus (9 GW) in Hauts-de-France, France.


# Domain
# Project Planning Summary

## Rationale

- Primary Domain: Data Center Infrastructure Planning (defined by 9 GW campus scope/scale/feasibility).
- Secondary Domains: Electrical Power Engineering, French Regulatory Compliance.
- Land Development supports central planning.

## Disciplines Involved

| Domain | Importance | Specificity | Role | Reason |
|---|---|---|---|---|

- Data Center Infrastructure Planning | 5 | 5 | outcome | Project defined by hyperscale DC planning/execution. |
- French Regulatory Compliance | 5 | 5 | constraint | Permitting, environmental law, security reviews are critical blockers. |
- Energy Grid Management | 5 | 5 | constraint | 9 GW power depends on French grid feasibility/coordination. |
- Electrical Power Engineering | 5 | 4 | constraint | Sourcing/integrating 9 GW power is a critical bottleneck. |
- Large Scale Land Development | 4 | 4 | method | Modeling 161 km² across zones is core planning. |
- Telecommunications Infrastructure | 4 | 4 | method | Diverse, low-latency fiber is essential for AI compute. |
- Urban and Regional Planning | 4 | 4 | outcome | Land parcel assembly and zoned land-use model require expertise. |
- Real Estate Acquisition | 4 | 4 | method | Assembling 161 km² requires specialized methods. |
- Environmental Impact Assessment | 4 | 4 | constraint | Water, biodiversity, remediation are key feasibility/permitting constraints. |


# Plan Type
# Project Classification

- Requires one or more physical locations.
- Cannot be executed digitally.

# Explanation

- Multi-year strategy focused on physical execution: building a massive data center campus (161 km²) in Hauts-de-France, France.
- Involves massive physical construction, land acquisition/assembly (161 km²).
- Coordinates multi-gigawatt electrical infrastructure (9 GW).
- Manages physical cooling systems (liquid cooling loops).
- Establishes physical fiber routes.
- Deals with brownfield remediation.
- Navigates physical permitting processes localized to specific parcels of land.
- Plan is overwhelmingly dedicated to overcoming rigorous physical, engineering, logistical, and regulatory hurdles required to place compute in the real world.


# Physical Locations
# Project Plan - Location Requirements

## Requirements for physical locations

- Footprint: 161 km² (30 km² buildable)
- Power: Access to 9 GW contracted, reliable, low-carbon/nuclear-backed post-Phase 2
- Proximity: Existing industrial revitalization zones (Cambrai, Dunkirk, Valenciennes)
- Cooling: Favorable climate (low high-water cooling risk)
- Latency: Strategic to Paris, London, Brussels, Frankfurt via diverse fiber
- Land: Suitable brownfield/industrial for remediation and large-scale development

## Location 1
France
Hauts-de-France Region: Cluster 1 (E-Valley/Cambrai)

- Land near Cambrai or Valenciennes (brownfield redevelopment).
- Rationale: Targets industrial redevelopment, high initial velocity for land assembly (1 GW phase) using existing logistics.

## Location 2
France
Hauts-de-France Region: Cluster 2 (Dunkirk Port Area)

- Industrial/reclaimed land near Port of Dunkirk.
- Rationale: Access to heavy logistics, potential maritime fiber, heat-reuse partners, or diverse power interconnection.

## Location 3
France
Hauts-de-France Region: Buffer/Expansion Reserve Zones

- Agricultural/ecological buffer parcels adjacent to Clusters 1 and 2.
- Rationale: Supports 'hyper-dense development model'; preserves 80% of 161 km² as non-buildable buffer/expansion reserve, mitigating sprawl/impact, maintaining expansion option up to 9 GW over 15 years.

## Location Summary
Targets Hauts-de-France, France (Cambrai, Valenciennes, Dunkirk zones). Three locations align with Skeptical Path: two primary clusters for dense buildout, one adjacent area for mandated ecological/community buffers (80% of 161 km²).

# Currency Strategy
# Currencies

- EUR: Primary for land, labor, local taxes, grid connection (project location: France).
- USD: Hardware procurement (GPUs/TPUs, networking) and international financing exposure.

Primary currency: EUR

Currency strategy:

- EUR for budgeting, accounting, reporting (local costs).
- Track USD exposure from hardware procurement.
- Implement formal FX hedging strategy (e.g., forward contracts) for major USD hardware purchases starting Phase 1.


# Identify Risks
# Project Risks and Mitigation

## Risk 1 - Regulatory & Permitting
Failure to secure land assembly consents/permits for fragmented development in Hauts-de-France. Legal challenges over buffer zone designation (Decision 2 - Choice 2) could stop construction.

- Impact: 12–24 month delay to Phase 1 FID; €500M–€1B overrun; forced buildable area reduction (<15 km² from 30 km²).
- Likelihood: High
- Severity: High
- Action: Proactively engage DREAL/DDETSPP for 'Projet d'Intérêt Général' (PIG) status for critical infrastructure; treat buffer zones as non-negotiable early concessions.

## Risk 2 - Technical
Inability to meet aggressive PUE target of 1.15–1.25 at 1 GW+ using default direct-to-chip liquid cooling at scale in brownfield deployment.

- Impact: PUE increase of 0.1 (1.25–1.35 average); €5M–€10M annual energy cost increase at 1 GW; potential violation of PUE clauses tied to anchor tenants (Decision 4).
- Likelihood: Medium
- Severity: Medium
- Action: Pilot liquid cooling validation via digital twins during design. De-risk Phase 1 with performance-based escalator clauses for anchor tenants if PUE misses target by >0.05 due to integration issues.

## Risk 3 - Financial
Sunk capital if RTE/EDF cannot confirm capacity for Phase 2 (3 GW) before Phase 1 (1 GW) financing closes (Decision 1 - Choice 2).

- Impact: Inability to secure binding transmission allocation could halt project, potentially stranding €1B–€2B Phase 0/1 capital if tenants withdraw.
- Likelihood: High
- Severity: High
- Action: Strictly adhere to Pragmatic Scale-Up: no Phase 2 expansion funding (beyond studies) until RTE provides a formal, legally binding contract for required transmission upgrades.

## Risk 4 - Supply Chain
Exposure to USD/EUR exchange rate volatility affecting hardware procurement despite hedging.

- Impact: If EUR depreciates >10% vs. USD, hardware costs could inflate by €8B–€15B on the €100B-€140B budget for 9 GW buildout.
- Likelihood: Medium
- Severity: High
- Action: Implement multi-year forward hedging for 70% of USD hardware needs (Phase 1 & 2). Require Phase 1 tenants to contract in EUR-equivalent terms to pass on minor FX deviation risk.

## Risk 5 - Operational / Security
Failure to secure DGSI/ANSSI protocols and sign-off on sovereign AI partition (Decision 3) before leasing 500 MW, risking denial of state contracts.

- Impact: Loss of premium domestic revenue stream, jeopardizing 60% commitment threshold for Phase 2 (Decision 4); potential loss of €10B–€20B in long-term contracted revenue.
- Likelihood: Medium
- Severity: High
- Action: Isolate initial 500 MW cluster from planned sovereign zone. Proactively engage DGSI in Phase 0/1 with detailed security schematics, integrating Layer 1 physical segregation into initial substation planning.

## Risk 6 - Environmental / Water
Hydrological constraints in Hauts-de-France making 'ultra-low-water' cooling non-viable or prohibitively expensive.

- Impact: If evaporative cooling is needed, water consumption may trigger regional restrictions, leading to mandatory curtailment (€1M–€5M penalty per week).
- Likelihood: Medium
- Severity: Medium
- Action: Mandate zero-water density heat rejection (e.g., dry coolers) for 100% of Phase 1, accepting temporary PUE degradation (max 1.20) until water sustainability is proven.

## Risk 7 - Social / Policy
Public opposition or judicial appeal on the 'hyper-dense development model' sacrificing 80% of land for buffers (Decision 2, Choice 2 & Decision 10).

- Impact: Prefecture could reduce buildable area to <20 km², constraining 9 GW target to 3–4 GW, forcing business case re-evaluation.
- Likelihood: High
- Severity: High
- Action: Aggressively implement Decision 8 (Workforce Uplift) and Decision 6 (Heat Reuse) in Phase 0. Use buffer land for tangible community benefits (e.g., local solar farm) to gain stakeholder cooperation.

## Risk 8 - Technical / Integration
Latency incompatibility between terrestrial fiber routes (Decision 5) and synchronized AI training needs across Paris/London/Brussels network (sub-millisecond consistency).

- Impact: Latency >1.5ms (terrestrial RT to Paris) may allow tenant SLA breach claims, risking contract loss if dark fiber/subsea investment is deferred until Phase 3.
- Likelihood: Medium
- Severity: Medium
- Action: Task specialists for independent, real-time latency benchmarking. If results are below requirement, commit Phase 1 CAPEX to securing dark fiber rights-of-way for the Phase 2 path, accepting conflict with Power Procurement Sequencing.

## Risk 9 - Financial / Budgeting
Underestimation of Brownfield Remediation Costs due to industrial history (steel, refinery, military zones).

- Impact: Remediation costs (€250M–€750M budget) could double/triple (€500M–€2.25B) if hazardous materials require advanced handling, delaying data hall construction start.
- Likelihood: Medium
- Severity: Medium
- Action: Dedicate 80% of Phase 0 budget to comprehensive environmental testing and risk modeling. Secure fixed-price remediation contracts with regional specialists before land assembly finalization.

## Risk Summary
Project profile is extremely high-risk, dominated by regulatory uncertainty and interdependent critical path items. 'Pragmatic Scale-Up' strategy reduces immediate financial exposure but elevates risk of political/social blockage due to land rationalization (80% buffers).

Critical Risks:
1. Regulatory Delays (High/High): Judicial review of fragmented development could halt progress.
2. RTE/Grid Confirmation (High/High): Deferring grid investment until Phase 2 FID risks stranding Phase 1 capital if capacity confirmation is delayed.
3. Social License Erosion (High/High): Failure of Workforce Uplift/Heat Reuse monetization risks political rejection or mandated footprint reduction, undermining 9 GW goal.

Mitigation overlap exists: successful social license programs support faster regulatory permitting. Core trade-off remains speed (AI market need) versus financial prudence (mandate).

# Make Assumptions
## Question 1 - Quantified Footprint Allocation

- Target buildable area (20% hyper-dense model): 32.2 km² (Data center/substations)
- Essential buffer/community/ecological zones (80%): 128.8 km²
- Assessments: Land Use Feasibility

    - Allocating 80% mitigates local opposition but reduces initial 15-year capacity.
    - Benefit: Streamlines permitting for the 20% core.
    - Risk: Fails if anchor tenants require contiguous expansion, requiring split-campus review.
    - Opportunity: Buffer allows long-term expansion for heat exchange/water management.

## Question 2 - Binding Go/No-Go Trigger for Phase 2 Transmission Upgrades

- Explicit trigger: Execution of signed, take-or-pay, non-cancellable Power Purchase Agreements covering 60% of the 2 GW expansion tranche.
- Assessments: Grid Investment Control

    - Links financial sign-off to physical grid commitment.
    - Risk: Stranded capital if RTE demands commitment before the 60% tenant threshold.
    - Benefit: Infrastructure investment scales directly with bankable revenue.

## Question 3 - Specific EUR Public Benefit Commitment Locked in Phase 0

- Commitment: Mandatory minimum of 5% of Phase 0 budget (€12.5M–€37.5M) allocated for initial operational funding of the regional skills academy and feasibility studies for the heat-reuse industrial partner.
- Assessments: Social License Stabilization

    - Front-loading visible benefits mitigates social risks (Risk 7).
    - Benefit: Turns opposition into cooperation, accelerating permitting.
    - Risk: Commitments must be non-binding to maintain efficacy.

## Question 4 - Projected Maximum Operational PUE for Phase 1

- Projected Maximum Operational PUE: 1.20 (includes BESS losses, liquid cooling mandate).
- Assumptions: Liquid cooling optimized for 1.15 target; BESS losses estimated at 2%.
- Assessments: Efficiency and Operational Cost Performance

    - Risk: PUE > 1.25 increases operational costs by ~€5M/GW/year.
    - Opportunity: Achievable PUE justifies liquid-cooling CAPEX.

## Question 5 - Projected EUR Cost Variance Based on 10% Unfavorable FX Shift

- Projected Cost Variance: Approximately €4.32 Billion (unhedged portion).
- Assumptions: 30% of €120B CAPEX is USD-denominated hardware; 70% hedged.
- Assessments: Financial Exposure and Hedging Efficacy

    - Residual exposure mandates contingency budgeting.
    - Benefit: Mandates immediate execution of forward contracts upon Phase 1 pricing lock.
    - Risk: Unhedged exposure requires contingency line item for debt servicing covenants.

## Question 6 - Minimum Acceptable Latency Deviation for Split-Campus Synchronization

- Minimum Latency: Below 2ms round-trip time (RTT) between Cluster 1 and Cluster 2.
- Assumptions: Requires dedicated, privately leased, high-grade terrestrial fiber paths.
- Assessments: Inter-Campus Synchronization Viability

    - If 2ms RTT fails, the split-campus model is unviable for demanding AI workloads.
    - Opportunity: If met, enables decoupling of regulatory/power risks.

## Question 7 - Initial 500 MW Hardware Procurement and DGSI Assurance

- Hardware Focus: Commercial-grade, non-restricted AI accelerators for Phase 1.
- Assurance Method: Hardware housed in physically separate buildings with legally ring-fenced primary substation capacity (Substation 1 isolated from Sovereign Zone substations).
- Assessments: Security Isolation and Initial Revenue Path

    - Benefit: Allows immediate revenue generation while sovereign zone designs are reviewed.
    - Risk: 'Non-classified' definition must be formally agreed in Phase 0 to prevent retrofitting.

## Question 8 - Temporary Land-Use Mechanism Secured in Phase 0 for Future Interconnection Points

- Mechanism: Preliminary right-of-way (ROW) easements secured for Phase 2 required expansion substations and tie-lines, including adjacent buffer land.
- Assessments: Long-Lead Physical Infrastructure Control

    - Securing ROW is a long-lead permitting activity decoupled from financing trigger.
    - Failure transforms grid uncertainty (Risk 3) into a physical blocker.
    - Benefit: Buffers implementation schedule against utility's internal timeline.

# Distill Assumptions
# Project Plan Summary

## Area & Buffers

- Buildable area: 32.2 km² (20% of 161 km²)
- Buffers: 80% reserved

## Funding & Tranches

- Phase 2 transmission funding triggers at 60% take-or-pay contracts for 2 GW tranche.

## Phase 0 Allocations

- 5% of initial budget for local skills academy.
- Heat-reuse feasibility studies.
- Secure preliminary right-of-way easements for Phase 2 transmission upgrades.

## Phase 1 Targets & Requirements

- Operational PUE target: 1.20 (conservative).
- Cooling: Mandatory direct-to-chip liquid cooling.
- Hardware isolation: Phase 1 commercial hardware must be physically isolated via separate substation capacity from future sovereign zones.

## Technical Requirements

- Inter-cluster latency (split campuses): Below 2ms RTT for synchronized AI workloads.

## Risks

- Financial Risk: 10% EUR/USD unfavorable shift creates approx. €4.32 Billion unhedged hardware cost exposure.


# Review Assumptions
## Domain of the expert reviewer
High-Scale Infrastructure Project Planning and Feasibility Assessment

## Domain-specific considerations

- Grid Interconnection Lead Times (RTE/EDF)
- French Regulatory/Sovereignty Alignment (DGSI/ANSSI)
- Large-Scale Land Assembly and Zoning Complexity (161 km²)
- Capital Allocation Sequencing vs. Revenue Triggering
- Workforce Development for Specialized Infrastructure

## Issue 1 - Critical Missing Assumption: Regulatory Time Buffer (RTE/Permitting)

- Plan uses 'Pragmatic Scale-Up' (deferring Phase 2 funding until 60% tenant commitment).
- Missing assumption: Explicit RTE approval/upgrade completion time after funding commitment (3-5 years typical).
- Dependency gap: Tenants commit based on power availability, but infrastructure completion is external.
- Recommendation: Assume minimum 36-month completion for RTE upgrades post-Phase 2 FID. Adjust Tenant Acquisition Trigger Threshold (Decision 4) with 'Power Readiness Lockout Clause': Phase 2 COD = Min(Tenant Anchor COD + 12 months, RTE Upgrade Completion Date).
- Sensitivity: 18-month vs 36-month grid lead time increases delay by 1.5 years, losing 8-12% ROI over four years, increasing CoC by €500M–€800M.

## Issue 2 - Under-Explored Assumption: Financial Viability of 80% Land Buffer

- Model reserves 80% (128.8 km²) as buffer/reserves (32.2 km² buildable).
- Assumption: Preserves optionality/smooths permitting.
- Viability hinges on holding cost coverage (operating budget vs. capitalized).
- Risk: Legally holding 80% as 'permanent ecological preservation' for 15 years without binding community benefit contracts (Decision 6) is questionable.
- Recommendation: Explicitly budget holding cost for 128.8 km² (€50k–€75k/ha annually). Decouple permanence: Reclassify 50% buffer as 'Phase 2/3 Expansion Reserve' (annual renewal) and 30% as 'Permanent Ecological Offset' (upfront, binding commitments via Decision 10).
- Sensitivity: Undershooting annual holding cost by €20k/ha risks €1.3B overrun in early CAPEX. Loss of 10 km² buildable area due to disputes reduces capacity from 9 GW to ~6 GW, decreasing potential ROI by 30-40%.

## Issue 3 - Unrealistic Assumption: Workforce Skill Uplift Velocity

- Decision 8 mandates 75% local workforce sourcing via apprenticeships for social license.
- Assumption ignores skill generation time from vocational schools (Decision 3/8) needed for specialized liquid-cooled DCs and DGSI isolation checks.
- Risk: Underestimates management overhead and quality control risks of unproven upskilling.
- Recommendation: Introduce staffing latency: Assume 30% local specialty hire in Year 1, rising to 50% in Year 2. Rely on higher-cost international contractors initially. Integrate contingency budget (€20M–€40M) for importing specialized management teams to oversee training.
- Sensitivity: Labor unavailability could extend Phase 1 (1 GW) from 24 months to 30-36 months. This 6-12 month delay plus management costs (€50M–€100M) reduces NPV by 4-6%.

## Review conclusion

- Plan is strategically sound (phased approach identified interdependencies).
- Execution timeline is overly optimistic regarding external dependencies.
- Critical weaknesses identified via quantified missing assumptions:

1. Missing Grid Completion Buffer: Poses 1.5-year revenue delay risk due to unbuffered RTE execution time.
2. Uncosted Land Holding: Massive 80% buffer lacks budget, risking €1.3B early CAPEX overrun.
3. Workforce Optimism: Rapid local upskilling risks 6-12 month technical delays in Year 1 impacting early ROI.

- Immediate Action: Lock in regulatory timing buffers, fully budget land holding costs, accept higher initial construction costs/delays for genuine local workforce integration.

---

# Review Plan

This review plan isolates critical project gates, cross-functional dependencies, and external validation requirements across power procurement, land rationalization, and security alignment that must be passed or meet specific performance thresholds to proceed with subsequent phases, directly framing the logic for sequential schedule analysis and risk dependency mapping.

## Numeric values
- Phase 2 binding transmission allocation needed prior to Phase 1 construction financing — required condition for gate  [explicit | e=4 r=5 | quote: verified]
- Phase 1 scope minimal commitment for power certainty: 500MW-1GW connection point — strategic choice checkpoint  [explicit | e=4 r=5 | quote: verified]
- Phase 1 scope minimal commitment for power certainty: 500 MW backed only by non-binding response — strategic choice checkpoint  [explicit | e=4 r=5 | quote: verified]
- Minimum take-or-pay commitment threshold for 1-3 GW expansion gate to 60% — tenant lock-in gate  [explicit | e=4 r=5 | quote: verified]
- Total contiguous land assembly target: 161 km² — land constraint  [explicit | e=4 r=5 | quote: verified]
- Hyper-dense model buildable area limited to 30 km² long-term — strategic choice checkpoint  [explicit | e=4 r=5 | quote: verified]

## Load-bearing assumptions
- Phase 2 expansion FID requires minimum 60% take-or-pay commitment threshold.  [explicit | e=4 r=5 | quote: verified]
- Phase 1 scope proceeds with 500 MW power backed only by non-binding RTE consultation.  [explicit | e=4 r=5 | quote: verified]
- Phase 1 commercial tenants operate before sovereign AI partition security protocols are signed.  [explicit | e=4 r=5 | quote: verified]
- The hyper-dense model limits buildable area to 30 km² of the 161 km² total footprint.  [explicit | e=3 r=5 | quote: verified]
- Operational PUE target ceiling for initial 1 GW capacity is 1.20.  [explicit | e=3 r=4 | quote: verified]
- Phase 1 power commitment requires immediate, pre-paid grid impact studies for 9 GW capacity.  [explicit | e=3 r=4 | quote: verified]

## Gates and thresholds
- If binding transmission is not allocated for Phase 2 (3 GW) before Phase 1 construction financing, then Phase 1 construction financing cannot proceed.  [explicit | e=4 r=5 | quote: verified]
- If Phase 2 expansion is triggered, then the minimum take-or-pay commitment for that tranche must reach 60%.  [explicit | e=4 r=5 | quote: verified]
- If the construction model is hyper-dense, then 80% of the 161 km² footprint must be designated as ecological buffer/retention.  [explicit | e=4 r=5 | quote: verified]
- If a formal, signed agreement for sovereign AI partition is not executed before Phase 1 Power FID, then access to premium state revenue streams is jeopardized.  [explicit | e=3 r=5 | quote: verified]
- If Phase 1 scope does not use a non-binding RTE consultation response, then Phase 1 financing proceeds with higher capital exposure.  [explicit | e=3 r=4 | quote: verified]
- If the full 161 km² target is not consolidated under one decree, then security perimeter centralization is sacrificed for speed.  [explicit | e=3 r=4 | quote: verified]

## Risks and shocks
- Failure to secure land assembly consents for fragmented development causes a 12–24 month delay to Phase 1 FID.  [stress_test | e=4 r=5 | quote: verified]
- RTE capacity confirmation failure post Phase 1 closing strands €1B–€2B of Phase 0/1 capital if leases are withdrawn.  [stress_test | e=4 r=5 | quote: verified]
- PUE increases of 0.1 causes €5M–€10M annual energy cost deviation at 1 GW operating capacity.  [stress_test | e=4 r=4 | quote: verified]
- Brownfield remediation cost overrun up to €2.25B if hazardous materials double or triple the initial €750M budget.  [stress_test | e=4 r=4 | quote: verified]
- Failure to secure DGSI/ANSSI protocols risks losing premium state revenue streams valued at €10B–€20B long-term.  [stress_test | e=3 r=5 | quote: verified]
- Judicial review challenging the 80% buffer model could constrain buildable area from 30 km² to under 15 km².  [stress_test | e=3 r=5 | quote: verified]

## Missing data to estimate
- RTE upgrade completion timeline in months after Phase 2 funding commitment — required for schedule contingency modeling.  [missing | e=4 r=5 | quote: verified]
- Annual holding cost per hectare EUR/ha/year for the non-buildable 80% buffer land — input for early CAPEX budget ceiling.  [missing | e=4 r=5 | quote: verified]
- Required financial collateral amount EUR demanded by RTE for Phase 2 (3 GW) grid interconnection initiation — input for capital drawdown scenarios.  [missing | e=3 r=5 | quote: verified]
- Time in months for DGSI/ANSSI review of initial Proof-of-Concept security architecture — input for determining Phase 1 revenue stream start date.  [missing | e=3 r=4 | quote: verified]
- Local technical school lead time in months to certify new apprentice cohort capable of specialized construction work — input for construction delay modeling.  [missing | e=3 r=4 | quote: verified]
- Cash cost per month for the remaining unhedged USD hardware exposure — input for residual FX risk NPV analysis.  [missing | e=2 r=4 | quote: unverified]

---

# Premortem

This section defines specific external failure assumptions centered on land approval friction, grid connection lead times, workforce competency velocity, sovereign security review timelines, and localized PUE challenges, all of which act as critical early tripwires that can halt Phase 1 commercialization or de-risk the overall 9 GW scaling ambition.

## Numeric values
- Phase 1 scope limited to 500 MW backed by non-binding transmission response — gates immediate land mobilization over power certainty.  [explicit | e=5 r=5 | quote: verified]
- Buildable area limited to 30 km² long-term after designating 80% of 161 km² footprint as buffer — determines maximum compute footprint.  [explicit | e=5 r=5 | quote: verified]
- Minimum take-or-pay commitment threshold raised to 60% of next tranche capacity for 1-3 GW expansion gate — financial stability gate.  [explicit | e=5 r=5 | quote: verified]
- Revenue shortfall resulting from denial of high-value government contracts could be €10B–€20B in long-term contracted revenue — security failure impact.  [stress_test | e=5 r=5 | quote: verified]
- Initial hardware procurement cost inflation projected at €8B–€15B if EUR depreciates >10% vs. USD on 9 GW buildout — financial shock magnitude.  [stress_test | e=5 r=4 | quote: verified]
- First 500 MW load remains exclusive to non-classified commercial tenants until sovereign partition agreement is executed — security gating mechanism.  [explicit | e=5 r=4 | quote: verified]

## Load-bearing assumptions
- Phase 1 commits to 500 MW using non-binding RTE consultation response for power certainty.  [explicit | e=5 r=5 | quote: verified]
- Phase 2 expansion financing requires a minimum 60% take-or-pay commitment threshold for next tranche capacity.  [explicit | e=5 r=5 | quote: verified]
- Buildable area is capped at 30 km² long-term under the hyper-dense development model strategy.  [explicit | e=5 r=5 | quote: verified]
- The aggressive 75% local workforce hiring mandate is achievable without causing cost premiums over 5% or major delays.  [inferred | e=5 r=4 | quote: verified]
- Initial 500 MW commercial load operates without sovereign security certification until formal DGSI/ANSSI agreement is signed.  [explicit | e=5 r=4 | quote: verified]
- The project avoids risk by deferring transmission upgrade capital expenditure until the 3 GW expansion gate occurs.  [explicit | e=5 r=4 | quote: verified]

## Risks and shocks
- Failure to secure 3 GW RTE capacity before Phase 1 financing closes risks stranding €1B–€2B Phase 0/1 capital.  [stress_test | e=5 r=5 | quote: verified]
- Failure to align DGSI/ANSSI protocols risks losing premium domestic revenue stream projected at €10B–€20B long-term.  [stress_test | e=5 r=5 | quote: verified]
- PUE degradation to 1.25–1.35 average causes €5M–€10M annual energy cost increase at 1 GW load.  [stress_test | e=5 r=4 | quote: verified]
- EUR depreciation greater than 10% vs. USD could inflate hardware costs by €8B–€15B on total 9 GW buildout budget.  [stress_test | e=5 r=4 | quote: verified]
- Hydrological failure forcing evaporative cooling leads to mandatory curtailment penalties of €1M–€5M per week.  [stress_test | e=5 r=4 | quote: verified]
- Brownfield remediation costs could double or triple the budget, impacting data hall start by up to €2.25B overrun.  [stress_test | e=5 r=4 | quote: verified]

## Missing data to estimate
- Minimum required Phase 2 committed tenant revenue amount in EUR/MW/year — needed to calculate the 60% trigger in gross revenue.  [missing | e=1 r=5 | quote: unverified]
- Annual holding cost per hectare in EUR for non-buildable land parcels in Hauts-de-France — needed to budget 128.8 km² buffer.  [missing | e=1 r=5 | quote: unverified]
- Duration in months RTE requires for 3 GW network upgrade completion after funding collateral payment — needed to resolve timeline conflict.  [missing | e=1 r=5 | quote: unverified]
- Initial Phase 1 CAPEX allocation in EUR earmarked directly for DGSI/ANSSI physical isolation infrastructure costs.  [missing | e=1 r=4 | quote: unverified]
- Minimum required EUR price per MW per month for sovereign AI workloads — needed to benchmark commercial lease rates.  [missing | e=1 r=4 | quote: unverified]
- Required FTE monthly cost burdened by benefits and overheads — needed to budget for imported management during workforce ramp-up.  [missing | e=1 r=3 | quote: unverified]

---

# Expert Criticism

Expert criticism highlights quantified failures in land use planning ambiguity, the necessity of binding Power Purchase Agreements from RTE to mitigate schedule risk, and the lack of a concrete strategy for early community engagement which can trigger legal delays.

## Numeric values
- Total footprint target: 161 km² — parameter for physical site constraint.  [explicit | e=5 r=5 | quote: verified]
- Full buildout power target: 9 GW — primary long-term capacity ceiling.  [explicit | e=5 r=5 | quote: verified]
- Phase 0 feasibility/site control budget maximum: €750M — input for initial capital outlay.  [explicit | e=5 r=4 | quote: verified]
- Phase 1 budget minimum (500 MW-1 GW): €5B — input for initial CAPEX.  [explicit | e=5 r=5 | quote: unverified]
- Phase 1 budget maximum (500 MW-1 GW): €10B — input for initial CAPEX.  [explicit | e=5 r=5 | quote: unverified]
- Phase 1 power range minimum: 500 MW — capacity trigger for expansion readiness.  [explicit | e=5 r=4 | quote: unverified]

## Load-bearing assumptions
- Hyper-dense land use model reserves 80% of total footprint as non-buildable buffer.  [explicit | e=5 r=5 | quote: verified]
- Phase 1 (500 MW commercial) must operate without sovereign classification until DGSI agreement.  [explicit | e=5 r=5 | quote: verified]
- Phase 1 power scope relies only on a non-binding RTE hosting consultation response.  [explicit | e=5 r=5 | quote: verified]
- Phase 2 expansion commits require 60% of next tranche capacity under take-or-pay contracts.  [explicit | e=4 r=5 | quote: verified]
- Anchor tenants will honor the 60% take-or-pay commitment required for Phase 2 expansion FID.  [explicit | e=4 r=4 | quote: verified]
- Local workforce mandate requires 75% of non-specialized labor hours to be local apprentices.  [explicit | e=4 r=3 | quote: verified]

## Gates and thresholds
- If anchor tenants have not signed commitments covering 50% of the next tranche, then there is no FID for expansion.  [explicit | e=5 r=5 | quote: verified]
- If power reliability, PUE, water, security, and community targets are not met, then do not expand beyond Phase 1 capacity.  [explicit | e=5 r=5 | quote: verified]
- If anchor tenants have not signed commitments covering 30% of the next tranche, then there is no FID for expansion.  [explicit | e=5 r=5 | quote: verified]
- If Phase 1 power, land, water, fiber, and social license are not credible, then proceed only if Phase 0 is passed.  [explicit | e=5 r=4 | quote: verified]
- If tenant commitments exceed 60% of the next tranche, then secure lower syndicated debt for expansion.  [explicit | e=4 r=4 | quote: verified]
- If demand, grid capacity, financing, and permits remain strong, then reach 9 GW capacity only by Year 15+.  [explicit | e=5 r=4 | quote: unverified]

## Risks and shocks
- RTE / Grid Confirmation Failure: Inability to secure binding 3 GW capacity before Phase 1 FID leads to schedule risk.  [stress_test | e=4 r=5 | quote: verified]
- Judicial challenges to the fragmented land assembly if the 80% buffer model is legally contested: halt construction momentum.  [stress_test | e=4 r=5 | quote: verified]
- Operational/Security Failure: Failure to physically isolate Phase 1 commercial load from future sovereign zone leads to premium revenue loss.  [stress_test | e=4 r=4 | quote: verified]
- Technical PUE Risk: Inability to maintain PUE of 1.20 during initial 1 GW deployment on brownfield sites.  [stress_test | e=3 r=4 | quote: verified]
- Financial overrun due to uncosted holding costs for the permanent and reserve buffer land: budget increase above expected Phase 1 CAPEX.  [stress_test | e=3 r=4 | quote: verified]
- Protracted DGSI/ANSSI vetting delays access to premium sovereign revenue streams beyond Year 3.  [stress_test | e=3 r=3 | quote: verified]

## Missing data to estimate
- Absolute cost (EUR) for 128.8 km² land buffer holding over 18 months — estimate annual property tax and maintenance.  [missing | e=1 r=5 | quote: verified]
- Required time (months) RTE needs for transmission upgrades following collateral payment for 3 GW connection — estimate required lead time after funding gate.  [missing | e=1 r=5 | quote: unverified]
- Total annual revenue benchmark (EUR) needed to stress-test the 60% take-or-pay commitment threshold — estimate total relevant market size.  [missing | e=1 r=5 | quote: unverified]
- Cost multiplier (EUR/USD) for Phase 1 hardware procurement without full 70% forward hedging coverage — estimate residual unhedged spend exposure.  [missing | e=1 r=4 | quote: unverified]
- Minimum local employment percentage required to secure rapid positive social license sign-off from the Prefect — estimate social license negotiation floor.  [missing | e=1 r=4 | quote: unverified]
- Estimated initial staffing cost (EUR/month per FTE) for the local workforce retraining program — estimate operational overhead input for initial years.  [missing | e=1 r=3 | quote: unverified]

---

# Data Collection

## 1. RTE Grid Upgrade Timeline & Collateral Requirement

This data directly validates the critical path dependency identified in Risk 3 and Review Issue 1. Deferring Phase 2 funding until 60% tenant commitment (Pragmatic Scale-Up) is infeasible if RTE requires an excessively long lead time (>36 months) for infrastructure completion, risking stranded capacity.

### Data to Collect

- Exact timeline (months) for RTE transmission upgrade completion following financial commitment for 3 GW capacity.
- Required financial collateral amount (EUR) demanded by RTE for Phase 2 (3 GW) grid interconnection initiation.
- Binding PPA template structure for capacity allocation post-Phase 1 FID.

### Simulation Steps

- Use PowerFactory/PSSE to model the 9 GW load injection profile onto the RTE network segments impacting Hauts-de-France.
- Develop a spreadsheet model applying the known French cost-per-MW metrics for substation upgrades (based on Suggestion 3 findings) to estimate collateral requirements as a function of required lead time.

### Expert Validation Steps

- Consult the European Energy Regulation Specialist (RTE/PPA expert) to calibrate the required collateral quantum and the minimum mandated timeline for RTE infrastructure completion post-funding.
- Request timeline confirmation data from the Land Use and Environmental Lawyer's network regarding average political/legal buffer applied to DREAL-approved grid infrastructure projects.

### Responsible Parties

- Grid & Power Procurement Specialist (IC)
- Chief Infrastructure Strategist & Project Architect (FTE)

### Assumptions

- **High:** RTE requires a minimum of 36 months for network upgrade completion after Phase 2 funding commitment is secured.
- **Medium:** The initial pre-paid hosting fee for Phase 1 (500MW) will accelerate the RTE planning process without influencing the longer-term 3 GW readiness timeline.

### SMART Validation Objective

Obtain formally documented range estimates (in months) for RTE transmission upgrade completion for 3 GW post-FID from the European Energy Regulation Specialist by 2026-11-01.

### Notes

- Focus on locking down the Phase 2 FID dependency rigorously against the validated power readiness timeline.


## 2. Land Holding Cost & Legal Structuring for Buffer Zones

Review Issue 2 highlighted that the holding cost for the 80% buffer is unbudgeted, posing a critical CAPEX risk (€1.3B+ overrun). This data is essential to integrate this strategic concession into the Phase 1 budget.

### Data to Collect

- Annual holding cost per hectare (EUR/ha/year) for non-buildable industrial/agricultural land in the Dunkirk/Cambrai zones (for 128.8 km²).
- Legal documentation requirements (e.g., specific deeds/clauses) for establishing a 30% 'Permanent Ecological Offset' under French law.
- Standard lease/easement costs for the 50% 'Expansion Reserve' area for an initial 18-month commitment period.

### Simulation Steps

- Use GIS/CAD software (managed by Land Modeler) to calculate the specific acreage breakdown for 32.2 km² buildable, 38.6 km² permanent offset, and 90.2 km² 18-month reserve.
- Model the cumulative 18-month holding cost based on interpolated local tax rates and maintenance estimates for 128.8 km².

### Expert Validation Steps

- Consult the French Land Use and Environmental Lawyer to validate the proposed legal structure for the 30% permanent offset and the viability/cost of the 18-month renewal option for the reserve area.
- Engage the Socio-Economic Impact Assessor to benchmark the proposed buffer holding costs against regional development incentive frameworks.

### Responsible Parties

- Large-Scale Land & Civil Works Model Modeler (IC)
- Financial Controller & Currency Risk Manager (FTE)

### Assumptions

- **High:** The modeled average holding cost per hectare is accurate within a 10% margin of the actual cadastral charges levied by local communes.
- **High:** A 30% permanent ecological offset is legally sufficient to preempt most land-use judicial challenges against the hyper-dense model.

### SMART Validation Objective

Formalize a binding 18-month operating budget line item for the 128.8 km² land holding costs, validated by the Land Use Lawyer, by 2026-09-01.

### Notes

- This directly addresses the critical financial risk associated with the hyper-dense land strategy.


## 3. DGSI/ANSSI Security Isolation Protocol Definition

Risk 5 highlights that failure to secure early security alignment jeopardizes access to premium sovereign revenues. Data collection must define the explicit boundary conditions for the initial commercial leasing (Decision 3, Choice 1).

### Data to Collect

- Formal document outlining DGSI/ANSSI requirements for physical and logical separation between non-classified commercial compute (Phase 1) and the future sovereign AI partition.
- Timeline (in months) for DGSI review of initial Proof-of-Concept security architecture for the 500 MW isolation.
- Definition of 'non-classified hardware' acceptable for immediate Phase 1 deployment.

### Simulation Steps

- N/A - This is primary regulatory documentation retrieval.
- Map the logical flow of substation capacity (Substation 1 isolation) against the DGSI security demarcation points within the BIM/Digital Twin model (managed by Chief Architect).

### Expert Validation Steps

- Consult the EU Sovereign AI & Cyber Security Policy Advisor to interpret the DGSI documentation and review the project's proposed physical isolation schematics for acceptance.
- Regulatory & Sovereignty Compliance Lead to arrange a formal Phase 0 architecture review meeting with DGSI.

### Responsible Parties

- Regulatory & Sovereignty Compliance Lead (FTE)
- Chief Infrastructure Strategist & Project Architect (FTE)

### Assumptions

- **Medium:** The DGSI/ANSSI review process for the initial 500 MW isolation concept can be completed within 10 months, concurrent with Phase 1 construction.
- **Medium:** The initial 500 MW hardware procurement (Risk 7) can be sourced without requiring specialized, nationally approved accelerators, allowing immediate revenue capture.

### SMART Validation Objective

Secure a written DGSI confirmation that the proposed physical segregation plan for Phase 1 (500 MW) meets the minimum standard required to *avoid* retrofitting when the sovereign zone is eventually built, by Q1 2027.

### Notes

- This is a high-stakes compliance gate that must inform tenant leasing terms.


## 4. Phase 1 Workforce Skill Uplift Velocity & Contractor Resistance

Review Issue 3 identified workforce optimism as a source of 6-12 month delays. Validating the realistic speed of skills development and contractor acceptance of the 75% mandate is necessary to accurately forecast Phase 1 completion date (Goal Statement constraint: 3 years).

### Data to Collect

- Average lead time (months) for local technical schools in Hauts-de-France to certify a new apprentice cohort capable of specialized construction work (e.g., piping for liquid cooling).
- Standard contract clauses used by EPC firms in the region regarding local hiring mandates (75% quota) and associated penalty/premium rates for compliance.
- Budgetary cost associated with importing specialized, non-local management/QC teams to oversee local training (Contingency budget input).

### Simulation Steps

- Modeling scheduling impact: Apply the estimated skill generation latency (if >6 months) to the Phase 1 construction schedule to quantify potential delay to 1 GW COD.
- Use cost modeling software to integrate premium/penalty costs from EPC resistance into the overall Phase 1 construction budget.

### Expert Validation Steps

- Consult the Socio-Economic Impact Assessor to confirm realistic velocity for local skills development and job integration.
- Consult the Program Director - Construction & Logistics (to be hired/assigned) to gauge typical EPC resistance levels to such strong local hiring mandates.
- Consult the Social License & Community Benefits Orchestrator regarding negotiated apprenticeship rates.

### Responsible Parties

- Social License & Community Benefits Orchestrator (IC)
- Chief Infrastructure Strategist & Project Architect (FTE)

### Assumptions

- **Medium:** The required 75% local hiring mandate will incur an average 5% premium on civil construction costs due to management overhead or contractor surcharge.
- **High:** Local technical schools can provide sufficient initial supervisors/trainers within 12 months to support the ramp-up.

### SMART Validation Objective

Establish a validated, 12-month phased local hiring roadmap, acceptable to contracted EPC partners (or resulting in finalized premium costs), by Q4 2026.

### Notes

- This data updates the strategic decision on workforce vs. speed trade-off.

## Summary

Immediate prioritization must focus on locking down the external timeline constraints that dictate Phase 1 feasibility and 9 GW optionality. The most critical data collection tasks are validating the RTE upgrade lead time (Data Item 1) and fully budgeting the land holding costs associated with the chosen 80% buffer strategy (Data Item 2), as these represent high-sensitivity, high-impact external dependencies impacting both schedule and CAPEX. Concurrently, the feasibility of large-scale local workforce integration must be quantified to manage schedule risk against social license requirements (Data Item 3). Actions should begin immediately by engaging the designated external experts (RTE/Land Use/Socio-Economic) to secure timeline assurances.

---
