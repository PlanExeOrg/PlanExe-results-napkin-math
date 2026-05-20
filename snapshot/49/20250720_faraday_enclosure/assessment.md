# Assessment: European Faraday Enclosure Launch (Pragmatic Foundation)

**Type:** commercial_consumer_hardware_launch  
**Primary goal:** Design, certify, and distribute a single-SKU Faraday enclosure on a €400K Year-1 budget, hitting €50K net cash from operations by Month 12 to unlock €350K follow-on funding for the MIL-STD server-grade pivot.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "European Faraday Enclosure Launch (Pragmatic Foundation)",
  "artifact_set": {
    "version": "v49",
    "plan_slug": "20250720_faraday_enclosure",
    "relative_dir": "output/v49/20250720_faraday_enclosure"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v49/20250720_faraday_enclosure",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "fragile",
    "reason": "at least one declared gate has pass rate in 20\u201350% (Fragile band)",
    "worst_gate": "sell_through_margin_units",
    "worst_gate_pass_rate": 0.2817
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "funding_trigger_margin_eur",
    "sell_through_margin_units",
    "year1_budget_surplus_eur"
  ],
  "primary_uncertainty_drivers": [
    "actual_year1_net_cash_eur",
    "actual_iso_run_sell_through_units",
    "actual_validated_demand_units"
  ],
  "known_unmodelled_existential_gates": [
    "funder_cash_flow_trigger_renegotiation_gate",
    "eu_emc_certification_pass_gate",
    "single_source_gasket_continuity_gate",
    "european_utility_model_filing_gate"
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

Tests five gates: Year-1 net-cash margin against the €50K Month-12 funding trigger; ISO-run sell-through margin against the 1,500-unit pivot threshold; gross-profit margin against the €120K MIL-STD certification cost; Year-1 budget surplus against the €400K ceiling; and validated-demand margin against the 1,000-unit Tallinn ISO commitment threshold. Funder cash-flow trigger renegotiation, EU EMC certification pass, single-source gasket continuity, and European utility-model filing are unmodelled existential gates.

**Note:** This assessment is a financial / operational stress test. 4 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `funder_cash_flow_trigger_renegotiation_gate` | Risk 1 names this as the single biggest governance risk: without renegotiation the funder retains unilateral interpretation of the trigger, and a single late retailer payment can withhold the €350K follow-on regardless of operational success. | report.html / premortem | €350K follow-on lost; server-grade pivot defunded; project terminates with €400K sunk Year-1 investment. |
| `eu_emc_certification_pass_gate` | Risk 5 / Issue 2 name certification as a hard prerequisite for consumer market entry; Issue 2 specifically names 30–50% cost escalation on test failure and 3-month delay killing the funding trigger. | report.html / expert_criticism | Consumer retail launch blocked; Year-1 revenue collapses to near-zero; funding trigger unreachable. |
| `single_source_gasket_continuity_gate` | Risk 6 names 4-8 week production delay on single-source German supplier failure; Issue 3 names 8-12 week typical lead time. The plan's split-production schedule has no slack for either. | report.html / review_plan | Production halts for weeks; pre-order chargebacks per Risk 9 trigger; funding trigger missed. |
| `european_utility_model_filing_gate` | Risk 13 names 6-month reverse-engineering window; without filing the design can be copied by Chinese manufacturers undercutting by 50%, eroding both Year-1 and B2B pivot margins. | report.html / review_plan | Price erosion 50%; gross-profit margin collapses; pivot trigger and Year-1 net cash both miss. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate funder agrees to renegotiate 'positive cash flow' to '€50K net cash by Month 12' by Month 6, EU EMC Directive certification (CE mark) achieved before Year-1 retail launch, conductive gasket / copper-beryllium finger stock supply continuity for the ISO run, or european utility model for the gasket-channel manufacturing process filed before Month 6. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **Fragile** — `funding_trigger_margin_eur` holds in only 40.1% of simulated runs under the current input bounds (fails in the majority).
- **Fragile** — `sell_through_margin_units` holds in only 28.2% of simulated runs under the current input bounds (fails in the majority).
- **Fragile** — `year1_budget_surplus_eur` holds in only 41.0% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **Robust**, 50–80% **Marginal**, 20–50% **Fragile**, <20% **Critical**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `funding_trigger_margin_eur` | >= 0.0000 | report_explicit | 40.1% | **Fragile** | fails in the majority of runs |
|  | `sell_through_margin_units` | >= 0.0000 | report_explicit | 28.2% | **Fragile** | fails in the majority of runs |
|  | `year1_budget_surplus_eur` | >= 0.0000 | report_explicit | 41.0% | **Fragile** | fails in the majority of runs |
|  | `certification_funding_margin_eur` | >= 0.0000 | report_explicit | 54.1% | **Marginal** | passes more often than not but uncomfortably close |
|  | `iso_commit_demand_margin_units` | >= 0.0000 | report_explicit | 54.2% | **Marginal** | passes more often than not but uncomfortably close |

### Aggregation warning

The thresholds above use incompatible units (EUR, units) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `funding_trigger_margin_eur` | **Fragile** | The `>= 0.0000` requirement fails in the majority of runs (59.9%). External commitments built on this gate are exposed. | `actual_year1_net_cash_eur` (improve toward its high bound; quartile Δ-pp +100.0) | Positive margin unlocks the €350K follow-on funding for the server-grade pivot; negative margin kills the entire pivot thesis regardless of operational success. Threshold parameter: `funding_trigger_net_cash_eur`. |
| `sell_through_margin_units` | **Fragile** | The `>= 0.0000` requirement fails in the majority of runs (71.8%). External commitments built on this gate are exposed. | `actual_iso_run_sell_through_units` (improve toward its high bound; quartile Δ-pp +100.0) | Positive margin clears inventory and funds the next stage; negative margin triggers Risk 2's €75K unsold-inventory scenario and depletes the cash runway. Threshold parameter: `iso_run_sell_through_units_target`. |
| `year1_budget_surplus_eur` | **Fragile** | The `>= 0.0000` requirement fails in the majority of runs (59.0%). External commitments built on this gate are exposed. | `actual_year1_spend_eur` (reduce toward its low bound; quartile Δ-pp -100.0) | Positive surplus preserves the 5% contingency for cert re-test or supplier resilience; negative surplus forces marketing cuts that depress the very pre-sales the pivot trigger depends on. Threshold parameter: `year1_budget_ceiling_eur`. |
| `certification_funding_margin_eur` | **Marginal** | The `>= 0.0000` requirement passes 54.1% of runs — close to coin-flip. Downstream commitments should not assume it holds. | `actual_gross_profit_eur` (improve toward its high bound; quartile Δ-pp +100.0) | Positive margin funds the server-grade pivot certification internally; negative margin forces the binary-bet pricing problem named in Risk 4 (€89K at €99) and stalls the B2B pivot. Threshold parameter: `mil_std_certification_cost_eur`. |
| `iso_commit_demand_margin_units` | **Marginal** | The `>= 0.0000` requirement passes 54.2% of runs — close to coin-flip. Downstream commitments should not assume it holds. | `actual_validated_demand_units` (improve toward its high bound; quartile Δ-pp +100.0) | Positive margin justifies committing €150K to the 2,000-unit ISO run; negative margin keeps production at the 500-unit Latvian-batch level and delays the certification-funded pivot. Threshold parameter: `iso_commit_demand_threshold_units`. |

## Failure drivers

For each failing gate (Critical or Fragile): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `funding_trigger_margin_eur` | `actual_year1_net_cash_eur` | +100.0 | `actual_year1_net_cash_eur` above p50 |
| `sell_through_margin_units` | `actual_iso_run_sell_through_units` | +100.0 | `actual_iso_run_sell_through_units` above p67 |
| `year1_budget_surplus_eur` | `actual_year1_spend_eur` | -100.0 | `actual_year1_spend_eur` below p50 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `actual_year1_net_cash_eur` | `funding_trigger_margin_eur` | 203.59 | 3.40 | report_derived |
| 2 | `actual_iso_run_sell_through_units` | `sell_through_margin_units` | 59.86 | 0.83 | report_derived |
| 3 | `actual_validated_demand_units` | `iso_commit_demand_margin_units` | 59.55 | 1.30 | model_assumption |
| 4 | `actual_gross_profit_eur` | `certification_funding_margin_eur` | 42.09 | 0.92 | report_derived |
| 5 | `actual_year1_spend_eur` | `year1_budget_surplus_eur` | 17.69 | 0.30 | report_derived |

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
| `funding_trigger_margin_eur` | **LOW** | 100% | 3.40 |
| `sell_through_margin_units` | **MEDIUM** | 100% | 0.83 |
| `certification_funding_margin_eur` | **MEDIUM** | 100% | 0.92 |
| `year1_budget_surplus_eur` | **HIGH** | 100% | 0.30 |
| `iso_commit_demand_margin_units` | **LOW** | 0% | 1.30 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `funding_trigger_margin_eur` | EUR | -100,000 | 0.0000 | 70,000 |
| `sell_through_margin_units` | units | -900.00 | 0.0000 | 350.00 |
| `certification_funding_margin_eur` | EUR | -50,000 | 0.0000 | 60,000 |
| `year1_budget_surplus_eur` | EUR | 50,000 | 0.0000 | -70,000 |
| `iso_commit_demand_margin_units` | units | -600.00 | 0.0000 | 700.00 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 3 in the Fragile band. Worst: `sell_through_margin_units` at 28.2% pass rate under current bounds.
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
