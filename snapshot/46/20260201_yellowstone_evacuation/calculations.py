"""
Generated PlanExe deterministic calculations.

Plan: Yellowstone Caldera VEI-6 Evacuation (Pioneer Strategy)
Plan type: catastrophic_disaster_response

One function per formula_hint entry from recommended_first_calculations.
No derived_questions emitted.
"""

from __future__ import annotations


def zone_zero_compliance_margin(
    actual_zone_zero_compliance_share: float,
    zone_zero_compliance_target: float,
) -> float:
    return actual_zone_zero_compliance_share - zone_zero_compliance_target


def drf_surplus_usd(
    drf_usd: float,
    actual_drf_spend_usd: float,
) -> float:
    return drf_usd - actual_drf_spend_usd


def n95_staging_margin(
    actual_n95_staging_share: float,
    n95_staging_target_share: float,
) -> float:
    return actual_n95_staging_share - n95_staging_target_share


def c2_fuel_endurance_margin_hours(
    actual_c2_fuel_endurance_hours: float,
    fuel_reserve_target_hours: float,
) -> float:
    return actual_c2_fuel_endurance_hours - fuel_reserve_target_hours


def public_compliance_margin(
    actual_public_compliance_share: float,
    public_compliance_threshold: float,
) -> float:
    return actual_public_compliance_share - public_compliance_threshold
