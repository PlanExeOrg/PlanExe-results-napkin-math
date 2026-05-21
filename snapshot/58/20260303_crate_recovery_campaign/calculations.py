"""
Generated PlanExe deterministic calculations.

Plan: Crate Escape: Arla Milk Crate Recovery Campaign 2026
Plan type: commercial_csr_reverse_logistics

One function per formula_hint entry from recommended_first_calculations and
derived_questions. Inputs are passed explicitly so callers (run_scenarios,
monte_carlo) can supply concrete values from key_values and bounds.
"""

from __future__ import annotations


def donation_outlay_dkk(expected_recovered_crates: float, donation_per_crate_dkk: float) -> float:
    return expected_recovered_crates * donation_per_crate_dkk


def donation_cap_buffer_dkk(max_donation_outlay_dkk: float, donation_outlay_dkk: float) -> float:
    return max_donation_outlay_dkk - donation_outlay_dkk


def logistics_cost_total_dkk(expected_recovered_crates: float, logistics_cost_per_crate_dkk: float) -> float:
    return expected_recovered_crates * logistics_cost_per_crate_dkk


def logistics_budget_surplus_dkk(logistics_budget_dkk: float, logistics_cost_total_dkk: float) -> float:
    return logistics_budget_dkk - logistics_cost_total_dkk


def total_budget_surplus_dkk(
    total_program_budget_dkk: float,
    donation_outlay_dkk: float,
    logistics_cost_total_dkk: float,
    marketing_cost_realized_dkk: float,
) -> float:
    return total_program_budget_dkk - donation_outlay_dkk - logistics_cost_total_dkk - marketing_cost_realized_dkk


def volume_target_surplus(expected_recovered_crates: float, target_recovery_crates: float) -> float:
    return expected_recovered_crates - target_recovery_crates


def foundation_donation_margin_dkk(donation_outlay_dkk: float, min_foundation_donation_dkk: float) -> float:
    return donation_outlay_dkk - min_foundation_donation_dkk


def recovery_rate_margin(expected_recovered_crates: float, annual_loss_volume_crates: float) -> float:
    if annual_loss_volume_crates <= 0:
        return float("inf")
    return (expected_recovered_crates / annual_loss_volume_crates) - 0.4
