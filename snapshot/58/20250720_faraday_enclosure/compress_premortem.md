# Premortem

This premortem section details nine critical failure modes, each stemming from an unvalidated assumption about supplier capacity, market size, funding triggers, product fit, logistics reliability, intellectual property protection, or external regulations, providing a basis for quantifying the probability and impact of key project risks.

## Numeric values
- Phone-only enclosure BOM cost is €45 vs laptop combo cost of €75 — scales variable material cost per SKU  [explicit | e=5 r=5 | quote: verified]
- Tallinn ISO run minimum order quantity is 2,000 units per run — gates production scale decision  [explicit | e=5 r=5 | quote: verified]
- Server-grade cage BOM cost is €400 — scales variable material cost for pivot product  [explicit | e=5 r=5 | quote: verified]
- ISO run raw materials and tooling cost is €150k — scales initial fixed manufacturing cost  [explicit | e=5 r=4 | quote: verified]
- European prepper market estimate is 15,000 to 20,000 active buyers — sets ceiling for consumer sales volume  [explicit | e=5 r=4 | quote: verified]
- B2B sales consultant annual cost is €30k — scales fixed overhead/marketing expense  [explicit | e=5 r=4 | quote: verified]

## Load-bearing assumptions
- Pre-sales must absorb at least 1,500 units within 6 months to fund the pivot.  [inferred | e=5 r=5 | quote: verified]
- The consumer product priced at €99 yields a 45% gross margin at 2,000 units.  [explicit | e=5 r=5 | quote: verified]
- The €99 pricing generates only €89k gross profit, insufficient for €120k certification.  [derived | e=5 r=5 | quote: verified]
- Positive cash flow trigger requires €50k net cash from operations by Month 12.  [explicit | e=5 r=5 | quote: verified]
- The Year-1 budget is €400k, with total budget of €750k.  [explicit | e=5 r=5 | quote: verified]
- Prepper networks yield fast cash but infrastructure buyers offer 10x per-unit revenue.  [inferred | e=5 r=5 | quote: verified]

## Gates and thresholds
- If pre-sales fall short of 1,500 units within 6 months, then the project cannot fund the server-grade pivot.  [inferred | e=5 r=5 | quote: verified]
- If sell-through is below 75% for the 2,000-unit run, then follow-on funding is jeopardized.  [explicit | e=5 r=5 | quote: verified]
- If using the €99 price, gross profit is insufficient to fund the €120k certification.  [derived | e=5 r=5 | quote: verified]
- If sell-through is 50% for the 2,000-unit run, then €75k of inventory results.  [stress_test | e=5 r=4 | quote: verified]
- If pre-sales confirm demand exceeds 1,000 units, then scale production to Tallinn's ISO facility.  [explicit | e=5 r=4 | quote: verified]
- If pre-sale deposits are not 50% non-refundable, then the project funds tooling risks chargebacks.  [inferred | e=5 r=4 | quote: verified]

## Risks and shocks
- ISO run unsold inventory risk is €75k if sell-through hits 50% — stress on Year-1 runway.  [stress_test | e=5 r=5 | quote: verified]
- Cash shortfall of €31k if €99 pricing fails to fund €120k certification cost.  [derived | e=5 r=5 | quote: verified]
- If pre-sales fall short of 1,500 units, failure to fund the pivot occurs.  [stress_test | e=5 r=5 | quote: verified]
- Pursuing MIL-STD-461 first adds 6 months and €80k to certification phase.  [explicit | e=5 r=4 | quote: verified]
- Reverse engineering by Chinese manufacturers could undercut price by 50%.  [stress_test | e=5 r=4 | quote: verified]
- Server-grade cage design work delays until €350k follow-on funding is confirmed.  [explicit | e=5 r=4 | quote: verified]

## Missing data to estimate
- Target logistics cost as a percentage of revenue percentage point limit.  [missing | e=5 r=3 | quote: verified]
- Cost per unit for 2,000-unit ISO run in €/unit — estimate based on €150k total cost.  [missing | e=1 r=5 | quote: unverified]
- Number of critical-infrastructure buyers targeted for B2B outreach count — estimate from B2B consultant pipeline build.  [missing | e=1 r=4 | quote: unverified]
- Total expected pre-order conversion rate percentage point — estimate from A/B test results.  [missing | e=1 r=5 | quote: unverified]
- Discount percentage point for retailer wholesale agreement — estimate from SurvivalAid.de terms research.  [missing | e=1 r=4 | quote: unverified]
- Average length of retailer payment period in days — estimate from standard net terms.  [missing | e=1 r=4 | quote: unverified]
