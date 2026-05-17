# Assessment: Arla 'Crate Escape' Milk-Crate Recovery (Pioneer Aggressive Volume)

**Type:** consumer_csr_reverse_logistics  
**Primary goal:** Recover at least 108,000 lost Arla milk crates (40% of annual loss) across Denmark in 2026 under the Pioneer Aggressive Volume strategy on a DKK 4M budget, with ≥DKK 500K to Arla Foundation and ≥20M organic social-media impressions.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "Arla 'Crate Escape' Milk-Crate Recovery (Pioneer Aggressive Volume)",
  "artifact_set": {
    "version": "v46",
    "plan_slug": "20260303_crate_recovery_campaign",
    "relative_dir": "output/v46/20260303_crate_recovery_campaign"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v46/20260303_crate_recovery_campaign",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "fragile",
    "reason": "at least one declared gate has pass rate in 20\u201350% (FRAGILE band)",
    "worst_gate": "per_crate_handling_cost_margin_dkk",
    "worst_gate_pass_rate": 0.4204
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "crate_recovery_volume_margin_units",
    "per_crate_handling_cost_margin_dkk"
  ],
  "primary_uncertainty_drivers": [
    "actual_social_impressions",
    "actual_crate_recovery_units",
    "actual_per_crate_handling_cost_dkk"
  ],
  "known_unmodelled_existential_gates": [
    "supermarket_partner_irreverent_signoff_gate",
    "municipal_indemnity_mou_q1_gate",
    "third_party_food_grade_cleaning_capacity_gate"
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

Tests the crate-recovery volume margin against the 108,000-unit Year-1 target; the budget surplus against bottom-up program spend; the donation margin against the DKK 500K floor; the social-impressions margin against the 20M organic threshold; and the per-crate handling-cost margin against the DKK 10 channel-review trigger. Supermarket-partner irreverent-marketing signoff, municipal liability MoU execution, and third-party food-grade cleaning capacity are treated as unmodelled existential gates.

**Note:** This assessment is a financial / operational stress test. 3 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `supermarket_partner_irreverent_signoff_gate` | Risk 3 names supermarket-partner alienation as the binary reputational hinge; without retailer signoff the entire dual-channel collection model collapses regardless of consumer demand for the 5 DKK incentive. | report.html / premortem | Supermarkets reduce support; 50% reduction in organic impressions per Risk 3; DKK 500K marketing-cost increase needed to backfill virality; dual-channel collection collapses to municipal-only. |
| `municipal_indemnity_mou_q1_gate` | Decision 12 routes triage liability to municipal waste authorities under signed MoU; without Q1 signoff Risk 4 caps Q3 rollout capacity below the 108K target regardless of supermarket-channel performance. | report.html / review_plan | Municipal channel curtailed for Q3 rollout; capacity caps the 108K target per Risk 4; legal exposure for ambiguous-crate triage falls back onto Arla. |
| `third_party_food_grade_cleaning_capacity_gate` | Risk 2 names cleaning-hub bottleneck as High/High; below 7K/week the 2027 production-reduction metric fails regardless of how many crates are collected, because crates can't return to circulation. | report.html / review_plan | Throughput stall of 4–8 weeks per Risk 2 sensitivity; 2027 new-crate production reduction target fails; recovered crates accumulate as backlog inventory. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate salling Group, Coop Danmark, and Rema 1000 sign off on irreverent marketing creatives, ≥50% of Tier-1 municipalities sign liability-transfer MoUs by end of Q1 2026, or third-party food-grade washing facilities deliver ≥7,000 crates/week throughput. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **FRAGILE** — `crate_recovery_volume_margin_units` holds in only 49.6% of simulated runs under the current input bounds (fails in the majority).
- **FRAGILE** — `per_crate_handling_cost_margin_dkk` holds in only 42.0% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **ROBUST**, 50–80% **MARGINAL**, 20–50% **FRAGILE**, <20% **DOOM**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `crate_recovery_volume_margin_units` | >= 0.0000 | report_explicit | 49.6% | **FRAGILE** | fails in the majority of runs |
|  | `per_crate_handling_cost_margin_dkk` | >= 0.0000 | report_explicit | 42.0% | **FRAGILE** | fails in the majority of runs |
|  | `budget_surplus_dkk` | >= 0.0000 | report_explicit | 55.2% | **MARGINAL** | passes more often than not but uncomfortably close |
|  | `social_impressions_margin` | >= 0.0000 | report_explicit | 56.8% | **MARGINAL** | passes more often than not but uncomfortably close |
|  | `donation_margin_dkk` | >= 0.0000 | report_explicit | 80.9% | **ROBUST** | passes in the strong majority of runs |

### Aggregation warning

The thresholds above use incompatible units (DKK, DKK_per_crate, crates, impressions) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `crate_recovery_volume_margin_units` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (50.4%). External commitments built on this gate are exposed. | `actual_crate_recovery_units` (improve toward its high bound; quartile Δ-pp +100.0) | Positive margin clears the 40%-recovery success metric and supports the 2027 production-reduction claim; negative margin invalidates the Pioneer strategy thesis and the environmental rationale. Threshold parameter: `target_recovery_units`. |
| `per_crate_handling_cost_margin_dkk` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (58.0%). External commitments built on this gate are exposed. | `actual_per_crate_handling_cost_dkk` (reduce toward its low bound; quartile Δ-pp -92.3) | Positive margin keeps logistics within the non-donation envelope; negative margin triggers the Decision-2 channel-prioritization review and the Risk-8 economic-viability collapse path. Threshold parameter: `per_crate_handling_cost_threshold_dkk`. |
| `budget_surplus_dkk` | **MARGINAL** | The `>= 0.0000` requirement passes 55.2% of runs — close to coin-flip. Downstream commitments should not assume it holds. | `actual_program_spend_dkk` (reduce toward its low bound; quartile Δ-pp -100.0) | Positive surplus preserves residual funds for Decision-15 Q1-2027 habit-bridging; negative surplus triggers premature campaign halt per Risk 1 budget-exhaustion path. Threshold parameter: `total_budget_dkk`. |
| `social_impressions_margin` | **MARGINAL** | The `>= 0.0000` requirement passes 56.8% of runs — close to coin-flip. Downstream commitments should not assume it holds. | `actual_social_impressions` (improve toward its high bound; quartile Δ-pp +99.4) | Positive margin earns back the irreverent-marketing posture risk; negative margin means the Risk-3 reputational exposure was incurred without virality compensation. Threshold parameter: `target_impressions`. |

## Failure drivers

For each failing gate (DOOM or FRAGILE): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `crate_recovery_volume_margin_units` | `actual_crate_recovery_units` | +100.0 | `actual_crate_recovery_units` above p50 |
| `per_crate_handling_cost_margin_dkk` | `actual_per_crate_handling_cost_dkk` | -92.3 | `actual_per_crate_handling_cost_dkk` below p67 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `actual_social_impressions` | `social_impressions_margin` | 107.36 | 2.50 | model_assumption |
| 2 | `actual_crate_recovery_units` | `crate_recovery_volume_margin_units` | 84.80 | 1.68 | model_assumption |
| 3 | `actual_per_crate_handling_cost_dkk` | `per_crate_handling_cost_margin_dkk` | 58.35 | 1.09 | report_derived |
| 4 | `actual_program_spend_dkk` | `budget_surplus_dkk` | 35.36 | 0.79 | model_assumption |
| 5 | `actual_donation_dkk` | `donation_margin_dkk` | 28.06 | 1.92 | report_derived |

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
| `crate_recovery_volume_margin_units` | **LOW** | 0% | 1.68 |
| `budget_surplus_dkk` | **LOW** | 0% | 0.79 |
| `donation_margin_dkk` | **LOW** | 100% | 1.92 |
| `social_impressions_margin` | **LOW** | 50% | 1.62 |
| `per_crate_handling_cost_margin_dkk` | **MEDIUM** | 100% | 0.90 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `crate_recovery_volume_margin_units` | crates | -68,000 | -13,000 | 92,000 |
| `budget_surplus_dkk` | DKK | 1,500,000 | 200,000 | -1,500,000 |
| `donation_margin_dkk` | DKK | -300,000 | 100,000 | 850,000 |
| `social_impressions_margin` | impressions | -10,000,000 | -2,000,000 | 20,000,000 |
| `per_crate_handling_cost_margin_dkk` | DKK_per_crate | 2.00 | -1.00 | -3.00 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 2 in the FRAGILE band. Worst: `per_crate_handling_cost_margin_dkk` at 42.0% pass rate under current bounds.
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
