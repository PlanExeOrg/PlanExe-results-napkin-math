# Assessment: Nuuk Community Clay Workshop

**Type:** commercial community venture  
**Primary goal:** Launch a financially viable community clay workshop in Nuuk by 2026-09-15 within a 2M DKK Year 1 budget.

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
    "version": "v49",
    "plan_slug": "20260215_nuuk_clay_workshop",
    "relative_dir": "output/v49/20260215_nuuk_clay_workshop"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v49/20260215_nuuk_clay_workshop",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (Critical band)",
    "worst_gate": "drop_in_revenue_surplus_dkk",
    "worst_gate_pass_rate": 0.0
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "drop_in_revenue_surplus_dkk"
  ],
  "primary_uncertainty_drivers": [],
  "known_unmodelled_existential_gates": [
    "contractor_labor_law_compliance_gate",
    "utility_variance_approval_gate",
    "commercial_lease_secured_gate"
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

Tests Year 1 viability of the 'Builder's Balance' plan against fixed labor cost, off-peak rental revenue, contingency depletion shocks, and Taster Session conversion.

**Note:** This assessment is a financial / operational stress test. 3 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `contractor_labor_law_compliance_gate` | Entire 2-FTE-equivalent fixed-cost base assumes contractor classification is lawful; if reclassified, salary and severance obligations would invalidate the budget structure. | report.html / expert_criticism | Contracts must halt and the plan must pivot to a salaried structure with 20-35% higher fixed labor cost. |
| `utility_variance_approval_gate` | High-draw kiln requires a C1 zoning variance; without it, fit-out cannot complete and the September 2026 readiness date fails. | report.html / project_plan | Fit-out stalls, Q3 peak revenue window is missed, and operational launch slips into low season. |
| `commercial_lease_secured_gate` | All location-dependent timelines (fit-out, utility, kiln install) anchor to the July lease date; without it the readiness target collapses. | report.html / review_plan | Operational readiness target of 2026-09-15 is threatened and material buffer order is automatically halved. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate greenlandic contractor staffing legality, nuuk municipal utility variance approval, or katuaq-area commercial lease secured by 2026-07-01. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **Critical** — `drop_in_revenue_surplus_dkk` fails >= 0.0000 in 100.0% of simulated runs under the current input bounds.
- **Still missing input** — `taster_conversion_minimum_threshold`: Explicit gate at 12.5% below which Taster budget is redirected; needed for conversion-margin calculation.

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **Robust**, 50–80% **Marginal**, 20–50% **Fragile**, <20% **Critical**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `drop_in_revenue_surplus_dkk` | >= 0.0000 | model_defined | 0.0% | **Critical** | rarely passes under current bounds |
|  | `contingency_reserve_dkk` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |
|  | `drop_in_expected_revenue_dkk` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |
|  | `annual_labor_cost_dkk` | >= 0.0000 | model_defined | 100.0% | **Robust** | passes in the strong majority of runs |
|  | `budget_after_labor_margin_dkk` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `drop_in_revenue_surplus_dkk` | **Critical** | The `>= 0.0000` requirement is not credible under current bounds: only 0.0% of runs hold. Commitments that depend on this should not be made without revision. | Saturated failure: pass rate is 0.0% and no single input quartile movement changes that. Quartile sensitivity is not informative; audit the input bounds and the threshold definition. | Direct test of the highest-risk revenue stream; positive means the speculative rental segment clears its share. Threshold parameter: `drop_in_revenue_share`. |

## Failure drivers

For each failing gate (Critical or Fragile): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `drop_in_revenue_surplus_dkk` | (saturated failure) | n/a | saturated failure: no single input restriction can lift the pass rate; revisit bounds and threshold |

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
| `drop_in_expected_revenue_dkk` | **LOW** | 0% | 0.79 |
| `drop_in_revenue_surplus_dkk` | **LOW** | 0% | 0.76 |
| `annual_labor_cost_dkk` | **LOW** | 0% | 0.65 |
| `budget_after_labor_margin_dkk` | **LOW** | 0% | 0.65 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `contingency_reserve_dkk` | DKK | 300,000 | 300,000 | 300,000 |
| `drop_in_expected_revenue_dkk` | DKK | 13,200 | 69,300 | 176,000 |
| `drop_in_revenue_surplus_dkk` | DKK | -166,800 | -380,700 | -664,000 |
| `annual_labor_cost_dkk` | DKK | 720,000 | 1,020,000 | 1,380,000 |
| `budget_after_labor_margin_dkk` | DKK | 980,000 | 680,000 | 320,000 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 1 declared gate in the Critical band. Worst: `drop_in_revenue_surplus_dkk` at 0.0% pass rate under current bounds.
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
