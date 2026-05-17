# Assessment: Yellowstone Caldera VEI-6 Evacuation (Pioneer Strategy)

**Type:** catastrophic_disaster_response  
**Primary goal:** Execute the Pioneer: Maximum Throughput First strategy to clear 35,800 occupants from Zone Zero within 6 hours of trigger, sustain decentralized Command & Control through the T+6 to T+18 logistical-vacuum window, and stage 30% of N95/water requirements at Bozeman / Idaho Falls by T+16.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "Yellowstone Caldera VEI-6 Evacuation (Pioneer Strategy)",
  "artifact_set": {
    "version": "v46",
    "plan_slug": "20260201_yellowstone_evacuation",
    "relative_dir": "output/v46/20260201_yellowstone_evacuation"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v46/20260201_yellowstone_evacuation",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "doom",
    "reason": "at least one declared gate has pass rate < 20% (DOOM band)",
    "worst_gate": "zone_zero_compliance_margin",
    "worst_gate_pass_rate": 0.008
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [
    "zone_zero_compliance_margin",
    "c2_fuel_endurance_margin_hours",
    "n95_staging_margin",
    "public_compliance_margin"
  ],
  "primary_uncertainty_drivers": [
    "actual_n95_staging_share",
    "actual_c2_fuel_endurance_hours",
    "actual_drf_spend_usd"
  ],
  "known_unmodelled_existential_gates": [
    "governor_jurisdictional_authority_transfer_gate",
    "faa_dod_emergency_airlift_authorization_gate",
    "national_guard_t3_mobilization_gate"
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

Tests the Zone-Zero compliance margin against the 98% T+6 threshold; the Disaster Relief Fund surplus against bottom-up evacuation spend; the N95/water staging margin against the 30%-by-T+16 target; the C2 fuel-endurance margin against the 72-hour cache target; and the public-compliance margin against the 70% panic-floor threshold. Governor jurisdictional-authority transfer, FAA/DoD emergency airlift authorization, and National Guard T+3 mobilization are treated as unmodelled existential gates.

**Note:** This assessment is a financial / operational stress test. 3 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `governor_jurisdictional_authority_transfer_gate` | Risk 3 names this as the binary governance hinge: without signed dual-hat MOUs the federal-to-state authority transfer at egress checkpoints collapses into 4–12 hour operational paralysis and ashfall-hardening assets cannot deploy under State control. | report.html / premortem | Operational paralysis 4–12 hours; ashfall-hardening (Decision 3) delayed; 25–50% increase in regional grid-collapse likelihood; engineering assets cannot legally cross state boundaries to harden substations. |
| `faa_dod_emergency_airlift_authorization_gate` | The Hybrid Flow Model that bridges the T+6 to T+18 logistical vacuum depends on FAA/DoD waiving Ground Stop in sectors ZLC/ZSE under ash-ingestion risk; without authorization the 30% N95 staging cannot be achieved by any modelled lever. | report.html / expert_criticism | Zero airlift achievable; Zone-One life support fails per Risk 2; respiratory/dehydration casualties escalate as the entire ingress vacuum spans 12 hours unmitigated. |
| `national_guard_t3_mobilization_gate` | The 72-hour C2 fuel-cache build and the M88 breach-vehicle staging both depend on Ready-Reserve mobilization within 3 hours of trigger; the plan offers no alternative path if mobilization slips. | report.html / review_plan | C2 fuel-cache target (72 hours) missed; ashfall-hardening delayed; contraflow-breach assets unavailable for the 90-minute internal response time; Zone-Zero T+6 clearance becomes unreachable. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate MT/WY/ID Governors execute the dual-hat Jurisdictional Authority Transfer Protocol at T+0, FAA/DoD authorize the 10 heavy-lift sorties for T+8 to T+16 emergency ingress, or wyoming/Montana National Guard engineering platoons mobilize heavy equipment by T+3. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.
- **DOOM** — `zone_zero_compliance_margin` fails >= 0.0000 in 99.2% of simulated runs under the current input bounds.
- **DOOM** — `c2_fuel_endurance_margin_hours` fails >= 0.0000 in 83.2% of simulated runs under the current input bounds.
- **FRAGILE** — `n95_staging_margin` holds in only 20.5% of simulated runs under the current input bounds (fails in the majority).
- **FRAGILE** — `public_compliance_margin` holds in only 49.3% of simulated runs under the current input bounds (fails in the majority).

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **ROBUST**, 50–80% **MARGINAL**, 20–50% **FRAGILE**, <20% **DOOM**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `zone_zero_compliance_margin` | >= 0.0000 | report_explicit | 0.8% | **DOOM** | rarely passes under current bounds |
|  | `c2_fuel_endurance_margin_hours` | >= 0.0000 | report_explicit | 16.8% | **DOOM** | rarely passes under current bounds |
|  | `n95_staging_margin` | >= 0.0000 | report_explicit | 20.5% | **FRAGILE** | fails in the majority of runs |
|  | `public_compliance_margin` | >= 0.0000 | report_explicit | 49.3% | **FRAGILE** | fails in the majority of runs |
|  | `drf_surplus_usd` | >= 0.0000 | report_explicit | 67.5% | **MARGINAL** | passes more often than not but uncomfortably close |

### Aggregation warning

The thresholds above use incompatible units (USD, fraction, hours) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

## Decision implications

Bridge from gate result to planning consequence. **Structural lever** names the input whose quartile movement has the largest effect on this gate (from `quartile_analysis` in `montecarlo.json`). **Gate meaning** surfaces the gate's own rationale lifted verbatim from `parameters.recommended_first_calculations[].why_first` (or `derived_questions[].why_it_matters`) plus the threshold parameter the formula tests against. This section identifies the affected planning lever; concrete revisions should be derived by reading the source report and the relevant intermediary artifacts.

| Gate | Verdict | Planning consequence | Structural lever | Gate meaning |
|---|---|---|---|---|
| `zone_zero_compliance_margin` | **DOOM** | The `>= 0.0000` requirement is not credible under current bounds: only 0.8% of runs hold. Commitments that depend on this should not be made without revision. | `actual_zone_zero_compliance_share` (improve toward its high bound; quartile Δ-pp +3.2) | Positive margin validates the Pioneer Maximum-Throughput-First thesis at the T+6 measurement point; negative margin triggers the VEI-7 contingency and resource reallocation cascade. Threshold parameter: `zone_zero_compliance_target`. |
| `c2_fuel_endurance_margin_hours` | **DOOM** | The `>= 0.0000` requirement is not credible under current bounds: only 16.8% of runs hold. Commitments that depend on this should not be made without revision. | `actual_c2_fuel_endurance_hours` (improve toward its high bound; quartile Δ-pp +67.3) | Positive margin keeps the decentralized UC operational through the post-grid-failure window; negative margin produces the Issue-2 decision-latency spike and 15–30% increase in premature VEI-7 activation probability. Threshold parameter: `fuel_reserve_target_hours`. |
| `n95_staging_margin` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (79.5%). External commitments built on this gate are exposed. | `actual_n95_staging_share` (improve toward its high bound; quartile Δ-pp +68.2) | Positive margin closes the T+6 to T+18 logistical vacuum; negative margin triggers the Issue-1 secondary-casualty path (10–20% increase in respiratory/dehydration cases). Threshold parameter: `n95_staging_target_share`. |
| `public_compliance_margin` | **FRAGILE** | The `>= 0.0000` requirement fails in the majority of runs (50.7%). External commitments built on this gate are exposed. | `actual_public_compliance_share` (improve toward its high bound; quartile Δ-pp +99.5) | Positive margin keeps evacuation routes orderly; negative margin triggers Risk-6 panic bottlenecks at I-90/Bozeman with 8–10 hours of staging delay and Phase-2 cascade risk. Threshold parameter: `public_compliance_threshold`. |
| `drf_surplus_usd` | **MARGINAL** | The `>= 0.0000` requirement passes 67.5% of runs — close to coin-flip. Downstream commitments should not assume it holds. | `actual_drf_spend_usd` (reduce toward its low bound; quartile Δ-pp -100.0) | Positive surplus preserves the $500M envelope for Phase-2 expansion and post-eruption stabilization; negative surplus forces a congressional supplemental request mid-event. Threshold parameter: `drf_usd`. |

## Failure drivers

For each failing gate (DOOM or FRAGILE): the single input with the largest pass-rate swing between its bottom and top quartile, and the conditional input restriction that would lift the gate to an 80% pass rate (when one exists). Full per-driver tables and binding-gate frequencies are in `montecarlo.json`.

| Failing gate | Top driver | Δ-pp (bottom→top quartile) | 80% pass requires |
|---|---|---:|---|
| `zone_zero_compliance_margin` | `actual_zone_zero_compliance_share` | +3.2 | no single input restriction sufficient |
| `c2_fuel_endurance_margin_hours` | `actual_c2_fuel_endurance_hours` | +67.3 | `actual_c2_fuel_endurance_hours` above p85 |
| `n95_staging_margin` | `actual_n95_staging_share` | +68.2 | `actual_n95_staging_share` above p85 |
| `public_compliance_margin` | `actual_public_compliance_share` | +99.5 | `actual_public_compliance_share` above p50 |

## Missing inputs ranked by impact

The plan does not state these values; the model assumed bounds. Rank by `|Δ-pp on the worst-affected gate| × (1 − that gate's pass rate) × bound-width-ratio` — the higher, the more decision-value in pinning this input down.

| Rank | Input | Worst-affected gate | Score | Bound width / base | Basis |
|---:|---|---|---:|---:|---|
| 1 | `actual_n95_staging_share` | `n95_staging_margin` | 108.45 | 2.00 | report_derived |
| 2 | `actual_c2_fuel_endurance_hours` | `c2_fuel_endurance_margin_hours` | 61.59 | 1.10 | report_derived |
| 3 | `actual_drf_spend_usd` | `drf_surplus_usd` | 36.08 | 1.11 | model_assumption |
| 4 | `actual_public_compliance_share` | `public_compliance_margin` | 29.44 | 0.58 | model_assumption |
| 5 | `actual_zone_zero_compliance_share` | `zone_zero_compliance_margin` | 0.82 | 0.26 | model_assumption |

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
| `zone_zero_compliance_margin` | **LOW** | 0% | 0.26 |
| `drf_surplus_usd` | **LOW** | 0% | 1.11 |
| `n95_staging_margin` | **MEDIUM** | 100% | 1.42 |
| `c2_fuel_endurance_margin_hours` | **MEDIUM** | 100% | 1.10 |
| `public_compliance_margin` | **MEDIUM** | 50% | 0.40 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `zone_zero_compliance_margin` | fraction | -0.2300 | -0.0500 | 0.0100 |
| `drf_surplus_usd` | USD | 300,000,000 | 50,000,000 | -200,000,000 |
| `n95_staging_margin` | fraction | -0.1500 | -0.1000 | 0.0000 |
| `c2_fuel_endurance_margin_hours` | hours | -48.00 | -12.00 | 18.00 |
| `public_compliance_margin` | fraction | -0.1500 | 0.0200 | 0.1200 |

## Suggested next actions

Imperatives for whatever consumes this file next.

1. To answer whether the plan is viable, lead with the gate verdicts above — not the source plan's narrative. 2 declared gates in the DOOM band; 2 in the FRAGILE band. Worst: `zone_zero_compliance_margin` at 0.8% pass rate under current bounds.
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
