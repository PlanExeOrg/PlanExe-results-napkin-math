"""
Generated PlanExe deterministic calculations.

Plan: Containerized Dark Data Ingestor Network (CDDIN)
Plan type: Large-scale physical-digital infrastructure preservation program

One function per formula_hint entry from recommended_first_calculations.
"""

from __future__ import annotations


def fleet_lifetime_opex_budget_margin_usd(total_program_budget_usd: float, annual_opex_per_miu_usd: float, target_fleet_size_units: float, program_duration_years: float) -> float:
    return total_program_budget_usd - (annual_opex_per_miu_usd * target_fleet_size_units * program_duration_years)


def uptime_margin_fraction(achieved_fleet_uptime_fraction: float, uptime_target_fraction: float) -> float:
    return achieved_fleet_uptime_fraction - uptime_target_fraction


def review_load_buffer_margin_fraction(review_load_safety_buffer_fraction: float, ai_flag_rate_fraction: float, review_override_fraction: float) -> float:
    return review_load_safety_buffer_fraction - (ai_flag_rate_fraction + review_override_fraction * ai_flag_rate_fraction)


def pretreatment_reliability_margin_fraction(achieved_pretreatment_reliability_fraction: float, pretreatment_reliability_threshold_fraction: float) -> float:
    return achieved_pretreatment_reliability_fraction - pretreatment_reliability_threshold_fraction


def phase1_budget_margin_usd(phase1_miu_capex_per_unit_usd: float, phase1_vintage_acquisition_usd: float, annual_opex_per_miu_usd: float) -> float:
    return 60000000 - (3 * phase1_miu_capex_per_unit_usd + phase1_vintage_acquisition_usd + annual_opex_per_miu_usd * 3)
