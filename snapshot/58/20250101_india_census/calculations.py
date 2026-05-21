"""
Generated PlanExe deterministic calculations.

Plan: India Decennial Census 2026-2027 (Pioneer's Gambit)
Plan type: public_sector_logistics

One function per formula_hint entry from recommended_first_calculations and
derived_questions. Inputs are passed explicitly so callers (run_scenarios,
monte_carlo) can supply concrete values from key_values and bounds.
"""

from __future__ import annotations


def household_coverage_margin(actual_household_coverage: float, target_household_coverage: float) -> float:
    return actual_household_coverage - target_household_coverage


def budget_surplus_crore(budget_ceiling_crore: float, expected_total_cost_crore: float) -> float:
    return budget_ceiling_crore - expected_total_cost_crore


def provisional_release_timing_margin_months(provisional_release_deadline_months: float, actual_provisional_release_months: float) -> float:
    return provisional_release_deadline_months - actual_provisional_release_months


def ingestion_mttr_margin_hours(ingestion_mttr_target_hours: float, actual_ingestion_mttr_hours: float) -> float:
    return ingestion_mttr_target_hours - actual_ingestion_mttr_hours


def contingency_buffer_crore(contingency_fund_crore: float, expected_contingency_draw_crore: float) -> float:
    return contingency_fund_crore - expected_contingency_draw_crore
