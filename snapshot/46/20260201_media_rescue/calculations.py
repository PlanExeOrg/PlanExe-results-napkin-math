"""
Generated PlanExe deterministic calculations.

Plan: Containerized Dark Data Ingestor Network (CDDIN)
Plan type: industrial_preservation_program

One function per formula_hint entry from recommended_first_calculations.
No derived_questions emitted.
"""

from __future__ import annotations


def estimated_total_lifetime_opex_usd(
    avg_annual_opex_per_miu_usd: float,
    avg_active_fleet_size_units: float,
    pilot_duration_years: float,
) -> float:
    return avg_annual_opex_per_miu_usd * avg_active_fleet_size_units * pilot_duration_years


def budget_opex_surplus_usd(
    total_budget_usd: float,
    estimated_total_lifetime_opex_usd: float,
) -> float:
    return total_budget_usd - estimated_total_lifetime_opex_usd


def uptime_margin(
    actual_uptime_share: float,
    target_uptime_share: float,
) -> float:
    return actual_uptime_share - target_uptime_share


def review_load_margin(
    safety_buffer_review_share: float,
    actual_review_load_share: float,
) -> float:
    return safety_buffer_review_share - actual_review_load_share


def modular_mtbf_improvement_margin(
    modular_mtbf_actual_improvement_share: float,
    modular_mtbf_improvement_target_share: float,
) -> float:
    return modular_mtbf_actual_improvement_share - modular_mtbf_improvement_target_share
