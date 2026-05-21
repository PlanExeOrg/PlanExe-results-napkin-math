"""
Generated PlanExe deterministic calculations.

Plan: Automated Paperclip Manufacturing and Fulfillment Pilot
Plan type: industrial_automation_pilot

One function per formula_hint entry from recommended_first_calculations and
derived_questions. Inputs are passed explicitly so callers (run_scenarios,
monte_carlo) can supply concrete values from key_values and bounds.
"""

from __future__ import annotations


def subtotal_named_components_usd(
    wire_bender_midpoint_usd: float,
    packing_machine_midpoint_usd: float,
    opc_ua_middleware_cost_usd: float,
    actual_onsite_expert_cost_usd: float,
    permits_and_safety_cost_usd: float,
    rigging_and_install_cost_usd: float,
    internal_developer_cost_usd: float,
) -> float:
    return (
        wire_bender_midpoint_usd
        + packing_machine_midpoint_usd
        + opc_ua_middleware_cost_usd
        + actual_onsite_expert_cost_usd
        + permits_and_safety_cost_usd
        + rigging_and_install_cost_usd
        + internal_developer_cost_usd
    )


def total_project_cost_estimate_usd(
    subtotal_named_components_usd: float,
    contingency_fraction: float,
) -> float:
    return subtotal_named_components_usd * (1 + contingency_fraction)


def budget_surplus_usd(
    total_budget_max_usd: float,
    total_project_cost_estimate_usd: float,
) -> float:
    return total_budget_max_usd - total_project_cost_estimate_usd


def manual_intervention_surplus_hours_per_week(
    max_manual_intervention_hours_per_week: float,
    actual_manual_intervention_hours_per_week: float,
) -> float:
    return max_manual_intervention_hours_per_week - actual_manual_intervention_hours_per_week


def expert_cap_margin_usd(
    onsite_expert_contract_cap_usd: float,
    actual_onsite_expert_cost_usd: float,
) -> float:
    return onsite_expert_contract_cap_usd - actual_onsite_expert_cost_usd


def expert_floor_margin_usd(
    actual_onsite_expert_cost_usd: float,
    onsite_expert_floor_usd: float,
) -> float:
    return actual_onsite_expert_cost_usd - onsite_expert_floor_usd
