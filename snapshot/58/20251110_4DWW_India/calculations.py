"""
Generated PlanExe deterministic calculations.

Plan: India 4-Day Work Week National Pilot
Plan type: public_policy_pilot

One function per formula_hint entry from recommended_first_calculations and
derived_questions. Inputs are passed explicitly so callers (run_scenarios,
monte_carlo) can supply concrete values from key_values and bounds.
"""

from __future__ import annotations


def formal_track_budget_inr_crore(total_program_budget_inr_crore: float, formal_track_allocation_fraction: float) -> float:
    return total_program_budget_inr_crore * formal_track_allocation_fraction


def contingency_reserve_inr_crore(total_program_budget_inr_crore: float, contingency_fund_fraction: float) -> float:
    return total_program_budget_inr_crore * contingency_fund_fraction


def contingency_shock_buffer_inr_crore(contingency_reserve_inr_crore: float, aggregate_risk_shock_cost_inr_crore: float) -> float:
    return contingency_reserve_inr_crore - aggregate_risk_shock_cost_inr_crore


def productivity_grants_pool_inr_crore(formal_track_budget_inr_crore: float, productivity_grants_share_of_incentive: float) -> float:
    return formal_track_budget_inr_crore * productivity_grants_share_of_incentive


def productivity_retention_margin(realised_productivity_retention_fraction: float, productivity_retention_threshold_fraction: float) -> float:
    return realised_productivity_retention_fraction - productivity_retention_threshold_fraction


def sme_share_margin(realised_sme_share: float, sme_share_target_fraction: float) -> float:
    return realised_sme_share - sme_share_target_fraction


def optin_margin(realised_optin_rate: float, voluntary_optin_threshold_fraction: float) -> float:
    return realised_optin_rate - voluntary_optin_threshold_fraction
