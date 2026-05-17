# Assessment: India Decennial Census 2026–2027

**Type:** national_governance_program  
**Primary goal:** Execute India's postponed decennial census across 1.4B people / 240M+ households between April 2026 and April 2027 under the Pioneer's Gambit strategy, achieving 99%+ coverage, publishing provisional totals within 6 months, and releasing the full caste-inclusive dataset within 18 months of Phase 2 completion.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "India Decennial Census 2026\u20132027",
  "artifact_set": {
    "version": "v46",
    "plan_slug": "20250101_india_census",
    "relative_dir": "output/v46/20250101_india_census"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v46/20250101_india_census",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (DOOM band)",
    "worst_gate": "household_coverage_margin",
    "worst_gate_pass_rate": 0.0098
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "household_coverage_margin",
    "device_audit_failure_margin",
    "provisional_publish_timing_margin_months",
    "mttr_margin_hours"
  ],
  "primary_uncertainty_drivers": [
    "actual_mttr_hours",
    "actual_provisional_publish_months",
    "actual_device_audit_failure_share"
  ],
  "known_unmodelled_existential_gates": [
    "caste_methodology_q4_2025_lockdown_gate",
    "judicial_review_board_constitution_gate",
    "state_government_mou_cooperation_gate"
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

Tests the budget overrun margin against the ₹15,000 crore ceiling; the household-coverage margin against the 99% target; the provisional-publish timing margin against the 6-month deadline; the cloud-ingestion MTTR margin against the 4-hour ceiling; and the device-audit-failure margin against the 1% threshold. Caste-methodology Q4 2025 lockdown, Judicial Review Board constitution by Q3 2025, and state-government MoU cooperation are treated as unmodelled existential gates.

**Note:** This assessment is a financial / operational stress test. 3 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `caste_methodology_q4_2025_lockdown_gate` | Expert Issue 1 and Assumption Issue 1 name this as the load-bearing political-credibility assumption; training 3M enumerators on a moving methodology invalidates the entire data-integrity argument regardless of any operational margin the model evaluates. | report.html / expert_criticism | Retraining and manual reprint costs ₹50–100 crore per Issue 1 sensitivity; quality-validation error rates spike from 5% to 15–20%; statistical-body credibility rejection invalidates the caste-table milestone. |
| `judicial_review_board_constitution_gate` | Decision 4 routes all data-sequencing disputes through the JRB; without statutory authority before Phase 1, the 6-month provisional-release deadline cannot be defended against state non-cooperation (Risk 2). | report.html / review_plan | Provisional release slips past 6 months per Risk 2 sensitivity (2–3 month aggregation delay); delimitation deadline missed; political crisis around constituency boundaries. |
| `state_government_mou_cooperation_gate` | Decision 6 and Assumption Q7 treat state-machinery cooperation as binary; without 80% local-staff dedication the 72-hour paper-audit window collapses and the Pioneer's Gambit redundancy fails on the 10% of blocks the satellite hubs cover. | report.html / premortem | Paper-audit capacity falls below the 72-hour window; digital-failure scenarios cascade directly into coverage gaps; the 99% target becomes unreachable in non-cooperating states (Risk 2). |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate ECI and NSC sign off on the final caste methodology by Q4 2025, judicial Review Board legally constituted with statutory authority by Q3 2025, or state governments commit 80% of local staff to paper audits and dual supervision. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **DOOM** — `household_coverage_margin` fails >= 0.0000 in 99.0% of simulated runs under the current input bounds.
- **DOOM** — `device_audit_failure_margin` fails >= 0.0000 in 98.6% of simulated runs under the current input bounds.
- **FRAGILE** — `provisional_publish_timing_margin_months` holds in only 33.8% of simulated runs under the current input bounds (fails in the majority).
- **FRAGILE** — `mttr_margin_hours` holds in only 34.1% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **ROBUST**, 50–80% **MARGINAL**, 20–50% **FRAGILE**, <20% **DOOM**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `household_coverage_margin` | >= 0.0000 | report_explicit | 1.0% | **DOOM** | rarely passes under current bounds |
|  | `device_audit_failure_margin` | >= 0.0000 | report_explicit | 1.4% | **DOOM** | rarely passes under current bounds |
|  | `provisional_publish_timing_margin_months` | >= 0.0000 | report_explicit | 33.8% | **FRAGILE** | fails in the majority of runs |
|  | `mttr_margin_hours` | >= 0.0000 | report_explicit | 34.1% | **FRAGILE** | fails in the majority of runs |
|  | `budget_overrun_margin_inr` | >= 0.0000 | report_explicit | 62.4% | **MARGINAL** | passes more often than not but uncomfortably close |

### Aggregation warning

The thresholds above use incompatible units (INR, fraction, hours, months) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `household_coverage_margin` | **DOOM** | The `>= 0.0000` requirement is not credible under current bounds: only 1.0% of runs hold. Commitments that depend on this should not be made without revision. | `actual_household_coverage_share` (improve toward its high bound; quartile Δ-pp +3.9) | Positive margin satisfies the primary viability criterion; negative margin invalidates the entire Pioneer's Gambit thesis and the methodological-credibility metric tied to statistical-body acceptance. Threshold parameter: `household_coverage_target_share`. |
| `device_audit_failure_margin` | **DOOM** | The `>= 0.0000` requirement is not credible under current bounds: only 1.4% of runs hold. Commitments that depend on this should not be made without revision. | `actual_device_audit_failure_share` (reduce toward its low bound; quartile Δ-pp -5.7) | Positive margin keeps supervisory penalties dormant and the chain-of-custody intact; negative margin escalates toward the Risk 5 10% loss scenario and the ₹400–600 crore emergency-procurement spend. Threshold parameter: `device_audit_failure_threshold_share`. |
| `provisional_publish_timing_margin_months` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (66.2%). External commitments built on this gate are exposed. | `actual_provisional_publish_months` (reduce toward its low bound; quartile Δ-pp -100.0) | Positive margin clears the 6-month deadline for delimitation data; negative margin triggers the political-crisis path that the data-sequencing strategy (population before caste) is designed to prevent. Threshold parameter: `provisional_publish_target_months`. |
| `mttr_margin_hours` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (65.9%). External commitments built on this gate are exposed. | `actual_mttr_hours` (reduce toward its low bound; quartile Δ-pp -85.5) | Positive margin keeps salary validation and real-time monitoring intact; negative margin triggers the Expert Issue 3 cascade of supervisor-review delay, salary delay, attrition, and timeline slip. Threshold parameter: `mttr_max_hours`. |
| `budget_overrun_margin_inr` | **MARGINAL** | The `>= 0.0000` requirement passes 62.4% of runs — close to coin-flip. Downstream commitments should not assume it holds. | `actual_total_census_spend_inr` (reduce toward its low bound; quartile Δ-pp -100.0) | Positive margin keeps the project within budget; negative margin forces austerity that the Risk 7 mitigation says will cut verification-survey quality assurance. Threshold parameter: `budget_high_inr`. |

## Failure drivers

For each failing gate (DOOM or FRAGILE): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `household_coverage_margin` | `actual_household_coverage_share` | +3.9 | no single input restriction sufficient |
| `device_audit_failure_margin` | `actual_device_audit_failure_share` | -5.7 | no single input restriction sufficient |
| `provisional_publish_timing_margin_months` | `actual_provisional_publish_months` | -100.0 | `actual_provisional_publish_months` below p67 |
| `mttr_margin_hours` | `actual_mttr_hours` | -85.5 | `actual_mttr_hours` below p75 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `actual_mttr_hours` | `mttr_margin_hours` | 137.72 | 2.44 | report_derived |
| 2 | `actual_provisional_publish_months` | `provisional_publish_timing_margin_months` | 56.73 | 0.86 | model_assumption |
| 3 | `actual_device_audit_failure_share` | `device_audit_failure_margin` | 26.60 | 4.75 | report_derived |
| 4 | `actual_total_census_spend_inr` | `budget_overrun_margin_inr` | 14.26 | 0.38 | report_derived |
| 5 | `actual_household_coverage_share` | `household_coverage_margin` | 0.46 | 0.12 | report_derived |

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
| `budget_overrun_margin_inr` | **HIGH** | 100% | 0.38 |
| `household_coverage_margin` | **HIGH** | 100% | 0.12 |
| `provisional_publish_timing_margin_months` | **LOW** | 0% | 0.86 |
| `mttr_margin_hours` | **LOW** | 100% | 1.97 |
| `device_audit_failure_margin` | **LOW** | 100% | 4.75 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `budget_overrun_margin_inr` | INR | 30,000,000,000 | 5,000,000,000 | -25,000,000,000 |
| `household_coverage_margin` | fraction | -0.1100 | -0.0200 | 0.0050 |
| `provisional_publish_timing_margin_months` | months | 2.00 | -1.00 | -4.00 |
| `mttr_margin_hours` | hours | 1.00 | -0.5000 | -4.00 |
| `device_audit_failure_margin` | fraction | 0.0050 | -0.0100 | -0.0900 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 2 declared gates in the DOOM band; 2 in the FRAGILE band. Worst: `household_coverage_margin` at 1.0% pass rate under current bounds.
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
