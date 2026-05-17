"""
Generated PlanExe deterministic calculations.

Plan: European Faraday Enclosure Launch (Tallinn-anchored)
Plan type: consumer_hardware_startup

One function per formula_hint entry from recommended_first_calculations.
No derived_questions emitted.
"""

from __future__ import annotations


def month12_net_cash_margin_eur(
    actual_net_cash_month12_eur: float,
    net_cash_target_month12_eur: float,
) -> float:
    return actual_net_cash_month12_eur - net_cash_target_month12_eur


def iso_run_sellthrough_margin(
    actual_sellthrough_share: float,
    sell_through_target_share: float,
) -> float:
    return actual_sellthrough_share - sell_through_target_share


def milstd_funding_margin_eur(
    actual_year1_gross_profit_eur: float,
    mil_std_cert_cost_eur: float,
) -> float:
    return actual_year1_gross_profit_eur - mil_std_cert_cost_eur


def presale_conversion_margin(
    actual_presale_conversion_share: float,
    presale_conversion_target_share: float,
) -> float:
    return actual_presale_conversion_share - presale_conversion_target_share


def eu_emc_cert_budget_margin_eur(
    eu_emc_cert_budget_eur: float,
    actual_eu_emc_cert_cost_eur: float,
) -> float:
    return eu_emc_cert_budget_eur - actual_eu_emc_cert_cost_eur
