"""
Generated PlanExe deterministic calculations.

Plan: India Decennial Census 2026-27 (Pioneer's Gambit)
Plan type: mega_scale_national_logistics

One function per formula_hint entry from recommended_first_calculations.
No derived_questions emitted.
"""

from __future__ import annotations


def household_coverage_margin(
    actual_household_coverage_share: float,
    household_coverage_target: float,
) -> float:
    return actual_household_coverage_share - household_coverage_target


def budget_surplus_crore(
    budget_ceiling_crore: float,
    actual_total_cost_crore: float,
) -> float:
    return budget_ceiling_crore - actual_total_cost_crore


def provisional_release_timing_margin_months(
    provisional_release_deadline_months: float,
    actual_provisional_release_months: float,
) -> float:
    return provisional_release_deadline_months - actual_provisional_release_months


def ingestion_mttr_margin_hours(
    ingestion_mttr_target_hours: float,
    actual_ingestion_mttr_hours: float,
) -> float:
    return ingestion_mttr_target_hours - actual_ingestion_mttr_hours


def device_integrity_margin(
    device_audit_failure_threshold: float,
    actual_device_audit_failure_share: float,
) -> float:
    return device_audit_failure_threshold - actual_device_audit_failure_share
