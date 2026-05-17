# Assessment: Nuuk Community Clay Workshop

**Type:** small_business_community_hub  
**Primary goal:** Establish a community clay workshop near Katuaq Cultural Centre in Nuuk, operational by 2026-09-15, surviving Year 1 within a 2,000,000 DKK budget under the 'Builder's Balance' low-risk strategy.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "Nuuk Community Clay Workshop",
  "artifact_set": {
    "version": "v46",
    "plan_slug": "20260215_nuuk_clay_workshop",
    "relative_dir": "output/v46/20260215_nuuk_clay_workshop"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v46/20260215_nuuk_clay_workshop",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (DOOM band)",
    "worst_gate": "monthly_off_peak_rental_overhead_margin_dkk",
    "worst_gate_pass_rate": 0.0001
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "monthly_off_peak_rental_overhead_margin_dkk",
    "year1_budget_surplus_dkk",
    "taster_conversion_margin"
  ],
  "primary_uncertainty_drivers": [
    "taster_conversion_actual_share",
    "monthly_fixed_operating_cost_dkk",
    "low_season_utilization_actual_share"
  ],
  "known_unmodelled_existential_gates": [
    "greenlandic_labor_law_contractor_gate",
    "commercial_lease_by_july_2026_gate",
    "utility_variance_approval_gate"
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

Tests the Year-1 budget surplus after ring-fencing the 15% contingency; the monthly off-peak rental revenue against monthly utility overhead; and the Taster-Session conversion margin against the 15% target. Greenlandic labor-law contractor viability, commercial lease execution by 2026-07-01, and Nuuk utility-variance approval by 2026-08-15 are treated as unmodelled existential gates.

**Note:** This assessment is a financial / operational stress test. 3 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `greenlandic_labor_law_contractor_gate` | Expert Issue 3 and Risk 4 name this as the single most critical staffing assumption; if Greenlandic labor law mandates employee classification, fixed labor cost rises 20–35% and consumes 60–90% of the contingency before any operational stress. | report.html / expert_criticism | Fixed labor cost rises 20–35% in Year 1, exhausting 60–90% of the 300K DKK contingency and delaying essential infrastructure improvements; staffing must pivot to a salaried model with full severance exposure. |
| `commercial_lease_by_july_2026_gate` | Without a lease executed by 2026-07-01 the 10-week fit-out cannot complete by the 2026-09-15 operational readiness target; the Q3 peak revenue window slips and Year-1 revenue mix assumptions collapse. | report.html / review_plan | Operational readiness slips past 2026-09-15; Year-1 revenue base loses the Q3 peak; material-buffer order may auto-reduce to 3 months per the Expert Criticism gate, weakening supply-chain resilience. |
| `utility_variance_approval_gate` | C1 zoning requires an 8–12 week variance review for the high-draw centralized kiln; without approval by 2026-08-15 the kiln cannot operate at planned load and the fit-out must stop to avoid rework. | report.html / review_plan | Up to 6 weeks delay to full capacity, ~150,000 DKK in lost revenue per Risk 4; potential pivot to the industrial-zone Location 3 with cultural-visibility tradeoffs. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate greenlandic labor law permits the part-time contractor staffing model, commercial lease near Katuaq secured by 2026-07-01, or nuuk municipal utility variance approved by 2026-08-15. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **DOOM** — `monthly_off_peak_rental_overhead_margin_dkk` fails >= 0.0000 in 100.0% of simulated runs under the current input bounds.
- **FRAGILE** — `year1_budget_surplus_dkk` holds in only 43.8% of simulated runs under the current input bounds (fails in the majority).
- **FRAGILE** — `taster_conversion_margin` holds in only 43.3% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **ROBUST**, 50–80% **MARGINAL**, 20–50% **FRAGILE**, <20% **DOOM**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `monthly_off_peak_rental_overhead_margin_dkk` | >= 0.0000 | model_defined | 0.0% | **DOOM** | rarely passes under current bounds |
|  | `year1_budget_surplus_dkk` | >= 0.0000 | report_explicit | 43.8% | **FRAGILE** | fails in the majority of runs |
|  | `taster_conversion_margin` | >= 0.0000 | report_explicit | 43.3% | **FRAGILE** | fails in the majority of runs |

### Aggregation warning

The thresholds above use incompatible units (DKK, DKK_per_month, fraction) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `monthly_off_peak_rental_overhead_margin_dkk` | **DOOM** | The `>= 0.0000` requirement is not credible under current bounds: only 0.0% of runs hold. Commitments that depend on this should not be made without revision. | Saturated failure: pass rate is 0.0% and no single input quartile movement changes that. Quartile sensitivity is not informative; audit the input bounds and the threshold definition. | Positive margin means the 165 DKK/hr off-peak rental stream covers utility/heating overhead during the Nov–Feb shoulder season; negative margin forces the pivot to low-margin co-op slots (Mitigation Plan). |
| `year1_budget_surplus_dkk` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (56.2%). External commitments built on this gate are exposed. | `monthly_fixed_operating_cost_dkk` (reduce toward its low bound; quartile Δ-pp -100.0) | Tests the central financial claim that 1.7M DKK (2M minus the 15% ring-fenced contingency) is enough to cover 12 months of Year-1 fixed operations under the Builder's Balance staffing model. Threshold parameter: `year1_budget_dkk`. |
| `taster_conversion_margin` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (56.7%). External commitments built on this gate are exposed. | `taster_conversion_actual_share` (improve toward its high bound; quartile Δ-pp +96.3) | Below zero the local membership pipeline starves the winter revenue base; below the Expert-Criticism 12.5% cut-off the entire Taster outreach budget must redirect to digital assets. Threshold parameter: `taster_conversion_target_share`. |

## Failure drivers

For each failing gate (DOOM or FRAGILE): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `monthly_off_peak_rental_overhead_margin_dkk` | (saturated failure) | n/a | saturated failure: no single input restriction can lift the pass rate; revisit bounds and threshold |
| `year1_budget_surplus_dkk` | `monthly_fixed_operating_cost_dkk` | -100.0 | `monthly_fixed_operating_cost_dkk` below p50 |
| `taster_conversion_margin` | `taster_conversion_actual_share` | +96.3 | `taster_conversion_actual_share` above p67 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

Note: the saturated DOOM gate `monthly_off_peak_rental_overhead_margin_dkk` is absent from the ranking because no single missing-input restriction can lift its pass rate under current bounds. The inputs below target the next most decision-relevant non-saturated gates; the saturated gate needs a bounds or threshold-definition audit, not a single input fix.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `taster_conversion_actual_share` | `taster_conversion_margin` | 84.05 | 1.54 | model_assumption |
| 2 | `monthly_fixed_operating_cost_dkk` | `year1_budget_surplus_dkk` | 40.14 | 0.71 | model_assumption |
| 3 | `low_season_utilization_actual_share` | `monthly_off_peak_rental_overhead_margin_dkk` | 0.06 | 1.60 | model_assumption |
| 4 | `monthly_utility_overhead_dkk` | `monthly_off_peak_rental_overhead_margin_dkk` | 0.06 | 1.60 | model_assumption |
| 5 | `off_peak_hours_per_month` | `monthly_off_peak_rental_overhead_margin_dkk` | 0.04 | 1.00 | model_assumption |

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
| `total_year1_fixed_operating_cost_dkk` | **LOW** | 0% | 0.71 |
| `year1_budget_surplus_dkk` | **LOW** | 0% | 0.71 |
| `monthly_off_peak_rental_revenue_dkk` | **MEDIUM** | 33% | 1.01 |
| `monthly_off_peak_rental_overhead_margin_dkk` | **LOW** | 25% | 1.16 |
| `taster_conversion_margin` | **MEDIUM** | 50% | 1.10 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `total_year1_fixed_operating_cost_dkk` | DKK | 1,200,000 | 1,680,000 | 2,400,000 |
| `year1_budget_surplus_dkk` | DKK | 500,000 | 20,000 | -700,000 |
| `monthly_off_peak_rental_revenue_dkk` | DKK_per_month | 780.00 | 4,125 | 16,000 |
| `monthly_off_peak_rental_overhead_margin_dkk` | DKK_per_month | -9,220 | -20,875 | -34,000 |
| `taster_conversion_margin` | fraction | -0.0500 | -0.0200 | 0.0500 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 1 declared gate in the DOOM band; 2 in the FRAGILE band. Worst: `monthly_off_peak_rental_overhead_margin_dkk` at 0.0% pass rate under current bounds.
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
