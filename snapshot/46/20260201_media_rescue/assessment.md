# Assessment: Containerized Dark Data Ingestor Network (CDDIN)

**Type:** industrial_preservation_program  
**Primary goal:** Deploy a 30-unit Containerized Dark Data Ingestor Network to recover 200+ petabytes of at-risk historical media over 10 years on a $250M budget, sustaining fleet uptime >90% and human review load <17.5%.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "Containerized Dark Data Ingestor Network (CDDIN)",
  "artifact_set": {
    "version": "v46",
    "plan_slug": "20260201_media_rescue",
    "relative_dir": "output/v46/20260201_media_rescue"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v46/20260201_media_rescue",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (DOOM band)",
    "worst_gate": "budget_opex_surplus_usd",
    "worst_gate_pass_rate": 0.0059
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "budget_opex_surplus_usd",
    "uptime_margin",
    "modular_mtbf_improvement_margin"
  ],
  "primary_uncertainty_drivers": [
    "modular_mtbf_actual_improvement_share",
    "actual_review_load_share",
    "actual_uptime_share"
  ],
  "known_unmodelled_existential_gates": [
    "archive_partner_liability_acceptance_gate",
    "zero_legal_compliance_incidents_gate",
    "data_escrow_long_term_format_independence_gate"
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

Tests the $250M budget surplus against bottom-up lifetime OpEx (annual OpEx/MIU × average active fleet × 10 years); the fleet uptime margin against the 90% operational target; the human review-load margin against the 17.5% safety-buffer; and the modular-replacement MTBF improvement margin against the 30%-over-OEM R&D commitment. Archive-partner liability acceptance, zero-legal-incident compliance, and long-term data-escrow format independence are treated as unmodelled existential gates.

**Note:** This assessment is a financial / operational stress test. 3 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `archive_partner_liability_acceptance_gate` | Issue 2 names this as a load-bearing assumption: without contractual liability for pre-treatment failures the reduced on-board MIU crew size is invalidated and hardware-damage costs flow back into Phase 1 OpEx. | report.html / expert_criticism | On-board crew must absorb pre-treatment risk; OpEx per MIU rises by the $400K/year/MIU savings the Builder strategy assumed, and the Phase 3 budget collapses. |
| `zero_legal_compliance_incidents_gate` | The plan's primary compliance metric is binary; a single GDPR or copyright incident invalidates the legal framework and exposes the project to claw-backs and partner termination regardless of any operational margin the model evaluates. | report.html / selected_scenario | Loss of state-archive partnerships; possible termination of the entire pilot at the Phase 2 funding gate; reputational damage that the simulation cannot quantify but that closes the path to 200 PB. |
| `data_escrow_long_term_format_independence_gate` | Risk 7 names this as a Low/High exposure: cloud policy shifts could lock data into a single vendor and erase the societal value of the entire 10-year preservation effort. | report.html / premortem | Forced single-vendor migration at Year 10 with ~50% hosting cost inflation; the decentralized-escrow theory of post-project resilience fails and long-term societal access depends on a single counterparty. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate pilot archives accept Tier-3 financial-penalty clauses and PTM staffing, zero legal or privacy incidents across the 10-year deployment, or three cloud-escrow providers maintain format independence and migration access through Year 10. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **DOOM** — `budget_opex_surplus_usd` fails >= 0.0000 in 99.4% of simulated runs under the current input bounds.
- **DOOM** — `uptime_margin` fails >= 0.0000 in 81.8% of simulated runs under the current input bounds.
- **FRAGILE** — `modular_mtbf_improvement_margin` holds in only 39.3% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **ROBUST**, 50–80% **MARGINAL**, 20–50% **FRAGILE**, <20% **DOOM**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `budget_opex_surplus_usd` | >= 0.0000 | report_explicit | 0.6% | **DOOM** | rarely passes under current bounds |
|  | `uptime_margin` | >= 0.0000 | report_explicit | 18.2% | **DOOM** | rarely passes under current bounds |
|  | `modular_mtbf_improvement_margin` | >= 0.0000 | report_explicit | 39.3% | **FRAGILE** | fails in the majority of runs |
|  | `review_load_margin` | >= 0.0000 | report_explicit | 58.1% | **MARGINAL** | passes more often than not but uncomfortably close |

### Aggregation warning

The thresholds above use incompatible units (USD, fraction) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `budget_opex_surplus_usd` | **DOOM** | The `>= 0.0000` requirement is not credible under current bounds: only 0.6% of runs hold. Commitments that depend on this should not be made without revision. | `avg_active_fleet_size_units` (reduce toward its low bound; quartile Δ-pp -2.4) | Positive surplus leaves room for the ~30-MIU CapEx and parts inventory; negative surplus means OpEx alone exceeds the program envelope before any equipment is built. Threshold parameter: `total_budget_usd`. |
| `uptime_margin` | **DOOM** | The `>= 0.0000` requirement is not credible under current bounds: only 18.2% of runs hold. Commitments that depend on this should not be made without revision. | `actual_uptime_share` (improve toward its high bound; quartile Δ-pp +73.0) | Positive margin unlocks the Month-18 Phase 2 scaling CapEx; negative margin triggers the technical-failure path that the Builder strategy's modular R&D is designed to prevent. Threshold parameter: `target_uptime_share`. |
| `modular_mtbf_improvement_margin` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (60.7%). External commitments built on this gate are exposed. | `modular_mtbf_actual_improvement_share` (improve toward its high bound; quartile Δ-pp +97.8) | Positive margin validates the central technical bet of the Builder strategy; negative margin forces the Issue-1 pivot to cannibalization and a 50–100% MTTR increase on complex repairs. Threshold parameter: `modular_mtbf_improvement_target_share`. |
| `review_load_margin` | **MARGINAL** | The `>= 0.0000` requirement passes 58.1% of runs — close to coin-flip. Downstream commitments should not assume it holds. | `actual_review_load_share` (reduce toward its low bound; quartile Δ-pp -100.0) | Positive margin means current staffing absorbs the AI override workload; negative margin forces surge staffing and risks the 20% bottleneck breach flagged in Risk 3. Threshold parameter: `safety_buffer_review_share`. |

## Failure drivers

For each failing gate (DOOM or FRAGILE): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `budget_opex_surplus_usd` | `avg_active_fleet_size_units` | -2.4 | no single input restriction sufficient |
| `uptime_margin` | `actual_uptime_share` | +73.0 | `actual_uptime_share` above p85 |
| `modular_mtbf_improvement_margin` | `modular_mtbf_actual_improvement_share` | +97.8 | `modular_mtbf_actual_improvement_share` above p67 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `modular_mtbf_actual_improvement_share` | `modular_mtbf_improvement_margin` | 134.93 | 2.27 | model_assumption |
| 2 | `actual_review_load_share` | `review_load_margin` | 39.30 | 0.94 | model_assumption |
| 3 | `actual_uptime_share` | `uptime_margin` | 13.56 | 0.23 | model_assumption |
| 4 | `avg_active_fleet_size_units` | `budget_opex_surplus_usd` | 1.56 | 0.67 | model_assumption |
| 5 | `avg_annual_opex_per_miu_usd` | `budget_opex_surplus_usd` | 1.35 | 0.64 | report_derived |

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
| `estimated_total_lifetime_opex_usd` | **MEDIUM** | 50% | 0.65 |
| `budget_opex_surplus_usd` | **MEDIUM** | 50% | 0.65 |
| `uptime_margin` | **LOW** | 0% | 0.23 |
| `review_load_margin` | **LOW** | 0% | 0.94 |
| `modular_mtbf_improvement_margin` | **MEDIUM** | 50% | 1.47 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `estimated_total_lifetime_opex_usd` | USD | 200,000,000 | 375,000,000 | 720,000,000 |
| `budget_opex_surplus_usd` | USD | 50,000,000 | -125,000,000 | -470,000,000 |
| `uptime_margin` | fraction | -0.1500 | -0.0200 | 0.0500 |
| `review_load_margin` | fraction | 0.0750 | 0.0150 | -0.0750 |
| `modular_mtbf_improvement_margin` | fraction | -0.1500 | -0.0800 | 0.1500 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 2 declared gates in the DOOM band; 1 in the FRAGILE band. Worst: `budget_opex_surplus_usd` at 0.6% pass rate under current bounds.
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
