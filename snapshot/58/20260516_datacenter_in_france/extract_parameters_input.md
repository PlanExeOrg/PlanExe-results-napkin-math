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

This section selects the 'The Builder: Pragmatic Scale-Up' scenario as the operational baseline for the 9 GW Hauts-de-France data center project, establishing a constrained, phased expansion contingent on validating external approvals and securing high-percentage tenant commitments before escalating capital expenditure into subsequent phases.

## Numeric values
- Estimated Phase 1 budget for 500 MW–1 GW: €5B–€10B — initial CapEx estimate.  [explicit | e=5 r=5 | quote: verified]
- Full 9 GW buildout cost estimate: €100B–€140B+ — maximum capital outlay estimate.  [explicit | e=5 r=5 | quote: verified]
- Phase 1 required anchor tenant commitment threshold: 30% – 50% of next expansion tranche — expansion gate trigger.  [explicit | e=5 r=5 | quote: verified]
- Total electric power target for full buildout: 9 GW — capacity ceiling for long-term model.  [explicit | e=5 r=5 | quote: verified]
- Phase 1 incremental power capacity range: 500 MW–1 GW — capacity ramp for short-term staging.  [explicit | e=5 r=4 | quote: verified]
- Projected power capacity target scale-up to Phase 2: 1 GW–3 GW — mid-term capacity milestone.  [explicit | e=5 r=4 | quote: verified]

## Load-bearing assumptions
- Project must pivot if Phase 1 power, land, water, and social license are not credible.  [explicit | e=5 r=5 | quote: verified]
- The chosen scenario rejects the contiguous 161 km² block in favor of distributed sites.  [explicit | e=5 r=5 | quote: verified]
- The plan must proceed skeptically, allowing for downsizing, splitting, or project cancellation.  [explicit | e=5 r=5 | quote: verified]
- Full 9 GW scale-up requires sustained demand, grid capacity, financing, and social license.  [explicit | e=5 r=4 | quote: verified]
- Expansion to Phase 2 is contingent upon meeting reliability, water, and community targets.  [explicit | e=5 r=4 | quote: verified]
- The plan assumes EUR is the primary currency impacting local costs and financing.  [explicit | e=5 r=4 | quote: verified]

## Gates and thresholds
- If credible commitments for power, land, and water are not secured, then do not proceed past Phase 0.  [explicit | e=5 r=5 | quote: verified]
- If anchor tenants commit less than 30% of the next tranche, then do not issue Final Decision to Invest for expansion.  [explicit | e=5 r=5 | quote: verified]
- If power reliability, PUE, water, and security targets are not met after Phase 1, then do not expand.  [explicit | e=5 r=4 | quote: verified]
- If national-security review is not clear by Phase 1 deadline, then project progress is halted.  [inferred | e=5 r=4 | quote: verified]
- If an RTS decision is not obtained for a single proven corridor, then the total capacity target is reduced to 3 GW.  [explicit | e=4 r=4 | quote: verified]
- If social license is not credible, then the project should not proceed past Phase 0.  [explicit | e=4 r=4 | quote: verified]

## Risks and shocks
- Grid overwhelming risk: failure of Hauts-de-France to host 9 GW without collapse — potential total project dependency failure.  [stress_test | e=4 r=5 | quote: verified]
- Land market failure risk: inability to assemble 161 km² — land assembly delay/cost overrun shock.  [stress_test | e=4 r=4 | quote: verified]
- Permitting process failure risk: environmental or municipal blockages leading to schedule overruns impacting viability.  [stress_test | e=4 r=4 | quote: verified]
- Grid upgrade cost overruns: unforeseen expenditure mandated by RTE/EDF beyond initial budget estimates.  [inferred | e=3 r=4 | quote: verified]
- Supply-chain security risk for hardware: failure to vet non-French GPUs/TPUs leading to security rejection shock.  [stress_test | e=3 r=4 | quote: verified]
- Sabotage or physical disruption impacting grid connection or fiber routes capacity.  [stress_test | e=3 r=4 | quote: verified]

## Missing data to estimate
- Percentage of total CAPEX allocated to USD-denominated GPU/TPU procurement — estimate capital exposure mix.  [missing | e=3 r=4 | quote: verified]
- Total land assembly budget required until commitment for the non-contiguous parcels — input for Phase 0/1 burn rate.  [missing | e=2 r=4 | quote: verified]
- Capital expenditure multiplier applied for substation construction per 1 GW of capacity — input for grid cost scaling.  [missing | e=2 r=4 | quote: verified]
- Average annual EUR/USD foreign exchange rate for hardware procurement — input for FX hedging model.  [missing | e=2 r=4 | quote: verified]
- Average annual cost per employee for French labor — input for workforce cost model.  [missing | e=2 r=3 | quote: verified]
- Unit cost for brownfield remediation per square hectare — input for environmental mitigation scaling.  [missing | e=2 r=3 | quote: verified]

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

---

# Premortem

This section outlines ten specific strategic decisions with quantified levers and trade-offs, providing the core potential failure modes for process simulation, and identifies nine specific, quantifiable assumptions whose failure triggers act as direct kill-switches for project viability or schedule adherence.

