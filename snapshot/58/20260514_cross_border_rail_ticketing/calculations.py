"""
Generated PlanExe deterministic calculations.

Plan: EU Cross-Border Rail Through-Ticketing Coordination Program
Plan type: public_coordination_program

One function per formula_hint entry from recommended_first_calculations and
derived_questions. Inputs are passed explicitly so callers (run_scenarios,
monte_carlo) can supply concrete values from key_values and bounds.
"""

from __future__ import annotations


def governance_two_year_personnel_cost_eur(
    governance_fte_count: float,
    monthly_fte_cost_eur: float,
) -> float:
    return governance_fte_count * monthly_fte_cost_eur * 24


def coordination_budget_buffer_eur(
    public_coordination_budget_eur: float,
    capacity_building_grants_eur: float,
    public_reference_distributor_cost_eur: float,
    emergency_float_reserve_eur: float,
    governance_two_year_personnel_cost_eur: float,
    residual_program_overhead_eur: float,
) -> float:
    return (
        public_coordination_budget_eur
        - capacity_building_grants_eur
        - public_reference_distributor_cost_eur
        - emergency_float_reserve_eur
        - governance_two_year_personnel_cost_eur
        - residual_program_overhead_eur
    )


def clearing_liquidity_surplus_eur(
    initial_clearing_float_eur: float,
    emergency_float_reserve_eur: float,
    clearing_liquidity_shock_eur: float,
) -> float:
    return initial_clearing_float_eur + emergency_float_reserve_eur - clearing_liquidity_shock_eur


def clearing_coverage_ratio(
    initial_clearing_float_eur: float,
    emergency_float_reserve_eur: float,
    peak_daily_clearing_obligation_eur: float,
) -> float:
    if peak_daily_clearing_obligation_eur <= 0:
        return float("inf")
    return (initial_clearing_float_eur + emergency_float_reserve_eur) / (1.5 * peak_daily_clearing_obligation_eur)


def through_ticket_volume_target(
    eligible_cross_border_journeys_per_year: float,
    through_ticket_adoption_target_fraction: float,
) -> float:
    return eligible_cross_border_journeys_per_year * through_ticket_adoption_target_fraction


def adoption_margin_fraction(
    projected_through_ticket_adoption_fraction: float,
    through_ticket_adoption_target_fraction: float,
) -> float:
    return projected_through_ticket_adoption_fraction - through_ticket_adoption_target_fraction
