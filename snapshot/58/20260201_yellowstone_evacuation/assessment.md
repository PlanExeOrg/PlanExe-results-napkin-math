# Assessment: Yellowstone Caldera Red Warning Evacuation (Pioneer Strategy)

**Type:** emergency_response  
**Primary goal:** Clear 35,800 Zone Zero occupants within 6 hours and bridge the T+6 to T+18 logistical ingress gap with airlifted N95/water supplies while keeping decentralized C2 nodes powered for 72 hours.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "Yellowstone Caldera Red Warning Evacuation (Pioneer Strategy)",
  "artifact_set": {
    "version": "v58",
    "plan_slug": "20260201_yellowstone_evacuation",
    "relative_dir": "output/v58/20260201_yellowstone_evacuation"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v58/20260201_yellowstone_evacuation",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "viable",
    "reason": "every declared gate has pass rate \u2265 80% (Robust band)",
    "worst_gate": "evacuation_throughput_surplus",
    "worst_gate_pass_rate": 0.9684
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [],
  "primary_uncertainty_drivers": [
    "vehicle_throughput_per_hour",
    "occupants_per_vehicle"
  ],
  "known_unmodelled_existential_gates": [
    "stafford_act_declaration_gate",
    "faa_dod_airspace_waiver_gate",
    "tri_state_governor_mou_gate"
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

Tests three executable viability gates: Zone Zero contraflow throughput vs the T+6 deadline, T+8 to T+16 airlift staging vs the 30% N95 target, and C2 72-hour fuel cache vs the UPS baseline. Stafford Act, FAA/DoD airspace waiver, and tri-state Governor MOU are treated as unmodelled authorisation gates.

**Note:** This assessment is a financial / operational stress test. 3 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `stafford_act_declaration_gate` | Without the declaration, the $500M DRF ceiling is unreachable and every financed component of the plan stalls. | report.html / assumptions | All airlift, fuel cache, shelter intake, and contractor mobilisation funding stalls; the Pioneer Strategy cannot execute. |
| `faa_dod_airspace_waiver_gate` | The 10 emergency sorties depend on a waiver against the silicate-ash grounding of ZLC/ZSE; without it the airlift cannot launch. | report.html / project_plan | 30% N95/water staging by T+16 cannot occur and Zone One faces respiratory/dehydration casualty surge. |
| `tri_state_governor_mou_gate` | Engineering tasking for fuel caches and ash hardening requires signed tri-state operational authority before boundary crossing. | report.html / review_plan | Jurisdictional friction delays ashfall hardening 4-12 hours, raising grid collapse probability and C2 failure risk. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate stafford Act declaration for $500M DRF access, FAA/DoD airspace waiver for T+8 to T+16 ingress, or MT/WY/ID Governor dual-hat MOU before T+0. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **Scenario warn (all)** — `q_jurisdictional_friction_delay`: Skipped: formula_hint is null.

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **Robust**, 50–80% **Marginal**, 20–50% **Fragile**, <20% **Critical**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `evacuation_throughput_surplus` | >= 0.0000 | model_defined | 96.8% | **Robust** | passes in the strong majority of runs |
|  | `airlift_staging_surplus_kg` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |
|  | `c2_fuel_cache_surplus_hours` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |

### Aggregation warning

The thresholds above use incompatible units (hours, kg, people_per_hour) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `vehicle_throughput_per_hour` | `evacuation_throughput_surplus` | 0.33 | 0.83 | report_derived |
| 2 | `occupants_per_vehicle` | `evacuation_throughput_surplus` | 0.14 | 0.54 | report_derived |

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
| `achievable_evacuee_throughput_per_hour` | **MEDIUM** | 100% | 0.68 |
| `evacuation_throughput_surplus` | **MEDIUM** | 100% | 0.68 |
| `airlift_staging_surplus_kg` | **MEDIUM** | 100% | 0.78 |
| `c2_fuel_cache_surplus_hours` | **MEDIUM** | 100% | 0.67 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `required_evacuee_throughput_per_hour` | people_per_hour | 5,847 | 5,847 | 5,847 |
| `achievable_evacuee_throughput_per_hour` | people_per_hour | 3,600 | 10,080 | 16,800 |
| `evacuation_throughput_surplus` | people_per_hour | -2,247 | 4,233 | 10,953 |
| `airlift_staging_surplus_kg` | kg | 48,500 | 88,500 | 118,500 |
| `c2_fuel_cache_surplus_hours` | hours | 48.00 | 36.00 | 24.00 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above. No declared gate is in the Critical or Fragile band — but read the bounds and trust boundaries before treating that as a green light.
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