## Numeric values
- Campus target power capacity: 9 GW — absolute physical ceiling for sizing power/grid models  [explicit | e=5 r=5 | quote: verified]
- Total contiguous land parcel target: 161 km² — defines the scope of land assembly challenge  [explicit | e=5 r=5 | quote: verified]
- Phase 2 contracted capacity threshold: 3 GW — gates Phase 1 construction financing  [explicit | e=4 r=5 | quote: verified]
- Minimum take-or-pay commitment threshold for expansion gate: 60% — financial gate for Phase 2 FID  [explicit | e=4 r=5 | quote: verified]
- Projected maximum cost for 9 GW buildup: €100B — ceiling for total CAPEX exposure  [explicit | e=4 r=5 | quote: verified]
- Hyper-dense model buildable area limit: 30 km² — effective hard constraint on immediate physical build  [explicit | e=4 r=5 | quote: verified]

## Load-bearing assumptions
- Phase 1 builds on non-binding RTE consultation, deferring large grid CAPEX until Phase 2.  [explicit | e=5 r=5 | quote: verified]
- Phase 2 power expansion FID triggers contingent on 60% take-or-pay commitment achievement.  [explicit | e=4 r=5 | quote: verified]
- Buildable area constrained to 30 km² via hyper-dense model, sacrificing 80% of land for buffers.  [explicit | e=4 r=5 | quote: verified]
- Phase 1 target operational PUE ceiling must be maintained at 1.20 or less.  [explicit | e=4 r=4 | quote: verified]
- Initial 500 MW load remains commercial-only until sovereign security protocols are formally signed off.  [explicit | e=4 r=4 | quote: verified]
- Local workforce mandate requires 75% of non-specialized labor hours be filled by in-region apprentices.  [explicit | e=4 r=4 | quote: verified]

## Gates and thresholds
- If binding transmission allocation for Phase 2 (3 GW) is not secured prior to Phase 1 construction financing, then construction cadence is jeopardized.  [explicit | e=4 r=5 | quote: verified]
- If the take-or-pay commitment threshold for Phase 2 expansion is less than 60%, then speed is prioritized over lower syndicated debt rates.  [explicit | e=4 r=5 | quote: verified]
- If the buildable area is constrained below 30 km² long-term, then the 9 GW target cannot be met.  [explicit | e=4 r=5 | quote: verified]
- If a formal DGSI/ANSSI agreement is not signed before Phase 1 Power FID, then access to premium state revenue streams is jeopardized.  [explicit | e=4 r=5 | quote: verified]
- If initial commercial leasing acceptance is below 30% commitment for the next tranche, then expansion financing is at material risk.  [explicit | e=4 r=4 | quote: verified]
- If PUE exceeds 1.25 (a 0.05 miss from target), then anchor tenant contract compliance may be violated.  [derived | e=4 r=4 | quote: verified]

## Risks and shocks
- Failure to secure binding PPA risks stranding €1B–€2B Phase 0/1 capital if tenants withdraw.  [stress_test | e=4 r=5 | quote: verified]
- Premature 9 GW power commitment risks substantial sunk costs in grid studies and rights-of-way.  [stress_test | e=4 r=5 | quote: verified]
- If EUR depreciates >10% vs. USD, hardware costs inflate by €8B–€15B on the full 9 GW budget.  [stress_test | e=4 r=4 | quote: verified]
- If sovereign security review is a post-Phase 1 milestone, revenue is delayed due to extended clearance timeline.  [stress_test | e=4 r=4 | quote: verified]
- If land assembly forces single monolithic parcel, schedule delays up to multi-year litigation result.  [stress_test | e=4 r=4 | quote: verified]
- Proceeding expansion based on soft LOIs risks stranded fixed power capacity if anchor tenants retract.  [stress_test | e=4 r=4 | quote: verified]

## Missing data to estimate
- Total cost of Phase 1 CAPEX in EUR — needed to calculate the 15% threshold for land holding cost risk.  [missing | e=1 r=5 | quote: unverified]
- Duration in months/years for RTE transmission upgrade completion following collateral payment commitment — derived via expert consultation timeline.  [missing | e=1 r=5 | quote: unverified]
- Annual holding cost per hectare in EUR/ha/year for non-buildable industrial land in Hauts-de-France — derived via local tax benchmarking.  [missing | e=1 r=5 | quote: unverified]
- Minimum required IRR percentage for Heat Reuse off-take contracts to cover OpEx plus two percent margin — needed for Decision 6 viability.  [missing | e=1 r=4 | quote: unverified]
- Average monthly or annual cost per local apprentice/trainee in EUR for specialized skills uplift programs — needed to budget the 75% mandate premium.  [missing | e=1 r=4 | quote: unverified]
- Total guaranteed USD-denominated hardware procurement budget in USD — needed to calculate the full Eur/USD FX exposure impact.  [missing | e=1 r=4 | quote: unverified]

---

# Expert Criticism

