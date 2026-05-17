"""
Generated PlanExe deterministic calculations.

Plan: White House East Wing Casino (Pioneer's Gauntlet)
Plan type: commercial_construction_phased

One function per formula_hint entry from recommended_first_calculations and
derived_questions. Inputs are passed explicitly so callers (run_scenarios,
monte_carlo) can supply concrete values from key_values and bounds.
"""

from __future__ import annotations


def expected_daily_revenue_usd(casino_capacity_guests: float, expected_utilization_rate: float, daily_revenue_per_guest_usd: float) -> float:
    return casino_capacity_guests * expected_utilization_rate * daily_revenue_per_guest_usd


def expected_daily_noi_usd(expected_daily_revenue_usd: float, daily_operating_cost_usd: float) -> float:
    return expected_daily_revenue_usd - daily_operating_cost_usd


def sponsor_profitability_trigger_margin_usd(expected_daily_noi_usd: float, required_daily_noi_usd: float) -> float:
    return expected_daily_noi_usd - required_daily_noi_usd


def sponsor_capital_release_usd(total_sponsor_budget_usd: float, sponsor_capital_release_fraction: float) -> float:
    return total_sponsor_budget_usd * sponsor_capital_release_fraction


def court_remediation_daily_burn_capacity_usd(political_reversal_contingency_usd: float, court_political_reversal_remediation_window_days: float) -> float:
    if court_political_reversal_remediation_window_days <= 0:
        return float("inf")
    return political_reversal_contingency_usd / court_political_reversal_remediation_window_days


def sponsor_profitability_window_margin_days(sponsor_profitability_window_days: float, relocation_blackout_days: float) -> float:
    return (sponsor_profitability_window_days - relocation_blackout_days) - sponsor_profitability_window_days


def aml_adjusted_daily_noi_margin_usd(expected_daily_revenue_usd: float, aml_bank_settlement_revenue_reduction_fraction: float, high_roller_capacity_share: float, daily_operating_cost_usd: float, required_daily_noi_usd: float) -> float:
    return (expected_daily_revenue_usd * (1 - aml_bank_settlement_revenue_reduction_fraction * high_roller_capacity_share)) - daily_operating_cost_usd - required_daily_noi_usd


def high_roller_daily_revenue_usd(expected_daily_revenue_usd: float, high_roller_capacity_share: float) -> float:
    return expected_daily_revenue_usd * high_roller_capacity_share
