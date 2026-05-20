"""
Generated PlanExe deterministic calculations.

Plan: 4-Day Work Week Pilot India
Plan type: public_policy_pilot

One function per formula_hint entry from recommended_first_calculations.
No derived_questions emitted.
"""

from __future__ import annotations


def formal_sector_budget_inr_crore(
    total_program_budget_inr_crore: float,
    formal_sector_budget_share: float,
) -> float:
    return total_program_budget_inr_crore * formal_sector_budget_share


def contingency_reserve_inr_crore(
    total_program_budget_inr_crore: float,
    contingency_budget_share: float,
) -> float:
    return total_program_budget_inr_crore * contingency_budget_share


def contingency_buffer_inr_crore(
    contingency_reserve_inr_crore: float,
    post_incentive_overrun_shock_inr_crore: float,
    sme_redesign_shock_inr_crore: float,
    legal_friction_shock_inr_crore: float,
) -> float:
    return contingency_reserve_inr_crore - post_incentive_overrun_shock_inr_crore - sme_redesign_shock_inr_crore - legal_friction_shock_inr_crore


def sme_admin_margin(
    sme_admin_hours_per_week_target: float,
    sme_admin_hours_per_week_actual: float,
) -> float:
    return sme_admin_hours_per_week_target - sme_admin_hours_per_week_actual


def sme_cohort_representation_margin(
    actual_sme_cohort_share: float,
    sme_cohort_share_target: float,
) -> float:
    return actual_sme_cohort_share - sme_cohort_share_target
