# Assessment: EU Cross-Border Rail Through-Ticketing Program

**Type:** regulatory_coordination_program  
**Primary goal:** Deliver a coordinated European program under the Pragmatic Harmonization strategy that makes cross-border train travel as easy to search/book/refund as national travel, reaching 40% single-through-ticket adoption within 5 years on a €1.5B coordination budget.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "EU Cross-Border Rail Through-Ticketing Program",
  "artifact_set": {
    "version": "v46",
    "plan_slug": "20260514_cross_border_rail_ticketing",
    "relative_dir": "output/v46/20260514_cross_border_rail_ticketing"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v46/20260514_cross_border_rail_ticketing",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "fragile",
    "reason": "at least one declared gate has pass rate in 20\u201350% (FRAGILE band)",
    "worst_gate": "binding_standards_timing_margin_months",
    "worst_gate_pass_rate": 0.2048
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "adoption_margin",
    "coordination_budget_surplus_eur",
    "clearing_float_coverage_eur",
    "binding_standards_timing_margin_months",
    "complaint_reduction_margin"
  ],
  "primary_uncertainty_drivers": [
    "actual_complaint_reduction_share",
    "actual_adoption_share",
    "peak_daily_clearing_obligation_eur"
  ],
  "known_unmodelled_existential_gates": [
    "dg_move_three_strikes_legal_authorization_gate",
    "incumbent_carrier_political_compliance_gate",
    "national_regulator_alignment_gate"
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

Tests the adoption margin against the 40% target; the coordination-budget surplus against bottom-up project cost; the clearing-float coverage against peak daily settlement obligation under a 150% safety buffer; the binding-standards timing margin against the 18-month deadline; and the distributor-complaint reduction margin against the 50% target. DG MOVE legal enforcement of 'Three Strikes', incumbent-carrier political compliance, and national-regulator alignment are treated as unmodelled existential gates.

**Note:** This assessment is a financial / operational stress test. 3 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `dg_move_three_strikes_legal_authorization_gate` | Risk 1 and the Decision-12 enforcement posture name this as the binary legal hook; without legally-unambiguous suspension authority, incumbent compliance becomes voluntary regardless of any operational margin the model evaluates. | report.html / selected_scenario | Enforcement collapses to political negotiation; SNCF/DB/ÖBB compliance slips past deadlines; 40% adoption target unreachable; €1.5B investment thesis fails. |
| `incumbent_carrier_political_compliance_gate` | Risk 6 and the Coordinated-Lobbying diverse-risk name a Medium/High likelihood-severity of incumbent operators lobbying to weaken the Passenger Rights Backstop; without acceptance the liability model collapses and distributor uptake stalls. | report.html / premortem | Backstop liability pushed to distributors/passengers; consumer-complaint goal fails; distributor adoption falls toward the Risk 7 20% scenario. |
| `national_regulator_alignment_gate` | Mandating non-discriminatory commercial terms and PRM accessibility schemas across 20+ carriers requires consistent national-regulator enforcement; uneven enforcement creates compliance arbitrage that the EU-level simulation cannot resolve. | report.html / review_plan | Compliance arbitrage between strict and permissive member states; OSDM data-layer fragmentation by jurisdiction; the 50% complaint-reduction target becomes structurally unreachable. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate DG MOVE legally pre-approves the 'Three Strikes' enforcement template, SNCF, DB, and ÖBB politically accept the tiered liability and API-exposure mandates, or national Competent Authorities enforce OSDM and PRM mandates uniformly across member states. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **FRAGILE** — `adoption_margin` holds in only 23.8% of simulated runs under the current input bounds (fails in the majority).
- **FRAGILE** — `coordination_budget_surplus_eur` holds in only 42.9% of simulated runs under the current input bounds (fails in the majority).
- **FRAGILE** — `clearing_float_coverage_eur` holds in only 43.8% of simulated runs under the current input bounds (fails in the majority).
- **FRAGILE** — `binding_standards_timing_margin_months` holds in only 20.5% of simulated runs under the current input bounds (fails in the majority).
- **FRAGILE** — `complaint_reduction_margin` holds in only 24.4% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **ROBUST**, 50–80% **MARGINAL**, 20–50% **FRAGILE**, <20% **DOOM**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `adoption_margin` | >= 0.0000 | report_explicit | 23.8% | **FRAGILE** | fails in the majority of runs |
|  | `coordination_budget_surplus_eur` | >= 0.0000 | report_explicit | 42.9% | **FRAGILE** | fails in the majority of runs |
|  | `clearing_float_coverage_eur` | >= 0.0000 | report_explicit | 43.8% | **FRAGILE** | fails in the majority of runs |
|  | `binding_standards_timing_margin_months` | >= 0.0000 | report_explicit | 20.5% | **FRAGILE** | fails in the majority of runs |
|  | `complaint_reduction_margin` | >= 0.0000 | report_explicit | 24.4% | **FRAGILE** | fails in the majority of runs |

### Aggregation warning

The thresholds above use incompatible units (EUR, fraction, months) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `adoption_margin` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (76.2%). External commitments built on this gate are exposed. | `actual_adoption_share` (improve toward its high bound; quartile Δ-pp +95.2) | Positive margin validates the €1.5B investment thesis and modal-shift case; negative margin produces the Risk 7 'economic justification diminishes' scenario at Year 5. Threshold parameter: `adoption_target_share`. |
| `coordination_budget_surplus_eur` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (57.1%). External commitments built on this gate are exposed. | `actual_total_project_cost_eur` (reduce toward its low bound; quartile Δ-pp -100.0) | Positive surplus preserves the Emergency Float Reserve and contingency headroom; negative surplus forces EU-budget top-ups per Risk 3 working-capital scenarios. Threshold parameter: `coordination_budget_eur`. |
| `clearing_float_coverage_eur` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (56.2%). External commitments built on this gate are exposed. | `peak_daily_clearing_obligation_eur` (reduce toward its low bound; quartile Δ-pp -100.0) | Positive coverage means the €200M float holds ≥150% of peak daily obligation; negative coverage triggers the €300M Emergency Float Reserve and signals clearing-mechanism instability. Threshold parameter: `initial_clearing_float_eur`. |
| `binding_standards_timing_margin_months` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (79.5%). External commitments built on this gate are exposed. | `actual_binding_standards_months` (reduce toward its low bound; quartile Δ-pp -67.0) | Positive margin keeps the 30-month API-exposure and 60-month full-corridor deadlines reachable; negative margin cascades schedule slippage into the Year-5 adoption gate. Threshold parameter: `binding_standards_deadline_months`. |
| `complaint_reduction_margin` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (75.6%). External commitments built on this gate are exposed. | `actual_complaint_reduction_share` (improve toward its high bound; quartile Δ-pp +97.5) | Positive margin attests to OSDM data-layer stability and clearing reliability; negative margin signals the Risk 2 'data layer unstable' failure mode and weakens distributor uptake. Threshold parameter: `complaint_reduction_target_share`. |

## Failure drivers

For each failing gate (DOOM or FRAGILE): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `adoption_margin` | `actual_adoption_share` | +95.2 | `actual_adoption_share` above p75 |
| `coordination_budget_surplus_eur` | `actual_total_project_cost_eur` | -100.0 | `actual_total_project_cost_eur` below p50 |
| `clearing_float_coverage_eur` | `peak_daily_clearing_obligation_eur` | -100.0 | `peak_daily_clearing_obligation_eur` below p50 |
| `binding_standards_timing_margin_months` | `actual_binding_standards_months` | -67.0 | `actual_binding_standards_months` below p85 |
| `complaint_reduction_margin` | `actual_complaint_reduction_share` | +97.5 | `actual_complaint_reduction_share` above p75 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `actual_complaint_reduction_share` | `complaint_reduction_margin` | 101.40 | 1.38 | model_assumption |
| 2 | `actual_adoption_share` | `adoption_margin` | 90.70 | 1.25 | model_assumption |
| 3 | `peak_daily_clearing_obligation_eur` | `clearing_float_coverage_eur` | 86.45 | 1.54 | model_assumption |
| 4 | `actual_binding_standards_months` | `binding_standards_timing_margin_months` | 42.62 | 0.80 | model_assumption |
| 5 | `actual_total_project_cost_eur` | `coordination_budget_surplus_eur` | 26.67 | 0.47 | report_derived |

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
| `adoption_margin` | **LOW** | 0% | 1.25 |
| `coordination_budget_surplus_eur` | **HIGH** | 100% | 0.47 |
| `clearing_float_coverage_eur` | **LOW** | 0% | 1.54 |
| `binding_standards_timing_margin_months` | **LOW** | 0% | 0.80 |
| `complaint_reduction_margin` | **LOW** | 0% | 1.38 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `adoption_margin` | fraction | -0.2500 | -0.0800 | 0.1500 |
| `coordination_budget_surplus_eur` | EUR | 300,000,000 | 0.0000 | -400,000,000 |
| `clearing_float_coverage_eur` | EUR | 125,000,000 | 5,000,000 | -175,000,000 |
| `binding_standards_timing_margin_months` | months | 4.00 | -2.00 | -12.00 |
| `complaint_reduction_margin` | fraction | -0.3500 | -0.1000 | 0.2000 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 5 in the FRAGILE band. Worst: `binding_standards_timing_margin_months` at 20.5% pass rate under current bounds.
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
