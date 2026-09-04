from backend.agents.prompts.system_base import SYSTEM_INSTRUCTION_BASE
from backend.agents.currency_helper import get_country_currency_info

def get_financial_planning_prompt(state: dict) -> str:
    country = state.get('country', 'Global')
    curr = get_country_currency_info(country)
    
    return f"""{SYSTEM_INSTRUCTION_BASE}
You are the Financial Planning Agent. 
Generate a comprehensive, numerically consistent financial model customized for the startup operating in {country}.
Startup Idea: {state['startup_idea']}
Industry: {state['industry']}
Target Country: {country} (Local Currency: {curr['name']} - {curr['code']} / {curr['symbol']})
Available Budget / Capital: {state['budget']}
Stage: {state['business_stage']}

CRITICAL LOCALIZATION REQUIREMENT:
All financial numbers (startup costs, recurring overheads, revenues, profits, break-even targets, and cash flows) MUST be calculated and stated in the local currency and realistic market scale of {country} ({curr['code']} / {curr['symbol']}).
Do NOT use USD if {country} uses a different local currency. Ensure numbers match the available capital scale: {state['budget']}.
Make sure the figures are mathematically and numerically consistent (e.g. Monthly * 12 = Yearly, Revenue - Expenses = Profit).

Provide your analysis in the following JSON format:
{{
    "startup_costs": {{
        "technology": 15000,
        "marketing": 10000,
        "operations": 5000,
        "team": 12000,
        "legal": 2000,
        "inventory": 0,
        "emergency_fund": 5000
    }},
    "recurring_expenses": {{
        "monthly": 5000,
        "quarterly": 15000,
        "yearly": 60000
    }},
    "revenue_forecast": {{
        "year_1": 80000,
        "year_2": 180000,
        "year_3": 400000
    }},
    "profit_forecast": {{
        "year_1": 20000,
        "year_2": 80000,
        "year_3": 220000
    }},
    "break_even": {{
        "units_or_revenue": 50000,
        "timeline_months": 8,
        "explanation": "Detailed explanation of break-even dynamics in the local currency context of {country}."
    }},
    "cash_flow": {{
        "year_1": 30000,
        "year_2": 110000,
        "year_3": 330000
    }},
    "financials_table_details": "All figures denominated in {curr['name']} ({curr['code']} {curr['symbol']}). Calculated based on economic indices and standard cost of operations in {country}."
}}
Ensure the values are pure integers without string symbols inside the numeric fields.
"""
