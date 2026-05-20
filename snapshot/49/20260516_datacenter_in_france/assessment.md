# Assessment: Hauts-de-France 9 GW Sovereign AI Data Center - Pragmatic Scale-Up

**Type:** Hyperscale infrastructure / industrial CAPEX programme  
**Primary goal:** Build Phase 1 (500 MW-1 GW) in 36 months at PUE <=1.20 and secure binding RTE + 60% tenant commitment before Phase 2 FID.

## Artifact contract

This assessment is a derived interpretation layer over the simulation artifacts listed in the provenance map below. It summarises what the model tested, which gates fail or pass, which inputs drive the result, which assumptions remain unvalidated, and what to inspect next. It is **not** a copy of the raw simulation data: for exact distributions, bounds rationales, formulas, and run settings, open the referenced artifacts directly.

## Machine summary

Compact manifest for programmatic consumers. The fields below are the structured form of the prose verdicts that follow. `artifact_set.relative_dir` is the portable identifier; `source_plan_dir` is the absolute path on the generating machine.

```json
{
  "assessment_schema_version": 6,
  "artifact_type": "interpretation_layer",
  "plan_name": "Hauts-de-France 9 GW Sovereign AI Data Center - Pragmatic Scale-Up",
  "artifact_set": {
    "version": "v49",
    "plan_slug": "20260516_datacenter_in_france",
    "relative_dir": "output/v49/20260516_datacenter_in_france"
  },
  "source_plan_dir": "/Users/neoneye/git/PlanExeGroup/PlanExe/experiments/napkin_math/output/v49/20260516_datacenter_in_france",
  "primary_model_result": {
    "basis": "worst declared gate's pass-rate band; not a calibrated whole-plan probability",
    "overall_risk_band": "viable",
    "reason": "every declared gate has pass rate \u2265 80% (Robust band)",
    "worst_gate": "buildable_area_km2",
    "worst_gate_pass_rate": 1.0
  },
  "validation_status": "valid",
  "simulation": {
    "n_runs": 10000,
    "seed": 12345,
    "distribution_default": "triangular"
  },
  "primary_failed_gates": [],
  "primary_uncertainty_drivers": [],
  "known_unmodelled_existential_gates": [
    "rte_binding_transmission_gate",
    "dgsi_anssi_sovereign_signoff_gate",
    "land_assembly_legal_consolidation_gate",
    "social_license_phase0_gate"
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

Tests Phase 1 CAPEX budget surplus, tenant take-or-pay margin vs the 60% gate, buildable-area capacity coverage, and land-holding cost buffer against the €1.3B overrun risk.

**Note:** This assessment is a financial / operational stress test. 4 unmodelled existential gates (legal, political, compliance, or external-actor commitments) are listed below but not evaluated by the simulation. Treat the gate-verdict pass rates as conditional on those gates holding.

## Known unmodelled existential gates

Gates whose failure would end the plan independently of any financial or operational threshold the model tests. Sourced from the extractor's flag in `parameters.unmodelled_gates`. The simulation does not evaluate these; the source report is the authoritative reference for each.

| Gate | Why it matters | Source anchor | Consequence if false |
|---|---|---|---|
| `rte_binding_transmission_gate` | Phase 1 construction financing cannot close unless RTE issues a binding transmission allocation for the Phase 2 3 GW expansion. | report.html / review_plan | Phase 1 FID is blocked and EUR 1B-2B Phase 0/1 capital risks being stranded if tenants withdraw. |
| `dgsi_anssi_sovereign_signoff_gate` | Access to premium domestic sovereign revenue depends on a formal signed DGSI/ANSSI agreement before scaling load. | report.html / premortem | Loss of EUR 10B-20B in long-term premium contracted revenue and jeopardised 60% Phase 2 tenant commitment. |
| `land_assembly_legal_consolidation_gate` | Judicial challenge to the hyper-dense 80% buffer model could halt construction and shrink buildable area below 15 km². | report.html / premortem | Phase 1 FID slips 12-24 months and the 9 GW long-term capacity ceiling is permanently reduced. |
| `social_license_phase0_gate` | Project cannot proceed past Phase 0 without a credible social license covering workforce uplift and buffer land use. | report.html / selected_scenario | Permitting stalls and the Prefecture may force a mandated footprint reduction independent of financial thresholds. |

## Simulation settings

- n_runs: 10,000
- seed: 12345
- distribution_default: triangular
- validation: valid (0 errors, 0 warnings)

## Critical findings

- **SCOPE WARNING** — The simulation does not evaluate binding RTE transmission allocation, DGSI/ANSSI sovereign partition sign-off, 161 km² land assembly legal decree, or credible social license before Phase 1. These are existential gates and may dominate the modelled financial result. See `## Known unmodelled existential gates` for details.

