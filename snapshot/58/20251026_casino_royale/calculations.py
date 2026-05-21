"""
Generated PlanExe deterministic calculations.

Plan: White House East Wing Casino - Pioneer's Gauntlet
Plan type: commercial

One function per formula_hint entry from recommended_first_calculations and
derived_questions. Inputs are passed explicitly so callers (run_scenarios,
monte_carlo) can supply concrete values from key_values and bounds.
"""

from __future__ import annotations


def contingency_reserve_usd(initial_sponsor_budget_usd: float, contingency_fund_share: float) -> float:
    return initial_sponsor_budget_usd * contingency_fund_share


def sponsor_capital_at_risk_usd(initial_sponsor_budget_usd: float, sponsor_release_share: float) -> float:
    return initial_sponsor_budget_usd * sponsor_release_share


def phase1_noi_gate_surplus(achievable_daily_noi_usd: float, profitability_window_days: float, relocation_blackout_days: float, required_daily_noi_usd: float) -> float:
    return achievable_daily_noi_usd * (profitability_window_days - relocation_blackout_days) - required_daily_noi_usd * profitability_window_days


def political_reversal_buffer_surplus(contingency_reserve_usd: float, political_reversal_shock_usd: float) -> float:
    return contingency_reserve_usd - political_reversal_shock_usd


def levy_coverage_surplus_usd(ancillary_gross_revenue_annual_usd: float, ancillary_margin_fraction: float, monthly_levy_target_usd: float) -> float:
    return ancillary_gross_revenue_annual_usd * ancillary_margin_fraction - monthly_levy_target_usd * 12


def phase1_noi_gate_margin(achievable_daily_noi_usd: float, profitability_window_days: float, relocation_blackout_days: float, required_daily_noi_usd: float) -> float:
    return achievable_daily_noi_usd * (profitability_window_days - relocation_blackout_days) - required_daily_noi_usd * profitability_window_days


def q_levy_coverage(ancillary_gross_revenue_annual_usd: float, ancillary_margin_fraction: float, monthly_levy_target_usd: float) -> float:
    return ancillary_gross_revenue_annual_usd * ancillary_margin_fraction - monthly_levy_target_usd * 12
