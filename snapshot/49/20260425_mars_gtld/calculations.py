"""
Generated PlanExe deterministic calculations.

Plan: .mars gTLD Application
Plan type: commercial

One function per formula_hint entry in recommended_first_calculations and
derived_questions. Inputs are supplied by the scenario runner from key_values,
missing_values_to_estimate, and prior outputs.
"""

from __future__ import annotations


def year1_revenue_usd(expected_year1_registrations: float, avg_price_per_domain_usd: float) -> float:
    return expected_year1_registrations * avg_price_per_domain_usd


def year1_revenue_surplus_usd(year1_revenue_usd: float, year1_base_opex_usd: float) -> float:
    return year1_revenue_usd - year1_base_opex_usd


def registration_volume_margin(expected_year1_registrations: float, year1_breakeven_registration_volume: float) -> float:
    return expected_year1_registrations - year1_breakeven_registration_volume


def budget_after_critical_draws_usd(total_program_budget_usd: float, hsm_capex_usd: float, string_contention_contingency_usd: float) -> float:
    return total_program_budget_usd - hsm_capex_usd - string_contention_contingency_usd


def pledge_coverage_surplus_usd(year1_revenue_surplus_usd: float, revenue_pledge_fraction: float, registration_volume_buffer_fraction: float, year1_base_opex_usd: float) -> float:
    return year1_revenue_surplus_usd - revenue_pledge_fraction * year1_revenue_surplus_usd - registration_volume_buffer_fraction * year1_base_opex_usd


def mos_compliance_margin(observed_mos_compliance_rate: float, mos_compliance_threshold: float) -> float:
    return observed_mos_compliance_rate - mos_compliance_threshold
