"""
Generated PlanExe deterministic calculations.

Plan: Nuuk Community Clay Workshop
Plan type: small_business_community_hub

One function per formula_hint entry from recommended_first_calculations.
No derived_questions emitted.
"""

from __future__ import annotations


def total_year1_fixed_operating_cost_dkk(
    monthly_fixed_operating_cost_dkk: float,
    operating_months_year1: float,
) -> float:
    return monthly_fixed_operating_cost_dkk * operating_months_year1


def year1_budget_surplus_dkk(
    year1_budget_dkk: float,
    contingency_share: float,
    total_year1_fixed_operating_cost_dkk: float,
) -> float:
    return year1_budget_dkk * (1 - contingency_share) - total_year1_fixed_operating_cost_dkk


def monthly_off_peak_rental_revenue_dkk(
    min_viable_hourly_rate_dkk: float,
    off_peak_hours_per_month: float,
    low_season_utilization_actual_share: float,
) -> float:
    return min_viable_hourly_rate_dkk * off_peak_hours_per_month * low_season_utilization_actual_share


def monthly_off_peak_rental_overhead_margin_dkk(
    monthly_off_peak_rental_revenue_dkk: float,
    monthly_utility_overhead_dkk: float,
) -> float:
    return monthly_off_peak_rental_revenue_dkk - monthly_utility_overhead_dkk


def taster_conversion_margin(
    taster_conversion_actual_share: float,
    taster_conversion_target_share: float,
) -> float:
    return taster_conversion_actual_share - taster_conversion_target_share
