"""
Generated PlanExe deterministic calculations.

Plan: Europe's first certified Faraday enclosure launch
Plan type: commercial product launch

One function per formula_hint entry from recommended_first_calculations and
derived_questions. Inputs are passed explicitly so callers (run_scenarios,
monte_carlo) can supply concrete values from key_values and bounds.
"""

from __future__ import annotations


def expected_year1_units_sold(iso_run_units: float, retailer_committed_units: float, addressable_prepper_buyers: float, presale_conversion_rate: float) -> float:
    return min(iso_run_units, retailer_committed_units + addressable_prepper_buyers * presale_conversion_rate)


def year1_gross_profit_eur(expected_year1_units_sold: float, premium_unit_price_eur: float, wholesale_discount_fraction: float, unit_bom_cost_eur: float) -> float:
    return expected_year1_units_sold * (premium_unit_price_eur * (1 - wholesale_discount_fraction) - unit_bom_cost_eur)


def net_cash_from_operations_eur(year1_gross_profit_eur: float, fixed_operating_cost_eur: float, iso_run_fixed_cost_eur: float) -> float:
    return year1_gross_profit_eur - fixed_operating_cost_eur - iso_run_fixed_cost_eur


def funding_gate_surplus_eur(net_cash_from_operations_eur: float, cash_trigger_threshold_eur: float) -> float:
    return net_cash_from_operations_eur - cash_trigger_threshold_eur


def year1_budget_surplus_eur(year1_budget_eur: float, fixed_operating_cost_eur: float, iso_run_fixed_cost_eur: float) -> float:
    return year1_budget_eur - fixed_operating_cost_eur - iso_run_fixed_cost_eur


def iso_inventory_surplus_units(expected_year1_units_sold: float, presale_target_units: float) -> float:
    return expected_year1_units_sold - presale_target_units
