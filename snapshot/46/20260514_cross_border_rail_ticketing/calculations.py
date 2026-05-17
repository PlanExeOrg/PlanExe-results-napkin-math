"""
Generated PlanExe deterministic calculations.

Plan: EU Cross-Border Rail Through-Ticketing Program
Plan type: regulatory_coordination_program

One function per formula_hint entry from recommended_first_calculations.
No derived_questions emitted.
"""

from __future__ import annotations


def adoption_margin(
    actual_adoption_share: float,
    adoption_target_share: float,
) -> float:
    return actual_adoption_share - adoption_target_share


def coordination_budget_surplus_eur(
    coordination_budget_eur: float,
    actual_total_project_cost_eur: float,
) -> float:
    return coordination_budget_eur - actual_total_project_cost_eur


def clearing_float_coverage_eur(
    initial_clearing_float_eur: float,
    peak_daily_clearing_obligation_eur: float,
    safety_buffer_multiplier: float,
) -> float:
    return initial_clearing_float_eur - peak_daily_clearing_obligation_eur * safety_buffer_multiplier


def binding_standards_timing_margin_months(
    binding_standards_deadline_months: float,
    actual_binding_standards_months: float,
) -> float:
    return binding_standards_deadline_months - actual_binding_standards_months


def complaint_reduction_margin(
    actual_complaint_reduction_share: float,
    complaint_reduction_target_share: float,
) -> float:
    return actual_complaint_reduction_share - complaint_reduction_target_share
