# Assessment: Containerized Dark Data Ingestor Network (CDDIN)

**Type:** Large-scale physical-digital infrastructure preservation program  
**Primary goal:** Recover 200+ petabytes of at-risk 1950-2000 archival media via 30 mobile ingest units over 10 years

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "Containerized Dark Data Ingestor Network (CDDIN)",
  "artifact_set": {
    "version": "v49",
    "plan_slug": "20260201_media_rescue",
    "relative_dir": "output/v49/20260201_media_rescue"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v49/20260201_media_rescue",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (Critical band)",
    "worst_gate": "fleet_lifetime_opex_budget_margin_usd",
    "worst_gate_pass_rate": 0.0
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "fleet_lifetime_opex_budget_margin_usd",
    "uptime_margin_fraction",
    "pretreatment_reliability_margin_fraction"
  ],
  "primary_uncertainty_drivers": [
    "achieved_pretreatment_reliability_fraction",
    "achieved_fleet_uptime_fraction"
  ],
  "known_unmodelled_existential_gates": [
    "data_escrow_agreements_gate",
    "archive_tier3_liability_acceptance_gate",
    "gdpr_marker_taxonomy_approval_gate",
    "transport_and_hazmat_licensing_gate"
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

Tests whether the $250M budget, 30-MIU fleet, AI-plus-human review buffer, uptime target, and pre-treatment reliability gates collectively support the 200 PB recovery mandate.

**Note:** This assessment is a financial / operational stress test. 4 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `data_escrow_agreements_gate` | Plan requires legally binding, irrevocable escrow with three global cloud providers to decentralize long-term data risk. | report.html / project_plan | Long-term format independence and post-10-year value of recovered data are lost; recovery mandate is partially negated. |
| `archive_tier3_liability_acceptance_gate` | Builder strategy assumes archives sign Tier 3 financial-penalty contracts covering pre-treatment failures causing >48h downtime. | report.html / premortem | Reduced on-board MIU crew assumption is invalidated and OpEx-saving $400k/year/MIU benefit collapses. |
| `gdpr_marker_taxonomy_approval_gate` | Compliance specialist must finalize a GDPR-aligned international marker taxonomy accepted across host jurisdictions. | report.html / data_collection | Zero-legal-incidents metric fails and human-review compliance framework loses regulatory standing. |
| `transport_and_hazmat_licensing_gate` | Global MIU deployment requires international transport permits, hazmat handling licences, and export-import clearances per host country. | report.html / project_plan | MIUs cannot legally cross borders or operate generators on partner sites, halting fleet deployment. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate binding three-provider data escrow agreements, archive partner Tier 3 liability acceptance, regulatory approval of PII/copyright marker taxonomy, or cross-border transport and hazmat licensing. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **Critical** — `fleet_lifetime_opex_budget_margin_usd` fails >= 0.0000 in 100.0% of simulated runs under the current input bounds.
- **Fragile** — `uptime_margin_fraction` holds in only 32.0% of simulated runs under the current input bounds (fails in the majority).
- **Fragile** — `pretreatment_reliability_margin_fraction` holds in only 40.4% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **Robust**, 50–80% **Marginal**, 20–50% **Fragile**, <20% **Critical**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `fleet_lifetime_opex_budget_margin_usd` | >= 0.0000 | report_explicit | 0.0% | **Critical** | rarely passes under current bounds |
|  | `uptime_margin_fraction` | >= 0.0000 | report_explicit | 32.0% | **Fragile** | fails in the majority of runs |
|  | `pretreatment_reliability_margin_fraction` | >= 0.0000 | report_explicit | 40.4% | **Fragile** | fails in the majority of runs |
|  | `review_load_buffer_margin_fraction` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |
|  | `phase1_budget_margin_usd` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |

### Aggregation warning

The thresholds above use incompatible units (USD, fraction) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `fleet_lifetime_opex_budget_margin_usd` | **Critical** | The `>= 0.0000` requirement is not credible under current bounds: only 0.0% of runs hold. Commitments that depend on this should not be made without revision. | Saturated failure: pass rate is 0.0% and no single input quartile movement changes that. Quartile sensitivity is not informative; audit the input bounds and the threshold definition. | Tests whether the $250M envelope can absorb full-fleet OpEx for the full program; positive means the budget covers steady-state operations. Threshold parameter: `total_program_budget_usd`. |
| `uptime_margin_fraction` | **Fragile** | The `>= 0.0000` requirement fails in the majority of runs (68.0%). External commitments built on this gate are exposed. | `achieved_fleet_uptime_fraction` (improve toward its high bound; quartile Δ-pp +100.0) | Direct read on the primary operational gate; positive means the maintenance program clears the 90% bar. Threshold parameter: `uptime_target_fraction`. |
| `pretreatment_reliability_margin_fraction` | **Fragile** | The `>= 0.0000` requirement fails in the majority of runs (59.7%). External commitments built on this gate are exposed. | `achieved_pretreatment_reliability_fraction` (improve toward its high bound; quartile Δ-pp +100.0) | Direct read on the archive-partner gate; positive means partners stay above the augmentation-fee trigger. Threshold parameter: `pretreatment_reliability_threshold_fraction`. |

## Failure drivers

For each failing gate (Critical or Fragile): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `fleet_lifetime_opex_budget_margin_usd` | (saturated failure) | n/a | saturated failure: no single input restriction can lift the pass rate; revisit bounds and threshold |
| `uptime_margin_fraction` | `achieved_fleet_uptime_fraction` | +100.0 | `achieved_fleet_uptime_fraction` above p67 |
| `pretreatment_reliability_margin_fraction` | `achieved_pretreatment_reliability_fraction` | +100.0 | `achieved_pretreatment_reliability_fraction` above p50 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

Note: the saturated Critical gate `fleet_lifetime_opex_budget_margin_usd` is absent from the ranking because no single missing-input restriction can lift its pass rate under current bounds. The inputs below target the next most decision-relevant non-saturated gates; the saturated gate needs a bounds or threshold-definition audit, not a single input fix.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `achieved_pretreatment_reliability_fraction` | `pretreatment_reliability_margin_fraction` | 17.54 | 0.29 | model_assumption |
| 2 | `achieved_fleet_uptime_fraction` | `uptime_margin_fraction` | 16.62 | 0.24 | model_assumption |

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
| `fleet_lifetime_opex_budget_margin_usd` | **HIGH** | 100% | 0.40 |
| `uptime_margin_fraction` | **LOW** | 0% | 0.24 |
| `review_load_buffer_margin_fraction` | **MEDIUM** | 100% | 0.80 |
| `pretreatment_reliability_margin_fraction` | **LOW** | 0% | 0.29 |
| `phase1_budget_margin_usd` | **HIGH** | 100% | 0.47 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `fleet_lifetime_opex_budget_margin_usd` | USD | -350,000,000 | -500,000,000 | -650,000,000 |
| `uptime_margin_fraction` | fraction | -0.1500 | 0.0000 | 0.0700 |
| `review_load_buffer_margin_fraction` | fraction | 0.0945 | 0.0600 | 0.0025 |
| `pretreatment_reliability_margin_fraction` | fraction | -0.1500 | 0.0000 | 0.1000 |
| `phase1_budget_margin_usd` | USD | 25,000,000 | 16,000,000 | 2,500,000 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 1 declared gate in the Critical band; 2 in the Fragile band. Worst: `fleet_lifetime_opex_budget_margin_usd` at 0.0% pass rate under current bounds.
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
