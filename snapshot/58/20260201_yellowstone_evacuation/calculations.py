"""
Generated PlanExe deterministic calculations.

Plan: Yellowstone Caldera Red Warning Evacuation (Pioneer Strategy)
Plan type: emergency_response

One function per formula_hint entry from recommended_first_calculations and
derived_questions. Inputs are passed explicitly so callers (run_scenarios,
monte_carlo) can supply concrete values from key_values and bounds.
"""

from __future__ import annotations


def required_evacuee_throughput_per_hour(zone_zero_population: float, zone_zero_clearance_target_fraction: float, zone_zero_clearance_window_hours: float) -> float:
    if zone_zero_clearance_window_hours <= 0:
        return float("inf")
    return (zone_zero_population * zone_zero_clearance_target_fraction) / zone_zero_clearance_window_hours


def achievable_evacuee_throughput_per_hour(vehicle_throughput_per_hour: float, occupants_per_vehicle: float) -> float:
    return vehicle_throughput_per_hour * occupants_per_vehicle


def evacuation_throughput_surplus(achievable_evacuee_throughput_per_hour: float, required_evacuee_throughput_per_hour: float) -> float:
    return achievable_evacuee_throughput_per_hour - required_evacuee_throughput_per_hour


def airlift_staging_surplus_kg(available_helicopter_sorties: float, sortie_payload_kg: float, airlift_staging_target_fraction: float, zone_one_n95_units_required: float) -> float:
    return (available_helicopter_sorties * sortie_payload_kg) - (airlift_staging_target_fraction * zone_one_n95_units_required * 0.05)


def c2_fuel_cache_surplus_hours(c2_fuel_cache_target_hours: float, c2_node_ups_baseline_hours: float) -> float:
    return c2_fuel_cache_target_hours - c2_node_ups_baseline_hours


# skipped: q_jurisdictional_friction_delay -- formula_hint is null
