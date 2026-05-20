"""
Generated PlanExe deterministic calculations.

Plan: EU Cross-Border Rail Single Through-Ticketing Program
Plan type: Public-sector regulatory and infrastructure coordination program

One function per formula_hint entry from recommended_first_calculations and
derived_questions in parameters.json.
"""

from __future__ import annotations


def expected_annual_through_tickets(annual_cross_border_journeys: float, through_ticket_adoption_target_fraction: float) -> float:
    return annual_cross_border_journeys * through_ticket_adoption_target_fraction


def expected_annual_clearing_revenue_eur(expected_annual_through_tickets: float, clearing_fee_per_ticket_eur: float) -> float:
    return expected_annual_through_tickets * clearing_fee_per_ticket_eur


def emergency_float_buffer_eur(emergency_float_reserve_eur: float, liquidity_trigger_multiple: float, peak_daily_clearing_obligation_eur: float) -> float:
    return emergency_float_reserve_eur - liquidity_trigger_multiple * peak_daily_clearing_obligation_eur


def budget_allocation_surplus_eur(total_public_coordination_budget_eur: float, capacity_building_grants_eur: float, reference_distributor_budget_eur: float, emergency_float_reserve_eur: float, initial_clearing_float_eur: float) -> float:
    return total_public_coordination_budget_eur - capacity_building_grants_eur - reference_distributor_budget_eur - emergency_float_reserve_eur - initial_clearing_float_eur


def governance_personnel_cost_two_year_eur(governance_ftes: float, average_fte_monthly_cost_eur: float) -> float:
    return governance_ftes * average_fte_monthly_cost_eur * 24


def clearing_revenue_buffer_eur(expected_annual_clearing_revenue_eur: float, initial_clearing_float_eur: float) -> float:
    return expected_annual_clearing_revenue_eur - initial_clearing_float_eur
