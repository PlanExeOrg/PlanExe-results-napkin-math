"""
Generated PlanExe deterministic calculations.

Plan: European Faraday Enclosure Launch (Pragmatic Foundation)
Plan type: commercial_consumer_hardware_launch

One function per formula_hint entry from recommended_first_calculations.
No derived_questions emitted.
"""

from __future__ import annotations


def funding_trigger_margin_eur(
    actual_year1_net_cash_eur: float,
    funding_trigger_net_cash_eur: float,
) -> float:
    return actual_year1_net_cash_eur - funding_trigger_net_cash_eur


def sell_through_margin_units(
    actual_iso_run_sell_through_units: float,
    iso_run_sell_through_units_target: float,
) -> float:
    return actual_iso_run_sell_through_units - iso_run_sell_through_units_target


def certification_funding_margin_eur(
    actual_gross_profit_eur: float,
    mil_std_certification_cost_eur: float,
) -> float:
    return actual_gross_profit_eur - mil_std_certification_cost_eur


def year1_budget_surplus_eur(
    year1_budget_ceiling_eur: float,
    actual_year1_spend_eur: float,
) -> float:
    return year1_budget_ceiling_eur - actual_year1_spend_eur


def iso_commit_demand_margin_units(
    actual_validated_demand_units: float,
    iso_commit_demand_threshold_units: float,
) -> float:
    return actual_validated_demand_units - iso_commit_demand_threshold_units
