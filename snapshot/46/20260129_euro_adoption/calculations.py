"""
Generated PlanExe deterministic calculations.

Plan: Denmark DKK→EUR Adoption (Builder's Blueprint)
Plan type: national_monetary_transition

One function per formula_hint entry from recommended_first_calculations.
No derived_questions emitted.
"""

from __future__ import annotations


def budget_surplus_dkk(
    max_budget_dkk: float,
    actual_total_transition_cost_dkk: float,
) -> float:
    return max_budget_dkk - actual_total_transition_cost_dkk


def timeline_margin_years(
    timeline_max_years: float,
    actual_timeline_years: float,
) -> float:
    return timeline_max_years - actual_timeline_years


def referendum_support_margin(
    actual_referendum_support_share: float,
    referendum_support_threshold: float,
) -> float:
    return actual_referendum_support_share - referendum_support_threshold


def deficit_compliance_margin(
    deficit_criterion_share: float,
    actual_deficit_share: float,
) -> float:
    return deficit_criterion_share - actual_deficit_share


def public_awareness_margin(
    actual_public_awareness_share: float,
    public_awareness_threshold: float,
) -> float:
    return actual_public_awareness_share - public_awareness_threshold