## Gate verdicts

Pass rate for every declared threshold over 10,000 simulated runs. Bands: ≥80% **Robust**, 50–80% **Marginal**, 20–50% **Fragile**, <20% **Critical**. The `Threshold basis` column reports whether the threshold value came from the source report explicitly (`report_explicit`), was inferred from the report (`report_inferred`), or has no narrative anchor (`model_defined` / `unknown`). Rows with a leading `min` marker are aggregate gates computed via `min()` over independent pools — their verdict is meaningful, their raw magnitude is not.

| | Output | Condition | Threshold basis | Pass rate | Verdict | Meaning |
|---|---|---|---|---:|---|---|
|  | `buildable_area_km2` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |
|  | `phase1_buffer_holding_cost_eur` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |
|  | `phase1_expected_revenue_eur_year` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |
|  | `phase1_capacity_surplus_km2` | >= 0.0000 | model_defined | 100.0% | **Robust** | passes in the strong majority of runs |
|  | `phase1_capex_combined_surplus_eur` | >= 0.0000 | report_explicit | 100.0% | **Robust** | passes in the strong majority of runs |

### Aggregation warning

The thresholds above use incompatible units (EUR, EUR_per_year, km2) and the source plan does not declare a combined-gate aggregate. **Do not average or otherwise combine these pass rates into a single scalar.** Use the categorical verdicts per gate, or read the per-output distributions in `montecarlo.json`.

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
| `phase1_buffer_holding_cost_eur` | **HIGH** | 100% | 0.40 |
| `phase1_expected_revenue_eur_year` | **MEDIUM** | 100% | 0.75 |
| `phase1_capacity_surplus_km2` | **LOW** | 100% | 1.67 |
| `phase1_capex_combined_surplus_eur` | **MEDIUM** | 75% | 0.89 |
| `phase1_capex_buffer_eur` | **MEDIUM** | 67% | 0.52 |
| `phase2_tenant_commitment_margin` | **LOW** | 0% | 0.67 |

Per-output reasons are in `montecarlo.json` under `model_confidence`. `Declared-source inputs` is the share of input bounds anchored in the source report's narrative (`bounds.source == data`); the remainder are modelling assumptions. **Neither is empirically observed real-world data.**

## Scenario sanity check

Three deterministic scenarios: every uncertain input at the **low** end of its range, every input at its **base** value, every input at the **high** end. The column labels refer to **inputs**, not to whether the outcome is good or bad. Column names match the `low`/`base`/`high` keys in `scenarios.json`. A negative `base inputs` column on a gate the plan needs to pass means the plan is already in trouble at its own central assumptions.

| Output | Unit | Low inputs | Base inputs | High inputs |
|---|---|---:|---:|---:|
| `buildable_area_km2` | km2 | 32.20 | 32.20 | 32.20 |
| `phase1_buffer_holding_cost_eur` | EUR | 966,000,000 | 1,207,500,000 | 1,449,000,000 |
| `phase1_expected_revenue_eur_year` | EUR_per_year | 750,000,000 | 2,500,000,000 | 4,000,000,000 |
| `phase1_capacity_surplus_km2` | km2 | 30.59 | 27.37 | 22.54 |
| `phase1_capex_combined_surplus_eur` | EUR | 6,634,000,000 | 6,742,500,000 | 6,551,000,000 |

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
