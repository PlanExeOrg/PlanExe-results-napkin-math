# Assessment: .mars gTLD ICANN Delegation (Builder's Pragmatic Infrastructure)

**Type:** internet_governance_program  
**Primary goal:** Secure ICANN delegation of the .mars gTLD into the DNS root zone by 2027-11-02 under the Builder's Pragmatic Infrastructure Leadership scenario, on a $25–100M+ budget, with internal HSM custody and a validated 100 kbps Mars MOS.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": ".mars gTLD ICANN Delegation (Builder's Pragmatic Infrastructure)",
  "artifact_set": {
    "version": "v46",
    "plan_slug": "20260425_mars_gtld",
    "relative_dir": "output/v46/20260425_mars_gtld"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v46/20260425_mars_gtld",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (DOOM band)",
    "worst_gate": "delegation_timing_margin_months",
    "worst_gate_pass_rate": 0.0706
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "delegation_timing_margin_months",
    "year1_registration_volume_margin_units",
    "mars_mos_margin_kbps"
  ],
  "primary_uncertainty_drivers": [
    "actual_year1_registrations_units",
    "actual_mars_endpoint_kbps",
    "actual_hsm_capex_usd"
  ],
  "known_unmodelled_existential_gates": [
    "icann_application_approval_gate",
    "major_space_agency_endorsement_gate",
    "string_contention_resolution_gate"
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

Tests the Year-1 registration-volume margin against the 5,000-domain break-even threshold; the ICANN delegation timing margin against the 18-month deadline; the budget surplus against bottom-up Year-1 cost; the Mars MOS margin against the 100 kbps sustained-downlink requirement; and the HSM-CapEx adequacy margin against the $5M minimum sovereignty floor. ICANN application approval, major space-agency endorsement, and string-contention resolution are treated as unmodelled existential gates.

**Note:** This assessment is a financial / operational stress test. 3 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `icann_application_approval_gate` | ICANN approval is the binary delegation event; without it the entire project's commercial premise collapses regardless of any operational margin the model evaluates. | report.html / selected_scenario | All Year-1 capital and political-outreach spending becomes sunk cost; first-mover advantage forfeited; the Builder strategy thesis fails entirely. |
| `major_space_agency_endorsement_gate` | Risk 1/5 names sovereign objection as the High/High blocking risk; without two major-agency endorsements the ICANN review panel faces unmitigated political controversy regardless of technical compliance. | report.html / premortem | 6–12 month delay per Risk 1 + $5–10M extra lobbying cost; ICANN may withhold delegation pending consensus that cannot be manufactured under the Builder strategy timeline. |
| `string_contention_resolution_gate` | Risk 3 names $10–20M as the contingency for string-contention defense; an aggressive competing applicant could trigger a private auction far above the contingency ceiling, exhausting the entire $100M envelope without delegation. | report.html / review_plan | Contingency drawdown beyond $20M; project must choose between auction exit (forfeiting strategy) or capital call to defend; either path threatens delegation timing and Year-1 budget surplus. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate ICANN approves the .mars gTLD application via the New gTLD Program, at least two major space agencies provide non-objection / observer support, or no competing .mars gTLD application reaches private-auction stage or contention resolves favourably. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **DOOM** — `delegation_timing_margin_months` fails >= 0.0000 in 92.9% of simulated runs under the current input bounds.
- **FRAGILE** — `year1_registration_volume_margin_units` holds in only 25.8% of simulated runs under the current input bounds (fails in the majority).
- **FRAGILE** — `mars_mos_margin_kbps` holds in only 38.8% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **ROBUST**, 50–80% **MARGINAL**, 20–50% **FRAGILE**, <20% **DOOM**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `delegation_timing_margin_months` | >= 0.0000 | report_explicit | 7.1% | **DOOM** | rarely passes under current bounds |
|  | `year1_registration_volume_margin_units` | >= 0.0000 | report_explicit | 25.8% | **FRAGILE** | fails in the majority of runs |
|  | `mars_mos_margin_kbps` | >= 0.0000 | report_explicit | 38.8% | **FRAGILE** | fails in the majority of runs |
|  | `budget_surplus_usd` | >= 0.0000 | report_explicit | 100.0% | **ROBUST** | passes in the strong majority of runs |
|  | `hsm_capex_adequacy_margin_usd` | >= 0.0000 | report_explicit | 80.5% | **ROBUST** | passes in the strong majority of runs |

### Aggregation warning

The thresholds above use incompatible units (USD, domains, kbps, months) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `delegation_timing_margin_months` | **DOOM** | The `>= 0.0000` requirement is not credible under current bounds: only 7.1% of runs hold. Commitments that depend on this should not be made without revision. | `actual_delegation_months` (reduce toward its low bound; quartile Δ-pp -20.1) | Positive margin secures first-mover advantage in interplanetary digital governance; negative margin triggers Risk 1/5 political-cost cascade and Risk 3 cost-overrun pressure on the budget envelope. Threshold parameter: `delegation_deadline_months`. |
| `year1_registration_volume_margin_units` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (74.2%). External commitments built on this gate are exposed. | `actual_year1_registrations_units` (improve toward its high bound; quartile Δ-pp +73.5) | Positive margin clears the Issue-2 break-even floor and keeps the 50% revenue pledge intact; negative margin forces conversion of the pledge to a fixed annual contribution and shrinks the Mars environmental commitment. Threshold parameter: `year1_breakeven_threshold_units`. |
| `mars_mos_margin_kbps` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (61.2%). External commitments built on this gate are exposed. | `actual_mars_endpoint_kbps` (improve toward its high bound; quartile Δ-pp +80.4) | Positive margin validates the 60-minute synchronization tier; negative margin forces the Beta-Tier restriction policy and the 15–25% Year-1 ROI loss flagged by Issue 1. Threshold parameter: `mars_mos_kbps`. |

## Failure drivers

For each failing gate (DOOM or FRAGILE): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `delegation_timing_margin_months` | `actual_delegation_months` | -20.1 | `actual_delegation_months` below p95 |
| `year1_registration_volume_margin_units` | `actual_year1_registrations_units` | +73.5 | `actual_year1_registrations_units` above p85 |
| `mars_mos_margin_kbps` | `actual_mars_endpoint_kbps` | +80.4 | `actual_mars_endpoint_kbps` above p75 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `actual_year1_registrations_units` | `year1_registration_volume_margin_units` | 109.03 | 2.00 | report_derived |
| 2 | `actual_mars_endpoint_kbps` | `mars_mos_margin_kbps` | 104.46 | 2.12 | model_assumption |
| 3 | `actual_hsm_capex_usd` | `hsm_capex_adequacy_margin_usd` | 17.84 | 1.17 | report_derived |
| 4 | `actual_delegation_months` | `delegation_timing_margin_months` | 11.89 | 0.64 | report_derived |

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
| `year1_registration_volume_margin_units` | **MEDIUM** | 100% | 1.50 |
| `delegation_timing_margin_months` | **MEDIUM** | 100% | 0.64 |
| `budget_surplus_usd` | **MEDIUM** | 100% | 1.40 |
| `mars_mos_margin_kbps` | **LOW** | 50% | 1.81 |
| `hsm_capex_adequacy_margin_usd` | **MEDIUM** | 100% | 1.17 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `year1_registration_volume_margin_units` | domains | -2,000 | -1,500 | 0.0000 |
| `delegation_timing_margin_months` | months | 2.00 | -4.00 | -12.00 |
| `budget_surplus_usd` | USD | 75,000,000 | 50,000,000 | 5,000,000 |
| `mars_mos_margin_kbps` | kbps | -20.00 | -20.00 | 0.0000 |
| `hsm_capex_adequacy_margin_usd` | USD | -2,000,000 | 1,000,000 | 5,000,000 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 1 declared gate in the DOOM band; 2 in the FRAGILE band. Worst: `delegation_timing_margin_months` at 7.1% pass rate under current bounds.
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
