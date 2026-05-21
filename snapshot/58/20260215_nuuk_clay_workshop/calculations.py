"""
Generated PlanExe deterministic calculations.

Plan: Nuuk Community Clay Workshop
Plan type: commercial community-arts venture

One function per formula_hint entry from recommended_first_calculations and
derived_questions. Inputs are passed explicitly so callers (run_scenarios,
monte_carlo) can supply concrete values from key_values and bounds.
"""

from __future__ import annotations


def contingency_reserve_dkk(year1_total_budget_dkk: float, contingency_reserve_share: float) -> float:
    return year1_total_budget_dkk * contingency_reserve_share


def annual_labor_cost_dkk(fte_equivalent_count: float, monthly_fte_cost_dkk: float, months_in_year1: float) -> float:
    return fte_equivalent_count * monthly_fte_cost_dkk * months_in_year1


def drop_in_revenue_shortfall_dkk(
    year1_revenue_target_dkk: float,
    drop_in_revenue_mix_share: float,
    minimum_viable_hourly_rate_dkk: float,
    off_peak_hours_per_year: float,
    drop_in_utilization_rate: float,
) -> float:
    return max(
        0,
        year1_revenue_target_dkk * drop_in_revenue_mix_share
        - minimum_viable_hourly_rate_dkk * off_peak_hours_per_year * drop_in_utilization_rate,
    )


def labor_law_shock_dkk(annual_labor_cost_dkk: float, labor_law_shock_cost_share: float) -> float:
    return annual_labor_cost_dkk * labor_law_shock_cost_share


def contingency_after_shocks_surplus_dkk(
    contingency_reserve_dkk: float,
    labor_law_shock_dkk: float,
    drop_in_revenue_shortfall_dkk: float,
) -> float:
    return contingency_reserve_dkk - labor_law_shock_dkk - drop_in_revenue_shortfall_dkk


def budget_after_labor_margin_dkk(year1_total_budget_dkk: float, annual_labor_cost_dkk: float) -> float:
    return year1_total_budget_dkk - annual_labor_cost_dkk
