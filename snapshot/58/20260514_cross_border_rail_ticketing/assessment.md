# Assessment: EU Cross-Border Rail Through-Ticketing Coordination Program

**Type:** public_coordination_program  
**Primary goal:** Achieve 40% of eligible cross-border journeys sold as single through-tickets within five years, supported by binding OSDM standards and a solvent clearing mechanism.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "EU Cross-Border Rail Through-Ticketing Coordination Program",
  "artifact_set": {
    "version": "v58",
    "plan_slug": "20260514_cross_border_rail_ticketing",
    "relative_dir": "output/v58/20260514_cross_border_rail_ticketing"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v58/20260514_cross_border_rail_ticketing",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "fragile",
    "reason": "at least one declared gate has pass rate in 20\u201350% (Fragile band)",
    "worst_gate": "adoption_margin_fraction",
    "worst_gate_pass_rate": 0.3784
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "adoption_margin_fraction"
  ],
  "primary_uncertainty_drivers": [
    "projected_through_ticket_adoption_fraction",
    "residual_program_overhead_eur",
    "monthly_fte_cost_eur"
  ],
  "known_unmodelled_existential_gates": [
    "dg_move_legal_authority_gate",
    "incumbent_political_acceptance_gate",
    "prm_accessibility_compliance_gate"
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

Budget allocation against the EUR 1.5B coordination fund, clearing-mechanism liquidity buffers against working-capital shocks, and through-ticket adoption against the 40% target.

**Note:** This assessment is a financial / operational stress test. 3 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `dg_move_legal_authority_gate` | Without a binding legal mandate from DG MOVE the 'Three Strikes' enforcement and mandatory API exposure cannot be applied to sovereign operators. | report.html / project_plan | Standards remain voluntary; major operators ignore deadlines; the 40% adoption target collapses regardless of budget. |
| `incumbent_political_acceptance_gate` | Coordinated lobbying or political resistance by SNCF/DB/OeBB can stall enforcement and the tiered-liability framework outside any modelled threshold. | report.html / premortem | 6-12 month delays on key routes and weakened liability framework, undermining clearing-mechanism and adoption assumptions. |
| `prm_accessibility_compliance_gate` | Failure to bind PRM accessibility schemas into the month-18 standard creates a regulatory equity breach the deterministic model cannot quantify. | report.html / expert_criticism | Mandatory non-compliance, fines, and reputational damage that block the program independently of budget or adoption outcomes. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate DG MOVE legal authority for OSDM/enforcement, incumbent operator political acceptance of enforcement, or PRM accessibility schema bound into core standard. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **Fragile** — `adoption_margin_fraction` holds in only 37.8% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **Robust**, 50–80% **Marginal**, 20–50% **Fragile**, <20% **Critical**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `adoption_margin_fraction` | >= 0.0000 | report_explicit | 37.8% | **Fragile** | fails in the majority of runs |
|  | `coordination_budget_buffer_eur` | >= 0.0000 | report_explicit | 73.8% | **Marginal** | passes more often than not but uncomfortably close |
|  | `clearing_liquidity_surplus_eur` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |
|  | `clearing_coverage_ratio` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |

### Aggregation warning

The thresholds above use incompatible units (EUR, fraction) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `adoption_margin_fraction` | **Fragile** | The `>= 0.0000` requirement fails in the majority of runs (62.2%). External commitments built on this gate are exposed. | `projected_through_ticket_adoption_fraction` (improve toward its high bound; quartile Δ-pp +100.0) | If projected adoption is below the target, the program's primary success metric is missed. Threshold parameter: `through_ticket_adoption_target_fraction`. |
| `coordination_budget_buffer_eur` | **Marginal** | The `>= 0.0000` requirement passes 73.8% of runs — just below the Robust band. The gate passes in most runs, but downstream commitments should not treat it as secure. | `residual_program_overhead_eur` (reduce toward its low bound; quartile Δ-pp -99.5) | Confirms whether the EUR 1.5B envelope actually covers grants, reference distributor, emergency reserve, governance overhead, and other testing/legal overheads. The EUR 200M operational float is financed via transactional-fee collateral and is not debited from the fund. Threshold parameter: `public_coordination_budget_eur`. |

## Failure drivers

For each failing gate (Critical or Fragile): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `adoption_margin_fraction` | `projected_through_ticket_adoption_fraction` | +100.0 | `projected_through_ticket_adoption_fraction` above p67 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `projected_through_ticket_adoption_fraction` | `adoption_margin_fraction` | 62.16 | 1.00 | model_assumption |
| 2 | `residual_program_overhead_eur` | `coordination_budget_buffer_eur` | 39.14 | 1.50 | model_assumption |
| 3 | `monthly_fte_cost_eur` | `coordination_budget_buffer_eur` | 0.94 | 0.71 | report_derived |

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
| `governance_two_year_personnel_cost_eur` | **MEDIUM** | 100% | 0.71 |
| `coordination_budget_buffer_eur` | **MEDIUM** | 50% | 1.11 |
| `clearing_liquidity_surplus_eur` | **MEDIUM** | 100% | 0.93 |
| `clearing_coverage_ratio` | **MEDIUM** | 50% | 1.29 |
| `through_ticket_volume_target` | **LOW** | 100% | 2.12 |
| `adoption_margin_fraction` | **LOW** | 0% | 1.00 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `governance_two_year_personnel_cost_eur` | EUR | 8,400,000 | 11,760,000 | 16,800,000 |
| `coordination_budget_buffer_eur` | EUR | 91,600,000 | 38,240,000 | -66,800,000 |
| `clearing_liquidity_surplus_eur` | EUR | 400,000,000 | 375,000,000 | 380,000,000 |
| `clearing_coverage_ratio` | fraction | 6.00 | 2.56 | 1.29 |
| `through_ticket_volume_target` | journeys_per_year | 12,000,000 | 32,000,000 | 80,000,000 |
| `adoption_margin_fraction` | fraction | -0.2500 | 0.0000 | 0.1500 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 1 in the Fragile band. Worst: `adoption_margin_fraction` at 37.8% pass rate under current bounds.
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
