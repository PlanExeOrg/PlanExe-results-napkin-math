# Assessment: White House East Wing Container Casino (Pioneer's Gauntlet)

**Type:** high_risk_political_commercial_venture  
**Primary goal:** Launch Phase 1 container casino on the demolished White House East Wing site to clear 90 continuous days of profitable operation at $50K daily NOI, unlock the 75% sponsor capital tranche, and segregate $90M into an externally auditable political-reversal contingency.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "White House East Wing Container Casino (Pioneer's Gauntlet)",
  "artifact_set": {
    "version": "v49",
    "plan_slug": "20251026_casino_royale",
    "relative_dir": "output/v49/20251026_casino_royale"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v49/20251026_casino_royale",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (Critical band)",
    "worst_gate": "contingency_fund_margin_usd",
    "worst_gate_pass_rate": 0.0
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "continuous_profitable_days_margin",
    "contingency_fund_margin_usd",
    "budget_surplus_usd",
    "blackout_duration_margin_days"
  ],
  "primary_uncertainty_drivers": [
    "actual_blackout_days",
    "actual_daily_noi_usd",
    "actual_continuous_profitable_days"
  ],
  "known_unmodelled_existential_gates": [
    "gsa_doi_post_facto_authorization_gate",
    "aml_kyc_banking_consortium_compliance_gate",
    "sovereign_leader_diplomatic_participation_gate",
    "court_injunction_avoidance_gate"
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

Tests five gates: continuous-profitable-days margin against the 90-day sponsor-unlock threshold; daily-NOI margin against the $50K/day Phase-1 floor; budget surplus against the $600M sponsor ceiling; political-contingency-fund margin against the $90M ring-fenced target; and relocation-blackout-duration margin against the 7-day operational pause. GSA/DOI post-facto authorization, AML/KYC International Banking Consortium acceptance, sovereign-leader diplomatic participation, and court-injunction avoidance are unmodelled existential gates.

**Note:** This assessment is a financial / operational stress test. 4 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `gsa_doi_post_facto_authorization_gate` | Issue 1 names this as a near-100%-probability existential failure mode: without legal pathway the entire $600M deployment is stranded regardless of operational performance; expert review judges the standard authorization timeline incompatible with the 15-day diplomatic engagement window. | report.html / expert_criticism | Project halts immediately; $90M contingency drawn down; 100% of $510M undeployed construction budget lost; ROI reduced 80–100% per Issue 1 sensitivity. |
| `aml_kyc_banking_consortium_compliance_gate` | Data Item 4 names AML/KYC compliance as the existential prerequisite for high-roller revenue capture; loss of banking access shocks liquidity from the consortium and halts settlement of patron markers regardless of physical operations. | report.html / expert_criticism | High-value patron settlements halt; daily NOI collapses well below $50K target; sponsor unlock missed; ancillary services cannot bridge the gap. |
| `sovereign_leader_diplomatic_participation_gate` | Review-plan names sovereign-leader participation as the load-bearing assumption for the 60/40 high-roller-diplomatic mix that the daily-NOI arithmetic depends on; boycotts driven by geopolitical instability are an unmodelled stress test. | report.html / review_plan | Diplomatic-allocation 40% sits empty; high-roller 60% cannot absorb full 999-guest capacity; daily NOI shifts below $50K floor. |
| `court_injunction_avoidance_gate` | Premortem FM1 / Expert Criticism: a single adverse court ruling halts the project mid-construction with 6–12 month delay and $10M+ legal cost, stranding all temporary-facility investment regardless of revenue performance. | report.html / premortem | 6–12 month construction halt; $10M+ legal costs; container facility stranded; all sponsor capital frozen pending legal resolution. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate GSA and DOI issue conditional Notice-to-Proceed for post-facto White House East Wing land-use authorization, international Banking Consortium accepts Decision-14 Option-1 (fungible bank-settled high-value transactions only), sovereign-leader delegations participate in the venue at expected levels (40% diplomatic-allocation prerequisite), or no adverse court ruling halts construction during Phase 1 build or Phase 2 foundation. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **Critical** — `continuous_profitable_days_margin` fails >= 0.0000 in 91.1% of simulated runs under the current input bounds.
- **Critical** — `contingency_fund_margin_usd` fails >= 0.0000 in 100.0% of simulated runs under the current input bounds.
- **Fragile** — `budget_surplus_usd` holds in only 44.9% of simulated runs under the current input bounds (fails in the majority).
- **Fragile** — `blackout_duration_margin_days` holds in only 32.6% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **Robust**, 50–80% **Marginal**, 20–50% **Fragile**, <20% **Critical**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `continuous_profitable_days_margin` | >= 0.0000 | report_explicit | 8.8% | **Critical** | rarely passes under current bounds |
|  | `contingency_fund_margin_usd` | >= 0.0000 | report_explicit | 0.0% | **Critical** | rarely passes under current bounds |
|  | `budget_surplus_usd` | >= 0.0000 | report_explicit | 44.9% | **Fragile** | fails in the majority of runs |
|  | `blackout_duration_margin_days` | >= 0.0000 | report_explicit | 32.6% | **Fragile** | fails in the majority of runs |
|  | `daily_noi_margin_usd` | >= 0.0000 | report_explicit | 53.8% | **Marginal** | passes more often than not but uncomfortably close |

### Aggregation warning

The thresholds above use incompatible units (USD, days) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `continuous_profitable_days_margin` | **Critical** | The `>= 0.0000` requirement is not credible under current bounds: only 8.8% of runs hold. Commitments that depend on this should not be made without revision. | `actual_continuous_profitable_days` (improve toward its high bound; quartile Δ-pp +33.9) | Positive margin unlocks the 75% sponsor capital tranche ($450M); negative margin strands Phase-2 mobilization and forces the project to draw down the $90M contingency for opex bridging. Threshold parameter: `profitable_days_target`. |
| `contingency_fund_margin_usd` | **Critical** | The `>= 0.0000` requirement is not credible under current bounds: only 0.0% of runs hold. Commitments that depend on this should not be made without revision. | Saturated failure: pass rate is 0.0% and no single input quartile movement changes that. Quartile sensitivity is not informative; audit the input bounds and the threshold definition. | Positive margin keeps the political-reversal remediation runway intact; negative margin leaves the project unable to execute Decision-10 site-restoration within the 90-day reversal mandate. Threshold parameter: `contingency_fund_target_usd`. |
| `budget_surplus_usd` | **Fragile** | The `>= 0.0000` requirement fails in the majority of runs (55.1%). External commitments built on this gate are exposed. | `actual_total_spend_usd` (reduce toward its low bound; quartile Δ-pp -100.0) | Positive surplus preserves the contingency for political-reversal remediation; negative surplus forces sponsor capital call mid-Phase-1 and erodes the unlock-trigger arithmetic. Threshold parameter: `budget_ceiling_usd`. |
| `blackout_duration_margin_days` | **Fragile** | The `>= 0.0000` requirement fails in the majority of runs (67.4%). External commitments built on this gate are exposed. | `actual_blackout_days` (reduce toward its low bound; quartile Δ-pp -100.0) | Positive margin keeps the post-relocation 60-day profit window inside the sponsor's 90-day clock; negative margin breaks the continuous-profit gate per Issue 2's stress test. Threshold parameter: `blackout_target_days`. |
| `daily_noi_margin_usd` | **Marginal** | The `>= 0.0000` requirement passes 53.8% of runs — close to coin-flip. Downstream commitments should not assume it holds. | `actual_daily_noi_usd` (improve toward its high bound; quartile Δ-pp +100.0) | Positive margin satisfies the profitability arithmetic of the sponsor unlock; negative margin breaks the unlock even on days the venue operates without incident. Threshold parameter: `daily_noi_target_usd`. |

## Failure drivers

For each failing gate (Critical or Fragile): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `continuous_profitable_days_margin` | `actual_continuous_profitable_days` | +33.9 | `actual_continuous_profitable_days` above p95 |
| `contingency_fund_margin_usd` | (saturated failure) | n/a | saturated failure: no single input restriction can lift the pass rate; revisit bounds and threshold |
| `budget_surplus_usd` | `actual_total_spend_usd` | -100.0 | `actual_total_spend_usd` below p50 |
| `blackout_duration_margin_days` | `actual_blackout_days` | -100.0 | `actual_blackout_days` below p75 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

Note: the saturated Critical gate `contingency_fund_margin_usd` is absent from the ranking because no single missing-input restriction can lift its pass rate under current bounds. The inputs below target the next most decision-relevant non-saturated gates; the saturated gate needs a bounds or threshold-definition audit, not a single input fix.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `actual_blackout_days` | `blackout_duration_margin_days` | 86.67 | 1.29 | report_derived |
| 2 | `actual_daily_noi_usd` | `daily_noi_margin_usd` | 60.02 | 1.30 | report_derived |
| 3 | `actual_continuous_profitable_days` | `continuous_profitable_days_margin` | 22.32 | 0.72 | report_derived |
| 4 | `actual_total_spend_usd` | `budget_surplus_usd` | 16.53 | 0.30 | report_derived |

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
| `continuous_profitable_days_margin` | **MEDIUM** | 100% | 0.72 |
| `daily_noi_margin_usd` | **MEDIUM** | 100% | 1.30 |
| `budget_surplus_usd` | **HIGH** | 100% | 0.30 |
| `contingency_fund_margin_usd` | **HIGH** | 100% | 0.33 |
| `blackout_duration_margin_days` | **MEDIUM** | 100% | 1.29 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `continuous_profitable_days_margin` | days | -60.00 | 0.0000 | 5.00 |
| `daily_noi_margin_usd` | USD | -30,000 | 0.0000 | 35,000 |
| `budget_surplus_usd` | USD | 80,000,000 | 0.0000 | -100,000,000 |
| `contingency_fund_margin_usd` | USD | -30,000,000 | 0.0000 | 0.0000 |
| `blackout_duration_margin_days` | days | 2.00 | 0.0000 | -7.00 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 2 declared gates in the Critical band; 2 in the Fragile band. Worst: `contingency_fund_margin_usd` at 0.0% pass rate under current bounds.
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
