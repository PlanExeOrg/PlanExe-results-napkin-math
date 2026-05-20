"""
Generated PlanExe deterministic calculations.

Plan: Nuuk Community Clay Workshop
Plan type: commercial community venture

One function per formula_hint entry in recommended_first_calculations.
"""

from __future__ import annotations


def contingency_reserve_dkk(year1_budget_dkk: float, contingency_fraction: float) -> float:
    return year1_budget_dkk * contingency_fraction


def drop_in_expected_revenue_dkk(minimum_viable_hourly_rate_dkk: float, drop_in_available_hours_per_year: float, drop_in_utilization_rate: float) -> float:
    return minimum_viable_hourly_rate_dkk * drop_in_available_hours_per_year * drop_in_utilization_rate


def drop_in_revenue_surplus_dkk(drop_in_expected_revenue_dkk: float, year1_revenue_target_dkk: float, drop_in_revenue_share: float) -> float:
    return drop_in_expected_revenue_dkk - (year1_revenue_target_dkk * drop_in_revenue_share)


def annual_labor_cost_dkk(monthly_fixed_labor_cost_dkk: float) -> float:
    return monthly_fixed_labor_cost_dkk * 12


def budget_after_labor_margin_dkk(year1_budget_dkk: float, annual_labor_cost_dkk: float, contingency_reserve_dkk: float) -> float:
    return year1_budget_dkk - annual_labor_cost_dkk - contingency_reserve_dkk
