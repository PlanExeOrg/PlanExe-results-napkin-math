"""
Generated PlanExe deterministic calculations.

Plan: Denmark DKK to EUR Adoption (Builder's Blueprint)
Plan type: public_finance_national_transition

One function per formula_hint entry from recommended_first_calculations and
derived_questions. Inputs are passed explicitly so callers (run_scenarios,
monte_carlo) can supply concrete values from key_values and bounds.
"""

from __future__ import annotations


def real_budget_after_inflation_dkk(
    total_transition_budget_floor_dkk: float,
    baseline_inflation_rate: float,
    inflation_excess_over_baseline_pp: float,
    transition_duration_years: float,
) -> float:
    denom = (1 + baseline_inflation_rate + inflation_excess_over_baseline_pp) ** transition_duration_years
    if denom <= 0:
        return float("inf")
    return total_transition_budget_floor_dkk / denom


def budget_envelope_surplus_dkk(
    real_budget_after_inflation_dkk: float,
    estimated_transition_cost_dkk: float,
) -> float:
    return real_budget_after_inflation_dkk - estimated_transition_cost_dkk


def contingency_buffer_after_cash_shock_dkk(
    ring_fenced_contingency_dkk: float,
    cash_logistics_shock_cost_dkk: float,
) -> float:
    return ring_fenced_contingency_dkk - cash_logistics_shock_cost_dkk


def public_info_funding_surplus_dkk(
    total_transition_budget_floor_dkk: float,
    public_info_funding_share: float,
    estimated_public_info_required_cost_dkk: float,
) -> float:
    return (total_transition_budget_floor_dkk * public_info_funding_share) - estimated_public_info_required_cost_dkk


def combined_financial_viability_surplus_dkk(
    budget_envelope_surplus_dkk: float,
    contingency_buffer_after_cash_shock_dkk: float,
    public_info_funding_surplus_dkk: float,
) -> float:
    return min(budget_envelope_surplus_dkk, contingency_buffer_after_cash_shock_dkk, public_info_funding_surplus_dkk)


# skipped: q_inflation_indexation_adequacy -- formula_hint is null (qualitative diagnostic)
