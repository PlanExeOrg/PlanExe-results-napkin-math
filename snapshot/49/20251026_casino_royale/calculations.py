"""
Generated PlanExe deterministic calculations.

Plan: White House East Wing Container Casino (Pioneer's Gauntlet)
Plan type: high_risk_political_commercial_venture

One function per formula_hint entry from recommended_first_calculations.
No derived_questions emitted.
"""

from __future__ import annotations


def continuous_profitable_days_margin(
    actual_continuous_profitable_days: float,
    profitable_days_target: float,
) -> float:
    return actual_continuous_profitable_days - profitable_days_target


def daily_noi_margin_usd(
    actual_daily_noi_usd: float,
    daily_noi_target_usd: float,
) -> float:
    return actual_daily_noi_usd - daily_noi_target_usd


def budget_surplus_usd(
    budget_ceiling_usd: float,
    actual_total_spend_usd: float,
) -> float:
    return budget_ceiling_usd - actual_total_spend_usd


def contingency_fund_margin_usd(
    actual_segregated_contingency_usd: float,
    contingency_fund_target_usd: float,
) -> float:
    return actual_segregated_contingency_usd - contingency_fund_target_usd


def blackout_duration_margin_days(
    blackout_target_days: float,
    actual_blackout_days: float,
) -> float:
    return blackout_target_days - actual_blackout_days
