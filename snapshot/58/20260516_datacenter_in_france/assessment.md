# Assessment: Hauts-de-France 9 GW Sovereign AI Engine — Pragmatic Scale-Up

**Type:** Hyperscale data center megaproject (multi-phase, EUR-denominated)  
**Primary goal:** Complete Phase 1 (1 GW operational, PUE <=1.20) within 36 months while securing the 60% take-or-pay anchor commitment and binding RTE 3 GW transmission contract required for Phase 2 FID.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "Hauts-de-France 9 GW Sovereign AI Engine \u2014 Pragmatic Scale-Up",
  "artifact_set": {
    "version": "v58",
    "plan_slug": "20260516_datacenter_in_france",
    "relative_dir": "output/v58/20260516_datacenter_in_france"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v58/20260516_datacenter_in_france",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (Critical band)",
    "worst_gate": "phase1_contingency_surplus_eur",
    "worst_gate_pass_rate": 0.017
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "phase1_contingency_surplus_eur",
    "phase2_takeorpay_commitment_margin",
    "phase1_pue_margin"
  ],
  "primary_uncertainty_drivers": [
    "actual_phase2_takeorpay_commitment_fraction",
    "remediation_cost_overrun_eur",
    "actual_phase1_pue"
  ],
  "known_unmodelled_existential_gates": [
    "rte_binding_3gw_allocation_gate",
    "dgsi_anssi_signoff_gate",
    "judicial_buffer_authorization_gate",
    "social_license_credibility_gate"
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

Tests Phase 1 viability gates: budget coverage of CAPEX plus land-holding overrun, anchor take-or-pay commitment margin against the 60% threshold, FX exposure absorption on USD-hardware, and PUE clearance margin. Existential gates (binding RTE 3 GW allocation, DGSI/ANSSI sign-off, judicial buffer authorization) are flagged but not financially tested.

**Note:** This assessment is a financial / operational stress test. 4 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `rte_binding_3gw_allocation_gate` | Phase 1 construction financing is contractually blocked until a binding RTE transmission contract for the 3 GW Phase 2 expansion is in hand; the model treats the gate as a fixed input. | report.html / review_plan | Phase 1 construction financing cannot close; 1B-2B Phase 0/1 capital stranded if tenants withdraw. |
| `dgsi_anssi_signoff_gate` | Without a formal DGSI/ANSSI agreement before Phase 1 Power FID, premium sovereign revenue streams (10B-20B long-term) are jeopardised; gate is regulatory, not quantitative. | report.html / expert_criticism | Premium domestic revenue stream lost; 60% Phase 2 commitment threshold becomes harder to clear. |
| `judicial_buffer_authorization_gate` | Prefectural/judicial review of the 80% buffer can reduce buildable area below 20 km^2, capping capacity at 3-4 GW; outcome is political, not financial. | report.html / premortem | Buildable area capped; 9 GW long-term goal abandoned; business case re-evaluated downward. |
| `social_license_credibility_gate` | Plan states it must not proceed past Phase 0 if social license is not credible; outcome depends on community acceptance of workforce mandate and heat reuse commitments. | report.html / selected_scenario | Phase 0 exit condition fails; project does not progress to Phase 1 FID. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate RTE binding 3 GW transmission allocation, DGSI/ANSSI sovereign-partition sign-off, judicial/permitting authorization for hyper-dense 80% buffer model, or social license credibility (workforce, heat reuse). These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **Critical** — `phase1_contingency_surplus_eur` fails >= 0.0000 in 98.3% of simulated runs under the current input bounds.
- **Fragile** — `phase2_takeorpay_commitment_margin` holds in only 30.2% of simulated runs under the current input bounds (fails in the majority).
- **Fragile** — `phase1_pue_margin` holds in only 29.8% of simulated runs under the current input bounds (fails in the majority).
- **Scenario warn (all)** — `q_phase1_capex_budget_usd_million`: Skipped: formula_hint is null.

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **Robust**, 50–80% **Marginal**, 20–50% **Fragile**, <20% **Critical**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `phase1_contingency_surplus_eur` | >= 0.0000 | report_inferred | 1.7% | **Critical** | rarely passes under current bounds |
|  | `phase2_takeorpay_commitment_margin` | >= 0.0000 | report_explicit | 30.2% | **Fragile** | fails in the majority of runs |
|  | `phase1_pue_margin` | >= 0.0000 | model_defined | 29.8% | **Fragile** | fails in the majority of runs |

### Aggregation warning

The thresholds above use incompatible units (EUR, fraction, ratio) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `phase1_contingency_surplus_eur` | **Critical** | The `>= 0.0000` requirement is not credible under current bounds: only 1.7% of runs hold. Commitments that depend on this should not be made without revision. | `remediation_cost_overrun_eur` (reduce toward its low bound; quartile Δ-pp -6.4) | Combined viability test of the 15% reserve against the three named Phase 1 cost overruns the plan attributes to one budget envelope. Threshold parameter: `phase1_contingency_reserve_eur`. |
| `phase2_takeorpay_commitment_margin` | **Fragile** | The `>= 0.0000` requirement fails in the majority of runs (69.8%). External commitments built on this gate are exposed. | `actual_phase2_takeorpay_commitment_fraction` (improve toward its high bound; quartile Δ-pp +100.0) | Tests the 60% take-or-pay financial gate; positive margin clears Phase 2 FID. Threshold parameter: `phase2_takeorpay_commitment_threshold`. |
| `phase1_pue_margin` | **Fragile** | The `>= 0.0000` requirement fails in the majority of runs (70.2%). External commitments built on this gate are exposed. | `actual_phase1_pue` (reduce toward its low bound; quartile Δ-pp -100.0) | Engineering SLA gate; tenant contract compliance and energy-cost penalties trip if realised PUE exceeds 1.20. |

## Failure drivers

For each failing gate (Critical or Fragile): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `phase1_contingency_surplus_eur` | `remediation_cost_overrun_eur` | -6.4 | no single input restriction sufficient |
| `phase2_takeorpay_commitment_margin` | `actual_phase2_takeorpay_commitment_fraction` | +100.0 | `actual_phase2_takeorpay_commitment_fraction` above p67 |
| `phase1_pue_margin` | `actual_phase1_pue` | -100.0 | `actual_phase1_pue` below p67 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `actual_phase2_takeorpay_commitment_fraction` | `phase2_takeorpay_commitment_margin` | 58.17 | 0.83 | model_assumption |
| 2 | `remediation_cost_overrun_eur` | `phase1_contingency_surplus_eur` | 18.87 | 3.00 | report_derived |
| 3 | `actual_phase1_pue` | `phase1_pue_margin` | 9.95 | 0.14 | model_assumption |
| 4 | `land_holding_cost_eur_per_hectare_year` | `phase1_contingency_surplus_eur` | 5.08 | 0.92 | report_derived |

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
| `land_holding_cost_total_eur` | **MEDIUM** | 100% | 0.92 |
| `fx_unhedged_exposure_eur` | **MEDIUM** | 50% | 1.00 |
| `phase2_takeorpay_commitment_margin` | **LOW** | 0% | 0.83 |
| `phase1_pue_margin` | **LOW** | 0% | 0.14 |
| `phase1_contingency_surplus_eur` | **MEDIUM** | 57% | 1.23 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `land_holding_cost_total_eur` | EUR | 676,200,000 | 1,159,200,000 | 1,738,800,000 |
| `fx_unhedged_exposure_eur` | EUR | 0.0000 | 67,500,000 | 135,000,000 |
| `phase2_takeorpay_commitment_margin` | fraction | -0.3500 | 0.0000 | 0.1500 |
| `phase1_pue_margin` | ratio | 0.0500 | 0.0000 | -0.1200 |
| `phase1_contingency_surplus_eur` | EUR | 73,800,000 | -601,700,000 | -1,873,800,000 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 1 declared gate in the Critical band; 2 in the Fragile band. Worst: `phase1_contingency_surplus_eur` at 1.7% pass rate under current bounds.
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
