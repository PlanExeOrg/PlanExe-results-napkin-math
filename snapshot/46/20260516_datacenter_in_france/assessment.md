# Assessment: Hauts-de-France 9 GW Sovereign AI Datacenter Campus

**Type:** hyperscale_infrastructure  
**Primary goal:** Complete Phase 1 (500 MW–1 GW) of the Hauts-de-France hyperscale AI campus within 36 months at PUE ≤1.20, while securing a binding RTE allocation and 60% tenant take-or-pay commitment for the 1–3 GW Phase 2 expansion before Phase 1 construction FID.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "Hauts-de-France 9 GW Sovereign AI Datacenter Campus",
  "artifact_set": {
    "version": "v46",
    "plan_slug": "20260516_datacenter_in_france",
    "relative_dir": "output/v46/20260516_datacenter_in_france"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v46/20260516_datacenter_in_france",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "fragile",
    "reason": "at least one declared gate has pass rate in 20\u201350% (FRAGILE band)",
    "worst_gate": "phase2_fid_margin",
    "worst_gate_pass_rate": 0.3256
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "phase2_fid_margin",
    "phase1_pue_margin"
  ],
  "primary_uncertainty_drivers": [
    "tenant_take_or_pay_actual_share",
    "phase1_pue_actual",
    "brownfield_remediation_actual_eur"
  ],
  "known_unmodelled_existential_gates": [
    "rte_binding_3gw_allocation_gate",
    "dgsi_anssi_sovereign_partition_signoff_gate",
    "judicial_review_80pct_buffer_gate",
    "social_license_workforce_heat_reuse_gate"
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

Tests the Phase 1 budget surplus against baseline CAPEX plus brownfield remediation plus the buffer-land 18-month holding cost; the Phase 2 FID tenant-commitment margin against the 60% take-or-pay threshold; and the Phase 1 PUE margin against the 1.20 operational ceiling. RTE binding 3 GW allocation, DGSI/ANSSI sovereign-partition signoff, judicial review of the 80% buffer model, and social license on local workforce and heat-reuse are treated as unmodelled existential gates.

**Note:** This assessment is a financial / operational stress test. 4 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `rte_binding_3gw_allocation_gate` | Risk 3 and Review Issue 1 name this as the keystone external dependency; without a binding RTE contract the Phase 2 expansion cannot be financed and Phase 1 capital is at risk of stranding. | report.html / premortem | Stranded €1B–€2B Phase 0/1 capital if tenants withdraw; the 9 GW scaling pathway is closed regardless of tenant commitment or operational performance. |
| `dgsi_anssi_sovereign_partition_signoff_gate` | Risk 5 and the Selected Scenario gates name DGSI/ANSSI signoff as binary; without it the premium domestic revenue stream (€10–20B long-term) is lost and the 60% Phase 2 commitment threshold becomes unreachable. | report.html / selected_scenario | Loss of €10–20B premium domestic revenue stream per Risk 5; tenant pipeline narrows to non-classified commercial only, depressing the Phase 2 commitment margin. |
| `judicial_review_80pct_buffer_gate` | Risk 7 names a High/High likelihood-severity for a judicial appeal cutting buildable area from 30 km² to <20 km²; that constrains the 9 GW target to 3–4 GW and forces a fundamental business-case re-evaluation. | report.html / review_plan | Prefecture-mandated buildable-area reduction to <20 km²; full 9 GW target is capped at 3–4 GW; long-term NPV collapses by 30–40% per Review Issue 2 sensitivity. |
| `social_license_workforce_heat_reuse_gate` | The Mitigation Plan ties social license to immediate skills-academy funding and heat-reuse feasibility; if these fail, the buffer-permit pathway and the workforce mandate trigger political backlash that the simulation cannot resolve. | report.html / expert_criticism | Prefecture-mandated footprint reduction; Phase 2 expansion permits stall; the workforce premium overshoots Review Issue 3's 5% modeling assumption and erodes the Phase 1 schedule by 6–12 months. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate RTE issues a binding 3 GW transmission allocation before Phase 1 construction FID, DGSI/ANSSI signoff for sovereign AI partition by Q1 2027, no successful judicial challenge to the hyper-dense 80% buffer model, or local social license sustained via 75% local workforce mandate and heat-reuse contracts. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **FRAGILE** — `phase2_fid_margin` holds in only 32.6% of simulated runs under the current input bounds (fails in the majority).
- **FRAGILE** — `phase1_pue_margin` holds in only 40.6% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **ROBUST**, 50–80% **MARGINAL**, 20–50% **FRAGILE**, <20% **DOOM**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `phase2_fid_margin` | >= 0.0000 | report_explicit | 32.6% | **FRAGILE** | fails in the majority of runs |
|  | `phase1_pue_margin` | >= 0.0000 | report_explicit | 40.6% | **FRAGILE** | fails in the majority of runs |
|  | `phase1_budget_surplus_eur` | >= 0.0000 | report_explicit | 87.9% | **ROBUST** | passes in the strong majority of runs |

### Aggregation warning

The thresholds above use incompatible units (EUR, fraction, ratio) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `phase2_fid_margin` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (67.4%). External commitments built on this gate are exposed. | `tenant_take_or_pay_actual_share` (improve toward its high bound; quartile Δ-pp +100.0) | Positive margin unlocks Phase 2 expansion FID and the path to 9 GW; negative margin strands the €1B–€2B Phase 0/1 capital flagged in Risk 3. Threshold parameter: `phase2_take_or_pay_threshold_share`. |
| `phase1_pue_margin` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (59.4%). External commitments built on this gate are exposed. | `phase1_pue_actual` (reduce toward its low bound; quartile Δ-pp -88.6) | Positive margin means Phase 1 holds PUE at or below 1.20; negative margin triggers Risk 2 tenant SLA escalators and threatens Phase 2 tenant retention. Threshold parameter: `phase1_pue_target_max`. |

## Failure drivers

For each failing gate (DOOM or FRAGILE): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `phase2_fid_margin` | `tenant_take_or_pay_actual_share` | +100.0 | `tenant_take_or_pay_actual_share` above p67 |
| `phase1_pue_margin` | `phase1_pue_actual` | -88.6 | `phase1_pue_actual` below p67 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `tenant_take_or_pay_actual_share` | `phase2_fid_margin` | 74.18 | 1.10 | model_assumption |
| 2 | `phase1_pue_actual` | `phase1_pue_margin` | 9.92 | 0.19 | report_derived |
| 3 | `brownfield_remediation_actual_eur` | `phase1_budget_surplus_eur` | 5.58 | 2.67 | report_derived |
| 4 | `phase1_baseline_capex_eur` | `phase1_budget_surplus_eur` | 5.01 | 0.92 | report_derived |
| 5 | `buffer_annual_holding_cost_per_ha_eur` | `phase1_budget_surplus_eur` | 1.73 | 1.17 | report_derived |

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
| `buffer_annual_holding_cost_eur` | **MEDIUM** | 100% | 1.17 |
| `buffer_total_holding_cost_eur` | **MEDIUM** | 100% | 1.17 |
| `phase1_budget_surplus_eur` | **LOW** | 100% | 1.58 |
| `phase2_fid_margin` | **LOW** | 0% | 1.10 |
| `phase1_pue_margin` | **HIGH** | 100% | 0.16 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `buffer_annual_holding_cost_eur` | EUR_per_year | 386,400,000 | 772,800,000 | 1,288,000,000 |
| `buffer_total_holding_cost_eur` | EUR | 579,600,000 | 1,159,200,000 | 1,932,000,000 |
| `phase1_budget_surplus_eur` | EUR | 5,670,400,000 | 2,090,800,000 | -3,182,000,000 |
| `phase2_fid_margin` | fraction | -0.3000 | -0.1000 | 0.2500 |
| `phase1_pue_margin` | ratio | 0.0300 | -0.0200 | -0.0500 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 2 in the FRAGILE band. Worst: `phase2_fid_margin` at 32.6% pass rate under current bounds.
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
