# Assessment: Hemispheric Partition (Builder Path)

**Type:** geopolitical_megaproject  
**Primary goal:** Legally partition Earth along the equator within 24 months: 85% critical infrastructure severance, 95% priority demographic relocation, hybrid IOB governance.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "Hemispheric Partition (Builder Path)",
  "artifact_set": {
    "version": "v49",
    "plan_slug": "20251220_global_relocation",
    "relative_dir": "output/v49/20251220_global_relocation"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v49/20251220_global_relocation",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (Critical band)",
    "worst_gate": "budget_24mo_surplus_usd",
    "worst_gate_pass_rate": 0.157
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "budget_24mo_surplus_usd"
  ],
  "primary_uncertainty_drivers": [
    "total_24mo_severance_and_stabilization_cost_usd",
    "achieved_machine_energy_contribution_fraction",
    "achieved_wave1_verification_fraction"
  ],
  "known_unmodelled_existential_gates": [
    "machine_southern_viability_gate",
    "iob_charter_ratification_gate",
    "non_coercion_welfare_continuity_gate",
    "sovereign_sensor_trust_latency_gate",
    "global_airspace_waiver_gate"
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

Tests whether the 24-month $12T front-loaded allocation covers severance and Northern stabilization while meeting the 85% Wave 1 severance, 95% relocation, 90% IOB transfer, 13k/km^2 density, and 10% machine energy contribution gates.

**Note:** This assessment is a financial / operational stress test. 5 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `machine_southern_viability_gate` | The partition premise assumes the machine domain can sustain energy and compute below 3 degrees S without Northern input; the model treats this as a fixed assumption rather than a probabilistic test. | report.html / expert_criticism | Physical separation premise collapses; partition reverts to managed co-dependency and the 24-month deadline becomes meaningless. |
| `iob_charter_ratification_gate` | Permanent hybrid Arbitration Panel must be ratified by Month 15 for legitimate post-Month-24 governance; the model cannot quantify political ratification probability. | report.html / project_plan | Dispute resolution defaults to a single emergency arbiter and the bilateral negotiation pathway is blocked. |
| `non_coercion_welfare_continuity_gate` | Severance must not interrupt civilian food, water, or power; this is a binding non-coercion compliance gate not captured in any financial threshold. | report.html / selected_scenario | The non-coercive constraint of the treaty is violated and the entire Builder mandate loses legitimacy. |
| `sovereign_sensor_trust_latency_gate` | Corridor governance fails if real-time sensor feeds breach the latency SLA; the deterministic model does not simulate network performance. | report.html / premortem | Sensor Trust fails as the corridor-dispute resolution layer, reintroducing kinetic-escalation risk. |
| `global_airspace_waiver_gate` | Demographic transport at planetary scale requires airspace waivers and resource-sharing treaties the model treats as granted. | report.html / project_plan | Logistical relocation cannot proceed at the scale required to hit the 95% relocation gate by Month 24. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate machine civilization independent viability south of 3 degrees S, hybrid IOB charter ratification by Month 15, civilian welfare continuity (food, water, power), sovereign Sensor Trust sub-50ms latency for 99.99% of streams, or global airspace and resource-sharing legal waivers. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **Critical** — `budget_24mo_surplus_usd` fails >= 0.0000 in 84.3% of simulated runs under the current input bounds.

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **Robust**, 50–80% **Marginal**, 20–50% **Fragile**, <20% **Critical**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `budget_24mo_surplus_usd` | >= 0.0000 | report_explicit | 15.7% | **Critical** | rarely passes under current bounds |
|  | `wave1_verification_margin` | >= 0.0000 | report_explicit | 50.2% | **Marginal** | passes more often than not but uncomfortably close |
|  | `machine_energy_contribution_margin` | >= 0.0000 | report_explicit | 59.7% | **Marginal** | passes more often than not but uncomfortably close |
|  | `required_relocated_people` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |
|  | `post_24mo_reserve_buffer_usd` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |

### Aggregation warning

The thresholds above use incompatible units (USD, fraction, people) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `budget_24mo_surplus_usd` | **Critical** | The `>= 0.0000` requirement is not credible under current bounds: only 15.7% of runs hold. Commitments that depend on this should not be made without revision. | `total_24mo_severance_and_stabilization_cost_usd` (reduce toward its low bound; quartile Δ-pp -62.8) | Tests whether the $12T tranche covers severance plus stabilization; negative surplus signals reserve raid. Threshold parameter: `initial_allocation_usd`. |
| `wave1_verification_margin` | **Marginal** | The `>= 0.0000` requirement passes 50.2% of runs — close to coin-flip. Downstream commitments should not assume it holds. | `achieved_wave1_verification_fraction` (improve toward its high bound; quartile Δ-pp +100.0) | Positive margin lets Wave 2 proceed; negative blocks subsequent waves and jeopardises the 24-month deadline. Threshold parameter: `wave1_verification_target_fraction`. |
| `machine_energy_contribution_margin` | **Marginal** | The `>= 0.0000` requirement passes 59.7% of runs — close to coin-flip. Downstream commitments should not assume it holds. | `achieved_machine_energy_contribution_fraction` (improve toward its high bound; quartile Δ-pp +100.0) | Positive margin keeps IOB stabilization funds flowing; sustained negative halts them. Threshold parameter: `machine_energy_contribution_target_fraction`. |

## Failure drivers

For each failing gate (Critical or Fragile): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `budget_24mo_surplus_usd` | `total_24mo_severance_and_stabilization_cost_usd` | -62.8 | `total_24mo_severance_and_stabilization_cost_usd` below p85 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `total_24mo_severance_and_stabilization_cost_usd` | `budget_24mo_surplus_usd` | 64.28 | 1.21 | model_assumption |
| 2 | `achieved_machine_energy_contribution_fraction` | `machine_energy_contribution_margin` | 28.25 | 0.70 | model_assumption |
| 3 | `achieved_wave1_verification_fraction` | `wave1_verification_margin` | 17.57 | 0.35 | model_assumption |

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
| `budget_24mo_surplus_usd` | **LOW** | 0% | 1.21 |
| `wave1_verification_margin` | **LOW** | 0% | 0.35 |
| `machine_energy_contribution_margin` | **LOW** | 0% | 0.70 |
| `required_relocated_people` | **LOW** | 0% | 2.17 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `budget_24mo_surplus_usd` | USD | 4,000,000,000,000 | -2,000,000,000,000 | -13,000,000,000,000 |
| `wave1_verification_margin` | fraction | -0.3000 | 0.0000 | 0.0000 |
| `machine_energy_contribution_margin` | fraction | -0.0700 | 0.0000 | 0.0000 |
| `required_relocated_people` | people | 190,000,000 | 570,000,000 | 1,425,000,000 |
| `post_24mo_reserve_buffer_usd` | USD | 18,000,000,000,000 | 18,000,000,000,000 | 18,000,000,000,000 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 1 declared gate in the Critical band. Worst: `budget_24mo_surplus_usd` at 15.7% pass rate under current bounds.
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
