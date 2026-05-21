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
How do we mandate complex pan-European rail IT convergence while ensuring financial stability and operator buy-in? This plan establishes the core technical, financial, and governance foundations required to deliver seamless cross-border ticketing, moving from fragmented national systems to a unified, regulatory-compliant service capable of supporting significant modal shift.

## Purpose and Goals
The primary goals are achieving 40% single through-ticket adoption within five years, completing binding OSDM standardization within 18 months, and establishing a solvent clearing mechanism supported by a robust passenger rights backstop. Success is measured by these adoption/timeline metrics and a 50% reduction in distributor complaints.

## Key Deliverables and Outcomes
1. Finalized OSDM V1.0 specification with concurrently validated PRM accessibility schema (Month 18). 2. Fully capitalized Inter-Carrier Clearing Mechanism (initial €200M float secured). 3. Operationalized 'Three Strikes' enforcement template against primary operators (SNCF, DB, ÖBB). 4. Governance structure finalized, featuring an agile Fast-Track subcommittee for essential post-launch amendments.

## Timeline and Budget
Five-year execution window. Key technical milestone: Binding Standards achieved at Month 18; Full API Exposure at Month 30. Budget: €1.5 Billion coordination fund, with €900M allocated primarily to IT capacity building grants and €150M reserved for the Public Reference Distributor.

## Risks and Mitigations
High risks include Stakeholder Non-Compliance (mitigated by 'Three Strikes' enforcement and political de-escalation planning) and Unstable Data Layer (mitigated by aggressive T+5 latency testing and early adopter incentives). Financial solvency of the clearing mechanism is protected via transactional fees and a ring-fenced €300M Emergency Float Reserve.

