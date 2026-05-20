"""
Generated PlanExe deterministic calculations.

Plan: Hauts-de-France 9 GW Sovereign AI Data Center - Pragmatic Scale-Up
Plan type: Hyperscale infrastructure / industrial CAPEX programme

One function per formula_hint entry in recommended_first_calculations and derived_questions.
"""

from __future__ import annotations


def buildable_area_km2(total_footprint_km2: float, buffer_share_fraction: float) -> float:
    return total_footprint_km2 * (1 - buffer_share_fraction)


def phase1_buffer_holding_cost_eur(total_footprint_km2: float, buffer_share_fraction: float, land_holding_cost_eur_per_ha_year: float, phase1_holding_duration_months: float) -> float:
    return total_footprint_km2 * buffer_share_fraction * 100 * land_holding_cost_eur_per_ha_year * (phase1_holding_duration_months / 12)


def phase1_expected_revenue_eur_year(phase1_power_target_mw: float, annual_revenue_per_mw_eur: float) -> float:
    return phase1_power_target_mw * annual_revenue_per_mw_eur


def phase1_capacity_surplus_km2(buildable_area_km2: float, buildable_area_utilization_fraction: float) -> float:
    return buildable_area_km2 - buildable_area_km2 * buildable_area_utilization_fraction


def phase1_capex_combined_surplus_eur(phase1_capex_budget_max_eur: float, phase1_buffer_holding_cost_eur: float, remediation_cost_overrun_eur: float, land_holding_cost_budget_envelope_eur: float) -> float:
    return phase1_capex_budget_max_eur - phase1_buffer_holding_cost_eur - remediation_cost_overrun_eur - land_holding_cost_budget_envelope_eur


def phase1_capex_buffer_eur(phase1_capex_budget_max_eur: float, land_holding_cost_budget_envelope_eur: float, phase1_buffer_holding_cost_eur: float) -> float:
    return phase1_capex_budget_max_eur - land_holding_cost_budget_envelope_eur - phase1_buffer_holding_cost_eur


def phase2_tenant_commitment_margin(expected_phase2_signed_commitment_fraction: float, phase2_takeorpay_gate_threshold: float) -> float:
    return expected_phase2_signed_commitment_fraction - phase2_takeorpay_gate_threshold
