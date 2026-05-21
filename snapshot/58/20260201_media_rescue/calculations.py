"""
Generated PlanExe deterministic calculations.

Plan: Containerized Dark Data Ingestor Network (CDDIN)
Plan type: industrial infrastructure deployment

One function per formula_hint entry from recommended_first_calculations and
derived_questions. Inputs are passed explicitly so callers (run_scenarios,
monte_carlo) can supply concrete values from key_values and bounds.
"""

from __future__ import annotations


def fleet_capex_total_usd(fleet_target_units: float, capex_per_miu_usd: float) -> float:
    return fleet_target_units * capex_per_miu_usd


def fleet_lifetime_opex_usd(fleet_target_units: float, annual_opex_per_miu_usd: float, program_duration_years: float) -> float:
    return fleet_target_units * annual_opex_per_miu_usd * program_duration_years


def program_budget_surplus_usd(total_budget_usd: float, fleet_capex_total_usd: float, fleet_lifetime_opex_usd: float) -> float:
    return total_budget_usd - fleet_capex_total_usd - fleet_lifetime_opex_usd


def realised_review_load_fraction(ai_false_positive_rate: float, mandatory_override_fraction: float) -> float:
    return ai_false_positive_rate + mandatory_override_fraction * ai_false_positive_rate


def review_load_margin(human_review_load_cap_fraction: float, realised_review_load_fraction: float) -> float:
    return human_review_load_cap_fraction - realised_review_load_fraction


def phase1_budget_surplus_usd(phase1_budget_usd: float, capex_per_miu_usd: float, annual_opex_per_miu_usd: float, phase1_duration_years: float) -> float:
    return phase1_budget_usd - (3 * capex_per_miu_usd) - (3 * annual_opex_per_miu_usd * phase1_duration_years)
