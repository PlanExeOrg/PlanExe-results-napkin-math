"""
Generated PlanExe deterministic calculations.

Plan: Arla 'Crate Escape' Milk-Crate Recovery (Pioneer Aggressive Volume)
Plan type: consumer_csr_reverse_logistics

One function per formula_hint entry from recommended_first_calculations.
No derived_questions emitted.
"""

from __future__ import annotations


def crate_recovery_volume_margin_units(
    actual_crate_recovery_units: float,
    target_recovery_units: float,
) -> float:
    return actual_crate_recovery_units - target_recovery_units


def budget_surplus_dkk(
    total_budget_dkk: float,
    actual_program_spend_dkk: float,
) -> float:
    return total_budget_dkk - actual_program_spend_dkk


def donation_margin_dkk(
    actual_donation_dkk: float,
    min_donation_dkk: float,
) -> float:
    return actual_donation_dkk - min_donation_dkk


def social_impressions_margin(
    actual_social_impressions: float,
    target_impressions: float,
) -> float:
    return actual_social_impressions - target_impressions


def per_crate_handling_cost_margin_dkk(
    per_crate_handling_cost_threshold_dkk: float,
    actual_per_crate_handling_cost_dkk: float,
) -> float:
    return per_crate_handling_cost_threshold_dkk - actual_per_crate_handling_cost_dkk
