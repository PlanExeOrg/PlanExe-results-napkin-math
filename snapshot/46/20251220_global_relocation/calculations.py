"""
Generated PlanExe deterministic calculations.

Plan: Split Evenly
Plan type: geopolitical_partition

One function per formula_hint entry from recommended_first_calculations.
No derived_questions emitted.
"""

from __future__ import annotations


def total_severance_stabilization_cost_usd(
    specialized_cip_replacement_cost_usd: float,
    legacy_system_monthly_maintenance_cost_usd: float,
    partition_legal_deadline_months: float,
) -> float:
    return specialized_cip_replacement_cost_usd + legacy_system_monthly_maintenance_cost_usd * partition_legal_deadline_months


def initial_budget_surplus_usd(
    initial_24_month_budget_usd: float,
    total_severance_stabilization_cost_usd: float,
) -> float:
    return initial_24_month_budget_usd - total_severance_stabilization_cost_usd


def infrastructure_transfer_margin(
    infrastructure_transfer_actual_share: float,
    infrastructure_transfer_target_share: float,
) -> float:
    return infrastructure_transfer_actual_share - infrastructure_transfer_target_share


def wave1_verification_margin(
    wave1_verification_actual_share: float,
    wave_verification_threshold_share: float,
) -> float:
    return wave1_verification_actual_share - wave_verification_threshold_share


def northern_density_margin_persons_per_km2(
    northern_density_cap_persons_per_km2: float,
    northern_hub_projected_density_persons_per_km2: float,
) -> float:
    return northern_density_cap_persons_per_km2 - northern_hub_projected_density_persons_per_km2
