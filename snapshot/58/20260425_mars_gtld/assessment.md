# Assessment: .mars gTLD Application

**Type:** Internet governance / gTLD registry acquisition  
**Primary goal:** Secure ICANN delegation of the .mars gTLD within 18 months under the 'Builder' strategy, with internal HSM-based DNSSEC control and a viable Year 1 financial base before the 50% revenue pledge re-activates.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": ".mars gTLD Application",
  "artifact_set": {
    "version": "v58",
    "plan_slug": "20260425_mars_gtld",
    "relative_dir": "output/v58/20260425_mars_gtld"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v58/20260425_mars_gtld",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (Critical band)",
    "worst_gate": "y1_revenue_surplus_usd",
    "worst_gate_pass_rate": 0.0
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "y1_revenue_surplus_usd",
    "contingency_after_shocks_surplus_usd"
  ],
  "primary_uncertainty_drivers": [
    "string_contention_probability",
    "annual_opex_usd"
  ],
  "known_unmodelled_existential_gates": [
    "icann_delegation_approval_gate",
    "space_agency_endorsement_gate",
    "sovereign_acceptance_gate",
    "fips_140_2_certification_gate"
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

Tests Year 1 financial viability of the registry: whether the upfront budget envelope covers HSM CapEx, base OpEx, and the contingency draw from regulatory/political and string-contention shocks, and whether projected Year 1 revenue covers base overhead before the suspended 50% pledge resumes.

**Note:** This assessment is a financial / operational stress test. 4 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `icann_delegation_approval_gate` | Without ICANN's Board approving the .mars delegation, no operational scenario matters; this is the binding regulatory authorization the model treats as a fixed yes/no input rather than a sampled probability. | report.html / project_plan | The registry never operates; all budgeted CapEx and OpEx is sunk cost. |
| `space_agency_endorsement_gate` | The 'Builder' strategy hinges on securing observational support / non-objection from at least two major space agencies before ICANN review; failure unwinds the political legitimacy claim. | report.html / executive_summary | ICANN review momentum stalls; political backlash risk (Risk 5) realizes at the high end. |
| `sovereign_acceptance_gate` | Premortem and Expert Criticism repeatedly warn that ITU/UN COPUOS or government objection to private operation of a planetary namespace is an existential gate the financial model cannot test. | report.html / premortem | Delegation rejected or reversed; the entire 7-year governance pathway collapses. |
| `fips_140_2_certification_gate` | Data Collection Item 3 mandates this certification by Q4 2026 to invalidate the externally-delegated DNSSEC posture; failure forfeits cryptographic sovereignty per Expert Criticism. | report.html / data_collection | Plan reverts to outsourced DNSSEC, re-introducing the existential security risk experts flagged. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate ICANN delegation approval, major space agency public endorsement, sovereign / international body acceptance of private planetary namespace, or internal HSM FIPS 140-2 Level 3 certification. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **Critical** — `y1_revenue_surplus_usd` fails >= 0.0000 in 100.0% of simulated runs under the current input bounds.
- **Fragile** — `contingency_after_shocks_surplus_usd` holds in only 23.4% of simulated runs under the current input bounds (fails in the majority).
- **Scenario warn (all)** — `q_breakeven_volume_feasibility`: Skipped: formula_hint is null.

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **Robust**, 50–80% **Marginal**, 20–50% **Fragile**, <20% **Critical**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `y1_revenue_surplus_usd` | >= 0.0000 | report_explicit | 0.0% | **Critical** | rarely passes under current bounds |
|  | `contingency_after_shocks_surplus_usd` | >= 0.0000 | report_explicit | 23.4% | **Fragile** | fails in the majority of runs |
|  | `capital_runway_surplus_usd` | >= 0.0000 | report_explicit | 93.0% | **Robust** | passes in the strong majority of runs |

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `y1_revenue_surplus_usd` | **Critical** | The `>= 0.0000` requirement is not credible under current bounds: only 0.0% of runs hold. Commitments that depend on this should not be made without revision. | Saturated failure: pass rate is 0.0% and no single input quartile movement changes that. Quartile sensitivity is not informative; audit the input bounds and the threshold definition. | Gate: positive surplus after OpEx AND the 50% pledge means the plan covers base overhead even with the pledge active; negative means the pledge must stay suspended or the operating base drains. Threshold parameter: `revenue_pledge_fraction`. |
| `contingency_after_shocks_surplus_usd` | **Fragile** | The `>= 0.0000` requirement fails in the majority of runs (76.6%). External commitments built on this gate are exposed. | `contingency_reserve_usd` (improve toward its high bound; quartile Δ-pp +51.0) | Tests whether the ring-fenced $10M-$20M contingency absorbs the named shocks; positive = the contingency line item survives. Threshold parameter: `contingency_reserve_usd`. |

## Failure drivers

For each failing gate (Critical or Fragile): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `y1_revenue_surplus_usd` | (saturated failure) | n/a | saturated failure: no single input restriction can lift the pass rate; revisit bounds and threshold |
| `contingency_after_shocks_surplus_usd` | `contingency_reserve_usd` | +51.0 | no single input restriction sufficient |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

Note: the saturated Critical gate `y1_revenue_surplus_usd` is absent from the ranking because no single missing-input restriction can lift its pass rate under current bounds. The inputs below target the next most decision-relevant non-saturated gates; the saturated gate needs a bounds or threshold-definition audit, not a single input fix.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `string_contention_probability` | `contingency_after_shocks_surplus_usd` | 32.50 | 1.25 | model_assumption |
| 2 | `annual_opex_usd` | `capital_runway_surplus_usd` | 0.56 | 0.93 | report_derived |

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
| `y1_revenue_usd` | **LOW** | 100% | 3.57 |
| `breakeven_registrations_y1` | **LOW** | 100% | 1.63 |
| `y1_revenue_surplus_usd` | **LOW** | 100% | 2.69 |
| `contingency_after_shocks_surplus_usd` | **MEDIUM** | 80% | 0.98 |
| `capital_runway_surplus_usd` | **MEDIUM** | 100% | 0.89 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `y1_revenue_usd` | USD | 25,000 | 375,000 | 5,000,000 |
| `breakeven_registrations_y1` | domains | 200,000 | 100,000 | 60,000 |
| `y1_revenue_surplus_usd` | USD | -4,975,000 | -7,125,000 | -7,000,000 |
| `contingency_after_shocks_surplus_usd` | USD | 2,000,000 | -1,500,000 | -15,000,000 |
| `capital_runway_surplus_usd` | USD | 3,750,000 | 16,250,000 | 43,000,000 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 1 declared gate in the Critical band; 1 in the Fragile band. Worst: `y1_revenue_surplus_usd` at 0.0% pass rate under current bounds.
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
