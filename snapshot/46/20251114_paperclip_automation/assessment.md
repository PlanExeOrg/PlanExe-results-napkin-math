# Assessment: Paperclip Automation Pilot Line (Builder Pragmatic Integration)

**Type:** industrial_automation_pilot  
**Primary goal:** Build a fully automated, end-to-end pilot paperclip line in 4,000 sq ft of the Cleveland building that takes API orders and stages labeled parcels for UPS/FedEx pickup with ≤2 hours/week of manual intervention, on a $300–500K budget under the Builder strategy.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "Paperclip Automation Pilot Line (Builder Pragmatic Integration)",
  "artifact_set": {
    "version": "v46",
    "plan_slug": "20251114_paperclip_automation",
    "relative_dir": "output/v46/20251114_paperclip_automation"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v46/20251114_paperclip_automation",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (DOOM band)",
    "worst_gate": "manual_intervention_margin_hours",
    "worst_gate_pass_rate": 0.1161
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "manual_intervention_margin_hours"
  ],
  "primary_uncertainty_drivers": [
    "actual_api_p99_latency_ms",
    "actual_manual_intervention_hours_per_week",
    "actual_opc_ua_bid_usd"
  ],
  "known_unmodelled_existential_gates": [
    "cleveland_building_electrical_osha_permits_gate",
    "used_wire_bender_modern_fieldbus_gate",
    "carrier_fixed_table_staging_gate"
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

Tests the manual-intervention-hours margin against the 2 hr/week ceiling; the budget surplus against bottom-up program spend; the OPC UA middleware bid margin against the $75K custom-IO-fallback trigger; the API p99 latency margin against the 100 ms HMI-pivot trigger; and the on-site PLC-expert contract margin against the $25K Phase-2 stabilization floor. Cleveland permits, used-wire-bender modern fieldbus availability, and UPS/FedEx fixed-table staging are treated as unmodelled existential gates.

**Note:** This assessment is a financial / operational stress test. 3 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `cleveland_building_electrical_osha_permits_gate` | Risk 1 names permitting as the primary regulatory blocker; without permits before Phase 2 the rigging crew cannot install machinery and the schedule slips 4–8 weeks regardless of integration progress. | report.html / review_plan | 4–8 week schedule delay; $10–20K additional cost; possible stop-work order during rigging; entire 6-phase sequence cascades. |
| `used_wire_bender_modern_fieldbus_gate` | The Decision-3 OPC UA abstraction layer presupposes a modern fieldbus on the used bender; without it the integration reverts to custom I/O translation and the Builder strategy thesis collapses regardless of budget. | report.html / expert_criticism | Custom I/O translator path activated; $15–30K extra cost per Risk 2; 4–6 weeks development time; internal-developer scope creeps off API into low-level driver work. |
| `carrier_fixed_table_staging_gate` | Premortem trigger: if carriers require dynamic conveyor staging beyond $40K mechanical redesign, the project pivots to B2B-volume-only shipment and the consumer-API feasibility claim is invalidated. | report.html / premortem | $40K+ mechanical redesign required or pivot to B2B-only shipment; Phase 5/6 demonstration scope shifts; carrier-API integration narrative weakens. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate building, electrical, and OSHA permits secured before Phase 2 rigging, a used wire bender within $20–40K supports a modern documented fieldbus (Modbus TCP / Ethernet/IP / Profinet), or UPS/FedEx accept fixed-table parcel staging without dynamic conveyor integration. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **DOOM** — `manual_intervention_margin_hours` fails >= 0.0000 in 88.4% of simulated runs under the current input bounds.

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **ROBUST**, 50–80% **MARGINAL**, 20–50% **FRAGILE**, <20% **DOOM**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `manual_intervention_margin_hours` | >= 0.0000 | report_explicit | 11.6% | **DOOM** | rarely passes under current bounds |
|  | `budget_surplus_usd` | >= 0.0000 | report_explicit | 72.4% | **MARGINAL** | passes more often than not but uncomfortably close |
|  | `opc_ua_bid_margin_usd` | >= 0.0000 | report_explicit | 67.4% | **MARGINAL** | passes more often than not but uncomfortably close |
|  | `api_latency_margin_ms` | >= 0.0000 | report_explicit | 55.0% | **MARGINAL** | passes more often than not but uncomfortably close |
|  | `onsite_expert_budget_margin_usd` | >= 0.0000 | report_explicit | 70.8% | **MARGINAL** | passes more often than not but uncomfortably close |

### Aggregation warning

The thresholds above use incompatible units (USD, hours_per_week, milliseconds) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `manual_intervention_margin_hours` | **DOOM** | The `>= 0.0000` requirement is not credible under current bounds: only 11.6% of runs hold. Commitments that depend on this should not be made without revision. | `actual_manual_intervention_hours_per_week` (reduce toward its low bound; quartile Δ-pp -46.4) | Positive margin clears the feasibility-proof success metric; negative margin invalidates the central Builder thesis regardless of how clean the integration is otherwise. Threshold parameter: `manual_intervention_threshold_hours_per_week`. |
| `budget_surplus_usd` | **MARGINAL** | The `>= 0.0000` requirement passes 72.4% of runs — just below the ROBUST band. The gate passes in most runs, but downstream commitments should not treat it as secure. | `actual_total_project_cost_usd` (reduce toward its low bound; quartile Δ-pp -100.0) | Positive surplus preserves the Risk-3 contingency and Issue-1 spare-parts reserve; negative surplus forces scope cuts or sponsor capital call. Threshold parameter: `budget_max_usd`. |
| `opc_ua_bid_margin_usd` | **MARGINAL** | The `>= 0.0000` requirement passes 67.4% of runs — close to coin-flip. Downstream commitments should not assume it holds. | `actual_opc_ua_bid_usd` (reduce toward its low bound; quartile Δ-pp -100.0) | Positive margin keeps the Decision-3 abstraction-layer strategy intact; negative margin forces the custom-IO translator pivot and scope creep onto the internal developer. Threshold parameter: `opc_ua_bid_threshold_usd`. |
| `api_latency_margin_ms` | **MARGINAL** | The `>= 0.0000` requirement passes 55.0% of runs — close to coin-flip. Downstream commitments should not assume it holds. | `actual_api_p99_latency_ms` (reduce toward its low bound; quartile Δ-pp -100.0) | Positive margin preserves the API-only Phase-6 demonstration target; negative margin forces HMI-controlled fallback and invalidates the autonomous-flow feasibility claim. Threshold parameter: `api_latency_p99_threshold_ms`. |
| `onsite_expert_budget_margin_usd` | **MARGINAL** | The `>= 0.0000` requirement passes 70.8% of runs — just below the ROBUST band. The gate passes in most runs, but downstream commitments should not treat it as secure. | `actual_onsite_expert_cost_usd` (reduce toward its low bound; quartile Δ-pp -100.0) | Positive margin secures the Issue-3 mandatory stabilization without reallocating reserves; negative margin reaches into the spare-parts or contingency pool and weakens later-phase resilience. Threshold parameter: `onsite_expert_max_cost_usd`. |

## Failure drivers

For each failing gate (DOOM or FRAGILE): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `manual_intervention_margin_hours` | `actual_manual_intervention_hours_per_week` | -46.4 | `actual_manual_intervention_hours_per_week` below p90 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `actual_api_p99_latency_ms` | `api_latency_margin_ms` | 108.05 | 2.40 | model_assumption |
| 2 | `actual_manual_intervention_hours_per_week` | `manual_intervention_margin_hours` | 102.62 | 2.50 | model_assumption |
| 3 | `actual_opc_ua_bid_usd` | `opc_ua_bid_margin_usd` | 40.71 | 1.25 | report_derived |
| 4 | `actual_onsite_expert_cost_usd` | `onsite_expert_budget_margin_usd` | 33.53 | 1.15 | report_derived |
| 5 | `actual_total_project_cost_usd` | `budget_surplus_usd` | 16.45 | 0.60 | report_derived |

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
| `manual_intervention_margin_hours` | **LOW** | 0% | 2.50 |
| `budget_surplus_usd` | **MEDIUM** | 100% | 0.60 |
| `opc_ua_bid_margin_usd` | **MEDIUM** | 100% | 1.25 |
| `api_latency_margin_ms` | **LOW** | 0% | 2.40 |
| `onsite_expert_budget_margin_usd` | **MEDIUM** | 100% | 1.15 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `manual_intervention_margin_hours` | hours_per_week | 1.50 | -1.00 | -6.00 |
| `budget_surplus_usd` | USD | 180,000 | 30,000 | -100,000 |
| `opc_ua_bid_margin_usd` | USD | 40,000 | 15,000 | -35,000 |
| `api_latency_margin_ms` | milliseconds | 80.00 | 25.00 | -100.00 |
| `onsite_expert_budget_margin_usd` | USD | 13,000 | 5,000 | -10,000 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 1 declared gate in the DOOM band. Worst: `manual_intervention_margin_hours` at 11.6% pass rate under current bounds.
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
