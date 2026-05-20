# Assessment: 4-Day Work Week Pilot India

**Type:** public_policy_pilot  
**Primary goal:** Generate evidence over 48 months to inform national 4DWW labor reform via formal-sector pilots with 50% SME inclusion.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "4-Day Work Week Pilot India",
  "artifact_set": {
    "version": "v49",
    "plan_slug": "20251110_4DWW_India",
    "relative_dir": "output/v49/20251110_4DWW_India"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v49/20251110_4DWW_India",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (Critical band)",
    "worst_gate": "contingency_buffer_inr_crore",
    "worst_gate_pass_rate": 0.0
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "contingency_buffer_inr_crore",
    "sme_cohort_representation_margin"
  ],
  "primary_uncertainty_drivers": [
    "actual_sme_cohort_share"
  ],
  "known_unmodelled_existential_gates": [
    "state_labor_department_sign_off_gate",
    "executive_notification_legal_gate",
    "pii_tokenization_compliance_gate"
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

Tests whether the INR 2,000 crore envelope, 70/30 split, and 10% contingency can absorb the named stress-test shocks (post-incentive overrun, SME redesign, legal delay) while sustaining voluntary opt-in above the load-bearing threshold.

**Note:** This assessment is a financial / operational stress test. 3 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `state_labor_department_sign_off_gate` | Pilot launch requires written No Objection affidavits from State Labour Secretaries by Month 3 and joint sign-off on operational gates. | report.html / premortem | Pilots cannot legally operate in non-cooperating states; PMO loses tie-breaking authority and decision gates stall. |
| `executive_notification_legal_gate` | The pilot relies on executive notifications rather than legislative amendment to alter workday/overtime definitions for 24 months. | report.html / expert_criticism | Jurisdictional litigation invalidates the INR 2,000 crore evidence mandate. |
| `pii_tokenization_compliance_gate` | Data privacy compliance under NITI Aayog/MeitY rules is required for third-party auditor access to UMF data. | report.html / data_collection | Audit pipeline blocked; evidence cannot be independently verified and the pilot's central deliverable fails. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate state Labor Department sign-off, executive notification legal validity, or PII tokenization compliance. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **Critical** — `contingency_buffer_inr_crore` fails >= 0.0000 in 100.0% of simulated runs under the current input bounds.
- **Fragile** — `sme_cohort_representation_margin` holds in only 40.4% of simulated runs under the current input bounds (fails in the majority).
- **Scenario warn (low)** — `sme_admin_margin`: Missing dependency 'sme_admin_hours_per_week_target' (declared in missing_values_to_estimate with no value and no bounds entry).
- **Scenario warn (base)** — `sme_admin_margin`: Missing dependency 'sme_admin_hours_per_week_target' (declared in missing_values_to_estimate with no value and no bounds entry).
- **Scenario warn (high)** — `sme_admin_margin`: Missing dependency 'sme_admin_hours_per_week_target' (declared in missing_values_to_estimate with no value and no bounds entry).
- **Model collapse** — `sme_admin_margin` came back blank in 100.0% of runs. An input is missing or a denominator can legitimately land at zero. Fix the inputs and re-run.
- **Still missing input** — `sme_admin_hours_per_week_target`: The ASI threshold the SME compliance design must beat; ≤2 worker-hours per week.

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **Robust**, 50–80% **Marginal**, 20–50% **Fragile**, <20% **Critical**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `contingency_buffer_inr_crore` | >= 0.0000 | report_inferred | 0.0% | **Critical** | rarely passes under current bounds |
|  | `sme_cohort_representation_margin` | >= 0.0000 | report_explicit | 40.4% | **Fragile** | fails in the majority of runs |
|  | `formal_sector_budget_inr_crore` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |
|  | `contingency_reserve_inr_crore` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |
|  | `sme_admin_margin` | >= 0.0000 | model_defined | n/a | **UNKNOWN** | no valid runs |

### Aggregation warning

The thresholds above use incompatible units (INR_crore, fraction, hours_per_week) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `contingency_buffer_inr_crore` | **Critical** | The `>= 0.0000` requirement is not credible under current bounds: only 0.0% of runs hold. Commitments that depend on this should not be made without revision. | Saturated failure: pass rate is 0.0% and no single input quartile movement changes that. Quartile sensitivity is not informative; audit the input bounds and the threshold definition. | Tests whether the ring-fenced reserve absorbs the named high-severity shocks; positive means coverage. Threshold parameter: `post_incentive_overrun_shock_inr_crore`. |
| `sme_cohort_representation_margin` | **Fragile** | The `>= 0.0000` requirement fails in the majority of runs (59.6%). External commitments built on this gate are exposed. | `actual_sme_cohort_share` (improve toward its high bound; quartile Δ-pp +100.0) | Tests whether the 50% SME mandate is met; failure invalidates the generalizability of evidence. Threshold parameter: `sme_cohort_share_target`. |

## Failure drivers

For each failing gate (Critical or Fragile): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `contingency_buffer_inr_crore` | (saturated failure) | n/a | saturated failure: no single input restriction can lift the pass rate; revisit bounds and threshold |
| `sme_cohort_representation_margin` | `actual_sme_cohort_share` | +100.0 | `actual_sme_cohort_share` above p50 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

Note: the saturated Critical gate `contingency_buffer_inr_crore` is absent from the ranking because no single missing-input restriction can lift its pass rate under current bounds. The inputs below target the next most decision-relevant non-saturated gates; the saturated gate needs a bounds or threshold-definition audit, not a single input fix.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `actual_sme_cohort_share` | `sme_cohort_representation_margin` | 29.80 | 0.50 | model_assumption |

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
| `contingency_buffer_inr_crore` | **MEDIUM** | 33% | 0.89 |
| `sme_admin_margin` | **LOW** | 0% | 1.75 |
| `sme_cohort_representation_margin` | **LOW** | 0% | 0.50 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `formal_sector_budget_inr_crore` | INR_crore | 1,400 | 1,400 | 1,400 |
| `contingency_reserve_inr_crore` | INR_crore | 200.00 | 200.00 | 200.00 |
| `contingency_buffer_inr_crore` | INR_crore | -300.00 | -725.00 | -1,150 |
| `sme_cohort_representation_margin` | fraction | -0.1500 | 0.0000 | 0.1000 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 1 declared gate in the Critical band; 1 in the Fragile band. Worst: `contingency_buffer_inr_crore` at 0.0% pass rate under current bounds.
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
