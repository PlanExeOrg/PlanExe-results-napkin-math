"""
Generated PlanExe deterministic calculations.

Plan: Global Hemispheric Partition (Builder Path)
Plan type: mega-project_geopolitical

One function per formula_hint entry from recommended_first_calculations and
derived_questions. Inputs are passed explicitly so callers (run_scenarios,
monte_carlo) can supply concrete values from key_values and bounds.
"""

from __future__ import annotations


def wave_verification_margin(actual_wave_verification_rate: float, handover_verification_threshold: float) -> float:
    return actual_wave_verification_rate - handover_verification_threshold


def schedule_audit_buffer_months(partition_deadline_months: float, wave3_actual_completion_month: float) -> float:
    return partition_deadline_months - wave3_actual_completion_month


def density_buffer_persons_per_km2(density_cap_persons_per_km2: float, projected_peak_hub_density: float) -> float:
    return density_cap_persons_per_km2 - projected_peak_hub_density


def cip_replacement_cost_usd(cip_count_moved_south: float, cip_replacement_ratio: float, monthly_replacement_unit_cost_usd: float, partition_deadline_months: float) -> float:
    return cip_count_moved_south * cip_replacement_ratio * monthly_replacement_unit_cost_usd * partition_deadline_months


def cip_cost_share_buffer(cip_cost_share_cap: float, cip_replacement_cost_usd: float, initial_24m_allocation_usd: float) -> float:
    if initial_24m_allocation_usd <= 0:
        return float("inf")
    return cip_cost_share_cap - (cip_replacement_cost_usd / initial_24m_allocation_usd)
