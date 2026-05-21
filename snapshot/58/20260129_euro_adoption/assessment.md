# Assessment: Denmark DKK to EUR Adoption (Builder's Blueprint)

**Type:** public_finance_national_transition  
**Primary goal:** Achieve full Denmark currency transition from DKK to EUR within 4-8 years via sequenced ERM II compliance, referendum mandate, and operational conversion.

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
    "version": "v58",
    "plan_slug": "20260129_euro_adoption",
    "relative_dir": "output/v58/20260129_euro_adoption"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v58/20260129_euro_adoption",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (Critical band)",
    "worst_gate": "contingency_buffer_after_cash_shock_dkk",
    "worst_gate_pass_rate": 0.0
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "budget_envelope_surplus_dkk",
    "contingency_buffer_after_cash_shock_dkk",
    "public_info_funding_surplus_dkk",
    "combined_financial_viability_surplus_dkk"
  ],
  "primary_uncertainty_drivers": [
    "estimated_public_info_required_cost_dkk",
    "estimated_transition_cost_dkk",
    "baseline_inflation_rate"
  ],
  "known_unmodelled_existential_gates": [
    "eu_optout_repeal_gate",
    "national_referendum_mandate_gate",
    "ecb_convergence_approval_gate",
    "nationalbank_eurosystem_integration_gate",
    "joint_ministerial_consensus_governance_gate"
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

Quantifies budget adequacy (transition cost vs envelope), inflation erosion of the multi-year budget, contingency runway against cash-logistics shock, and public-information funding coverage. Does not model EU treaty repeal, referendum mandate, or ECB convergence approval — those are unmodelled gates.

**Note:** This assessment is a financial / operational stress test. 5 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `eu_optout_repeal_gate` | Requires unanimous EU agreement / Extraordinary Council protocol amendment; the model treats this as binary and does not test it. | report.html / project_plan | 12-24 month delay or project termination; no legal path to EUR adoption. |
| `national_referendum_mandate_gate` | Binary Yes/No referendum is the constitutional gate; failure ends the program and triggers DKK 500M-1B sunk-cost write-off. | report.html / project_plan | Project termination; return to permanent opt-out; preparatory legislation auto-repealed. |
| `ecb_convergence_approval_gate` | Maastricht criteria (deficit, debt, inflation, interest rates) must be met during ERM II; pass/fail is determined by ECB, not by the model. | report.html / project_plan | 6-18 month delay; forced fiscal adjustments; referendum cannot be scheduled. |
| `nationalbank_eurosystem_integration_gate` | TARGET2 / payment-system integration is a technical readiness gate the model assumes succeeds; integration failure adds 4-6 months remediation. | report.html / project_plan | Inability to operate on Euro Day; isolation/non-compliance with Eurosystem. |
| `joint_ministerial_consensus_governance_gate` | Quarterly consensus-based governance must avoid paralysis; bottlenecks could extend timeline beyond 8 years, but the model has no quantitative test. | report.html / selected_scenario | Cascading delays across IT, contracts, and cash-logistics workstreams. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate EU treaty opt-out repeal agreement, danish national referendum mandate, ECB convergence criteria approval, danmarks Nationalbank Eurosystem integration, or joint Ministerial Consultative Body consensus velocity. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **Critical** — `budget_envelope_surplus_dkk` fails >= 0.0000 in 92.6% of simulated runs under the current input bounds.
- **Critical** — `contingency_buffer_after_cash_shock_dkk` fails >= 0.0000 in 100.0% of simulated runs under the current input bounds.
- **Critical** — `public_info_funding_surplus_dkk` fails >= 0.0000 in 84.6% of simulated runs under the current input bounds.
- **Critical** — `combined_financial_viability_surplus_dkk` fails >= 0.0000 in 100.0% of simulated runs under the current input bounds.
- **Scenario warn (all)** — `q_inflation_indexation_adequacy`: Skipped: formula_hint is null.

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **Robust**, 50–80% **Marginal**, 20–50% **Fragile**, <20% **Critical**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `budget_envelope_surplus_dkk` | >= 0.0000 | model_defined | 7.4% | **Critical** | rarely passes under current bounds |
|  | `contingency_buffer_after_cash_shock_dkk` | >= 0.0000 | report_explicit | 0.0% | **Critical** | rarely passes under current bounds |
|  | `public_info_funding_surplus_dkk` | >= 0.0000 | report_explicit | 15.4% | **Critical** | rarely passes under current bounds |
| min | `combined_financial_viability_surplus_dkk` | >= 0.0000 | model_defined | 0.0% | **Critical** | rarely passes under current bounds |

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `budget_envelope_surplus_dkk` | **Critical** | The `>= 0.0000` requirement is not credible under current bounds: only 7.4% of runs hold. Commitments that depend on this should not be made without revision. | `estimated_transition_cost_dkk` (reduce toward its low bound; quartile Δ-pp -29.2) | Tests whether the stated DKK 15B floor (in real terms) covers the estimated bottom-up cost of executing the transition. |
| `contingency_buffer_after_cash_shock_dkk` | **Critical** | The `>= 0.0000` requirement is not credible under current bounds: only 0.0% of runs hold. Commitments that depend on this should not be made without revision. | Saturated failure: pass rate is 0.0% and no single input quartile movement changes that. Quartile sensitivity is not informative; audit the input bounds and the threshold definition. | Tests whether the DKK 50M ring-fenced reserve covers the stated DKK 100M dual-circulation overhead shock. Threshold parameter: `ring_fenced_contingency_dkk`. |
| `public_info_funding_surplus_dkk` | **Critical** | The `>= 0.0000` requirement is not credible under current bounds: only 15.4% of runs hold. Commitments that depend on this should not be made without revision. | `estimated_public_info_required_cost_dkk` (reduce toward its low bound; quartile Δ-pp -59.8) | Tests whether the 0.5% mandated allocation covers required campaign scope — referendum mitigation depends on this. Threshold parameter: `total_transition_budget_floor_dkk`. |
| `combined_financial_viability_surplus_dkk` | **Critical** | The `>= 0.0000` requirement is not credible under current bounds: only 0.0% of runs hold. Commitments that depend on this should not be made without revision. | Saturated failure: pass rate is 0.0% and no single input quartile movement changes that. Quartile sensitivity is not informative; audit the input bounds and the threshold definition. | Worst-of-three gate: each pressure draws on a different pool (capital envelope vs contingency escrow vs comms allocation), so min() — not sum — is the right aggregator. |

## Failure drivers

For each failing gate (Critical or Fragile): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `budget_envelope_surplus_dkk` | `estimated_transition_cost_dkk` | -29.2 | no single input restriction sufficient |
| `contingency_buffer_after_cash_shock_dkk` | (saturated failure) | n/a | saturated failure: no single input restriction can lift the pass rate; revisit bounds and threshold |
| `public_info_funding_surplus_dkk` | `estimated_public_info_required_cost_dkk` | -59.8 | `estimated_public_info_required_cost_dkk` below p85 |
| `combined_financial_viability_surplus_dkk` | (saturated failure) | n/a | saturated failure: no single input restriction can lift the pass rate; revisit bounds and threshold |

Binding-gate notes (aggregates only):

- `combined_financial_viability_surplus_dkk` (fails 10,000 runs): `budget_envelope_surplus_dkk` is the binder in 92.3% of failed runs.

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

Note: the saturated Critical gates `contingency_buffer_after_cash_shock_dkk`, `combined_financial_viability_surplus_dkk` are absent from the ranking because no single missing-input restriction can lift their pass rates under current bounds. The inputs below target the next most decision-relevant non-saturated gates; saturated gates need a bounds or threshold-definition audit, not a single input fix.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `estimated_public_info_required_cost_dkk` | `public_info_funding_surplus_dkk` | 80.02 | 1.58 | model_assumption |
| 2 | `estimated_transition_cost_dkk` | `budget_envelope_surplus_dkk` | 37.91 | 1.40 | model_assumption |
| 3 | `baseline_inflation_rate` | `budget_envelope_surplus_dkk` | 5.42 | 1.25 | report_derived |

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
| `real_budget_after_inflation_dkk` | **MEDIUM** | 100% | 1.10 |
| `budget_envelope_surplus_dkk` | **MEDIUM** | 80% | 1.16 |
| `contingency_buffer_after_cash_shock_dkk` | **MEDIUM** | 100% | 1.50 |
| `public_info_funding_surplus_dkk` | **MEDIUM** | 50% | 1.04 |
| `combined_financial_viability_surplus_dkk` | **MEDIUM** | 71% | 1.27 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `real_budget_after_inflation_dkk` | DKK | 14,414,705,167 | 15,806,290,515 | 14,017,555,835 |
| `budget_envelope_surplus_dkk` | DKK | 2,414,705,167 | -4,193,709,485 | -25,982,444,165 |
| `contingency_buffer_after_cash_shock_dkk` | DKK | 0.0000 | -50,000,000 | -150,000,000 |
| `public_info_funding_surplus_dkk` | DKK | 15,000,000 | -20,000,000 | -125,000,000 |
| `combined_financial_viability_surplus_dkk` | DKK | 0.0000 | -4,193,709,485 | -25,982,444,165 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 4 declared gates in the Critical band. Worst: `contingency_buffer_after_cash_shock_dkk` at 0.0% pass rate under current bounds.
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
