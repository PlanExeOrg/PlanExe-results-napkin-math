# Assessment: EU Cross-Border Rail Single Through-Ticketing Program

**Type:** Public-sector regulatory and infrastructure coordination program  
**Primary goal:** Achieve 40% of eligible cross-border journeys sold as single through-tickets within five years via OSDM standardization and inter-carrier clearing.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "EU Cross-Border Rail Single Through-Ticketing Program",
  "artifact_set": {
    "version": "v49",
    "plan_slug": "20260514_cross_border_rail_ticketing",
    "relative_dir": "output/v49/20260514_cross_border_rail_ticketing"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v49/20260514_cross_border_rail_ticketing",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (Critical band)",
    "worst_gate": "budget_allocation_surplus_eur",
    "worst_gate_pass_rate": 0.0
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "budget_allocation_surplus_eur"
  ],
  "primary_uncertainty_drivers": [],
  "known_unmodelled_existential_gates": [
    "dg_move_legal_mandate_gate",
    "three_strikes_political_acceptance_gate",
    "tiered_liability_legal_defensibility_gate",
    "clearing_mechanism_banking_authorization_gate"
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

Five-year EU coordination program with a EUR 1.5B public budget; the model evaluates budget allocation coverage, clearing-float adequacy versus peak daily obligation, expected through-ticket volume and clearing revenue at the 40% adoption gate, and governance personnel burn.

**Note:** This assessment is a financial / operational stress test. 4 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `dg_move_legal_mandate_gate` | Mandatory API exposure and three-strikes enforcement require legal authority from DG MOVE; without it, no compliance lever exists. | report.html / project_plan | Operators face no enforceable obligation, three-strikes is unusable, and the 40% adoption target collapses. |
| `three_strikes_political_acceptance_gate` | Suspending sales for SNCF, DB, or OEBB risks coordinated political resistance the model cannot quantify. | report.html / premortem | Enforcement is blocked at Council level, allowing non-compliance to persist past the 18- and 30-month deadlines. |
| `tiered_liability_legal_defensibility_gate` | Strict tiered liability must survive operator legal challenge under EU passenger rights law; this is a binary legal outcome. | report.html / expert_criticism | Backstop architecture collapses, forcing renegotiation and stalling rollout on contested corridors. |
| `clearing_mechanism_banking_authorization_gate` | Managing the centralized clearing float requires specific regulatory authorization that the model treats as given. | report.html / project_plan | Clearing mechanism cannot legally hold the EUR 200M float, blocking single-payment settlement entirely. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate DG MOVE legal mandate for OSDM exposure, political acceptance of three-strikes enforcement, legal defensibility of tiered liability model, or authorization to operate centralized clearing/settlement float. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **Critical** — `budget_allocation_surplus_eur` fails >= 0.0000 in 100.0% of simulated runs under the current input bounds.

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **Robust**, 50–80% **Marginal**, 20–50% **Fragile**, <20% **Critical**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `budget_allocation_surplus_eur` | >= 0.0000 | report_explicit | 0.0% | **Critical** | rarely passes under current bounds |
|  | `expected_annual_through_tickets` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |
|  | `expected_annual_clearing_revenue_eur` | >= 0.0000 | model_defined | 100.0% | **Robust** | passes in the strong majority of runs |
|  | `emergency_float_buffer_eur` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |
|  | `governance_personnel_cost_two_year_eur` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |

### Aggregation warning

The thresholds above use incompatible units (EUR, tickets_per_year) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `budget_allocation_surplus_eur` | **Critical** | The `>= 0.0000` requirement is not credible under current bounds: only 0.0% of runs hold. Commitments that depend on this should not be made without revision. | Saturated failure: pass rate is 0.0% and no single input quartile movement changes that. Quartile sensitivity is not informative; audit the input bounds and the threshold definition. | Shows residual headroom in the EUR 1.5B envelope after named allocations; positive means slack for governance, contingencies, or top-ups. Threshold parameter: `total_public_coordination_budget_eur`. |

## Failure drivers

For each failing gate (Critical or Fragile): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `budget_allocation_surplus_eur` | (saturated failure) | n/a | saturated failure: no single input restriction can lift the pass rate; revisit bounds and threshold |

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
| `expected_annual_through_tickets` | **MEDIUM** | 100% | 1.14 |
| `expected_annual_clearing_revenue_eur` | **LOW** | 100% | 1.63 |
| `emergency_float_buffer_eur` | **LOW** | 0% | 1.56 |
| `governance_personnel_cost_two_year_eur` | **MEDIUM** | 100% | 0.80 |
| `clearing_revenue_buffer_eur` | **LOW** | 100% | 1.63 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `expected_annual_through_tickets` | tickets_per_year | 8,000,000 | 14,000,000 | 24,000,000 |
| `expected_annual_clearing_revenue_eur` | EUR | 2,400,000 | 11,200,000 | 48,000,000 |
| `emergency_float_buffer_eur` | EUR | 240,000,000 | 165,000,000 | 30,000,000 |
| `budget_allocation_surplus_eur` | EUR | -50,000,000 | -50,000,000 | -50,000,000 |
| `governance_personnel_cost_two_year_eur` | EUR | 8,400,000 | 12,600,000 | 18,480,000 |
| `clearing_revenue_buffer_eur` | EUR | -197,600,000 | -188,800,000 | -152,000,000 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 1 declared gate in the Critical band. Worst: `budget_allocation_surplus_eur` at 0.0% pass rate under current bounds.
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
