# Assessment: India Decennial Census 2026-2027 (Pioneer's Gambit)

**Type:** public_sector_logistics  
**Primary goal:** Achieve 99%+ household enumeration coverage with sequenced political data release within budget and timeline.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "India Decennial Census 2026-2027 (Pioneer's Gambit)",
  "artifact_set": {
    "version": "v58",
    "plan_slug": "20250101_india_census",
    "relative_dir": "output/v58/20250101_india_census"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v58/20250101_india_census",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (Critical band)",
    "worst_gate": "household_coverage_margin",
    "worst_gate_pass_rate": 0.0512
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "household_coverage_margin",
    "provisional_release_timing_margin_months",
    "ingestion_mttr_margin_hours"
  ],
  "primary_uncertainty_drivers": [
    "actual_ingestion_mttr_hours",
    "expected_contingency_draw_crore",
    "actual_provisional_release_months"
  ],
  "known_unmodelled_existential_gates": [
    "caste_methodology_lockdown_gate",
    "judicial_review_board_authority_gate",
    "presidential_census_authorization_gate"
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

Tests whether budget, enumerator pay validation cycle, device integrity, ingestion pipeline MTTR, and political-release timing leave positive margin against stated thresholds.

**Note:** This assessment is a financial / operational stress test. 3 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `caste_methodology_lockdown_gate` | Mass training of 3M enumerators presumes ECI/NSC sign-off on the final caste data dictionary and linkage logic before deployment. | report.html / expert_criticism | Late methodology shifts invalidate training, spike error rates, and risk international statistical-body rejection — independent of any financial threshold. |
| `judicial_review_board_authority_gate` | Provides binding arbitration over methodology disputes and sequencing; absent it, regional non-cooperation cannot be resolved within the 6-month window. | report.html / project_plan | Methodology disputes escalate to constitutional crisis, freezing delimitation regardless of operational performance. |
| `presidential_census_authorization_gate` | Mandatory legal prerequisite for the census to occur at all; no quantifiable threshold the simulation can test. | report.html / project_plan | Without authorization the census cannot lawfully proceed, ending the plan irrespective of budget or coverage. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate q4 2025 legal lock-in of caste methodology, statutory Judicial Review Board by Q3 2025, or presidential authorization under Census Act 1948. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **Critical** — `household_coverage_margin` fails >= 0.0000 in 94.9% of simulated runs under the current input bounds.
- **Fragile** — `provisional_release_timing_margin_months` holds in only 40.1% of simulated runs under the current input bounds (fails in the majority).
- **Fragile** — `ingestion_mttr_margin_hours` holds in only 24.2% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **Robust**, 50–80% **Marginal**, 20–50% **Fragile**, <20% **Critical**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `household_coverage_margin` | >= 0.0000 | report_explicit | 5.1% | **Critical** | rarely passes under current bounds |
|  | `provisional_release_timing_margin_months` | >= 0.0000 | report_explicit | 40.1% | **Fragile** | fails in the majority of runs |
|  | `ingestion_mttr_margin_hours` | >= 0.0000 | report_explicit | 24.2% | **Fragile** | fails in the majority of runs |
|  | `budget_surplus_crore` | >= 0.0000 | report_explicit | 67.4% | **Marginal** | passes more often than not but uncomfortably close |
|  | `contingency_buffer_crore` | >= 0.0000 | report_explicit | 66.1% | **Marginal** | passes more often than not but uncomfortably close |

### Aggregation warning

The thresholds above use incompatible units (crore_INR, fraction, hours, months) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `household_coverage_margin` | **Critical** | The `>= 0.0000` requirement is not credible under current bounds: only 5.1% of runs hold. Commitments that depend on this should not be made without revision. | `actual_household_coverage` (improve toward its high bound; quartile Δ-pp +20.5) | Primary success gate of the census; positive means the headcount criterion passes. Threshold parameter: `target_household_coverage`. |
| `provisional_release_timing_margin_months` | **Fragile** | The `>= 0.0000` requirement fails in the majority of runs (59.9%). External commitments built on this gate are exposed. | `actual_provisional_release_months` (reduce toward its low bound; quartile Δ-pp -100.0) | Political delimitation gate; positive = data released ahead of the deadline. Threshold parameter: `provisional_release_deadline_months`. |
| `ingestion_mttr_margin_hours` | **Fragile** | The `>= 0.0000` requirement fails in the majority of runs (75.8%). External commitments built on this gate are exposed. | `actual_ingestion_mttr_hours` (reduce toward its low bound; quartile Δ-pp -96.8) | Pipeline stability gates 50% contingent pay; positive = validation backlog avoided. Threshold parameter: `ingestion_mttr_target_hours`. |
| `budget_surplus_crore` | **Marginal** | The `>= 0.0000` requirement passes 67.4% of runs — close to coin-flip. Downstream commitments should not assume it holds. | `expected_total_cost_crore` (reduce toward its low bound; quartile Δ-pp -100.0) | Tests fiscal viability before contingency draw; positive = within stated cap. Threshold parameter: `budget_ceiling_crore`. |
| `contingency_buffer_crore` | **Marginal** | The `>= 0.0000` requirement passes 66.1% of runs — close to coin-flip. Downstream commitments should not assume it holds. | `expected_contingency_draw_crore` (reduce toward its low bound; quartile Δ-pp -100.0) | Tests whether the single 750-crore reserve absorbs device, satellite, and paper-audit shocks per the plan's stated single-pool framing. Threshold parameter: `contingency_fund_crore`. |

## Failure drivers

For each failing gate (Critical or Fragile): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `household_coverage_margin` | `actual_household_coverage` | +20.5 | `actual_household_coverage` above p95 |
| `provisional_release_timing_margin_months` | `actual_provisional_release_months` | -100.0 | `actual_provisional_release_months` below p50 |
| `ingestion_mttr_margin_hours` | `actual_ingestion_mttr_hours` | -96.8 | `actual_ingestion_mttr_hours` below p75 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `actual_ingestion_mttr_hours` | `ingestion_mttr_margin_hours` | 146.79 | 2.00 | model_assumption |
| 2 | `expected_contingency_draw_crore` | `contingency_buffer_crore` | 56.48 | 1.67 | report_derived |
| 3 | `actual_provisional_release_months` | `provisional_release_timing_margin_months` | 49.94 | 0.83 | model_assumption |
| 4 | `expected_total_cost_crore` | `budget_surplus_crore` | 12.81 | 0.39 | report_derived |
| 5 | `actual_household_coverage` | `household_coverage_margin` | 1.86 | 0.10 | model_assumption |

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
| `household_coverage_margin` | **LOW** | 0% | 0.10 |
| `budget_surplus_crore` | **HIGH** | 100% | 0.39 |
| `provisional_release_timing_margin_months` | **LOW** | 0% | 0.83 |
| `ingestion_mttr_margin_hours` | **LOW** | 0% | 2.00 |
| `contingency_buffer_crore` | **LOW** | 100% | 1.67 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `household_coverage_margin` | fraction | -0.0900 | 0.0000 | 0.0050 |
| `budget_surplus_crore` | crore_INR | 3,000 | 1,000 | -2,500 |
| `provisional_release_timing_margin_months` | months | 2.00 | 0.0000 | -3.00 |
| `ingestion_mttr_margin_hours` | hours | 2.00 | 0.0000 | -6.00 |
| `contingency_buffer_crore` | crore_INR | 550.00 | 150.00 | -450.00 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 1 declared gate in the Critical band; 2 in the Fragile band. Worst: `household_coverage_margin` at 5.1% pass rate under current bounds.
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