This section identifies two quantitative modeling pitfalls: the lack of a specific land-use breakdown for the 161 km² footprint, making buffer/buildable area ratio uncertain, and an overly reliant power procurement strategy relying on non-binding commitments, which introduces indefinite major schedule slippages tied to RTE approvals. A third systemic risk flagged is the insufficient definition of community engagement, which translates directly into an unknown political risk multiplier on land assembly timelines.

## Numeric values
- Phase 1 expansion tenant commitment trigger threshold is 30% to 50% — financial gate for Phase 2 build readiness.  [explicit | e=5 r=5 | quote: verified]
- Full 9 GW buildout estimated cost is €100B–€140B+ — primary driver for total project NPV/ROI calculation.  [explicit | e=5 r=5 | quote: verified]
- Expansion commitment trigger threshold for Phase 2 is 60% take-or-pay — financial gate for next capacity tranche.  [explicit | e=5 r=5 | quote: verified]
- Full buildout power target is 9 GW — modelling driver for total power procurement duration.  [explicit | e=5 r=5 | quote: verified]
- Phase 1 minimum power capacity is 500 MW — input for initial stage CAPEX and revenue model.  [explicit | e=5 r=4 | quote: verified]
- Phase 0 feasibility budget minimum is €250M — initial sunk cost input for feasibility phase burn.  [explicit | e=5 r=4 | quote: verified]

## Load-bearing assumptions
- Phase 1 construction financing requires binding RTE allocation for Phase 2 (3 GW) beforehand.  [explicit | e=5 r=5 | quote: verified]
- Expansion to Phase 2 requires anchor tenants with financial take-or-pay for 60% of next tranche.  [explicit | e=5 r=5 | quote: verified]
- Phase 1 (500 MW) commercial load must operate without sovereign AI partition security clearance.  [explicit | e=5 r=5 | quote: verified]
- Phase 1 power connection for 500 MW is reliant only on a non-binding RTE consultation response.  [explicit | e=5 r=5 | quote: verified]
- The hyper-dense development model limits buildable area to 30 km² long-term.  [derived | e=4 r=5 | quote: verified]
- The contiguous 161 km² land assembly faces extreme political and litigation risk.  [inferred | e=5 r=4 | quote: verified]

## Gates and thresholds
- If anchor tenants have not signed capacity commitments for 30% to 50%, then Phase 2 expansion is blocked.  [explicit | e=5 r=5 | quote: verified]
- If Phase 1 power, land, water, permits, tenants, fiber, and social license are not credible, then proceed Phase 0 decision fails.  [explicit | e=5 r=5 | quote: verified]
- If Phase 2 expansion trigger requires 60% take-or-pay, then syndicated debt financing rates are lower.  [explicit | e=5 r=5 | quote: verified]
- If power reliability, PUE, water, security, and community targets are not met, then expansion is blocked.  [explicit | e=5 r=5 | quote: verified]
- If the required PUE target of 1.15 is not met, then this feeds into the technical performance measurement.  [explicit | e=5 r=4 | quote: verified]
- If a formal DGSI agreement is not signed before Phase 1 Power FID, then sovereign revenue streams are jeopardized.  [derived | e=4 r=5 | quote: verified]

## Risks and shocks
- RTE/Grid Confirmation Failure: Inability to secure binding 3 GW capacity allocation before Phase 1 construction FID.  [stress_test | e=3 r=5 | quote: verified]
- Technical Risk: Inability to maintain required PUE less than or equal to 1.20 during liquid cooling scale-up on brownfield sites.  [stress_test | e=4 r=4 | quote: verified]
- Financial Risk of Overrun: Budget overrun exceeding €1.3B due to uncosted holding expenses for permanent and reserve buffer land.  [stress_test | e=4 r=4 | quote: verified]
- Security Review Bottleneck: Protracted national security vetting delays access to premium sovereign revenue streams.  [stress_test | e=4 r=4 | quote: verified]
- Permitting Hold-Up: Legal review challenges the 80% land buffer model, stopping construction momentum post-Phase 1.  [stress_test | e=3 r=4 | quote: verified]
- Judicial challenges to fragmented land assembly could arrest construction momentum past Phase 1 success.  [stress_test | e=3 r=4 | quote: verified]

## Missing data to estimate
- Time duration in months (or years) required for RTE to complete 3 GW transmission upgrade construction following funding — needed to scale Phase 2 capacity.  [missing | e=1 r=5 | quote: unverified]
- Average annual EUR cost per hectare for holding 128.8 km² of non-buildable buffer land — needed for holding cost modeling.  [missing | e=1 r=4 | quote: unverified]
- Specific failure duration in weeks/months if major fiber backhaul route is disrupted — needed for continuity stress testing.  [missing | e=1 r=4 | quote: unverified]
- Specific revenue/kW/month generated by the premium sovereign AI partition once cleared by DGSI — needed to calculate premium revenue stream floor.  [missing | e=1 r=4 | quote: unverified]
- Cost per apprentice or FTE technician per month/year for the local workforce uplift program — needed to calculate training CapEx/OpEx.  [missing | e=1 r=3 | quote: unverified]
- The exact conversion factor required to translate EUR budget overruns into USD equivalent hardware cost increases — needed for FX risk sensitivity.  [missing | e=1 r=3 | quote: unverified]

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
