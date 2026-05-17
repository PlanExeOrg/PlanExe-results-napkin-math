# Assessment: 4-Day Work Week (4DWW) India Pilot

**Type:** public_policy_pilot  
**Primary goal:** Generate robust, attributable evidence over a 48-month controlled pilot to inform national labor-reform tooling on the 4-day work week.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "4-Day Work Week (4DWW) India Pilot",
  "artifact_set": {
    "version": "v46",
    "plan_slug": "20251110_4DWW_India",
    "relative_dir": "output/v46/20251110_4DWW_India"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v46/20251110_4DWW_India",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "fragile",
    "reason": "at least one declared gate has pass rate in 20\u201350% (FRAGILE band)",
    "worst_gate": "sme_admin_overhead_margin_hours_per_week",
    "worst_gate_pass_rate": 0.2352
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "sme_admin_overhead_margin_hours_per_week",
    "voluntary_participation_margin",
    "sustained_productivity_retention_margin"
  ],
  "primary_uncertainty_drivers": [
    "sme_admin_overhead_actual_hours_per_week",
    "monthly_program_operating_cost_inr",
    "sustained_productivity_retention_actual_share"
  ],
  "known_unmodelled_existential_gates": [
    "state_labor_dept_binding_signoff_gate",
    "legal_executive_notification_gate",
    "union_political_acceptance_gate"
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

Tests the formal-track operations envelope against projected monthly program cost; the SME administrative-overhead margin against the 2 worker-hour/week cap; the voluntary-participation margin against the 75% threshold; and the post-incentive productivity-retention margin against the 75% sustained-efficiency target. State Labor Department binding sign-off, legal executive-notification viability, and union/political acceptance are treated as unmodelled existential gates.

**Note:** This assessment is a financial / operational stress test. 3 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `state_labor_dept_binding_signoff_gate` | Premortem A1 and Expert Issue 1.6 name this as the single most critical authority assumption; without it the quarterly decision gates and rollback execution lack enforceable jurisdiction, regardless of any financial or operational margin the model evaluates. | report.html / premortem | Decision-gate paralysis; rollback execution stalls past two quarterly review cycles per Expert Criticism; central PMO cannot enforce standardised metrics or operational rollbacks across the federal/state split. |
| `legal_executive_notification_gate` | Expert Criticism flags reliance on minimal executive notification (rather than full legislative amendment) as a load-bearing legal assumption; if notifications fail or are challenged, the pilot's legal basis collapses without a legislative fallback inside the 12-month launch window. | report.html / expert_criticism | Halting 10% of formal cohort pending clarification; INR 5 crore unplanned legal review; 4-week data collection pause; potential 3–6 month pilot delay per Risk 1. |
| `union_political_acceptance_gate` | Premortem A7 and Risk 5 treat sustained union cooperation as binary; organized opposition, boycotts, or a political-cycle reversal would shut the pilot down independently of any productivity-retention margin the model evaluates. | report.html / premortem | Industrial disputes, boycotts stopping pilot operations, INR 10 crore crisis-communication spend per Risk 5; risk of forced 5-day reversion invalidating the structural-change objective. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate state Labor Departments accept binding PMO tie-breaking vote, executive notification suffices for 4DWW workday redefinition across 24 months, or unions remain cooperative and political climate stable across the 48-month pilot. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **FRAGILE** — `sme_admin_overhead_margin_hours_per_week` holds in only 23.5% of simulated runs under the current input bounds (fails in the majority).
- **FRAGILE** — `voluntary_participation_margin` holds in only 26.3% of simulated runs under the current input bounds (fails in the majority).
- **FRAGILE** — `sustained_productivity_retention_margin` holds in only 25.9% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **ROBUST**, 50–80% **MARGINAL**, 20–50% **FRAGILE**, <20% **DOOM**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `sme_admin_overhead_margin_hours_per_week` | >= 0.0000 | report_inferred | 23.5% | **FRAGILE** | fails in the majority of runs |
|  | `voluntary_participation_margin` | >= 0.0000 | report_inferred | 26.3% | **FRAGILE** | fails in the majority of runs |
|  | `sustained_productivity_retention_margin` | >= 0.0000 | report_inferred | 25.9% | **FRAGILE** | fails in the majority of runs |
|  | `formal_operations_budget_surplus_inr` | >= 0.0000 | report_explicit | 56.0% | **MARGINAL** | passes more often than not but uncomfortably close |

### Aggregation warning

The thresholds above use incompatible units (INR, fraction, hours_per_week) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `sme_admin_overhead_margin_hours_per_week` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (76.5%). External commitments built on this gate are exposed. | `sme_admin_overhead_actual_hours_per_week` (reduce toward its low bound; quartile Δ-pp -76.4) | Positive margin means SMEs can comply without breaching the 2 hr/week ceiling; negative margin triggers the FM2 Data Integrity Collapse path identified in the premortem. Threshold parameter: `sme_admin_overhead_cap_hours_per_week`. |
| `voluntary_participation_margin` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (73.7%). External commitments built on this gate are exposed. | `voluntary_participation_actual_share` (improve toward its high bound; quartile Δ-pp +84.2) | Below zero the cohort loses statistical power and selection bias dominates; the M&E claim on national generalisability cannot be made. Threshold parameter: `voluntary_participation_target_share`. |
| `sustained_productivity_retention_margin` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (74.1%). External commitments built on this gate are exposed. | `sustained_productivity_retention_actual_share` (improve toward its high bound; quartile Δ-pp +73.8) | Tests the structural-vs-subsidised claim; if retention falls below 75%, the national-toolkit recommendation rests on incentive dependency rather than durable productivity change. Threshold parameter: `sustained_productivity_retention_target_share`. |
| `formal_operations_budget_surplus_inr` | **MARGINAL** | The `>= 0.0000` requirement passes 56.0% of runs — close to coin-flip. Downstream commitments should not assume it holds. | `monthly_program_operating_cost_inr` (reduce toward its low bound; quartile Δ-pp -100.0) | Tests whether the 20% non-incentive slice of the formal-track envelope (~INR 280 crore) is sufficient for PMO, audits, liaison-team, and hardware operations across 48 months. Threshold parameter: `total_budget_inr`. |

## Failure drivers

For each failing gate (DOOM or FRAGILE): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `sme_admin_overhead_margin_hours_per_week` | `sme_admin_overhead_actual_hours_per_week` | -76.4 | `sme_admin_overhead_actual_hours_per_week` below p85 |
| `voluntary_participation_margin` | `voluntary_participation_actual_share` | +84.2 | `voluntary_participation_actual_share` above p75 |
| `sustained_productivity_retention_margin` | `sustained_productivity_retention_actual_share` | +73.8 | `sustained_productivity_retention_actual_share` above p85 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `sme_admin_overhead_actual_hours_per_week` | `sme_admin_overhead_margin_hours_per_week` | 93.44 | 1.60 | model_assumption |
| 2 | `monthly_program_operating_cost_inr` | `formal_operations_budget_surplus_inr` | 70.45 | 1.60 | model_assumption |
| 3 | `sustained_productivity_retention_actual_share` | `sustained_productivity_retention_margin` | 39.06 | 0.71 | report_derived |
| 4 | `voluntary_participation_actual_share` | `voluntary_participation_margin` | 34.46 | 0.56 | model_assumption |

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
| `total_program_operating_cost_inr` | **LOW** | 0% | 1.60 |
| `formal_operations_budget_surplus_inr` | **LOW** | 0% | 1.60 |
| `sme_admin_overhead_margin_hours_per_week` | **MEDIUM** | 50% | 1.18 |
| `voluntary_participation_margin` | **MEDIUM** | 50% | 0.38 |
| `sustained_productivity_retention_margin` | **MEDIUM** | 100% | 0.56 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `total_program_operating_cost_inr` | INR | 960,000,000 | 2,400,000,000 | 4,800,000,000 |
| `formal_operations_budget_surplus_inr` | INR | 1,840,000,000 | 400,000,000 | -2,000,000,000 |
| `sme_admin_overhead_margin_hours_per_week` | hours_per_week | 0.5000 | -0.5000 | -2.00 |
| `voluntary_participation_margin` | fraction | -0.2000 | -0.0300 | 0.0500 |
| `sustained_productivity_retention_margin` | fraction | -0.2000 | -0.0500 | 0.0000 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 3 in the FRAGILE band. Worst: `sme_admin_overhead_margin_hours_per_week` at 23.5% pass rate under current bounds.
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
