# Assessment: European Faraday Enclosure Launch (Tallinn-anchored)

**Type:** consumer_hardware_startup  
**Primary goal:** Design, certify, and distribute a single-SKU consumer Faraday enclosure under the Pragmatic Foundation strategy, reaching €50k net cash from operations by Month 12 to unlock the €350k follow-on funding for a server-grade B2B pivot.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "European Faraday Enclosure Launch (Tallinn-anchored)",
  "artifact_set": {
    "version": "v46",
    "plan_slug": "20250720_faraday_enclosure",
    "relative_dir": "output/v46/20250720_faraday_enclosure"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v46/20250720_faraday_enclosure",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (DOOM band)",
    "worst_gate": "iso_run_sellthrough_margin",
    "worst_gate_pass_rate": 0.1544
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "iso_run_sellthrough_margin",
    "month12_net_cash_margin_eur",
    "milstd_funding_margin_eur",
    "presale_conversion_margin",
    "eu_emc_cert_budget_margin_eur"
  ],
  "primary_uncertainty_drivers": [
    "actual_net_cash_month12_eur",
    "actual_presale_conversion_share",
    "actual_year1_gross_profit_eur"
  ],
  "known_unmodelled_existential_gates": [
    "funding_trigger_renegotiation_gate",
    "eu_emc_certification_passes_gate",
    "gasket_supply_continuity_gate"
  ],
  "assessment_scope_warning": "Declared simulation gates cover financial / operational viability only; the gates listed in `known_unmodelled_existential_gates` are not simulated and may dominate the modelled financial result.",
  "do_not_treat_as": [
    "an external feasibility proof for the plan's claims",
    "a real-world probability calibration",
    "a replacement for the source report",
    "evidence that the input bounds match reality"
  ],
  "schema_notes": {
    "overall_risk_band_enum": [
      "viable",
      "marginal",
      "fragile",
      "doom",
      "unknown"
    ],
    "verdict_enum": [
      "ROBUST",
      "MARGINAL",
      "FRAGILE",
      "DOOM",
      "UNKNOWN"
    ],
    "basis_enum": [
      "report_explicit",
      "report_inferred",
      "report_derived",
      "model_assumption",
      "external_reference",
      "manual_override",
      "unknown"
    ],
    "threshold_basis_enum": [
      "report_explicit",
      "report_inferred",
      "model_defined",
      "unknown"
    ],
    "primary_model_result_semantics": "overall_risk_band reflects the worst declared gate's pass-rate band; it is not a calibrated whole-plan probability and does not mean the plan is impossible."
  }
}
```

## Provenance map

Each intermediary file and the question it answers.

| File | Role | Open when |
|---|---|---|
| `extract_parameters_input.md` | Source-text digest fed to the parameter extractor. | Auditing what the extractor actually saw. |
| `parameters.json` | Extracted constants, missing inputs, derived questions, formula hints. | Need model structure or to confirm a formula's wording. |
| `bounds.json` | low/base/high ranges with rationales, sampling discipline, source labels. | Auditing the source of an uncertainty range. |
| `calculations.py` | Executable Python formula implementation, one function per gate. | Need the exact arithmetic. |
| `scenarios.json` | Three deterministic scenarios (low/base/high) with outputs and warnings. | Sanity-checking the model against deterministic anchor points. |
| `scenario_outputs.json` _(not in this run)_ | Auxiliary per-scenario output file. | Cross-referencing the scenario outputs. |
| `montecarlo_settings.json` | Run settings: n_runs, seed, distribution_default, threshold definitions. | Reproducing the run or changing the threshold definitions. |
| `montecarlo.json` | Full simulation results: distributions, pass rates, sensitivity, quartile_analysis, binding_gate_analysis, required_input_thresholds, missing_value_priority, model_confidence. | Need raw simulation data, distributions, or per-driver analysis. |
| `validation.json` | Structural validation report (which checks passed, which failed). | Confirming the pipeline ran without structural problems. |

## Modelling frame

Tests the Month-12 net-cash margin against the €50k funder trigger; the 2,000-unit ISO-run sell-through margin against the 75% threshold; the Year-1 gross-profit margin against the €120k MIL-STD certification budget; the pre-sale conversion margin against the 5% Issue-1 floor; and the EU EMC certification budget margin against the €80k allocation. Funder trigger renegotiation, EU EMC certification pass, and conductive-gasket supply continuity are treated as unmodelled existential gates.

**Note:** This assessment is a financial / operational stress test. 3 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `funding_trigger_renegotiation_gate` | Risk 1 names the vague trigger as the single largest governance risk; without renegotiation the €350k follow-on is at the funder's discretion regardless of any quantitative margin the model evaluates. | report.html / premortem | A single late retailer payment or certification slip pushes 'cash flow' negative under the loose definition; funder withholds €350k; server-grade pivot path closes and the €400k Year-1 capital is stranded. |
| `eu_emc_certification_passes_gate` | Risk 8 and Issue 2 name a redesign event as a €20–40k unbudgeted cost plus 3–6 month delay; certification failure is a binary event the simulation models only via cost overrun, not as a redesign-triggered restart. | report.html / expert_criticism | Combo-SKU redesign costs €20–40k; market entry delays 3–6 months; the Year-1 revenue window collapses and the Month-12 trigger becomes unreachable regardless of pre-sale conversion. |
| `gasket_supply_continuity_gate` | Risk 6 and Issue 3 name an 8–12 week gasket-supply delay as the dominant supply-chain shock; the plan single-sources from a German supplier and the mitigation (qualify two backup suppliers) takes 8–12 weeks itself. | report.html / review_plan | Production halts 4–8 weeks; pre-sale delivery slippage triggers chargeback exposure (Risk 9); cash-flow trigger missed; pivot path closed before Month 12. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate funder agrees to renegotiate 'positive cash flow' to '€50k net cash by Month 12' by Month 6, product passes EU EMC certification without requiring fundamental redesign, or conductive-gasket and copper-beryllium finger-stock supply remains continuous. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **DOOM** — `iso_run_sellthrough_margin` fails >= 0.0000 in 84.6% of simulated runs under the current input bounds.
- **FRAGILE** — `month12_net_cash_margin_eur` holds in only 24.7% of simulated runs under the current input bounds (fails in the majority).
- **FRAGILE** — `milstd_funding_margin_eur` holds in only 26.9% of simulated runs under the current input bounds (fails in the majority).
- **FRAGILE** — `presale_conversion_margin` holds in only 42.8% of simulated runs under the current input bounds (fails in the majority).
- **FRAGILE** — `eu_emc_cert_budget_margin_eur` holds in only 28.1% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **ROBUST**, 50–80% **MARGINAL**, 20–50% **FRAGILE**, <20% **DOOM**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `iso_run_sellthrough_margin` | >= 0.0000 | report_explicit | 15.4% | **DOOM** | rarely passes under current bounds |
|  | `month12_net_cash_margin_eur` | >= 0.0000 | report_explicit | 24.7% | **FRAGILE** | fails in the majority of runs |
|  | `milstd_funding_margin_eur` | >= 0.0000 | report_explicit | 26.9% | **FRAGILE** | fails in the majority of runs |
|  | `presale_conversion_margin` | >= 0.0000 | report_inferred | 42.8% | **FRAGILE** | fails in the majority of runs |
|  | `eu_emc_cert_budget_margin_eur` | >= 0.0000 | report_explicit | 28.1% | **FRAGILE** | fails in the majority of runs |

### Aggregation warning

The thresholds above use incompatible units (EUR, fraction) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `iso_run_sellthrough_margin` | **DOOM** | The `>= 0.0000` requirement is not credible under current bounds: only 15.4% of runs hold. Commitments that depend on this should not be made without revision. | `actual_sellthrough_share` (improve toward its high bound; quartile Δ-pp +61.8) | Positive margin clears the production-cash recovery threshold; negative margin produces the €75k+ unsold-inventory scenario that Risk 2 names as the operational failure mode. Threshold parameter: `sell_through_target_share`. |
| `month12_net_cash_margin_eur` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (75.3%). External commitments built on this gate are exposed. | `actual_net_cash_month12_eur` (improve toward its high bound; quartile Δ-pp +98.7) | Positive margin unlocks the €350k follow-on funding and the server-grade pivot path; negative margin closes the entire growth pathway regardless of any other operational metric. Threshold parameter: `net_cash_target_month12_eur`. |
| `milstd_funding_margin_eur` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (73.1%). External commitments built on this gate are exposed. | `actual_year1_gross_profit_eur` (improve toward its high bound; quartile Δ-pp +100.0) | Positive margin self-funds the €120k MIL-STD pivot path; negative margin forces reliance on the €350k follow-on (already gated by the Month-12 trigger) and risks stalling the B2B strategy entirely. Threshold parameter: `mil_std_cert_cost_eur`. |
| `presale_conversion_margin` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (57.2%). External commitments built on this gate are exposed. | `actual_presale_conversion_share` (improve toward its high bound; quartile Δ-pp +94.9) | Positive margin justifies the 2,000-unit ISO commitment; negative margin invalidates the entire production-scale decision per Expert Issue 1's sensitivity model. Threshold parameter: `presale_conversion_target_share`. |
| `eu_emc_cert_budget_margin_eur` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (71.9%). External commitments built on this gate are exposed. | `actual_eu_emc_cert_cost_eur` (reduce toward its low bound; quartile Δ-pp -80.4) | Positive margin preserves the €20k contingency for marketing and supply-chain surprises; negative margin (Expert Issue 2's 30–50% re-test scenario) directly threatens the Month-12 net-cash trigger. Threshold parameter: `eu_emc_cert_budget_eur`. |

## Failure drivers

For each failing gate (DOOM or FRAGILE): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `iso_run_sellthrough_margin` | `actual_sellthrough_share` | +61.8 | `actual_sellthrough_share` above p85 |
| `month12_net_cash_margin_eur` | `actual_net_cash_month12_eur` | +98.7 | `actual_net_cash_month12_eur` above p75 |
| `milstd_funding_margin_eur` | `actual_year1_gross_profit_eur` | +100.0 | `actual_year1_gross_profit_eur` above p67 |
| `presale_conversion_margin` | `actual_presale_conversion_share` | +94.9 | `actual_presale_conversion_share` above p67 |
| `eu_emc_cert_budget_margin_eur` | `actual_eu_emc_cert_cost_eur` | -80.4 | `actual_eu_emc_cert_cost_eur` below p75 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `actual_net_cash_month12_eur` | `month12_net_cash_margin_eur` | 545.28 | 7.33 | model_assumption |
| 2 | `actual_presale_conversion_share` | `presale_conversion_margin` | 122.05 | 2.25 | report_derived |
| 3 | `actual_year1_gross_profit_eur` | `milstd_funding_margin_eur` | 121.90 | 1.67 | report_derived |
| 4 | `actual_eu_emc_cert_cost_eur` | `eu_emc_cert_budget_margin_eur` | 48.69 | 0.84 | report_derived |
| 5 | `actual_sellthrough_share` | `iso_run_sellthrough_margin` | 48.21 | 0.92 | model_assumption |

`Basis` values: `report_derived` = bound anchored in the source report's narrative (not externally verified); `model_assumption` = bound is a modelling assumption with no narrative anchor. Neither value is empirical ground truth.

## Confidence and trust boundaries

### Validated

Structural checks that passed (`validation.json`): `json_parse`, `top_level_structure`, `required_fields`, `array_length_caps`, `global_id_uniqueness`, `snake_case_ids`, `depends_on_declared`, `formula_rhs_declared`, `fraction_value_range`, `comment_word_caps`, `source_text_word_caps`, `output_name_present_when_formula_hint`, `output_unit_present_when_formula_hint`, `no_dead_end_variables`, `threshold_friendly_naming`, `shared_pool_legitimacy`.

### Not validated

- real-world accuracy of the input bounds
- independence or correlation assumptions across inputs
- external feasibility of regulatory, grid, supply, or market dependencies
- factual truth of the source plan's narrative claims

### Per-output confidence

| Output | Grade | Declared-source inputs | Bound-width / base |
|---|:---:|---:|---:|
| `month12_net_cash_margin_eur` | **LOW** | 0% | 7.33 |
| `iso_run_sellthrough_margin` | **LOW** | 0% | 0.92 |
| `milstd_funding_margin_eur` | **LOW** | 100% | 1.67 |
| `presale_conversion_margin` | **LOW** | 100% | 1.62 |
| `eu_emc_cert_budget_margin_eur` | **MEDIUM** | 100% | 0.67 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `month12_net_cash_margin_eur` | EUR | -150,000 | -20,000 | 70,000 |
| `iso_run_sellthrough_margin` | fraction | -0.4500 | -0.1000 | 0.1500 |
| `milstd_funding_margin_eur` | EUR | -90,000 | -30,000 | 60,000 |
| `presale_conversion_margin` | fraction | -0.0200 | -0.0100 | 0.0200 |
| `eu_emc_cert_budget_margin_eur` | EUR | 10,000 | -15,000 | -30,000 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 1 declared gate in the DOOM band; 4 in the FRAGILE band. Worst: `iso_run_sellthrough_margin` at 15.4% pass rate under current bounds.
2. To prioritise data-gathering, inspect `missing_value_priority` in `montecarlo.json`. The top-scored entries are the cheapest improvements to the simulation's predictive value.
3. To audit whether the simulation is trustworthy, open `bounds.json` (range rationales and the `source` label per bound, surfaced here as the `Basis` column in `Missing inputs ranked by impact`), `montecarlo_settings.json` (n_runs, seed, distribution_default, threshold definitions), and `validation.json` (which structural checks passed). Neither `report_derived` nor `model_assumption` constitutes externally observed ground truth.
4. To improve the plan, target the gates with the lowest pass rates first. Failure-driver rows above name the single input whose quartile movement has the largest effect on each failing gate.
5. For exact formulas and the executable model, use `parameters.json` (declared formula hints) and `calculations.py` (implementation). Do not infer formulas from prose elsewhere in this file.

## Open questions for next analysis pass

Standing questions for whoever picks this directory up next. These are not gate verdicts; they are the audit checks the simulation can't answer on its own.

1. Are the current input bounds too narrow, too wide, or directionally biased?
2. Which failed gates are truly independent, and which are correlated?
3. Which gates are hard stop/go gates versus soft optimisation targets?
4. Which missing inputs can be replaced by external research or user-supplied facts?
5. Does the source report contain unmodelled gates that should be added?
