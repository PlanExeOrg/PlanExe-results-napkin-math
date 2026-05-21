# Assessment: Crate Escape: Arla Milk Crate Recovery Campaign 2026

**Type:** commercial_csr_reverse_logistics  
**Primary goal:** Recover 108,000 lost Arla milk crates (40% of 270,000 annual loss) in 2026 via dual-channel reverse logistics under a 4,000,000 DKK budget ceiling.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "Crate Escape: Arla Milk Crate Recovery Campaign 2026",
  "artifact_set": {
    "version": "v58",
    "plan_slug": "20260303_crate_recovery_campaign",
    "relative_dir": "output/v58/20260303_crate_recovery_campaign"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v58/20260303_crate_recovery_campaign",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "fragile",
    "reason": "at least one declared gate has pass rate in 20\u201350% (Fragile band)",
    "worst_gate": "logistics_budget_surplus_dkk",
    "worst_gate_pass_rate": 0.4427
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "logistics_budget_surplus_dkk"
  ],
  "primary_uncertainty_drivers": [
    "logistics_cost_per_crate_dkk",
    "expected_recovered_crates",
    "marketing_cost_realized_dkk"
  ],
  "known_unmodelled_existential_gates": [
    "municipal_indemnity_mou_gate",
    "supermarket_marketing_signoff_gate",
    "food_grade_compliance_gate"
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

Tests volume gate, donation cap, logistics budget, foundation contribution floor, and the overall 4M DKK envelope against per-crate donation outlay and logistics burn.

**Note:** This assessment is a financial / operational stress test. 3 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `municipal_indemnity_mou_gate` | Q3 nationwide rollout depends on legally executed indemnity agreements with at least 50% of Tier 1 municipalities. | report.html / project_plan | Municipal channel cannot launch in Q3; volume capped well below 108,000 and program viability collapses. |
| `supermarket_marketing_signoff_gate` | Salling Group, Coop Danmark, and Rema 1000 must approve creatives or the primary collection channel withdraws partnership. | report.html / data_collection | Forced pivot to testimonial/CO2 tone with up to 50% loss of organic impressions and additional paid-media cost. |
| `food_grade_compliance_gate` | Cleaned crates re-entering the dairy supply chain must meet Danish food-grade standards; non-compliance halts reintroduction. | report.html / project_plan | Cleaned inventory cannot re-enter dairy cycle; 2027 production-reduction goal fails. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate municipal liability transfer MoUs by Q1 end, supermarket pre-approval of irreverent marketing tone, or food-grade sanitation certification of cleaning hubs. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **Fragile** — `logistics_budget_surplus_dkk` holds in only 44.3% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **Robust**, 50–80% **Marginal**, 20–50% **Fragile**, <20% **Critical**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `logistics_budget_surplus_dkk` | >= 0.0000 | report_explicit | 44.3% | **Fragile** | fails in the majority of runs |
|  | `donation_cap_buffer_dkk` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |
|  | `total_budget_surplus_dkk` | >= 0.0000 | report_explicit | 83.5% | **Robust** | passes in the strong majority of runs |

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `logistics_budget_surplus_dkk` | **Fragile** | The `>= 0.0000` requirement fails in the majority of runs (55.7%). External commitments built on this gate are exposed. | `logistics_cost_per_crate_dkk` (reduce toward its low bound; quartile Δ-pp -85.3) | Positive value confirms logistics burn stays within the dedicated 1.65M DKK line item. Threshold parameter: `logistics_budget_dkk`. |

## Failure drivers

For each failing gate (Critical or Fragile): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `logistics_budget_surplus_dkk` | `logistics_cost_per_crate_dkk` | -85.3 | `logistics_cost_per_crate_dkk` below p67 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `logistics_cost_per_crate_dkk` | `logistics_budget_surplus_dkk` | 53.89 | 1.13 | report_derived |
| 2 | `expected_recovered_crates` | `logistics_budget_surplus_dkk` | 30.36 | 0.88 | report_derived |
| 3 | `marketing_cost_realized_dkk` | `total_budget_surplus_dkk` | 1.63 | 0.70 | report_derived |

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
| `donation_outlay_dkk` | **MEDIUM** | 100% | 0.88 |
| `donation_cap_buffer_dkk` | **MEDIUM** | 100% | 0.88 |
| `logistics_cost_total_dkk` | **MEDIUM** | 100% | 1.01 |
| `logistics_budget_surplus_dkk` | **MEDIUM** | 100% | 1.01 |
| `total_budget_surplus_dkk` | **MEDIUM** | 100% | 0.90 |
| `volume_target_surplus` | **MEDIUM** | 100% | 0.88 |
| `foundation_donation_margin_dkk` | **MEDIUM** | 100% | 0.88 |
| `recovery_rate_margin` | **MEDIUM** | 100% | 0.88 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `donation_outlay_dkk` | DKK | 325,000 | 540,000 | 800,000 |
| `donation_cap_buffer_dkk` | DKK | 1,025,000 | 810,000 | 550,000 |
| `logistics_cost_total_dkk` | DKK | 520,000 | 1,620,000 | 4,000,000 |
| `logistics_budget_surplus_dkk` | DKK | 1,130,000 | 30,000 | -2,350,000 |
| `total_budget_surplus_dkk` | DKK | 2,355,000 | 840,000 | -2,300,000 |
| `volume_target_surplus` | crates | -43,000 | 0.0000 | 52,000 |
| `foundation_donation_margin_dkk` | DKK | -175,000 | 40,000 | 300,000 |
| `recovery_rate_margin` | fraction | -0.1593 | 0.0000 | 0.1926 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 1 in the Fragile band. Worst: `logistics_budget_surplus_dkk` at 44.3% pass rate under current bounds.
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
