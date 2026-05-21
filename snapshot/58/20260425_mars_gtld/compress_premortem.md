# Premortem

This section defines twelve discrete strategic decisions or levers, each with specific hard trade-offs concerning governance, technical standards, and political navigation, which will serve as branching parameters for scenario simulation. Nine key assumptions, which represent high-leverage uncertainties (e.g., Mars endpoint capability, financial pacing, and core control retention), are identified as critical failure points that must be validated to ensure project survival and determine subsequent feasibility gates. Failure modes provide quantified impact and trigger points for major internal pivots, such as suspending revenue pledges or halting outreach if core technical or security infrastructure milestones are missed.

## Numeric values
- Target ICANN delegation date: 2027-November-02 — gates primary timeline metric  [explicit | e=5 r=5 | quote: verified]
- Mandatory synchronization freshness guarantee: 60-minute window — gates technical standard choice for high freshness tier  [explicit | e=5 r=5 | quote: verified]
- Percentage of net registry revenue committed to environmental fund: 50% — scales mandatory non-commercial outgoing fund  [explicit | e=5 r=5 | quote: verified]
- Target time for ICANN delegation: 18 months — primary timeline driver for external dependencies  [explicit | e=5 r=5 | quote: verified]
- Anticipated secondary expenditure range for legal/lobbying delay cost: $5M–$10M USD — stress test for regulatory objection cost  [stress_test | e=5 r=4 | quote: verified]
- Anticipated secondary expenditure range for technical sync mechanism cost: $2M–$5M USD — stress test for latency protocol investment  [stress_test | e=5 r=4 | quote: verified]

## Load-bearing assumptions
- Mandating a strict 60-minute synchronization window creates a high barrier to entry for low-bandwidth Mars operators.  [explicit | e=5 r=5 | quote: verified]
- Framing the TLD as a non-profit utility sacrifices long-term financial sustainability and profitability.  [explicit | e=5 r=5 | quote: verified]
- Adopting a Board of Trustees structure introduces governance latency which delays responsiveness to security threats.  [explicit | e=5 r=4 | quote: verified]
- Adopting HSM-based key management strains the operational budget needed for policy dispute management.  [explicit | e=5 r=4 | quote: verified]
- Seeking formal agency endorsements subjects the operational handbook to slow, diverse policy mandates.  [explicit | e=5 r=4 | quote: verified]
- Proactive defense via defensive registration consumes budget needed for legitimacy-building activities.  [explicit | e=5 r=4 | quote: verified]

## Gates and thresholds
- If the registry is framed solely as non-profit utility, then long-term financial sustainability will be undermined.  [explicit | e=5 r=5 | quote: verified]
- If the synchronization interval mandate is too short, then high entry barriers will slow adoption by Mars operators.  [explicit | e=5 r=5 | quote: verified]
- If the synchronization TTL maximum is strictly 300 seconds, then high query volume may overwhelm Earth primary infrastructure.  [explicit | e=5 r=4 | quote: verified]
- If advisory board veto power is granted, then governance latency will slow responses to interplanetary security threats.  [explicit | e=5 r=4 | quote: verified]
- If full DNSSEC signing authority is delegated externally, then internal expertise requirements minimize but reliance on third-party SLA increases.  [explicit | e=5 r=4 | quote: verified]
- If sovereign endorsement is actively sought, then the operational handbook will be subjected to slow, conflicting policy mandates.  [explicit | e=5 r=4 | quote: verified]

## Risks and shocks
- Governmental objection risk causes 6–12 month delay plus $5M–$10M extra cost if private planetary namespace operation is challenged.  [stress_test | e=5 r=5 | quote: verified]
- Technical latency risk causes $2M–$5M extra operational cost for sync mechanisms or potential service outages.  [stress_test | e=5 r=4 | quote: verified]
- Financial risk overrun from string contention or compliance costs is modeled at $10M–$20M cost extension.  [stress_test | e=5 r=4 | quote: verified]
- Political backlash over private operation causes 3–6 month delays plus $2M–$4M extra legal costs.  [stress_test | e=5 r=4 | quote: verified]
- Operational risk from sync issues causes 2–4 weeks of operational delays affecting availability during sync updates.  [stress_test | e=5 r=3 | quote: verified]
- Supply chain risk reliance on external providers causes 1–3 month service deployment delays or $1M–$3M alternative costs.  [stress_test | e=5 r=3 | quote: verified]

## Missing data to estimate
- Total duration in months the $25M-$100M+ budget must sustain operations before positive cash flow — needed to scale OpEx burn rate  [missing | e=1 r=4 | quote: unverified]
- Target number of domain registrations required in Year 1 to cover base operating expenses — needed to validate revenue model  [missing | e=1 r=5 | quote: unverified]
- Required revenue per domain registration per year — needed to calculate break-even volume against OpEx and pledge  [missing | e=1 r=5 | quote: unverified]
- Cost per month for sustaining the high-security Earth-mirror DNS infrastructure — needed to scale OpEx  [missing | e=1 r=4 | quote: unverified]
- Total staff months required for the technical team to complete proprietary synchronization tooling development — needed to calculate labor cost  [missing | e=1 r=4 | quote: unverified]
- Maximum acceptable duration in months for the ICANN delegation review process — needed to project political risk exposure  [missing | e=1 r=4 | quote: unverified]
