# Assessment: Automated Paperclip Manufacturing and Fulfillment Pilot

**Type:** industrial_automation_pilot  
**Primary goal:** Demonstrate end-to-end autonomous paperclip production from API call to staged parcel with documented manual intervention under 2 hours per week, inside a $300k-$500k budget under the 'Builder' strategy.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "Automated Paperclip Manufacturing and Fulfillment Pilot",
  "artifact_set": {
    "version": "v58",
    "plan_slug": "20251114_paperclip_automation",
    "relative_dir": "output/v58/20251114_paperclip_automation"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v58/20251114_paperclip_automation",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "fragile",
    "reason": "at least one declared gate has pass rate in 20\u201350% (Fragile band)",
    "worst_gate": "manual_intervention_surplus_hours_per_week",
    "worst_gate_pass_rate": 0.4142
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "manual_intervention_surplus_hours_per_week"
  ],
  "primary_uncertainty_drivers": [
    "actual_manual_intervention_hours_per_week",
    "actual_onsite_expert_cost_usd"
  ],
  "known_unmodelled_existential_gates": [
    "building_electrical_osha_permits_gate",
    "control_architecture_resolution_gate",
    "wire_bender_fieldbus_support_gate",
    "carrier_staging_acceptance_gate"
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

Tests whether the named hardware, integration, and expert-commissioning components plus a 10% contingency fit under the $500k cap, whether the realised on-site expert contract clears the mandatory $15k floor and stays under the $25k SMART contract cap, and whether the realised manual-intervention load stays under the 2-hour autonomy gate.

**Note:** This assessment is a financial / operational stress test. 4 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `building_electrical_osha_permits_gate` | Phase 2+ cannot begin until permits are in hand; failure halts physical install regardless of any financial gate. | report.html / selected_scenario | Project blocked at Phase 1; sunk costs on design and pre-procurement without operational continuation. |
| `control_architecture_resolution_gate` | Without an architecture decision the integration timeline cannot start; binary architect sign-off the model cannot simulate. | report.html / data_collection | Control System Protocol Selection blocked; software phases stall; scope creep for the internal developer. |
| `wire_bender_fieldbus_support_gate` | Premortem stops the purchase if the chosen machine lacks fieldbus support; integration then becomes a custom-driver gamble the plan refuses to take. | report.html / data_collection | Purchase blocked; alternative bender must be sourced, or strategy pivots to a custom-I/O posture with budget implications. |
| `carrier_staging_acceptance_gate` | Phase 6 demo depends on carrier acceptance of fixed-table mechanical handoff rather than dynamic conveyor staging; binary external decision. | report.html / data_collection | Phase 6 demonstration fails; mechanical handoff must be re-engineered with dynamic staging at additional CAPEX. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate building, electrical, and OSHA permits granted in Phase 1, formal OPC UA vs. custom-I/O selection signed off by D+10, selected wire bender supports a documented fieldbus protocol by D+14, or carrier accepts fixed-table staging for the Phase 6 demo. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **Fragile** — `manual_intervention_surplus_hours_per_week` holds in only 41.4% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **Robust**, 50–80% **Marginal**, 20–50% **Fragile**, <20% **Critical**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `manual_intervention_surplus_hours_per_week` | >= 0.0000 | report_explicit | 41.4% | **Fragile** | fails in the majority of runs |
|  | `budget_surplus_usd` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |
|  | `expert_cap_margin_usd` | >= 0.0000 | report_explicit | 87.8% | **Robust** | passes in the strong majority of runs |

### Aggregation warning

The thresholds above use incompatible units (USD, hours_per_week) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `manual_intervention_surplus_hours_per_week` | **Fragile** | The `>= 0.0000` requirement fails in the majority of runs (58.6%). External commitments built on this gate are exposed. | `actual_manual_intervention_hours_per_week` (reduce toward its low bound; quartile Δ-pp -100.0) | Primary autonomy-feasibility gate; positive means the pilot meets the headline feasibility goal. Threshold parameter: `max_manual_intervention_hours_per_week`. |

## Failure drivers

For each failing gate (Critical or Fragile): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `manual_intervention_surplus_hours_per_week` | `actual_manual_intervention_hours_per_week` | -100.0 | `actual_manual_intervention_hours_per_week` below p50 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `actual_manual_intervention_hours_per_week` | `manual_intervention_surplus_hours_per_week` | 130.18 | 2.22 | report_derived |
| 2 | `actual_onsite_expert_cost_usd` | `expert_cap_margin_usd` | 5.90 | 1.00 | report_derived |

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
| `subtotal_named_components_usd` | **MEDIUM** | 71% | 1.06 |
| `total_project_cost_estimate_usd` | **MEDIUM** | 71% | 1.06 |
| `budget_surplus_usd` | **MEDIUM** | 71% | 1.06 |
| `manual_intervention_surplus_hours_per_week` | **LOW** | 100% | 2.22 |
| `expert_cap_margin_usd` | **MEDIUM** | 100% | 1.00 |
| `expert_floor_margin_usd` | **MEDIUM** | 100% | 1.00 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `subtotal_named_components_usd` | USD | 140,000 | 246,000 | 395,000 |
| `total_project_cost_estimate_usd` | USD | 154,000 | 270,600 | 434,500 |
| `budget_surplus_usd` | USD | 346,000 | 229,400 | 65,500 |
| `manual_intervention_surplus_hours_per_week` | hours_per_week | 1.50 | 0.2000 | -2.50 |
| `expert_cap_margin_usd` | USD | 13,000 | 7,000 | -5,000 |
| `expert_floor_margin_usd` | USD | -3,000 | 3,000 | 15,000 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 1 in the Fragile band. Worst: `manual_intervention_surplus_hours_per_week` at 41.4% pass rate under current bounds.
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
