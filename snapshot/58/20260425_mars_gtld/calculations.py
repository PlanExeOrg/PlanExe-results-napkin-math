"""
Generated PlanExe deterministic calculations.

Plan: .mars gTLD Application
Plan type: Internet governance / gTLD registry acquisition

One function per formula_hint entry from recommended_first_calculations and
derived_questions. Inputs are passed explicitly so callers (run_scenarios,
monte_carlo) can supply concrete values from key_values and bounds.
"""

from __future__ import annotations


def y1_revenue_usd(y1_registration_volume: float, avg_registration_price_usd: float) -> float:
    return y1_registration_volume * avg_registration_price_usd


def breakeven_registrations_y1(annual_opex_usd: float, avg_registration_price_usd: float) -> float:
    if avg_registration_price_usd <= 0:
        return float("inf")
    return annual_opex_usd / avg_registration_price_usd


def y1_revenue_surplus_usd(y1_revenue_usd: float, annual_opex_usd: float, revenue_pledge_fraction: float) -> float:
    return y1_revenue_usd - annual_opex_usd - revenue_pledge_fraction * max(0, y1_revenue_usd - annual_opex_usd)


def contingency_after_shocks_surplus_usd(
    contingency_reserve_usd: float,
    string_contention_overrun_usd: float,
    string_contention_probability: float,
    regulatory_shock_cost_usd: float,
    political_backlash_cost_usd: float,
) -> float:
    return (
        contingency_reserve_usd
        - string_contention_overrun_usd * string_contention_probability
        - regulatory_shock_cost_usd
        - political_backlash_cost_usd
    )


def capital_runway_surplus_usd(
    initial_budget_envelope_usd: float,
    hsm_capex_usd: float,
    annual_opex_usd: float,
    review_duration_months: float,
    contingency_reserve_usd: float,
) -> float:
    return (
        initial_budget_envelope_usd
        - hsm_capex_usd
        - (annual_opex_usd * review_duration_months / 12)
        - contingency_reserve_usd
    )


# skipped: q_breakeven_volume_feasibility -- formula_hint is null (qualitative diagnostic question)
