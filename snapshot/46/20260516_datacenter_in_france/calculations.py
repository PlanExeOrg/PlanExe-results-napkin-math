"""
Generated PlanExe deterministic calculations.

Plan: Hauts-de-France 9 GW Sovereign AI Datacenter Campus
Plan type: hyperscale_infrastructure

One function per formula_hint entry from recommended_first_calculations.
No derived_questions emitted.
"""

from __future__ import annotations


def buffer_annual_holding_cost_eur(
    buffer_annual_holding_cost_per_ha_eur: float,
    buffer_area_km2: float,
) -> float:
    return buffer_annual_holding_cost_per_ha_eur * buffer_area_km2 * 100


def buffer_total_holding_cost_eur(
    buffer_annual_holding_cost_eur: float,
    buffer_holding_period_months: float,
) -> float:
    return buffer_annual_holding_cost_eur * buffer_holding_period_months / 12


def phase1_budget_surplus_eur(
    phase1_budget_max_eur: float,
    phase1_baseline_capex_eur: float,
    brownfield_remediation_actual_eur: float,
    buffer_total_holding_cost_eur: float,
) -> float:
    return phase1_budget_max_eur - phase1_baseline_capex_eur - brownfield_remediation_actual_eur - buffer_total_holding_cost_eur


def phase2_fid_margin(
    tenant_take_or_pay_actual_share: float,
    phase2_take_or_pay_threshold_share: float,
) -> float:
    return tenant_take_or_pay_actual_share - phase2_take_or_pay_threshold_share


def phase1_pue_margin(
    phase1_pue_target_max: float,
    phase1_pue_actual: float,
) -> float:
    return phase1_pue_target_max - phase1_pue_actual
