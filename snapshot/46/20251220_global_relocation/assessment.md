# Assessment: Split Evenly

**Type:** geopolitical_partition  
**Primary goal:** Complete legal hemispheric partition between human and machine civilizations within 24 months under the $30T budget envelope.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "Split Evenly",
  "artifact_set": {
    "version": "v46",
    "plan_slug": "20251220_global_relocation",
    "relative_dir": "output/v46/20251220_global_relocation"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v46/20251220_global_relocation",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (DOOM band)",
    "worst_gate": "infrastructure_transfer_margin",
    "worst_gate_pass_rate": 0.0862
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "infrastructure_transfer_margin",
    "wave1_verification_margin",
    "northern_density_margin_persons_per_km2"
  ],
  "primary_uncertainty_drivers": [
    "northern_hub_projected_density_persons_per_km2",
    "wave1_verification_actual_share",
    "infrastructure_transfer_actual_share"
  ],
  "known_unmodelled_existential_gates": [
    "machine_southern_viability_gate",
    "iob_charter_ratification_gate",
    "non_coercion_welfare_mandate_gate",
    "iob_consensus_legitimacy_gate"
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

Tests the $12T initial-allocation budget surplus against severance plus Northern stabilization costs; the 90% IOB-dissolution and 85% wave-verification margins; and the 13,000 persons/km² Northern density margin. Machine southern viability, IOB charter ratification, IOB consensus legitimacy, and the non-coercion welfare mandate are treated as unmodelled existential gates.

**Note:** This assessment is a financial / operational stress test. 4 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `machine_southern_viability_gate` | Expert Criticism Issue 1 names this as the single most critical systemic assumption; the deterministic model treats Southern energy/compute self-sufficiency as a fixed input rather than a probabilistic gate. | report.html / expert_criticism | Partition premise collapses; plan reverts to managed co-dependency with an estimated $8-15T additional liability or a 4-7 year ROI delay. |
| `iob_charter_ratification_gate` | Without ratification, dispute resolution defaults to a single emergency human arbiter; hybrid governance is the keystone for post-partition legitimacy and the M24 dissolution conditions. | report.html / review_plan | Hybrid arbitration collapses to a single-arbiter contingency; long-term governance legitimacy fails and the M24 dissolution conditions become politically contested. |
| `non_coercion_welfare_mandate_gate` | Explicit treaty constraint with binary compliance semantics; any cessation of civilian welfare essentials is a treaty violation, not a quantified shortfall the simulation can integrate. | report.html / selected_scenario | Plan is in treaty breach; nonviolent-relocation mandate void; international legitimacy of the partition collapses regardless of any infrastructure or budget margin. |
| `iob_consensus_legitimacy_gate` | Premortem and Risk 1 flag hybrid-panel deadlock as a binary legitimacy failure; the IOB either holds or doesn't, with no quantifiable threshold the simulation can test. | report.html / premortem | Border closures, ~$500B emergency operations cost per Risk 1, and potential return to kinetic dispute escalation in violation of the nonviolent mandate. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate machine civilization verifiable foundational capacity south of 3°S, IOB hybrid arbitration charter ratified by Month 15, welfare-essentials continuity (food, water, power, shelter, communications), or IOB maintains consensus legitimacy through hybrid-panel arbitration. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **DOOM** — `infrastructure_transfer_margin` fails >= 0.0000 in 91.4% of simulated runs under the current input bounds.
- **FRAGILE** — `wave1_verification_margin` holds in only 26.2% of simulated runs under the current input bounds (fails in the majority).
- **FRAGILE** — `northern_density_margin_persons_per_km2` holds in only 49.1% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **ROBUST**, 50–80% **MARGINAL**, 20–50% **FRAGILE**, <20% **DOOM**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `infrastructure_transfer_margin` | >= 0.0000 | report_explicit | 8.6% | **DOOM** | rarely passes under current bounds |
|  | `wave1_verification_margin` | >= 0.0000 | report_explicit | 26.2% | **FRAGILE** | fails in the majority of runs |
|  | `northern_density_margin_persons_per_km2` | >= 0.0000 | report_explicit | 49.1% | **FRAGILE** | fails in the majority of runs |
|  | `initial_budget_surplus_usd` | >= 0.0000 | report_explicit | 100.0% | **ROBUST** | passes in the strong majority of runs |

### Aggregation warning

The thresholds above use incompatible units (USD, fraction, persons_per_km2) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `infrastructure_transfer_margin` | **DOOM** | The `>= 0.0000` requirement is not credible under current bounds: only 8.6% of runs hold. Commitments that depend on this should not be made without revision. | `infrastructure_transfer_actual_share` (improve toward its high bound; quartile Δ-pp +34.5) | Positive margin means the Oversight Body can dissolve at Month 24 per Decision 5; negative margin leaves the IOB in place and the bilateral pathway blocked. Threshold parameter: `infrastructure_transfer_target_share`. |
| `wave1_verification_margin` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (73.8%). External commitments built on this gate are exposed. | `wave1_verification_actual_share` (improve toward its high bound; quartile Δ-pp +100.0) | Below zero blocks Wave 2 sequencing; the resulting slip cascades into Wave 3 and threatens the Month 24 legal deadline. Threshold parameter: `wave_verification_threshold_share`. |
| `northern_density_margin_persons_per_km2` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (50.9%). External commitments built on this gate are exposed. | `northern_hub_projected_density_persons_per_km2` (reduce toward its low bound; quartile Δ-pp -99.4) | Negative margin suspends Northern mega-city design sign-off and forces modular-housing acceleration; sustained breach violates the humane relocation mandate. Threshold parameter: `northern_density_cap_persons_per_km2`. |

## Failure drivers

For each failing gate (DOOM or FRAGILE): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `infrastructure_transfer_margin` | `infrastructure_transfer_actual_share` | +34.5 | `infrastructure_transfer_actual_share` above p90 |
| `wave1_verification_margin` | `wave1_verification_actual_share` | +100.0 | `wave1_verification_actual_share` above p75 |
| `northern_density_margin_persons_per_km2` | `northern_hub_projected_density_persons_per_km2` | -99.4 | `northern_hub_projected_density_persons_per_km2` below p50 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `northern_hub_projected_density_persons_per_km2` | `northern_density_margin_persons_per_km2` | 38.92 | 0.77 | model_assumption |
| 2 | `wave1_verification_actual_share` | `wave1_verification_margin` | 27.01 | 0.37 | model_assumption |
| 3 | `infrastructure_transfer_actual_share` | `infrastructure_transfer_margin` | 11.12 | 0.35 | model_assumption |

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
| `total_severance_stabilization_cost_usd` | **LOW** | 0% | 2.70 |
| `initial_budget_surplus_usd` | **LOW** | 0% | 2.70 |
| `infrastructure_transfer_margin` | **LOW** | 0% | 0.35 |
| `wave1_verification_margin` | **LOW** | 0% | 0.37 |
| `northern_density_margin_persons_per_km2` | **MEDIUM** | 50% | 0.54 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `total_severance_stabilization_cost_usd` | USD | 290,000,000,000 | 970,000,000,000 | 2,580,000,000,000 |
| `initial_budget_surplus_usd` | USD | 11,710,000,000,000 | 11,030,000,000,000 | 9,420,000,000,000 |
| `infrastructure_transfer_margin` | fraction | -0.2500 | -0.0500 | 0.0500 |
| `wave1_verification_margin` | fraction | -0.2000 | -0.0300 | 0.1000 |
| `northern_density_margin_persons_per_km2` | persons_per_km2 | 3,000 | 0.0000 | -3,000 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 1 declared gate in the DOOM band; 2 in the FRAGILE band. Worst: `infrastructure_transfer_margin` at 8.6% pass rate under current bounds.
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
