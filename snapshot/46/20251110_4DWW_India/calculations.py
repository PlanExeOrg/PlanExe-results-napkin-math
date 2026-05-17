"""
Generated PlanExe deterministic calculations.

Plan: 4-Day Work Week (4DWW) India Pilot
Plan type: public_policy_pilot

One function per formula_hint entry from recommended_first_calculations.
No derived_questions emitted.
"""

from __future__ import annotations


def total_program_operating_cost_inr(
    monthly_program_operating_cost_inr: float,
    pilot_duration_months: float,
) -> float:
    return monthly_program_operating_cost_inr * pilot_duration_months


def formal_operations_budget_surplus_inr(
    total_budget_inr: float,
    formal_track_budget_share: float,
    incentive_budget_share_of_formal: float,
    total_program_operating_cost_inr: float,
) -> float:
    return total_budget_inr * formal_track_budget_share * (1 - incentive_budget_share_of_formal) - total_program_operating_cost_inr


def sme_admin_overhead_margin_hours_per_week(
    sme_admin_overhead_cap_hours_per_week: float,
    sme_admin_overhead_actual_hours_per_week: float,
) -> float:
    return sme_admin_overhead_cap_hours_per_week - sme_admin_overhead_actual_hours_per_week


def voluntary_participation_margin(
    voluntary_participation_actual_share: float,
    voluntary_participation_target_share: float,
) -> float:
    return voluntary_participation_actual_share - voluntary_participation_target_share


def sustained_productivity_retention_margin(
    sustained_productivity_retention_actual_share: float,
    sustained_productivity_retention_target_share: float,
) -> float:
    return sustained_productivity_retention_actual_share - sustained_productivity_retention_target_share