## Audience Tailoring
The summary is tailored for senior regulatory and operational executives (DG MOVE, Agency for Railways, National Operator CTOs). The language is direct, policy-aware, and emphasizes decision synthesis, cross-dependencies, risk management, and alignment with the mandated 'Pragmatic Harmonization' strategy ('The Builder' scenario').

## Action Orientation
Immediate action is required to pivot the liability model (Decision 3) from strict tiered risk to a Collective Insurance Pool to align with the pragmatic pace. Simultaneously, grant formal authority to the Technical Steering Committee for rapid provisional amendments (Decision 10 modification) and prioritize functional conformance testing of PRM accessibility data mapping alongside core API load testing (T+5 validation).

## Overall Takeaway
The Pragmatic Harmonization strategy successfully balances ambitious regulatory requirements with operational realism by sequencing standardized technical delivery, sharing financial risk via collective pooling, and embedding agile governance, making the five-year 40% adoption goal highly achievable.

## Feedback
To increase persuasive impact, explicitly quantify the expected ROI of the 40% adoption target against the €1.5B investment. Strengthen the financial integrity by confirming the long-term sustainability model for the clearing mechanism post-initial float exhaustion (e.g., required transaction velocity). Detail the specific scope of the OSDM V2.0 contingency planning, as governance flexibility implies future unbudgeted CAPEX.

---

# Project Plan

**Goal Statement:** Deliver a coordinated European program making cross-border train travel as easy to search, book, and refund as national travel, achieving 40% of eligible cross-border journeys sold as single through-tickets within five years.

## SMART Criteria

- **Specific:** Establish the technical, commercial, and governance arrangements for compliant distributors to sell single through-tickets across all participating carriers with continuity-of-journey rights, single-payment settlement, and harmonized refunds.
- **Measurable:** Success will be measured by achieving 40% of cross-border journeys sold as single through-tickets, a 50% reduction in distributor complaints, and making the train the more attractive option than flying on competitive short-haul routes.
- **Achievable:** The goal is achievable through the strategic adoption of the 'Pragmatic Harmonization and Shared Burden' scenario, utilizing phased standardization, regulator-mandated data exposure (OSDM), and a structured €1.5 billion public coordination budget to bridge implementation gaps.
- **Relevant:** This is necessary to fulfill the EU Commission's proposed Regulation on Digital Booking and Ticketing Services for Rail, significantly improving consumer experience, ensuring passenger rights, and promoting modal shift away from air travel.
- **Time-bound:** Five years for the 40% adoption target; binding standards within eighteen months; mandatory API exposure within thirty months.

## Dependencies

- Establish common technical specifications (OSDM-compatible APIs) across all participating carriers.
- Define and agree upon non-discriminatory commercial terms for data access and API exposure.
- Establish and capitalize the inter-carrier clearing and settlement mechanism.
- Formalize the governance structure for standard adoption, amendment, and enforcement.
- Establish the liability framework and fund the passenger-rights backstop.

## Resources Required

- €1.5 billion public coordination budget (for standards work, testing, clearing fund, public reference distributor)
- Defined OSDM version 1.0 standard documentation
- Personnel capacity (35 FTEs for governance/standards/testing in the first two years)
- Legal and regulatory mandate from DG MOVE

## Related Goals

- Achieve timely harmonization of reduction card recognition.
- Ensure full accessibility mandates (PRM booking) are integrated into the V1.0 standard.
- Integrate provisional API hooks for buses, ferries, and short-haul air (post five-year target).

## Tags

- Rail
- Ticketing
- Interoperability
- OSDM
- Passenger Rights
- EU Regulation
- Digitalization

## Risk Assessment and Mitigation Strategies


### Key Risks

- Political resistance or insufficient legal enforcement from state operators delaying standard compliance past deadlines.
- Integration challenges causing unstable OSDM-compatible real-time data layer (latency, semantic errors).
- Under-capitalization or low liquidity in the clearing/settlement mechanism due to slow initial transactional velocity.
- National operators prioritizing core API compliance over harmonizing mandatory ancillary services (Accessibility/Reduction Cards).
- Slow governance structure preventing timely technical pivots post-launch.

### Diverse Risks

- Coordinated lobbying by major incumbent operators to weaken the tiered liability framework.
- Over-ambitious scope creep via early integration of non-core transport modes.
- Distributors failing to rapidly adopt the new system due to perceived friction, jeopardizing the 40% sales goal.
- Inflation of IT operational costs by carriers to justify higher cost-recovery royalties for data access.

### Mitigation Plans

- Implement a clear 'three strikes' enforcement posture, leading to suspension of through-ticketing sales for non-compliant carriers (SNCF, DB, ÖBB targeted first).
- Apply early incentives (funding grants) tied to achieving high uptime (90%+) on test systems for the shared data layer.
- Implement a transactional fee model for clearing capitalization, backed by a ring-fenced €300 million 'Emergency Float Reserve' available if the operational float drops below 150% of peak daily obligation.
- Require functional conformance testing for Accessibility Reservation data schemas to complete concurrently with core API finalization at month 18, despite the longer service rollout grace period.
- Empower the Technical Steering Committee with an emergency review mandate (65% consensus) for the first twelve months post-launch to issue provisional operational directives for immediate change.

## Stakeholder Analysis


### Primary Stakeholders

- DG MOVE (European Commission Directorate-General for Mobility and Transport)
- EU Agency for Railways (Technical oversight, testing coordination)
- National Rail Operators (SNCF, DB, Trenitalia, Renfe, ÖBB, NS, SJ, etc. - IT providers and commercial entities)
- Independent Distributors (e.g., Trainline, Omio - API consumers)

### Secondary Stakeholders

- CER (Community of European Railways - Industry representative)
- BEUC (European Consumer Organisation)
- National Regulatory Bodies
- Disability Rights Bodies / Consumer Groups

### Engagement Strategies

- DG MOVE/Agency for Railways: Provide weekly progress reports focused on governance adoption and adherence to binding standard timelines.
- National Rail Operators (Primary): Engage via structured workshops for OSDM specification finalization; enforce commercial terms (cost recovery) via annual audited reporting; apply enforcement posture decisively.
- Independent Distributors: Conduct monthly technical feedback sessions focusing on API stability and commercial cost structures (Decision 2).
- BEUC/Disability Groups: Hold mandated quarterly review sessions specifically on the 90-minute continuity threshold and accessibility integration progress (Decision 9/13).

## Regulatory and Compliance Requirements


### Permits and Licenses

- Authorization for management of centralized financial clearing/settlement mechanism float
- Legal basis for enforcing data sharing requirements on sovereign entities

### Compliance Standards

- Alignment with proposed EU Regulation on Digital Booking and Ticketing Services for Rail
- OSDM technical standard adherence (binding timeline at 18 months)
- Compliance with all EU passenger rights regulations (T+90 min threshold defines activation)
- Non-discriminatory commercial terms for API access

### Regulatory Bodies

- European Commission (DG MOVE)
- EU Agency for Railways
- National Competent Authorities (National Regulators)

### Compliance Actions

- Draft legal framework mandating OSDM API exposure (T+30 months deadline).
- Schedule external conformance testing audits based on phased standardization progress (provisional binding at 6 months).
- Implement compliance plan for accessibility standardization by incorporating PRM data schema validation into the core binding standard sign-off process.
- Obtain DG MOVE legal pre-approval for the 'Three Strikes' enforcement template.

---

# Selected Scenario

This section commits the project to 'The Builder: Pragmatic Harmonization and Shared Burden' scenario, defining the specific operational parameters selected for the five-year implementation plan, including phased standardization timelines, structured liability models, and cost-recovery mechanisms for data access.

## Numeric values
- Public coordination budget total: €1.5 billion — total expenditure input for public activities.  [explicit | e=5 r=5 | quote: verified]
- Cross-border journeys sold as single through-tickets target proportion: 40% within five years — primary success metric.  [explicit | e=5 r=5 | quote: verified]
- Project horizon duration: five years — defines total modelling time frame.  [explicit | e=5 r=5 | quote: verified]
- Binding standards to be finalized target date: six months after start date — gate for technical specification finality.  [explicit | e=4 r=4 | quote: verified]
- Full corridor through-ticketing target by: sixty months after start date — project completion KPI.  [explicit | e=4 r=4 | quote: verified]
- Mandatory API exposure target date: thirty months after start date — operational readiness milestone.  [explicit | e=4 r=4 | quote: verified]

## Load-bearing assumptions
- The plan assumes successful alignment with the European Commission's proposed Regulation on Digital Booking and Ticketing Services for Rail.  [explicit | e=5 r=5 | quote: verified]
- The plan assumes the chosen scenario avoids the aggressively risky path in favor of realism.  [explicit | e=5 r=5 | quote: verified]
- The plan assumes initial rollout will cover the four specific busiest cross-border corridors.  [explicit | e=5 r=4 | quote: verified]
- The plan implicitly assumes continuity-of-journey rights protection will be legally enforceable across all journey segments.  [explicit | e=4 r=5 | quote: verified]
- The success metric requires that the train becomes the more attractive option than flying on competitive short-haul routes.  [explicit | e=5 r=4 | quote: verified]
- The plan assumes the technical, commercial, and governance arrangements will be stood up within five years.  [explicit | e=4 r=4 | quote: verified]

## Gates and thresholds
- If the single through-ticket sales target is not met by five years, then the fundamental project goal is missed.  [explicit | e=5 r=5 | quote: verified]
- If the cross-border rail modal shift goal is not met by five years, then the project's success criteria fail.  [explicit | e=4 r=5 | quote: verified]
- If technical specifications do not achieve provisional binding status by six months, then the subsequent eighteen-month finalization is jeopardized.  [explicit | e=4 r=4 | quote: verified]
- If formal binding status for core OSDM standards is not achieved by eighteen months, then disruption rights harmonization is delayed.  [explicit | e=4 r=4 | quote: verified]
- If the initial set of corridors do not demonstrate operational stability by eighteen months, then standardized specifications are not finalized.  [explicit | e=4 r=4 | quote: verified]
- If API access fees are not strictly cost-recovery, then the regulator must intervene to enforce compliance.  [explicit | e=4 r=4 | quote: verified]

## Risks and shocks
- Inconsistent access to real-time inventory from national operators: hinders ability of distributors to sell through-tickets reliably.  [inferred | e=4 r=4 | quote: verified]
- Failure to establish harmonized refunds: results in passenger rights protection loss upon missed connections.  [inferred | e=4 r=4 | quote: verified]
- Rejection of OSDM-compatible APIs due to non-discriminatory commercial terms: delays data layer rollout significantly.  [inferred | e=4 r=4 | quote: verified]
- Failure to properly capitalize the passenger-rights backstop: strains solvency when systemic failures occur.  [inferred | e=4 r=4 | quote: verified]
- Moral hazard from pooled insurance: reliable national carriers overpay disproportionately for systemic failures of poorly managed operators.  [inferred | e=4 r=4 | quote: verified]
- Front-loading liability risk on the initial distributor: discourages innovative third-party platforms from entering the market.  [stress_test | e=4 r=4 | quote: verified]

## Missing data to estimate
- Private carrier IT investment total amount — to be estimated separately from public budget.  [missing | e=5 r=5 | quote: verified]
- Total volume of cross-border journeys sold annually — needed to calculate revenue implications of the 40% target.  [missing | e=4 r=5 | quote: verified]
- Cost-recovery percentage used to calculate API access fees — needed to convert transaction volume into carrier revenue.  [missing | e=4 r=4 | quote: verified]
- Average monthly cost per carrier participating in the inter-carrier clearing mechanism — needed to total the transactional fee model.  [missing | e=4 r=4 | quote: verified]
- Total number of competitive short-haul routes where air travel is substitutable for rail — needed to scale modal shift assumptions.  [missing | e=4 r=4 | quote: verified]
- Average revenue loss per distributor complaint resolved late — needed to quantify impact of halved complaint metric.  [missing | e=4 r=3 | quote: verified]

---

# Assumptions

# Purpose
# Coordinated European cross-border rail booking and ticketing infrastructure

## Purpose

- Developing and implementing a unified technical, commercial, and governance framework for seamless cross-border train travel across the EU.
- Improving market efficiency, passenger rights, and modal shift from air travel.
- Creating shared APIs, clearing mechanisms, and standardization aligned with EU regulation.


# Domain
# Project Structure Summary

## Primary Domains

- Financial Clearing Mechanisms

## Secondary Domains

- Digital Transport Regulation
- Rail Infrastructure Management
- Interoperability Standards

## Rationale
Financial Clearing Mechanisms is primary (single-payment settlement success). Financial Settlement Systems is secondary but related. Digital Transport Regulation and Interoperability Standards are foundational constraints/methods.

## Involved Disciplines

### Core (Outcome/Method/Constraint)

- Digital Transport Regulation (5/5): Constraint, aligned with proposed EU Regulation on Digital Booking.
- Interoperability Standards (5/5): Method, requires OSDM-compatible APIs and binding standards.
- Financial Clearing Mechanisms (5/5): Outcome, establishing inter-carrier clearing/settlement.
- Digital Distribution Systems (5/5): Method, building shared OSDM-compatible APIs.

### Supporting (Stakeholder/Method/Outcome)

- Rail Infrastructure Management (4/4): Stakeholder, National rail operators/infrastructure bodies.
- Passenger Rights Advocacy (4/4): Stakeholder, Disability rights/consumer groups.
- IT System Integration (4/4): Method, relies on unified APIs and system integration.
- Financial Settlement Systems (4/4): Outcome, single-payment inter-carrier clearing/settlement.
- European Union Law (4/3): Constraint, alignment with proposed EU Regulation on Digital Booking.


# Plan Type
# Project Planning Summary

## Execution Requirement

- Requires one or more physical locations.
- Cannot be executed digitally.

## Execution Justification

- Develop and implement multi-year program: shared technical standards (OSDM-compatible APIs), governance, and new financial clearing mechanisms across European countries.
- Requires extensive physical collaboration: stakeholders (DG MOVE, EU Agency for Railways, national operators, regulators) in physical meetings, workshops, and governance bodies.
- Necessary activities: define standards, perform conformance testing, manage rollout.
- Success relies on physical integration into real-world operator IT systems and testing end-to-end process (purchasing, journey execution, refunds).
- Inherently a physical process involving rail networks and passengers.
- Budget allocation and capacity building imply physical coordination.
- Plan is overwhelmingly physical due to implementation, governance, and real-world system integration.


# Physical Locations
# Requirements for physical locations

- Proximity to major EU institutions (DG MOVE, EU Agency for Railways)
- Facilities for high-level governance meetings and standards workshops
- Access to central European transport hubs for corridor testing coordination

## Location 1

- Belgium, Brussels (European Quarter/Near EU Institutions)
- Rationale: Ideal administrative/coordination hub for standards-setting/governance due to host of EC (DG MOVE) and proximity to initial launch corridor (Paris–Brussels–Amsterdam–Köln).

## Location 2

- France/Germany/Benelux (Paris–Brussels–Amsterdam–Köln Corridor Region)
- Testing facilities within central cluster areas (e.g., Lille, Frankfurt, or Rotterdam)
- Rationale: Critical for initial conformance testing and resolving early technical issues proximal to operators/infrastructure in the very first corridor slated for roll-out.

## Location 3

- Austria/Germany/Switzerland (Wien–München–Zürich Corridor Region)
- Munich or Vienna (as central connection points)
- Rationale: To facilitate parallel coordination/testing for the second primary corridor; a central base allows engagement with ÖBB, DB, and Swiss partners without diverting focus from Brussels.

## Location Summary
Physical locations must serve administrative coordination and initial corridor testing due to the multi-national nature of the program. Brussels is essential for EU body engagement. Additional locations are near the two highest-priority initial corridors (Paris-Amsterdam-Cologne and Vienna-Munich-Zurich) to facilitate on-the-ground testing and localized operational alignment.

# Currency Strategy
## Currencies

- EUR: Primary currency for EU-centered project.

- Primary currency: EUR
- Currency strategy: Budget in EUR. Local expenditures reconciled to EUR using standard FX procedures; no complex hedging assumed.


# Identify Risks
## Risk 1 - Regulatory & Permitting

- Political resistance or insufficient legal enforcement from rail operators/states leads to non-compliance with data/ticketing standards by deadlines.
- Impact: Invalidates 'continuity-of-journey' for large segments, 6–12 month delay on key routes, jeopardizes 40% through-ticket target.
- Likelihood: Medium, Severity: High
- Action: Maintain strong Enforcement Posture (Decision 12) via EU Agency for Railways mandatory pre-launch audits. Ensure linkage between standard adherence and clearing/settlement access is legally unambiguous.

## Risk 2 - Technical

- Integration challenges causing unstable OSDM-compatible real-time data layer (quality, latency, semantic mismatches).
- Impact: Distributors sell inaccurate tickets, high failed bookings/complaints (target requires halving), trust erosion. 2–3 month delay in commercial rollout on initial four corridors.
- Likelihood: High, Severity: High
- Action: Aggressively apply early incentives (Decision 6) for high data uptime. Use Public Reference Distributor (Decision 11) as validation sandbox to stress-test data transmission.

## Risk 3 - Financial

- Under-capitalization/insufficient liquidity in clearing/settlement due to the Builder transactional fee model, causing settlement delays/disputes.
- Impact: Stalls single-payment settlement, forces EU budget to cover float gaps (€50–€200 million in working capital support).
- Likelihood: Medium, Severity: Medium
- Action: Monitor rolling reserve fund balance (Decision 5). If below safety buffer, trigger swift request for temporary capitalization or mandate higher bank guarantees.

## Risk 4 - Supply Chain / Integration

- National operators prioritize mandatory API deadline (30 months) over harmonizing post-sale/ancillary services (accessibility, bicycle rules).
- Impact: Basic ticketing launches, but failure to integrate accessibility (Decision 9) or reduction cards (Decision 8) limits modal shift gain by 10–15% and causes regulatory non-compliance on equity grounds.
- Likelihood: High, Severity: Medium
- Action: Use phased standardization approach (Decision 4). Allocate mandatory conformance testing for accessibility data (Decision 9) immediately post-standards, ensuring parallel development with core APIs.

## Risk 5 - Operational/Governance

- Overly complex governance structure for OSDM amendment prevents rapid response to unforeseen bugs or refinements post-launch.
- Impact: Security patches or functional improvements take 6–9 months via dual-approval, leading to prolonged vulnerabilities (e.g., buggy refunds).
- Likelihood: Medium, Severity: Medium
- Action: Empower technical steering committee with expedited authority to issue 'clarification notices' for immediate implementation pending formal ratification (Decision 10).

## Risk 6 - Social / Stakeholder Management

- Operators resist defined liability framework (Decision 3), lobbying to weaken the Passenger Rights Backstop.
- Impact: Backstop failure (liability pushed to distributor/passenger) threatens reduced consumer complaints goal and 40% adoption target.
- Likelihood: Medium, Severity: High
- Action: Frame tiered liability (Decision 3) as necessary risk pooling supported by data transparency. Provide early actuarial modeling showing pooled risk is lower than unmanaged individual risk.

## Risk 7 - Market / Competition

- Distributors fail to rapidly adopt new system, preferring legacy methods, jeopardizing the 40% single through-tickets goal (5-year target).
- Impact: Economic justification for €1.5B investment diminishes. 20% adoption misses operational success metric.
- Likelihood: Medium, Severity: High
- Action: Aggressively implement Decision 2 (Capped Royalty Structure) to ensure fair commercial terms maximize distributor incentive for cross-border sales.

## Risk 8 - Environmental/Scope Creep

- Overly ambitious integration of non-core modes (buses, ferries) too early, diverting resources from stabilizing core rail ticketing.
- Impact: Core objective (corridor through-ticketing) delayed by 9–12 months due to engineering complexity spillover.
- Likelihood: Low, Severity: Medium
- Action: Adhere strictly to Decision 7: De-scope non-core integrations from Phase 1 (first 60 months). Focus on rail-to-rail OSDM compliance.

## Risk summary
Project faces high inherent risks due to regulatory mandate, multi-stakeholder complexity (20+ carriers), and dependency on novel OSDM APIs. Primary existential threats are Stakeholder Non-Compliance (Regulatory) and Shared Data Layer Instability (Technical). Political resistance endangers the project if enforcement is weak, while unreliable data functional failure. Mitigations rely on tight deadlines, phased implementation (Decision 4), and financial incentives (Decision 6). Builder scenario acceptance heightens need for technical validation to manage liability disputes.

# Make Assumptions
## Question 1 - Capitalization and Settlement Duration

- Initial capitalization requirement (float): €200 million.
- Acceptable settlement reconciliation duration: T+3 (99% of transactions).

Assumptions:

- Initial float set at €200 million based on busiest corridors.
- T+3 standard assumed manageable for 99% of transactions.

Assessments:

- Title: Financial Mechanism Viability Assessment
- Monitioring float (€200M) is necessary under transactional fee model.
- Risk: Low velocity depletes float, requiring public top-up (Risk 3).
- Opportunity: T+3 aligns with B2B standards, boosting carrier confidence.
- Mitigation: Weekly monitoring trigger on reserve fund balance.

## Question 2 - Standardization Grace Period

- Mandated grace period for legacy systems (reduction cards/accessibility booking): Additional 12 months (Total 30 months from start) after core APIs stabilize at 18 months.

Assumptions:

- Phased standardization: Core APIs stable by month 18 (final binding).
- Ancillary services (Accessibility/Reduction Cards) get an additional 12 months grace (30 months total mandate).

Assessments:

- Title: Harmonization Implementation Timeline Assessment
- Deferring complex features to month 30 provides necessary time for national operators (Risk 4 mitigation).
- Benefit: Prevents immediate overload jeopardizing core OSDM stability (month 18).
- Risk: Delaying accessibility risks early regulatory challenges on equity.

## Question 3 - API Data Access Audit Mechanism

- Mechanism: Annual audit via balance sheets focusing on IT operational costs attributable to OSDM data maintenance.
- Metric: Cost-recovery royalty rate capped at 5% of maintenance expenditure for the API endpoint.

Assumptions:

- Verification via annual audited balance sheets for IT operational costs.
- Standard cost-recovery royalty capped at 5% of required OSDM endpoint maintenance expenditure.

Assessments:

- Title: Commercial Governance Effectiveness Assessment
- Capped royalties necessitate robust audit capability (Decision 2).
- Risk: Operators inflating indirect IT costs, requiring strong regulatory challenge.
- Opportunity: Fair pricing lowers entry barriers for distributors (Risk 7), supporting 40% sales target.

## Question 4 - Primary Participants for Initial Audit Cycle

- Primary participants for first thirty-month audit cycle concerning 'Enforcement Posture': SNCF, Deutsche Bahn (DB), and ÖBB.

Assumptions:

- Mandated participants are SNCF, DB, and ÖBB due to centrality in two highest-volume initial corridors.
- Enforcement actions applied first to these three.

Assessments:

- Title: Regulatory Compliance Risk Management
- Focusing initial high-stakes enforcement (Risk 1) on these three is pragmatic.
- Benefit: Early success sets a strong operational precedent.
- Risk: Strong resistance from major players could trigger political friction.

## Question 5 - Public Funding Allocation

- Capacity building allocation: 60% (€900M) of €1.5B budget for IT grants/testing support.
- Ring-fenced percentage for the public reference distributor: 10% (€150M) for establishment and initial five-year running costs (Decision 11).

Assumptions:

- 60% (€900M) allocated to capacity building (IT grants/testing).
- 10% (€150M) reserved for the reference distributor (Decision 11).

Assessments:

- Title: Budget Allocation and Sustainable Operations Assessment
- Allocating 60% for grants mitigates resource strain (Risk 4).
- Fixed cost base from 10% reservation for reference distributor must be managed against usage fees.

## Question 6 - Real-Time Disruption Data Integration

- Operational Plan: Mandatory real-time latency benchmark required.
- Latency Benchmark: T+5 minutes (from event occurrence to API availability).

Assumptions:

- Mandatory real-time latency benchmark of T+5 minutes established via provisional binding standards (Decision 4, Month 6).
- T+5 is essential for automatically triggering passenger rights backstop (Decision 13).

Assessments:

- Title: Operational Data Interoperability Assessment
- T+5 latency benchmark forces high operational standards (Risk 2 mitigation).
- Benefit: Clear thresholds (Decision 13) enable automated backstop activation.
- Risk: Older infrastructure carriers might struggle with T+5, increasing enforcement pressure (Decision 12).

## Question 7 - Governance Body Staffing Plan

- Staffing Plan (First two years): 35 FTEs.

    - Standards management: 10 FTEs.
    - Conformance testing coordination: 15 FTEs (focused on physical locations).
    - Stakeholder relations: 10 FTEs.

Assumptions:

- Total required FTEs: 35 (Standards: 10, Testing Coordination: 15, Relations: 10).
- Testing coordination heavily focused on identified physical locations.

Assessments:

- Title: Resource Deployment and Physical Coordination Assessment
- Deploying 15 FTEs to testing coordination across physical locations is critical for resolving integration technical risks (Risk 2).
- Staffing 35 FTEs requires immediate operational budget allocation, separate from IT grants.

## Question 8 - Governance Structure for Rapid Adjustments

- Mechanism for rapid adjustments: Emergency review mandate granted to the Technical Steering Committee for the first twelve months post-launch (Decision 10).
- Amendment Process: Allows immediate enactment of 'provisional operational directives' via 65% consensus, requiring later final ratification.

Assumptions:

- Governance Structure (Decision 10) grants emergency review power to the Technical Steering Committee for 12 months post-launch.
- Amendments require only 65% consensus for provisional directives.

Assessments:

- Title: Governance Agility and Risk Tolerance Assessment
- Emergency override mitigates Risk 5 (slow amendments) and allows rapid adaptation to issues with liability (Decision 3) or data access (Decision 2).
- Benefit: Balances stability with necessary agility.


# Distill Assumptions
# Project Planning Summary

## Financial Allocations & Funding

- Initial clearing mechanism float: €200 million.
- Capacity building grants: €900M (60% of €1.5B) for national operators.
- Public reference distributor running costs: 10% (€150M) of €1.5B fund.
- Initial capitalization financed via transactional fee collateral.
- API access royalties capped at 5% of attributable IT O&M expenditure; strictly cost-recovery, regulator overseen.

## Governance & Standards

- Central governance body requires 35 dedicated FTEs for the first two years.
- Governing structure allows 65% consensus for emergency amendments for the first twelve months post-launch.
- Technical specifications achieve provisional binding status within six months.
- Core OSDM data exchange standards mandate formal binding status within eighteen months.
- Provisional binding status required at six months, finalization at eighteen months.

## Operational Assumptions & Benchmarks

- Settlement reconciliation delays assumed manageable within T+3 for 99% of transactions.
- Mandatory real-time latency benchmark (T+5 minutes) established at month 6.
- Full harmonization of accessibility and reduction cards granted a 30-month grace period.

## Enforcement & Liability

- Primary participants for initial audit: SNCF, DB, and ÖBB.
- Enforcement posture: 'three strikes' rule leading to suspension of through-ticketing sales.
- Tiered liability: segment carrier fully responsible for compensation costs unless negligence is proven.
- Initial operators bear 100% compensation costs unless gross distributor negligence is proven.
- Backstop protection activates only for connections cancelled or delayed/missed exceeding 90 minutes.
- EU backstop limits compensation to connecting failures between the first and last known segment failures.


# Review Assumptions
# Domain of the expert reviewer
Multi-Jurisdictional Project Governance and Infrastructure Integration

## Domain-specific considerations

- Regulatory Harmonization Across Sovereign Entities
- Financial Clearing Mechanism Solvency
- IT Standards Adoption (OSDM) Across Legacy Systems
- Commercial Non-Discrimination and Cost Recovery
- Critical Path Dependencies (Data Layer before Clearing/Ticketing)

## Issue 1 - Unrealistic Grace Period for Ancillary Harmonization (Accessibility/Loyalty)
The 30-month grace period for ancillary systems (Accessibility/Loyalty) conflicts with the 18-month mandate for core ticketing APIs. Accessibility (Decision 9) is a non-negotiable equity requirement; delay risks non-compliance and undermines modal shift goals.

Recommendation: Adjust governance (Decision 10) to require functional conformance testing for Accessibility Reservations (Decision 9) completion *before* core ticketing APIs reach final binding status at month 18. Provisional binding at month 6 must require PRM data schema finalization.

Sensitivity: Delaying accessibility past Month 24 risks regulatory fines (3-7% operational budget annually), reducing ROI by 8-12% (brand damage/legal costs).

## Issue 2 - Insufficient Contingency for Clearing Mechanism Float Depletion
The plan relies on a provisional €200M float financed by transactional collateral (Decision 5, Builder Scenario), settling at T+3. Low initial velocity risks insufficient collateral to cover peak risk or liquidity gaps before the reserve fund capitalizes, jeopardizing the financial backbone.

Recommendation: Ring-fence 20% of the €1.5B coordination budget (€300M total) as an 'Emergency Float Reserve' for the clearing mechanism, accessible if T+3 fails for 48 hours or collateral drops below 150% of peak daily obligation.

Sensitivity: If the initial €200M float requires a public €50M injection, CapEx increases by 3.3% (€50M / €1.5B), reducing ROI by 2-4 points via overhead.

## Issue 3 - Lack of Assumption on Key Operator Behavioral Response to Enforcement
Success hinges on aggressive Enforcement Posture (Decision 12—'three strikes' suspension) against major operators (SNCF, DB, ÖBB). No mitigation is planned for political fallout or coordinated resistance if majors lobby to weaken governance (Decision 10) or delay compliance past 18 months.

Recommendation: Develop a 'Political De-escalation' plan prioritized over technical mitigation. Pre-negotiate short-term (90-day) technical assistance packages funded by the capacity budget (€900M) for the first operator facing the third strike, maintaining the threat of exclusion.

Sensitivity: If lobbying causes a 6-month delay in enforcing posture against the top 3 operators, technical integration risk (Risk 2) rises, likely causing a 4-6 month delay in achieving 40% through-ticket sales (15-20% Year 2 revenue shortfall).

## Review conclusion
The plan shows excessive optimism regarding ancillary system alignment and clearing mechanism self-sufficiency. Critical missing factors involve managing regulatory pushback on enforcement, securing day-one clearing mechanism stability, and resolving accessibility integration without early regulatory risk. Immediate focus must be on contingency funding for clearing and integrating accessibility compliance testing into the core standard ratification timeline.

---

# Review Plan

This section specifies the quantitative gates, validated assumptions, and critical numeric targets—such as KPI deadlines, minimum uptime percentages, specific monetary thresholds for financial reserves, required personnel counts, and targeted enforcement participants—that serve as direct inputs for stress testing, scenario analysis, and defining model failure conditions for the project plan.

## Numeric values
- Emergency Float Reserve ring-fenced budget: €300 million — capacity ceiling for financial shock absorption  [explicit | e=4 r=5 | quote: verified]
- Initial clearing mechanism float requirement: €200 million — requirement for initial liquidity buffer  [inferred | e=4 r=5 | quote: verified]
- Real-time disruption data latency benchmark: T+5 minutes — gates automated rights trigger functionality  [explicit | e=4 r=5 | quote: verified]
- Minimum required adoption rate for target success: 40% of eligible cross-border journeys within five years — primary success metric driver for ROI  [explicit | e=4 r=5 | quote: verified]
- Provisional binding status target for technical specifications: six months — gates initial technical commitment speed  [explicit | e=4 r=5 | quote: verified]
- Final binding status target for standards: eighteen months — gates core architectural stability  [explicit | e=4 r=5 | quote: verified]

## Load-bearing assumptions
- Functional conformance testing for Accessibility Reservations must complete before core APIs reach final binding status.  [inferred | e=5 r=5 | quote: verified]
- The T+3 settlement reconciliation duration is assumed achievable for ninety-nine percent of transactions.  [explicit | e=4 r=5 | quote: verified]
- The technical feasibility of the T+5 minute latency benchmark must be achievable with existing infrastructure and support funding.  [explicit | e=4 r=5 | quote: verified]
- The liability framework decision must be pivoted from strict tiered liability to collective insurance pooling.  [stress_test | e=4 r=5 | quote: verified]
- The Builder scenario is aligned with the requirement for a realistic path, not the most aggressive one.  [explicit | e=5 r=4 | quote: verified]
- The core objective relies on successfully integrating PRM data requirements into the binding standard by the deadline.  [explicit | e=4 r=5 | quote: verified]

## Gates and thresholds
- If a carrier commits three documented, non-remediated API failures within a quarter, then ticket sales are suspended.  [explicit | e=5 r=5 | quote: verified]
- If a transaction's liquidity drops below one hundred fifty percent of peak daily obligation, then the Emergency Float Reserve is assessed.  [explicit | e=4 r=5 | quote: verified]
- If a journey segment failure results in a delay exceeding ninety minutes, then integrated passenger rights protections must activate.  [explicit | e=4 r=5 | quote: verified]
- If the formal binding status for core standards is not secured by eighteen months, then technical development pace is jeopardized.  [explicit | e=4 r=5 | quote: verified]
- If API uptime demonstration is below 90% on test systems, then the operator does not receive disproportionately larger funding allocations.  [explicit | e=4 r=4 | quote: verified]
- If OSDM API uptime by compliant carriers is below 95% on core routes, then distributors may give twelve months priority window to others.  [explicit | e=4 r=4 | quote: verified]

## Risks and shocks
- Political resistance or insufficient legal enforcement from state operators leads to 6 to 12 month delay on key routes.  [stress_test | e=4 r=5 | quote: verified]
- Integration challenges causing unstable OSDM data layer leads to 2 to 3 month delay in commercial rollout.  [stress_test | e=4 r=5 | quote: verified]
- Under-capitalization in the clearing mechanism could force EU budget to cover float gaps of €50 to €200 million in working capital support.  [stress_test | e=4 r=5 | quote: verified]
- Lobbying successfully weakens the liability framework, threatening reduced consumer complaints goal and leading to 15 to 20 percent Year 2 revenue shortfall.  [stress_test | e=4 r=5 | quote: verified]
- Failure to harmonize ancillary services limits modal shift gain by 10 to 15 percent.  [stress_test | e=4 r=4 | quote: verified]
- Overly complex governance structure causes security patches or functional improvements to take 6 to 9 months.  [stress_test | e=4 r=4 | quote: verified]

## Missing data to estimate
- Total eligible cross-border journeys per year — needed to calculate 40% adoption target  [missing | e=1 r=5 | quote: unverified]
- Average monthly revenue exposure interrupted by a ninety-minute delay event — needed to size the backstop liability impact  [missing | e=1 r=5 | quote: unverified]
- Total duration in months the clearing mechanism requires capitalization before transactional fees balance the float — needed for liquidity modelling  [missing | e=1 r=5 | quote: unverified]
- Average operational cost to maintain one OSDM-compatible API endpoint per month — needed for cost-recovery royalty model scaling  [missing | e=1 r=4 | quote: unverified]
- Cost per FTE per month for governance body staff — needed to calculate total fixed overhead burn rate  [missing | e=1 r=4 | quote: unverified]
- Base daily transaction rate across all four initial corridors — needed to calculate collateral requirements  [missing | e=1 r=4 | quote: unverified]

---

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

---

# Expert Criticism

Expert criticism identifies critical inconsistencies between the chosen pragmatic mitigation scenario and the selected strategic options, specifically highlighting that pairing aggressive enforcement with strict, high-carrier-liability models will cause political deadlock, and that failing to immediately bind mandatory accessibility data schemas into the provisional standard creates a major regulatory risk deadline that the current pacing strategy ignores.

## Numeric values
- Emergency Float Reserve allocation amount is €300 million — contingency funding for clearing mechanism  [explicit | e=5 r=5 | quote: verified]
- Cross-border journeys sold as single through-tickets target 40% within five years — metric for five-year success  [explicit | e=5 r=5 | quote: verified]
- Public coordination budget total amount is €1.5 billion — total initial expenditure cap  [explicit | e=5 r=5 | quote: verified]
- Binding standards achieved within eighteen months from start date — target date milestone  [explicit | e=5 r=5 | quote: verified]
- Mandatory API exposure achieved within thirty months from start date — target date milestone  [explicit | e=5 r=5 | quote: verified]
- Full corridor through-ticketing achieved within sixty months from start date — target date milestone  [explicit | e=5 r=5 | quote: verified]

## Load-bearing assumptions
- The final system must enable continuity-of-journey rights for passengers holding single tickets.  [explicit | e=5 r=5 | quote: verified]
- National carriers must expose real-time inventory via OSDM-compatible APIs on non-discriminatory terms.  [explicit | e=5 r=5 | quote: verified]
- The binding standards must be finalized after the first set of corridors demonstrate operational stability.  [explicit | e=4 r=4 | quote: verified]
- The 'Builder' scenario logic balances public investment with carrier accountability for sustainability.  [explicit | e=4 r=4 | quote: verified]
- The most reliable national carriers will disproportionately subsidize systemic failures within the pooled backstop.  [inferred | e=4 r=4 | quote: verified]
- The chosen scenario avoids completely socializing all financial risk onto the public budget.  [inferred | e=3 r=4 | quote: verified]

## Gates and thresholds
- If PRM booking data mapping against the most restrictive standard is not complete by 2026-12-31, regulatory failure occurs.  [explicit | e=4 r=5 | quote: verified]
- If the clearing reserve dips below 150% of peak daily obligation, binding liquidity reporting is triggered.  [explicit | e=4 r=4 | quote: verified]
- If fault attribution confidence is not greater than 95%, the tiered liability model fails to recoup costs.  [explicit | e=4 r=4 | quote: verified]
- If OSDM standards do not achieve provisional binding status by six months, regulatory finalization is delayed.  [explicit | e=4 r=4 | quote: verified]
- If the railway becomes less attractive than flying on competitive short-haul routes, the modal shift goal is missed.  [explicit | e=4 r=4 | quote: verified]
- If a carrier exceeds the regulator-imposed maximum commercial fee for inventory access, it risks being barred from settlement.  [explicit | e=4 r=4 | quote: verified]

## Risks and shocks
- Under-capitalization or low liquidity in the clearing mechanism due to slow initial transactional velocity — financial mechanism risk.  [explicit | e=4 r=5 | quote: verified]
- Political resistance from state operators delays standard compliance past deadlines — risk to timeline adherence.  [explicit | e=4 r=4 | quote: verified]
- Integration challenges cause unstable OSDM real-time data layer latency or semantic errors — risk to data integrity.  [explicit | e=4 r=4 | quote: verified]
- National operators prioritize core API compliance over harmonizing mandatory ancillary services like accessibility — scope risk.  [explicit | e=4 r=4 | quote: verified]
- Coordinated lobbying by incumbent operators weakens the tiered liability framework — challenge to risk allocation model.  [explicit | e=4 r=4 | quote: verified]
- If incumbent carriers pay disproportionately for systemic delays in the backstop pool, moral hazard is created.  [explicit | e=4 r=4 | quote: verified]

## Missing data to estimate
- Number of months/years required to achieve the 40% through-ticket adoption target — duration to impact  [missing | e=4 r=5 | quote: verified]
- Total private carrier IT investment amount needed — estimate based on carrier class/size  [missing | e=4 r=5 | quote: verified]
- Average cost per transaction for the clearing mechanism transactional fee model — unit cost for settlement  [missing | e=3 r=4 | quote: verified]
- Total eligible cross-border journeys count subject to the 40% penetration goal — adoption base total  [missing | e=3 r=5 | quote: unverified]
- Required average monthly cost for the 35 FTEs for governance and testing — personnel expense basis  [missing | e=2 r=4 | quote: unverified]
- Required liquidity buffer factor for the clearing mechanism float — solvency contingency multiplier  [missing | e=3 r=3 | quote: unverified]

---

# Data Collection

## 1. Passenger Rights Backstop Capitalization & Liability Model Costs

As the backstop mechanism (Decision 1 & 3) is fundamental to consumer trust and financial stability, understanding the actual cost implications and legal defensibility of the liability split is critical. This directly impacts the required capitalization of the clearing house.

### Data to Collect

- Actuarial cost modeling for pooled backstop under Decision 1, Strategic Choice 2 (Collective Pool)
- Estimated frequency and severity of multi-operator fault claims based on historical data (cross-border rail incidents)
- Legal analysis of the enforceability of Strict Tiered Liability (Decision 3, Choice 1) versus Collective Insurance (Decision 3, Choice 2) under current EU transport law.

### Simulation Steps

- Use commercial actuarial software (e.g., R or Python with specific insurance libraries) to simulate 10,000 journey scenarios spanning the four priority corridors, modeling claim severity based on historical OTP/cancellation records from European Rail Agency archives (if accessible under a confidentiality agreement or public use proxy data).
- Model the float depletion curve for Decision 5 using the Builder scenario's transactional fee model, assuming a T+3 settlement speed, projecting reserve fund balance over the first 48 months.

### Expert Validation Steps

- Consult a Special Counsel for EU Consumer Protection Law to validate the legal robustness of the Strict Tiered Liability (Decision 3, Choice 1) proposal against existing passenger rights regulations.
- Consult the Financial Settlement Specialist (Expert 6) to calibrate the required capital buffer for the €200M operational float under the T+3 assumption.
- Consult the Regulatory Economist (Expert 1) to assess the long-term financial viability and regulatory risk profile of mandated insurance pooling (Decision 1, Choice 1 vs Choice 3).

### Responsible Parties

- Financial Clearing & Settlement Specialist (Expert 6)
- Passenger Rights & Equity Policy Analyst (Expert 5)
- EU Regulatory & Governance Architect (Expert 1)

### Assumptions

- **High:** The T+3 settlement reconciliation duration is achievable for 99% of transactions.
- **High:** The selected Liability model (Strict Tiered Liability, Decision 3/Choice 1 in Builder Scenario) is legally sound and defensible against immediate operator legal challenge.
- **Medium:** Historical cross-border rail incident data provides a statistically significant proxy for projected failure rates under the new unified system.

### SMART Validation Objective

Validate that the projected solvency buffer requirement for the collective insurance pool (Decision 3, Choice 2) falls within 160% of the currently allocated Emergency Float Reserve (€300M) by 2027-03-01, confirmed via financial simulation and external actuarial review.

### Notes

- The Intermodal Logistics Architect explicitly recommended pivoting Decision 3 to Choice 2 (Collective Pool) due to conflict with the 'Builder' scenario's pragmatic pace. This validation must confirm the feasibility of the *revised* liability approach.


## 2. OSDM API Latency and Technical Conformance (T+5 Benchmark)

The unified data layer is the project's technical dependency bedrock. Failure to meet T+5 latency undermines automated passenger rights (Decision 13) and invalidates operational trust. The aggressive Pacing (Decision 4) requires immediate technical proof.

### Data to Collect

- Test results validating T+5 minute latency achievement for real-time disruption data availability across OSDM endpoints on test environments.
- Feasibility assessment mapping mandatory PRM data schema requirements (Decision 9) against T+5 latency constraints against current operator IT capabilities.
- Draft Technical Failure Criteria report defining data quality metrics that trigger the first warning under the 'Three Strikes' enforcement posture (Decision 12).

### Simulation Steps

- Utilize the high-performance isolated testing environment (per Kenji Ito's needs) to run structured load tests simulating peak hourly transactions across the four core corridors.
- Run the T+5 latency monitoring tools rigorously against simulated 'disruption events' fed into the test environment to measure actual data propagation time.

### Expert Validation Steps

- Consult the IT Compliance and Enforcement Strategist (Expert 8) to finalize the technical failure thresholds that constitute a 'strike' under Decision 12.
- Consult the Accessibility Compliance Auditor (Expert 7) to verify that PRM data exchange flows meet regulatory mandates *while* adhering to the T+5 latency benchmark.
- Consult the Intermodal Logistics Architect (Expert 2) on the test result interpretation concerning the technical feasibility of the PRM integration schedule mandated by the expert review.

### Responsible Parties

- Cross-Corridor Conformance Testing Coordinator (Expert 8)
- Interoperability Standards Lead (Expert 2)
- EU Regulatory & Governance Architect (Expert 1)

### Assumptions

- **High:** The T+5 minute real-time latency benchmark is technically achievable using existing national infrastructure (with capacity grant support).
- **Medium:** Conforming SNCF, DB, and ÖBB IT systems can generate necessary OSDM data streams without requiring major architectural overhauls beyond capacity support funding.

### SMART Validation Objective

Achieve verifiable, sustained T+5 minute average latency across 95% of simulated core inventory and disruption endpoints for the initial four corridors in the test environment by 2027-03-14.

### Notes

- This validation must explicitly integrate PRM data structure testing concurrently, as advised by the expert review.


## 3. Commercial Terms Auditability and Cost Recovery Compliance

The mandated cost-recovery for data access (Decision 2) is crucial for balancing operator buy-in against distributor market entry. Its auditability must be proven immediately to prevent regulatory delays or financial disputes post-launch.

### Data to Collect

- Sample audit templates for verifying National Rail Operators' IT operational costs attributable to OSDM data provisioning.
- Initial regulatory guidance drafts detailing the enforcement mechanism for capping royalties at 5% of attributable maintenance expenditure (Decision 2).
- Comparative data on historical third-party distributor access costs vs. the proposed cost-recovery royalty structure.

### Simulation Steps

- Develop a mock financial submission template for a major operator (e.g., DB) based on known industry IT budget benchmarks, applying the 5% royalty cap to determine potential operator revenue loss/gain.
- Simulate distributor integration cost savings realized by the 5% cap versus market prevailing rates observed in the PSD2 implementation (Expert 2 Rationale).

### Expert Validation Steps

- Consult the Regulatory Economist (Expert 1) to sign off on the fairness and compliance (State Aid implications) of the 5% royalty cap model.
- Consult the Digital Distributor & Market Adoption Strategist (Expert 6) to confirm that this cost structure maximizes distributor incentive for adoption (Risk 7 mitigation).
- Consult the Rail Operator Liaison Manager (Expert 4) to anticipate operator resistance/misreporting strategies regarding cost attribution.

### Responsible Parties

- Rail Operator Liaison & Integration Manager (Expert 4)
- EU Regulatory & Governance Architect (Expert 1)

### Assumptions

- **High:** National operators will provide auditable financial records detailing IT operational costs attributable specifically to OSDM API maintenance.
- **Medium:** The 5% cap on royalties is sufficient to cover the national carrier's verifiable marginal costs for data provisioning.

### SMART Validation Objective

By 2027-05-01, secure documented agreement from SNCF, DB, and ÖBB representatives (via the Liaison Manager) on the audit methodology used to verify OSDM cost attribution for the first fiscal year calculation.

### Notes

- This validation directly addresses expert concern regarding verification processes for cost recovery.

## Summary

The immediate next steps must focus on reconciling the conflicting demands of the 'Builder' scenario: aggressive technical compliance (T+5 latency, PRM integration) under a pragmatic timeline, while managing political resistance to shared financial risk (Liability Pivot). The most sensitive assumptions relate to operator compliance with technical deadlines and the legal/financial viability of the chosen liability model. Action must prioritize rigorous, simultaneous testing of the core data layer stability and binding accessibility schemas, alongside establishing the auditability proof for commercial terms. The immediate actionable tasks are detailed below, focusing on validation Item 2 (Technical Stability) and Item 1 (Liability Validation) due to their high associated risk scores.

---
