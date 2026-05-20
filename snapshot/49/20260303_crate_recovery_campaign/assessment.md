# Assessment: Arla 'Crate Escape' Milk Crate Recovery Campaign 2026

**Type:** commercial_csr_reverse_logistics  
**Primary goal:** Recover 40% (108,000) of annually lost Arla milk crates in 2026 within a 4M DKK budget while donating at least 500,000 DKK to the Arla Foundation.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "Arla 'Crate Escape' Milk Crate Recovery Campaign 2026",
  "artifact_set": {
    "version": "v49",
    "plan_slug": "20260303_crate_recovery_campaign",
    "relative_dir": "output/v49/20260303_crate_recovery_campaign"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v49/20260303_crate_recovery_campaign",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "marginal",
    "reason": "at least one declared gate has pass rate in 50\u201380% (Marginal band)",
    "worst_gate": "volume_target_margin",
    "worst_gate_pass_rate": 0.683
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [],
  "primary_uncertainty_drivers": [
    "expected_recovered_crates"
  ],
  "known_unmodelled_existential_gates": [
    "municipal_liability_transfer_gate",
    "supermarket_marketing_preapproval_gate",
    "food_grade_cleaning_compliance_gate"
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

Bottom-up viability of dual-channel recovery: per-crate handling cost vs logistics budget, donation spend vs donation ceiling, and combined budget surplus against the 4M DKK cap.

**Note:** This assessment is a financial / operational stress test. 3 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `municipal_liability_transfer_gate` | Q3 national rollout depends on signed indemnity agreements with Tier 1 municipal waste authorities; legal failure curtails the municipal channel. | report.html / project_plan | Municipal channel cannot operate; volume capped below 108,000 and Q3/Q4 capacity collapses. |
| `supermarket_marketing_preapproval_gate` | Salling, Coop, and Rema 1000 must approve creatives or partnerships fracture, jeopardizing the primary collection channel. | report.html / data_collection | Retail partners withdraw in-store drop-off support; primary collection channel and viral marketing both fail. |
| `food_grade_cleaning_compliance_gate` | Cleaned crates must pass Danish food-grade standards to re-enter the dairy supply chain; non-compliance blocks reuse entirely. | report.html / project_plan | Recovered crates cannot be reintroduced; 2027 new-crate production reduction goal fails regardless of volume. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate municipal triage liability transfer MoUs, supermarket sign-off on irreverent marketing tone, or food-grade sanitation certification for third-party cleaning hubs. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **Still missing input** — `projected_donation_spend_dkk`: Tests whether actual recovered volume * 5 DKK incentive lands between 500k floor and 1.35M ceiling.

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **Robust**, 50–80% **Marginal**, 20–50% **Fragile**, <20% **Critical**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `volume_target_margin` | >= 0.0000 | model_defined | 68.3% | **Marginal** | passes more often than not but uncomfortably close |
|  | `projected_donation_spend_dkk` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |
|  | `donation_ceiling_margin_dkk` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |
|  | `total_projected_spend_dkk` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |
|  | `program_budget_surplus_dkk` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |

### Aggregation warning

The thresholds above use incompatible units (DKK, crates) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `volume_target_margin` | **Marginal** | The `>= 0.0000` requirement passes 68.3% of runs — close to coin-flip. Downstream commitments should not assume it holds. | `expected_recovered_crates` (improve toward its high bound; quartile Δ-pp +100.0) | Tests the primary 40% volume gate; positive means the year-one KPI is cleared. Threshold parameter: `target_recovered_crates`. |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `expected_recovered_crates` | `volume_target_margin` | 30.82 | 0.97 | model_assumption |

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
| `projected_donation_spend_dkk` | **LOW** | 0% | 0.97 |
| `donation_ceiling_margin_dkk` | **LOW** | 0% | 0.97 |
| `volume_target_margin` | **LOW** | 0% | 0.97 |
| `total_projected_spend_dkk` | **LOW** | 0% | 0.97 |
| `program_budget_surplus_dkk` | **LOW** | 0% | 0.97 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `projected_donation_spend_dkk` | DKK | 375,000 | 540,000 | 900,000 |
| `donation_ceiling_margin_dkk` | DKK | 975,000 | 810,000 | 450,000 |
| `volume_target_margin` | crates | -33,000 | 0.0000 | 72,000 |
| `total_projected_spend_dkk` | DKK | 3,025,000 | 3,190,000 | 3,550,000 |
| `program_budget_surplus_dkk` | DKK | 975,000 | 810,000 | 450,000 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above. No declared gate is in the Critical or Fragile band — but read the bounds and trust boundaries before treating that as a green light.
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
