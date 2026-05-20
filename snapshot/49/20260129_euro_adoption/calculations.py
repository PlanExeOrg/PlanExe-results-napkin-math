"""
Generated PlanExe deterministic calculations.

Plan: Denmark DKK to EUR Adoption (Builder's Blueprint)
Plan type: public_finance_transition

One function per formula_hint entry in recommended_first_calculations.
"""

from __future__ import annotations


def public_info_budget_dkk(total_transition_budget_dkk: float, public_info_funding_share: float) -> float:
    return total_transition_budget_dkk * public_info_funding_share


def referendum_support_margin(actual_referendum_support: float, referendum_support_threshold: float) -> float:
    return actual_referendum_support - referendum_support_threshold


def public_awareness_margin(actual_public_awareness: float, public_awareness_threshold: float) -> float:
    return actual_public_awareness - public_awareness_threshold


def contingency_buffer_dkk(contingency_reserve_dkk: float, cash_logistics_shock_cost_dkk: float) -> float:
    return contingency_reserve_dkk - cash_logistics_shock_cost_dkk


def real_indexation_margin(annual_real_indexation_factor: float, baseline_annual_inflation_rate: float) -> float:
    return annual_real_indexation_factor - (1 + baseline_annual_inflation_rate)
