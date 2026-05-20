"""
Generated PlanExe deterministic calculations.

Plan: Arla 'Crate Escape' Milk Crate Recovery Campaign 2026
Plan type: commercial_csr_reverse_logistics

One function per formula_hint entry in recommended_first_calculations.
"""

from __future__ import annotations


def projected_donation_spend_dkk(incentive_per_crate_dkk: float, expected_recovered_crates: float) -> float:
    return incentive_per_crate_dkk * expected_recovered_crates


def donation_ceiling_margin_dkk(donation_outlay_ceiling_dkk: float, projected_donation_spend_dkk: float) -> float:
    return donation_outlay_ceiling_dkk - projected_donation_spend_dkk


def volume_target_margin(expected_recovered_crates: float, target_recovered_crates: float) -> float:
    return expected_recovered_crates - target_recovered_crates


def total_projected_spend_dkk(projected_donation_spend_dkk: float, logistics_budget_dkk: float, marketing_budget_dkk: float) -> float:
    return projected_donation_spend_dkk + logistics_budget_dkk + marketing_budget_dkk


def program_budget_surplus_dkk(total_program_budget_ceiling_dkk: float, total_projected_spend_dkk: float) -> float:
    return total_program_budget_ceiling_dkk - total_projected_spend_dkk
