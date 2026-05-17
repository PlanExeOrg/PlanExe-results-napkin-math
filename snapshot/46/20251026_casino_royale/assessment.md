# Assessment: White House East Wing Casino (Pioneer's Gauntlet)

**Type:** commercial_construction_phased  
**Primary goal:** Launch Phase 1 container casino, prove 60-90 days continuous profitability to unlock 75% sponsor capital, fund permanent Phase 2 build.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "White House East Wing Casino (Pioneer's Gauntlet)",
  "artifact_set": {
    "version": "v46",
    "plan_slug": "20251026_casino_royale",
    "relative_dir": "output/v46/20251026_casino_royale"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v46/20251026_casino_royale",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (DOOM band)",
    "worst_gate": "sponsor_profitability_window_margin_days",
    "worst_gate_pass_rate": 0.0
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "sponsor_profitability_window_margin_days"
  ],
  "primary_uncertainty_drivers": [
    "daily_revenue_per_guest_usd",
    "daily_operating_cost_usd",
    "expected_utilization_rate"
  ],
  "known_unmodelled_existential_gates": [
    "gsa_doi_post_facto_authorization_gate",
    "aml_banking_consortium_certification_gate",
    "high_security_gaming_license_gate",
    "t2ca_diplomatic_acceptance_gate"
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

Tests Phase 1 daily revenue, NOI, sponsor profitability gate margin, sponsor capital release, contingency remediation burn capacity, and AML-shock NOI resilience. Existential regulatory and AML-licensing gates are out-of-model and tracked as unmodelled_gates.

**Note:** This assessment is a financial / operational stress test. 4 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `gsa_doi_post_facto_authorization_gate` | Construction proceeds before federal authorization for converting demolished White House East Wing land to commercial casino use; no quantitative threshold exists. | report.html / premortem | Court ruling halts the project mid-construction; sponsor tranche never releases and Phase 2 capital becomes stranded regardless of Phase 1 NOI performance. |
| `aml_banking_consortium_certification_gate` | All high-value markers must settle through the pre-approved consortium; without certification, the only legal settlement rail is blocked. | report.html / data_collection | Loss of banking access shuts down high-roller settlement, collapsing the revenue assumption underlying the sponsor profitability gate. |
| `high_security_gaming_license_gate` | Phase 1 operations are conditional on this Phase-1 license; the model treats it as granted but cannot probabilistically test issuance. | report.html / project_plan | Phase 1 cannot open; the 90-day continuous-profit clock never starts and the sponsor capital gate cannot be reached. |
| `t2ca_diplomatic_acceptance_gate` | Revenue concentration on diplomatic high-rollers depends on world-leader delegations accepting a commercial-grade (non-sovereign) vetting tier. | report.html / expert_criticism | Patron boycott collapses the 60/40 high-roller mix and the revenue assumptions underlying the sponsor gate. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate GSA/DOI post-facto land-use authorization, international Banking Consortium AML/KYC certification, conditional High-Security Gaming Operation License, or diplomatic acceptance of Tier 2 Commercial Access vetting. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **DOOM** — `sponsor_profitability_window_margin_days` fails >= 0.0000 in 100.0% of simulated runs under the current input bounds.
- **Scenario warn (low)** — `sponsor_profitability_trigger_margin_usd`: Negative margin (-100100 USD/day): daily NOI fails the $50k sponsor profitability gate in the low scenario.
- **Scenario warn (low)** — `aml_adjusted_daily_noi_margin_usd`: Negative margin (-103097 USD/day): AML-shocked daily NOI fails the $50k sponsor gate in the low scenario.
- **Scenario warn (low)** — `sponsor_profitability_window_margin_days`: Negative margin (-5 days): achievable profitable-operation days (window minus blackout) fall short of the 90-day sponsor requirement in the low scenario.
- **Scenario warn (base)** — `sponsor_profitability_window_margin_days`: Negative margin (-7 days): achievable profitable-operation days (window minus blackout) fall short of the 90-day sponsor requirement in the base scenario.
- **Scenario warn (high)** — `sponsor_profitability_window_margin_days`: Negative margin (-12 days): achievable profitable-operation days (window minus blackout) fall short of the 90-day sponsor requirement in the high scenario.

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **ROBUST**, 50–80% **MARGINAL**, 20–50% **FRAGILE**, <20% **DOOM**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `sponsor_profitability_window_margin_days` | >= 0.0000 | report_explicit | 0.0% | **DOOM** | rarely passes under current bounds |
|  | `aml_adjusted_daily_noi_margin_usd` | >= 0.0000 | report_explicit | 79.8% | **MARGINAL** | passes more often than not but uncomfortably close |
|  | `sponsor_profitability_trigger_margin_usd` | >= 0.0000 | report_explicit | 85.2% | **ROBUST** | passes in the strong majority of runs |

### Aggregation warning

The thresholds above use incompatible units (USD_per_day, days) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `sponsor_profitability_window_margin_days` | **DOOM** | The `>= 0.0000` requirement is not credible under current bounds: only 0.0% of runs hold. Commitments that depend on this should not be made without revision. | Saturated failure: pass rate is 0.0% and no single input quartile movement changes that. Quartile sensitivity is not informative; audit the input bounds and the threshold definition. | Threshold-friendly margin: achieved profitable-operation days (window minus blackout) minus the contractually required window. Positive means the gate clears at >= 0; negative quantifies the days short of the sponsor's 90-day continuous-profit requirement, which would fail the capital release gate regardless of daily NOI. Threshold parameter: `sponsor_profitability_window_days`. |
| `aml_adjusted_daily_noi_margin_usd` | **MARGINAL** | The `>= 0.0000` requirement passes 79.8% of runs — just below the ROBUST band. The gate passes in most runs, but downstream commitments should not treat it as secure. | `daily_revenue_per_guest_usd` (improve toward its high bound; quartile Δ-pp +59.3) | AML compliance forces bank-settled markers, projected to cut top-tier spend; this stress-tests the sponsor gate under that shock. Threshold parameter: `high_roller_capacity_share`. |

## Failure drivers

For each failing gate (DOOM or FRAGILE): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `sponsor_profitability_window_margin_days` | (saturated failure) | n/a | saturated failure: no single input restriction can lift the pass rate; revisit bounds and threshold |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

Note: the saturated DOOM gate `sponsor_profitability_window_margin_days` is absent from the ranking because no single missing-input restriction can lift its pass rate under current bounds. The inputs below target the next most decision-relevant non-saturated gates; the saturated gate needs a bounds or threshold-definition audit, not a single input fix.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `daily_revenue_per_guest_usd` | `aml_adjusted_daily_noi_margin_usd` | 30.91 | 2.58 | report_derived |
| 2 | `daily_operating_cost_usd` | `aml_adjusted_daily_noi_margin_usd` | 10.40 | 1.57 | model_assumption |
| 3 | `expected_utilization_rate` | `aml_adjusted_daily_noi_margin_usd` | 5.81 | 1.00 | report_derived |
| 4 | `aml_bank_settlement_revenue_reduction_fraction` | `aml_adjusted_daily_noi_margin_usd` | 1.05 | 1.25 | report_derived |

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
| `expected_daily_revenue_usd` | **LOW** | 100% | 1.79 |
| `expected_daily_noi_usd` | **LOW** | 67% | 1.72 |
| `sponsor_profitability_trigger_margin_usd` | **LOW** | 67% | 1.72 |
| `court_remediation_daily_burn_capacity_usd` | **MEDIUM** | 100% | 0.67 |
| `sponsor_profitability_window_margin_days` | **MEDIUM** | 100% | 1.00 |
| `aml_adjusted_daily_noi_margin_usd` | **LOW** | 75% | 1.60 |
| `high_roller_daily_revenue_usd` | **LOW** | 100% | 1.79 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `expected_daily_revenue_usd` | USD_per_day | 99,900 | 599,400 | 2,622,375 |
| `expected_daily_noi_usd` | USD_per_day | -50,100 | 249,400 | 1,922,375 |
| `sponsor_profitability_trigger_margin_usd` | USD_per_day | -100,100 | 199,400 | 1,872,375 |
| `sponsor_capital_release_usd` | USD | 450,000,000 | 450,000,000 | 450,000,000 |
| `court_remediation_daily_burn_capacity_usd` | USD_per_day | 1,500,000 | 1,000,000 | 750,000 |
| `sponsor_profitability_window_margin_days` | days | -5.00 | -7.00 | -12.00 |
| `aml_adjusted_daily_noi_margin_usd` | USD_per_day | -103,097 | 127,472 | 1,400,348 |
| `high_roller_daily_revenue_usd` | USD_per_day | 59,940 | 359,640 | 1,573,425 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 1 declared gate in the DOOM band. Worst: `sponsor_profitability_window_margin_days` at 0.0% pass rate under current bounds.
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
