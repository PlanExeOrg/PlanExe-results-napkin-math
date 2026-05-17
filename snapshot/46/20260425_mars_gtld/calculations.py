"""
Generated PlanExe deterministic calculations.

Plan: .mars gTLD ICANN Delegation (Builder's Pragmatic Infrastructure)
Plan type: internet_governance_program

One function per formula_hint entry from recommended_first_calculations.
No derived_questions emitted.
"""

from __future__ import annotations


def year1_registration_volume_margin_units(
    actual_year1_registrations_units: float,
    year1_breakeven_threshold_units: float,
) -> float:
    return actual_year1_registrations_units - year1_breakeven_threshold_units


def delegation_timing_margin_months(
    delegation_deadline_months: float,
    actual_delegation_months: float,
) -> float:
    return delegation_deadline_months - actual_delegation_months


def budget_surplus_usd(
    budget_high_usd: float,
    actual_year1_total_cost_usd: float,
) -> float:
    return budget_high_usd - actual_year1_total_cost_usd


def mars_mos_margin_kbps(
    actual_mars_endpoint_kbps: float,
    mars_mos_kbps: float,
) -> float:
    return actual_mars_endpoint_kbps - mars_mos_kbps


def hsm_capex_adequacy_margin_usd(
    actual_hsm_capex_usd: float,
    hsm_capex_min_usd: float,
) -> float:
    return actual_hsm_capex_usd - hsm_capex_min_usd
