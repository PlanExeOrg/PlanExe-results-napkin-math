"""
Generated PlanExe deterministic calculations.

Plan: Paperclip Automation Pilot Line (Builder Pragmatic Integration)
Plan type: industrial_automation_pilot

One function per formula_hint entry from recommended_first_calculations.
No derived_questions emitted.
"""

from __future__ import annotations


def manual_intervention_margin_hours(
    manual_intervention_threshold_hours_per_week: float,
    actual_manual_intervention_hours_per_week: float,
) -> float:
    return manual_intervention_threshold_hours_per_week - actual_manual_intervention_hours_per_week


def budget_surplus_usd(
    budget_max_usd: float,
    actual_total_project_cost_usd: float,
) -> float:
    return budget_max_usd - actual_total_project_cost_usd


def opc_ua_bid_margin_usd(
    opc_ua_bid_threshold_usd: float,
    actual_opc_ua_bid_usd: float,
) -> float:
    return opc_ua_bid_threshold_usd - actual_opc_ua_bid_usd


def api_latency_margin_ms(
    api_latency_p99_threshold_ms: float,
    actual_api_p99_latency_ms: float,
) -> float:
    return api_latency_p99_threshold_ms - actual_api_p99_latency_ms


def onsite_expert_budget_margin_usd(
    onsite_expert_max_cost_usd: float,
    actual_onsite_expert_cost_usd: float,
) -> float:
    return onsite_expert_max_cost_usd - actual_onsite_expert_cost_usd
