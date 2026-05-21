# Assessment: Nuuk Community Clay Workshop

**Type:** commercial community-arts venture  
**Primary goal:** Establish a financially resilient community clay workshop in Nuuk on a 2M DKK Year 1 budget, hitting a 40/35/25 revenue mix while preserving a 15% contingency.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "Nuuk Community Clay Workshop",
  "artifact_set": {
    "version": "v58",
    "plan_slug": "20260215_nuuk_clay_workshop",
    "relative_dir": "output/v58/20260215_nuuk_clay_workshop"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v58/20260215_nuuk_clay_workshop",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (Critical band)",
    "worst_gate": "contingency_after_shocks_surplus_dkk",
    "worst_gate_pass_rate": 0.0042
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "contingency_after_shocks_surplus_dkk"
  ],
  "primary_uncertainty_drivers": [
    "year1_revenue_target_dkk",
    "off_peak_hours_per_year"
  ],
  "known_unmodelled_existential_gates": [
    "contractor_labor_law_compliance_gate",
    "utility_variance_authorization_gate",
    "commercial_lease_gate"
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

Year 1 break-even and contingency survival: tests whether the speculative drop-in/rental revenue stream clears its 25% target at the minimum viable hourly rate, and whether the 15% contingency absorbs labor-law reclassification and rental-shortfall shocks.

**Note:** This assessment is a financial / operational stress test. 3 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `contractor_labor_law_compliance_gate` | Plan budgets assume contractor classification; a non-compliance ruling forces mandatory salaried structure and could deplete the 2M DKK budget independently of any operational threshold. | report.html / expert_criticism | Mandatory severance/salary cost overrides the 15% contingency and may consume the entire Year 1 budget. |
| `utility_variance_authorization_gate` | Centralized kiln operation depends on a zoning/utility variance the plan treats as a fixed pre-condition; without it the workshop cannot fire ceramics. | report.html / project_plan | Fit-out cannot complete, Q3 readiness target missed, and no kiln-based revenue is generated. |
| `commercial_lease_gate` | All downstream timelines and material-buffer prepayments are conditional on securing the lease on time; treated as binary in the source narrative. | report.html / expert_criticism | Material buffer prepayment contracts cannot proceed and the September 2026 readiness target is lost. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 1 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate greenlandic labor-law contractor classification, nuuk municipal utility variance for high-draw kiln, or commercial lease near Katuaq by 2026-07-01. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **Critical** — `contingency_after_shocks_surplus_dkk` fails >= 0.0000 in 99.6% of simulated runs under the current input bounds.

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **Robust**, 50–80% **Marginal**, 20–50% **Fragile**, <20% **Critical**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `contingency_after_shocks_surplus_dkk` | >= 0.0000 | model_defined | 0.4% | **Critical** | rarely passes under current bounds |

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `contingency_after_shocks_surplus_dkk` | **Critical** | The `>= 0.0000` requirement is not credible under current bounds: only 0.4% of runs hold. Commitments that depend on this should not be made without revision. | `labor_law_shock_cost_share` (reduce toward its low bound; quartile Δ-pp -1.7) | Top-level viability gate: the single 15% reserve must absorb both named shocks from the same pool. |

## Failure drivers

For each failing gate (Critical or Fragile): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `contingency_after_shocks_surplus_dkk` | `labor_law_shock_cost_share` | -1.7 | no single input restriction sufficient |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `year1_revenue_target_dkk` | `contingency_after_shocks_surplus_dkk` | 0.81 | 0.60 | model_assumption |
| 2 | `off_peak_hours_per_year` | `contingency_after_shocks_surplus_dkk` | 0.56 | 1.00 | model_assumption |

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
| `annual_labor_cost_dkk` | **MEDIUM** | 50% | 0.41 |
| `drop_in_revenue_shortfall_dkk` | **MEDIUM** | 60% | 0.82 |
| `labor_law_shock_dkk` | **MEDIUM** | 67% | 0.70 |
| `contingency_after_shocks_surplus_dkk` | **MEDIUM** | 62% | 0.78 |
| `budget_after_labor_margin_dkk` | **MEDIUM** | 50% | 0.41 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `contingency_reserve_dkk` | DKK | 300,000 | 300,000 | 300,000 |
| `annual_labor_cost_dkk` | DKK | 504,000 | 912,000 | 1,200,000 |
| `drop_in_revenue_shortfall_dkk` | DKK | 204,000 | 420,800 | 564,000 |
| `labor_law_shock_dkk` | DKK | 0.0000 | 250,800 | 420,000 |
| `contingency_after_shocks_surplus_dkk` | DKK | 96,000 | -371,600 | -684,000 |
| `budget_after_labor_margin_dkk` | DKK | 1,496,000 | 1,088,000 | 800,000 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 1 declared gate in the Critical band. Worst: `contingency_after_shocks_surplus_dkk` at 0.4% pass rate under current bounds.
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
