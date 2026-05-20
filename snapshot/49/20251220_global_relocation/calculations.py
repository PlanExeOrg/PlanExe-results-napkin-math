"""
Generated PlanExe deterministic calculations.

Plan: Hemispheric Partition (Builder Path)
Plan type: geopolitical_megaproject

One function per formula_hint entry from recommended_first_calculations.
No derived_questions emitted.
"""

from __future__ import annotations


def budget_24mo_surplus_usd(
    initial_allocation_usd: float,
    total_24mo_severance_and_stabilization_cost_usd: float,
) -> float:
    return initial_allocation_usd - total_24mo_severance_and_stabilization_cost_usd


def wave1_verification_margin(
    achieved_wave1_verification_fraction: float,
    wave1_verification_target_fraction: float,
) -> float:
    return achieved_wave1_verification_fraction - wave1_verification_target_fraction


def machine_energy_contribution_margin(
    achieved_machine_energy_contribution_fraction: float,
    machine_energy_contribution_target_fraction: float,
) -> float:
    return achieved_machine_energy_contribution_fraction - machine_energy_contribution_target_fraction


def required_relocated_people(
    total_relocation_headcount: float,
    relocation_completion_target_fraction: float,
) -> float:
    return total_relocation_headcount * relocation_completion_target_fraction


def post_24mo_reserve_buffer_usd(
    total_program_budget_usd: float,
    initial_allocation_usd: float,
) -> float:
    return total_program_budget_usd - initial_allocation_usd
