from backend.agents.prompts.system_base import SYSTEM_INSTRUCTION_BASE

def get_financial_planning_prompt(state: dict) -> str:
    return f"""{SYSTEM_INSTRUCTION_BASE}
You are the Financial Planning Agent. Generate detailed financial planning using the budget: {state['budget']}.
Make sure the figures are numerically consistent (e.g. Monthly * 12 = Yearly, Revenue > Expenses leads to profit).
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
        "explanation": "Explanation of break-even dynamics."
    }},
    "cash_flow": {{
        "year_1": 30000,
        "year_2": 110000,
        "year_3": 330000
    }},
    "financials_table_details": "Contextual notes about the currency, inflation, tax or assumptions."
}}
Ensure the values are integers where applicable.
"""
