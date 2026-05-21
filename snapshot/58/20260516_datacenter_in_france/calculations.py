"""
Generated PlanExe deterministic calculations.

Plan: Hauts-de-France 9 GW Sovereign AI Engine — Pragmatic Scale-Up
Plan type: Hyperscale data center megaproject (multi-phase, EUR-denominated)

One function per formula_hint entry from recommended_first_calculations and
derived_questions. Inputs are passed explicitly so callers (run_scenarios,
monte_carlo) can supply concrete values from key_values and bounds.
"""

from __future__ import annotations


def land_holding_cost_total_eur(land_buffer_area_hectares: float, land_holding_cost_eur_per_hectare_year: float, land_holding_duration_months: float) -> float:
    return land_buffer_area_hectares * land_holding_cost_eur_per_hectare_year * (land_holding_duration_months / 12)


def fx_unhedged_exposure_eur(phase1_capex_budget_eur: float, usd_hardware_capex_share: float, fx_hedge_coverage_fraction: float, fx_shock_magnitude_fraction: float) -> float:
    return phase1_capex_budget_eur * usd_hardware_capex_share * (1 - fx_hedge_coverage_fraction) * fx_shock_magnitude_fraction


def phase2_takeorpay_commitment_margin(actual_phase2_takeorpay_commitment_fraction: float, phase2_takeorpay_commitment_threshold: float) -> float:
    return actual_phase2_takeorpay_commitment_fraction - phase2_takeorpay_commitment_threshold


def phase1_pue_margin(actual_phase1_pue: float) -> float:
    return 1.20 - actual_phase1_pue


def phase1_contingency_surplus_eur(phase1_contingency_reserve_eur: float, land_holding_cost_total_eur: float, fx_unhedged_exposure_eur: float, remediation_cost_overrun_eur: float) -> float:
    return phase1_contingency_reserve_eur - land_holding_cost_total_eur - fx_unhedged_exposure_eur - remediation_cost_overrun_eur


# skipped: q_phase1_capex_budget_usd_million -- formula_hint is null
