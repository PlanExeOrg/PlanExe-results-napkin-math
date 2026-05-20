# Assessment: India Decennial Census 2026-27 (Pioneer's Gambit)

**Type:** mega_scale_national_logistics  
**Primary goal:** Execute the decennial population and caste census across 28 states and 8 UTs (1.4B people, 240M households, 3M enumerators) between April 2026 and April 2027, achieving 99%+ household coverage, releasing provisional totals within 6 months of Phase 2 and the full caste dataset within 18 months, on a ₹12,000–15,000 crore budget.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "India Decennial Census 2026-27 (Pioneer's Gambit)",
  "artifact_set": {
    "version": "v49",
    "plan_slug": "20250101_india_census",
    "relative_dir": "output/v49/20250101_india_census"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v49/20250101_india_census",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (Critical band)",
    "worst_gate": "household_coverage_margin",
    "worst_gate_pass_rate": 0.0331
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "household_coverage_margin",
    "ingestion_mttr_margin_hours",
    "device_integrity_margin",
    "provisional_release_timing_margin_months"
  ],
  "primary_uncertainty_drivers": [
    "actual_device_audit_failure_share",
    "actual_ingestion_mttr_hours",
    "actual_provisional_release_months"
  ],
  "known_unmodelled_existential_gates": [
    "eci_nsc_caste_methodology_signoff_gate",
    "judicial_review_board_statutory_authority_gate",
    "state_mou_eighty_percent_staff_dedication_gate",
    "census_act_presidential_authorization_gate"
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

Tests the household-coverage margin against the 99% gate; the budget surplus against the ₹15,000 crore ceiling; the provisional-release-timing margin against the 6-month post-Phase-2 deadline; the ingestion-pipeline MTTR margin against the 4-hour Issue-3 target; and the device-audit-failure margin against the 1% supervisory-penalty trigger. ECI/NSC caste-methodology sign-off, Judicial Review Board statutory authority, and Census Act presidential authorization are treated as unmodelled existential gates.

**Note:** This assessment is a financial / operational stress test. 4 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `eci_nsc_caste_methodology_signoff_gate` | Issue 1 / Expert Criticism: training 3M enumerators on a moving methodology is catastrophic; without ECI/NSC lockdown by Dec 2025 the entire credibility-and-validation chain collapses regardless of operational success. | report.html / expert_criticism | Caste-data invalidation by statistical bodies; retraining cost ₹50–100 crore; quality-validation error rates spike from 5% to 15-20%; ROI drops 3-5%. |
| `judicial_review_board_statutory_authority_gate` | Decision 4 governance hinge: without the JRB the data-release-sequencing arbitration mechanism collapses; provisional-vs-caste sequencing becomes politically litigable mid-Phase-2. | report.html / review_plan | JRB arbitration delays exceed 6 months; provisional release missed; delimitation political crisis cascades. |
| `state_mou_eighty_percent_staff_dedication_gate` | Risk 2 / Question 7: without signed state MoUs the paper-audit-within-72-hours commitment becomes unilateral federal action; states fearing delimitation impact can sabotage by withholding revenue staff. | report.html / selected_scenario | Paper audits cannot meet 72-hour window; Pioneer's Gambit redundancy thesis collapses; coverage drops to digital-only success rate. |
| `census_act_presidential_authorization_gate` | Mandatory legal prerequisite — no field operation can begin without it; not a probabilistic gate but treated as a fixed input by the rest of the model. | report.html / project_plan | All field operations halt; ₹12,000-15,000 crore allocation cannot be drawn; constitutional/legal crisis. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate ECI and NSC sign off on the finalized caste linkage logic and acceptance thresholds by Q4 2025, judicial Review Board legally constituted with statutory authority over data disputes by Q3 2025, moUs from MT/WY/ID state governments dedicating ≥80% of local staff to audit support and dual supervision, or president of India authorizes execution under Census Act 1948 prior to Phase 1. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **Critical** — `household_coverage_margin` fails >= 0.0000 in 96.7% of simulated runs under the current input bounds.
- **Critical** — `ingestion_mttr_margin_hours` fails >= 0.0000 in 80.6% of simulated runs under the current input bounds.
- **Critical** — `device_integrity_margin` fails >= 0.0000 in 86.2% of simulated runs under the current input bounds.
- **Fragile** — `provisional_release_timing_margin_months` holds in only 25.4% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **Robust**, 50–80% **Marginal**, 20–50% **Fragile**, <20% **Critical**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `household_coverage_margin` | >= 0.0000 | report_explicit | 3.3% | **Critical** | rarely passes under current bounds |
|  | `ingestion_mttr_margin_hours` | >= 0.0000 | report_explicit | 19.4% | **Critical** | rarely passes under current bounds |
|  | `device_integrity_margin` | >= 0.0000 | report_explicit | 13.8% | **Critical** | rarely passes under current bounds |
|  | `provisional_release_timing_margin_months` | >= 0.0000 | report_explicit | 25.4% | **Fragile** | fails in the majority of runs |
|  | `budget_surplus_crore` | >= 0.0000 | report_explicit | 56.2% | **Marginal** | passes more often than not but uncomfortably close |

### Aggregation warning

The thresholds above use incompatible units (INR_crore, fraction, hours, months) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `household_coverage_margin` | **Critical** | The `>= 0.0000` requirement is not credible under current bounds: only 3.3% of runs hold. Commitments that depend on this should not be made without revision. | `actual_household_coverage_share` (improve toward its high bound; quartile Δ-pp +13.2) | Positive margin validates the Pioneer's Gambit at the primary success criterion; negative margin invalidates the credibility of the entire census regardless of timeline. Threshold parameter: `household_coverage_target`. |
| `ingestion_mttr_margin_hours` | **Critical** | The `>= 0.0000` requirement is not credible under current bounds: only 19.4% of runs hold. Commitments that depend on this should not be made without revision. | `actual_ingestion_mttr_hours` (reduce toward its low bound; quartile Δ-pp -77.5) | Positive margin keeps validation and 50% performance pay flowing; negative margin breaks the Decision-5 incentive structure and triggers attrition cascade. Threshold parameter: `ingestion_mttr_target_hours`. |
| `device_integrity_margin` | **Critical** | The `>= 0.0000` requirement is not credible under current bounds: only 13.8% of runs hold. Commitments that depend on this should not be made without revision. | `actual_device_audit_failure_share` (reduce toward its low bound; quartile Δ-pp -55.0) | Positive margin keeps device-fleet penalties from cascading into supervisory pay; negative margin compounds Risk-5 emergency procurement with morale collapse. Threshold parameter: `device_audit_failure_threshold`. |
| `provisional_release_timing_margin_months` | **Fragile** | The `>= 0.0000` requirement fails in the majority of runs (74.6%). External commitments built on this gate are exposed. | `actual_provisional_release_months` (reduce toward its low bound; quartile Δ-pp -100.0) | Positive margin secures the delimitation handoff to ECI on time; negative margin triggers Risk-2 political crisis and 6-month criterion failure. Threshold parameter: `provisional_release_deadline_months`. |
| `budget_surplus_crore` | **Marginal** | The `>= 0.0000` requirement passes 56.2% of runs — close to coin-flip. Downstream commitments should not assume it holds. | `actual_total_cost_crore` (reduce toward its low bound; quartile Δ-pp -100.0) | Positive surplus preserves the 5% contingency and DAMF reserves; negative surplus triggers Risk-7 austerity that cuts the verification-survey QA backstop. Threshold parameter: `budget_ceiling_crore`. |

## Failure drivers

For each failing gate (Critical or Fragile): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `household_coverage_margin` | `actual_household_coverage_share` | +13.2 | no single input restriction sufficient |
| `ingestion_mttr_margin_hours` | `actual_ingestion_mttr_hours` | -77.5 | `actual_ingestion_mttr_hours` below p85 |
| `device_integrity_margin` | `actual_device_audit_failure_share` | -55.0 | `actual_device_audit_failure_share` below p85 |
| `provisional_release_timing_margin_months` | `actual_provisional_release_months` | -100.0 | `actual_provisional_release_months` below p75 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `actual_device_audit_failure_share` | `device_integrity_margin` | 166.13 | 3.50 | model_assumption |
| 2 | `actual_ingestion_mttr_hours` | `ingestion_mttr_margin_hours` | 156.18 | 2.50 | report_derived |
| 3 | `actual_provisional_release_months` | `provisional_release_timing_margin_months` | 49.70 | 0.67 | report_derived |
| 4 | `actual_total_cost_crore` | `budget_surplus_crore` | 13.15 | 0.30 | report_derived |
| 5 | `actual_household_coverage_share` | `household_coverage_margin` | 1.88 | 0.15 | report_derived |

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
| `household_coverage_margin` | **HIGH** | 100% | 0.15 |
| `budget_surplus_crore` | **HIGH** | 100% | 0.30 |
| `provisional_release_timing_margin_months` | **MEDIUM** | 100% | 0.67 |
| `ingestion_mttr_margin_hours` | **LOW** | 100% | 2.50 |
| `device_integrity_margin` | **LOW** | 0% | 3.50 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `household_coverage_margin` | fraction | -0.1400 | 0.0000 | 0.0050 |
| `budget_surplus_crore` | INR_crore | 2,500 | 0.0000 | -2,000 |
| `provisional_release_timing_margin_months` | months | 1.00 | 0.0000 | -3.00 |
| `ingestion_mttr_margin_hours` | hours | 2.00 | 0.0000 | -8.00 |
| `device_integrity_margin` | fraction | 0.0050 | 0.0000 | -0.0300 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 3 declared gates in the Critical band; 1 in the Fragile band. Worst: `household_coverage_margin` at 3.3% pass rate under current bounds.
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
