# Assessment: Denmark DKK to EUR Adoption (Builder's Blueprint)

**Type:** public_finance_transition  
**Primary goal:** Achieve full DKK to EUR currency adoption within 4-8 years via ERM II, referendum, and Eurosystem integration.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "Denmark DKK to EUR Adoption (Builder's Blueprint)",
  "artifact_set": {
    "version": "v49",
    "plan_slug": "20260129_euro_adoption",
    "relative_dir": "output/v49/20260129_euro_adoption"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v49/20260129_euro_adoption",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (Critical band)",
    "worst_gate": "contingency_buffer_dkk",
    "worst_gate_pass_rate": 0.0283
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "contingency_buffer_dkk",
    "real_indexation_margin",
    "referendum_support_margin",
    "public_awareness_margin"
  ],
  "primary_uncertainty_drivers": [
    "baseline_annual_inflation_rate",
    "actual_public_awareness",
    "actual_referendum_support"
  ],
  "known_unmodelled_existential_gates": [
    "eu_protocol_amendment_gate",
    "national_referendum_mandate_gate",
    "ecb_convergence_approval_gate"
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

Tests budget allocation, referendum and awareness thresholds, contingency reserve vs cash shock, and real-budget protection against inflation.

**Note:** This assessment is a financial / operational stress test. 3 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `eu_protocol_amendment_gate` | Requires unanimous EU agreement on a targeted protocol amendment to lift the Danish opt-out; outside any quantitative threshold. | report.html / selected_scenario | Legal pathway stalls and the entire adoption sequence cannot proceed regardless of budget or convergence. |
| `national_referendum_mandate_gate` | Binary Yes/No referendum mandate is a hard democratic gate independent of any modelled support margin. | report.html / project_plan | Project terminates; sunk costs written off and EU opt-out remains in place. |
| `ecb_convergence_approval_gate` | ECB must approve fulfilment of Maastricht convergence criteria after 24 months of ERM II participation. | report.html / project_plan | Euro adoption is blocked or delayed pending further fiscal adjustment and re-assessment. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate EU Council opt-out protocol amendment, national referendum yields mandate, or ECB convergence criteria approval. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **Critical** — `contingency_buffer_dkk` fails >= 0.0000 in 97.2% of simulated runs under the current input bounds.
- **Critical** — `real_indexation_margin` fails >= 0.0000 in 86.4% of simulated runs under the current input bounds.
- **Fragile** — `referendum_support_margin` holds in only 44.3% of simulated runs under the current input bounds (fails in the majority).
- **Fragile** — `public_awareness_margin` holds in only 40.4% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **Robust**, 50–80% **Marginal**, 20–50% **Fragile**, <20% **Critical**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `contingency_buffer_dkk` | >= 0.0000 | report_explicit | 2.8% | **Critical** | rarely passes under current bounds |
|  | `real_indexation_margin` | >= 0.0000 | report_explicit | 13.6% | **Critical** | rarely passes under current bounds |
|  | `referendum_support_margin` | >= 0.0000 | report_inferred | 44.3% | **Fragile** | fails in the majority of runs |
|  | `public_awareness_margin` | >= 0.0000 | report_inferred | 40.4% | **Fragile** | fails in the majority of runs |
|  | `public_info_budget_dkk` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |

### Aggregation warning

The thresholds above use incompatible units (DKK, fraction, ratio) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `contingency_buffer_dkk` | **Critical** | The `>= 0.0000` requirement is not credible under current bounds: only 2.8% of runs hold. Commitments that depend on this should not be made without revision. | `cash_logistics_shock_cost_dkk` (reduce toward its low bound; quartile Δ-pp -11.3) | Tests whether the ring-fenced reserve covers the cash logistics shock scenario. Threshold parameter: `contingency_reserve_dkk`. |
| `real_indexation_margin` | **Critical** | The `>= 0.0000` requirement is not credible under current bounds: only 13.6% of runs hold. Commitments that depend on this should not be made without revision. | `baseline_annual_inflation_rate` (reduce toward its low bound; quartile Δ-pp -43.8) | Tests whether annual indexation keeps committed budget value above realised inflation. Threshold parameter: `annual_real_indexation_factor`. |
| `referendum_support_margin` | **Fragile** | The `>= 0.0000` requirement fails in the majority of runs (55.7%). External commitments built on this gate are exposed. | `actual_referendum_support` (improve toward its high bound; quartile Δ-pp +100.0) | Pass/fail gate determining whether the referendum mandate is strong enough for accession. Threshold parameter: `referendum_support_threshold`. |
| `public_awareness_margin` | **Fragile** | The `>= 0.0000` requirement fails in the majority of runs (59.7%). External commitments built on this gate are exposed. | `actual_public_awareness` (improve toward its high bound; quartile Δ-pp +100.0) | Tests whether campaign pacing meets the awareness gate before referendum scheduling. Threshold parameter: `public_awareness_threshold`. |

## Failure drivers

For each failing gate (Critical or Fragile): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `contingency_buffer_dkk` | `cash_logistics_shock_cost_dkk` | -11.3 | no single input restriction sufficient |
| `real_indexation_margin` | `baseline_annual_inflation_rate` | -43.8 | no single input restriction sufficient |
| `referendum_support_margin` | `actual_referendum_support` | +100.0 | `actual_referendum_support` above p50 |
| `public_awareness_margin` | `actual_public_awareness` | +100.0 | `actual_public_awareness` above p50 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `baseline_annual_inflation_rate` | `real_indexation_margin` | 56.83 | 1.50 | report_derived |
| 2 | `actual_public_awareness` | `public_awareness_margin` | 42.61 | 0.71 | report_derived |
| 3 | `actual_referendum_support` | `referendum_support_margin` | 25.08 | 0.45 | model_assumption |
| 4 | `cash_logistics_shock_cost_dkk` | `contingency_buffer_dkk` | 18.70 | 1.70 | report_derived |

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
| `public_info_budget_dkk` | **MEDIUM** | 100% | 0.50 |
| `referendum_support_margin` | **LOW** | 0% | 0.45 |
| `public_awareness_margin` | **MEDIUM** | 100% | 0.71 |
| `contingency_buffer_dkk` | **LOW** | 100% | 1.70 |
| `real_indexation_margin` | **MEDIUM** | 50% | 0.76 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `public_info_budget_dkk` | DKK | 75,000,000 | 100,000,000 | 125,000,000 |
| `referendum_support_margin` | fraction | -0.1500 | 0.0000 | 0.1200 |
| `public_awareness_margin` | fraction | -0.3000 | 0.0000 | 0.2000 |
| `contingency_buffer_dkk` | DKK | 20,000,000 | -50,000,000 | -150,000,000 |
| `real_indexation_margin` | ratio | -0.0050 | -0.0050 | -0.0150 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 2 declared gates in the Critical band; 2 in the Fragile band. Worst: `contingency_buffer_dkk` at 2.8% pass rate under current bounds.
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
