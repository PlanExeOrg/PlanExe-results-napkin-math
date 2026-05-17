"""
Generated PlanExe deterministic calculations.

Plan: India Decennial Census 2026–2027
Plan type: national_governance_program

One function per formula_hint entry from recommended_first_calculations.
No derived_questions emitted.
"""

from __future__ import annotations


def budget_overrun_margin_inr(
    budget_high_inr: float,
    actual_total_census_spend_inr: float,
) -> float:
    return budget_high_inr - actual_total_census_spend_inr


def household_coverage_margin(
    actual_household_coverage_share: float,
    household_coverage_target_share: float,
) -> float:
    return actual_household_coverage_share - household_coverage_target_share


def provisional_publish_timing_margin_months(
    provisional_publish_target_months: float,
    actual_provisional_publish_months: float,
) -> float:
    return provisional_publish_target_months - actual_provisional_publish_months


def mttr_margin_hours(
    mttr_max_hours: float,
    actual_mttr_hours: float,
) -> float:
    return mttr_max_hours - actual_mttr_hours


def device_audit_failure_margin(
    device_audit_failure_threshold_share: float,
    actual_device_audit_failure_share: float,
) -> float:
    return device_audit_failure_threshold_share - actual_device_audit_failure_share
