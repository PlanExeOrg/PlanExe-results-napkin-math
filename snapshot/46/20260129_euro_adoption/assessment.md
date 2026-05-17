# Assessment: Denmark DKK→EUR Adoption (Builder's Blueprint)

**Type:** national_monetary_transition  
**Primary goal:** Replace the Danish Krone with the Euro within 4–8 years under the Builder's Blueprint, sequencing 24+ months of ERM II convergence before securing the binding referendum and opt-out repeal, all within a DKK 15–25B public-finance envelope.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "Denmark DKK\u2192EUR Adoption (Builder's Blueprint)",
  "artifact_set": {
    "version": "v46",
    "plan_slug": "20260129_euro_adoption",
    "relative_dir": "output/v46/20260129_euro_adoption"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v46/20260129_euro_adoption",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "fragile",
    "reason": "at least one declared gate has pass rate in 20\u201350% (FRAGILE band)",
    "worst_gate": "public_awareness_margin",
    "worst_gate_pass_rate": 0.3017
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "referendum_support_margin",
    "public_awareness_margin"
  ],
  "primary_uncertainty_drivers": [
    "actual_deficit_share",
    "actual_public_awareness_share",
    "actual_total_transition_cost_dkk"
  ],
  "known_unmodelled_existential_gates": [
    "eu_unanimous_optout_repeal_gate",
    "erm2_24month_completion_gate",
    "folketinget_enabling_legislation_passage_gate"
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

Tests the DKK 25B budget surplus against bottom-up transition cost; the 8-year timeline margin against projected start-to-Euro-Day duration; the referendum-support margin against the 60% mandate threshold; the deficit-compliance margin against the 3%-of-GDP Maastricht criterion; and the public-awareness margin against the 70% campaign threshold. EU unanimous opt-out repeal, completion of the 24-month ERM II period without exit, and Folketinget passage of enabling treaty legislation are treated as unmodelled existential gates.

**Note:** This assessment is a financial / operational stress test. 3 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `eu_unanimous_optout_repeal_gate` | Risk 1 names this as the central treaty-level political dependency; without unanimous EU agreement on the protocol amendment the entire Builder's Blueprint legal sequence stalls regardless of any operational margin the model evaluates. | report.html / premortem | 12–24 month delay per Risk 1; political-capital burnout in Copenhagen and Brussels; forced fallback to an uncertain legal pathway with no clear precedent for unwinding a permanent opt-out. |
| `erm2_24month_completion_gate` | The minimum 24-month ERM II window is a hard ECB requirement; a speculative-attack-driven exit or DKK realignment during the window resets the convergence clock and adds 24+ months to the timeline regardless of fiscal performance. | report.html / selected_scenario | Convergence clock restarts; 2+ additional years added to timeline; Risk 8 speculative-pressure scenario materialises with reserve depletion and unfavourable conversion-rate negotiation. |
| `folketinget_enabling_legislation_passage_gate` | Danish constitutional practice requires Folketinget approval before the referendum can ratify treaty change; without enabling legislation the referendum cannot be scheduled regardless of EU progress or convergence compliance. | report.html / review_plan | Project termination per Risk 2; DKK 500M–1B sunk costs; return to permanent opt-out and a likely multi-decade political moratorium on euro adoption. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate EU Council unanimously agrees to amend the TEU protocol lifting the Danish opt-out, denmark completes the mandatory 24-month ERM II participation without forced exit, or folketinget passes enabling treaty-change legislation by qualified majority. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **FRAGILE** — `referendum_support_margin` holds in only 31.9% of simulated runs under the current input bounds (fails in the majority).
- **FRAGILE** — `public_awareness_margin` holds in only 30.2% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **ROBUST**, 50–80% **MARGINAL**, 20–50% **FRAGILE**, <20% **DOOM**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `referendum_support_margin` | >= 0.0000 | report_explicit | 31.9% | **FRAGILE** | fails in the majority of runs |
|  | `public_awareness_margin` | >= 0.0000 | report_explicit | 30.2% | **FRAGILE** | fails in the majority of runs |
|  | `budget_surplus_dkk` | >= 0.0000 | report_explicit | 63.4% | **MARGINAL** | passes more often than not but uncomfortably close |
|  | `deficit_compliance_margin` | >= 0.0000 | report_explicit | 67.5% | **MARGINAL** | passes more often than not but uncomfortably close |
|  | `timeline_margin_years` | >= 0.0000 | report_explicit | 84.6% | **ROBUST** | passes in the strong majority of runs |

### Aggregation warning

The thresholds above use incompatible units (DKK, fraction, years) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `referendum_support_margin` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (68.1%). External commitments built on this gate are exposed. | `actual_referendum_support_share` (improve toward its high bound; quartile Δ-pp +87.6) | Positive margin secures a credible Yes mandate for treaty change; negative margin terminates the project per Risk 2 with DKK 500M–1B sunk-cost write-off. Threshold parameter: `referendum_support_threshold`. |
| `public_awareness_margin` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (69.8%). External commitments built on this gate are exposed. | `actual_public_awareness_share` (improve toward its high bound; quartile Δ-pp +85.0) | Positive margin defends the 60% Yes mandate against late-stage misinformation; negative margin forces the Strategy-11 campaign to accelerate and consumes contingency reserves. Threshold parameter: `public_awareness_threshold`. |
| `budget_surplus_dkk` | **MARGINAL** | The `>= 0.0000` requirement passes 63.4% of runs — close to coin-flip. Downstream commitments should not assume it holds. | `actual_total_transition_cost_dkk` (reduce toward its low bound; quartile Δ-pp -100.0) | Positive surplus preserves the DKK 50M+ contingency and Issue 2's inflation buffer; negative surplus forces austerity that delays Shadow Integration Team funding and cascades into Risk 4 timeline slip. Threshold parameter: `max_budget_dkk`. |
| `deficit_compliance_margin` | **MARGINAL** | The `>= 0.0000` requirement passes 67.5% of runs — close to coin-flip. Downstream commitments should not assume it holds. | `actual_deficit_share` (reduce toward its low bound; quartile Δ-pp -100.0) | Positive margin (deficit below 3% GDP) clears the ECB convergence audit; negative margin triggers Risk 3's 6–18 month delay and painful last-minute fiscal adjustments. Threshold parameter: `deficit_criterion_share`. |

## Failure drivers

For each failing gate (DOOM or FRAGILE): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `referendum_support_margin` | `actual_referendum_support_share` | +87.6 | `actual_referendum_support_share` above p75 |
| `public_awareness_margin` | `actual_public_awareness_share` | +85.0 | `actual_public_awareness_share` above p75 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `actual_deficit_share` | `deficit_compliance_margin` | 45.44 | 1.40 | report_derived |
| 2 | `actual_public_awareness_share` | `public_awareness_margin` | 36.53 | 0.62 | model_assumption |
| 3 | `actual_total_transition_cost_dkk` | `budget_surplus_dkk` | 34.96 | 0.95 | report_derived |
| 4 | `actual_referendum_support_share` | `referendum_support_margin` | 32.54 | 0.55 | model_assumption |
| 5 | `actual_timeline_years` | `timeline_margin_years` | 4.04 | 0.71 | model_assumption |

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
| `budget_surplus_dkk` | **MEDIUM** | 100% | 0.95 |
| `timeline_margin_years` | **LOW** | 0% | 0.71 |
| `referendum_support_margin` | **MEDIUM** | 50% | 0.40 |
| `deficit_compliance_margin` | **MEDIUM** | 100% | 1.40 |
| `public_awareness_margin` | **MEDIUM** | 50% | 0.45 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `budget_surplus_dkk` | DKK | 11,000,000,000 | 3,000,000,000 | -10,000,000,000 |
| `timeline_margin_years` | years | 3.00 | 1.00 | -2.00 |
| `referendum_support_margin` | fraction | -0.1000 | -0.0500 | 0.0500 |
| `deficit_compliance_margin` | fraction | 0.0200 | 0.0050 | -0.0150 |
| `public_awareness_margin` | fraction | -0.1500 | -0.0500 | 0.0500 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 2 in the FRAGILE band. Worst: `public_awareness_margin` at 30.2% pass rate under current bounds.
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
