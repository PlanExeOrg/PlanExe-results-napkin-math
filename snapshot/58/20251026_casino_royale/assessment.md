# Assessment: White House East Wing Casino - Pioneer's Gauntlet

**Type:** commercial  
**Primary goal:** Launch Phase 1 container casino, hit 90-day continuous profitability to unlock 75% sponsor capital, and seed a long-term Infrastructure Levy.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "White House East Wing Casino - Pioneer's Gauntlet",
  "artifact_set": {
    "version": "v58",
    "plan_slug": "20251026_casino_royale",
    "relative_dir": "output/v58/20251026_casino_royale"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v58/20251026_casino_royale",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "fragile",
    "reason": "at least one declared gate has pass rate in 20\u201350% (Fragile band)",
    "worst_gate": "political_reversal_buffer_surplus",
    "worst_gate_pass_rate": 0.272
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "political_reversal_buffer_surplus"
  ],
  "primary_uncertainty_drivers": [
    "political_reversal_shock_usd",
    "achievable_daily_noi_usd",
    "ancillary_gross_revenue_annual_usd"
  ],
  "known_unmodelled_existential_gates": [
    "post_facto_regulatory_authorization_gate",
    "aml_banking_consortium_gate",
    "infrastructure_levy_political_acceptance_gate"
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
      "Robust",
      "Marginal",
      "Fragile",
      "Critical",
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

Tests Phase 1 NOI gate against the sponsor 75% capital release, the $90M contingency buffer against a political reversal shock, and the ancillary Infrastructure Levy against required long-term operating cost. Regulatory shutdown and AML compliance are tracked as unmodelled existential gates.

**Note:** This assessment is a financial / operational stress test. 3 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `post_facto_regulatory_authorization_gate` | Phase 1 construction proceeds in parallel with seeking post-facto authorization for repurposing the East Wing site; without it the whole project halts. | report.html / expert_criticism | Adverse court ruling or denial halts construction, stranding Phase 1 assets; review estimates near-100% probability of failure and 80-100% ROI loss. |
| `aml_banking_consortium_gate` | Tier 2 Commercial Access settlement of high-value markers must run through pre-approved banks meeting AML/KYC; loss of access blocks the high-roller revenue model. | report.html / data_collection | Without AML-compliant settlement the 60% high-roller revenue stream cannot be operated legally and Phase 1 NOI collapses. |
| `infrastructure_levy_political_acceptance_gate` | Long-term funding depends on replacing the opaque National Security Surcharge with a transparent ancillary levy that survives political and regulatory scrutiny. | report.html / review_plan | If the levy is blocked or politically reversed, the $50M/month operating funding disappears post-sponsorship and the venue becomes insolvent. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate post-facto GSA/DOI land-use authorization, international banking consortium AML/KYC certification, or political acceptance of the Infrastructure Levy successor mechanism. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **Fragile** — `political_reversal_buffer_surplus` holds in only 27.2% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **Robust**, 50–80% **Marginal**, 20–50% **Fragile**, <20% **Critical**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `political_reversal_buffer_surplus` | >= 0.0000 | model_defined | 27.2% | **Fragile** | fails in the majority of runs |
|  | `phase1_noi_gate_surplus` | >= 0.0000 | report_explicit | 75.3% | **Marginal** | passes more often than not but uncomfortably close |
|  | `levy_coverage_surplus_usd` | >= 0.0000 | report_explicit | 67.7% | **Marginal** | passes more often than not but uncomfortably close |

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `political_reversal_buffer_surplus` | **Fragile** | The `>= 0.0000` requirement fails in the majority of runs (72.8%). External commitments built on this gate are exposed. | `political_reversal_shock_usd` (reduce toward its low bound; quartile Δ-pp -100.0) | Checks whether the $90M ring-fenced reserve can absorb a stated political reversal restoration cost. |
| `phase1_noi_gate_surplus` | **Marginal** | The `>= 0.0000` requirement passes 75.3% of runs — just below the Robust band. The gate passes in most runs, but downstream commitments should not treat it as secure. | `achievable_daily_noi_usd` (improve toward its high bound; quartile Δ-pp +96.9) | Tests whether realised NOI clears the contractual sponsor gate after the relocation blackout consumes operating days. Threshold parameter: `profitability_window_days`. |
| `levy_coverage_surplus_usd` | **Marginal** | The `>= 0.0000` requirement passes 67.7% of runs — close to coin-flip. Downstream commitments should not assume it holds. | `ancillary_gross_revenue_annual_usd` (improve toward its high bound; quartile Δ-pp +84.8) | Tests long-term solvency claim that on-site ancillary services can fund the $50M/month operating deficit. Threshold parameter: `monthly_levy_target_usd`. |

## Failure drivers

For each failing gate (Critical or Fragile): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `political_reversal_buffer_surplus` | `political_reversal_shock_usd` | -100.0 | `political_reversal_shock_usd` below p67 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `political_reversal_shock_usd` | `political_reversal_buffer_surplus` | 177.96 | 2.44 | report_derived |
| 2 | `achievable_daily_noi_usd` | `phase1_noi_gate_surplus` | 67.94 | 2.83 | model_assumption |
| 3 | `ancillary_gross_revenue_annual_usd` | `levy_coverage_surplus_usd` | 57.55 | 2.10 | report_derived |
| 4 | `ancillary_margin_fraction` | `levy_coverage_surplus_usd` | 14.61 | 1.00 | report_derived |

`Basis` values: `report_derived` = bound anchored in the source report's narrative (not externally verified); `model_assumption` = bound is a modelling assumption with no narrative anchor. Neither value is empirical ground truth.

## Confidence and trust boundaries

### Validated

Structural checks that passed (`validation.json`): `json_parse`, `top_level_structure`, `required_fields`, `array_length_caps`, `global_id_uniqueness`, `snake_case_ids`, `depends_on_declared`, `formula_rhs_declared`, `fraction_value_range`, `comment_word_caps`, `source_text_word_caps`, `output_name_present_when_formula_hint`, `output_unit_present_when_formula_hint`, `no_dead_end_variables`, `threshold_friendly_naming`, `shared_pool_legitimacy`, `aggregate_not_bounded`, `requirement_has_margin`, `dropped_signals_schema`.

### Not validated

- real-world accuracy of the input bounds
- independence or correlation assumptions across inputs
- external feasibility of regulatory, grid, supply, or market dependencies
- factual truth of the source plan's narrative claims

### Per-output confidence

| Output | Grade | Declared-source inputs | Bound-width / base |
|---|:---:|---:|---:|
| `phase1_noi_gate_surplus` | **LOW** | 50% | 2.06 |
| `political_reversal_buffer_surplus` | **LOW** | 100% | 2.44 |
| `levy_coverage_surplus_usd` | **LOW** | 100% | 1.55 |
| `phase1_noi_gate_margin` | **LOW** | 50% | 2.06 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `contingency_reserve_usd` | USD | 90,000,000 | 90,000,000 | 90,000,000 |
| `sponsor_capital_at_risk_usd` | USD | 450,000,000 | 450,000,000 | 450,000,000 |
| `phase1_noi_gate_surplus` | USD | -3,650,000 | 480,000 | 9,180,000 |
| `political_reversal_buffer_surplus` | USD | 60,000,000 | 0.0000 | -160,000,000 |
| `levy_coverage_surplus_usd` | USD | -480,000,000 | 0.0000 | 1,650,000,000 |
| `phase1_noi_gate_margin` | USD | -3,650,000 | 480,000 | 9,180,000 |
| `q_levy_coverage` | USD | -480,000,000 | 0.0000 | 1,650,000,000 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 1 in the Fragile band. Worst: `political_reversal_buffer_surplus` at 27.2% pass rate under current bounds.
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
