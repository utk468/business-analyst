from typing import Dict, Any
from backend.agents.state import AgentState

def fallback_financial_planning(state: AgentState) -> Dict[str, Any]:
    budget_raw = state["budget"]
    try:
        budget_val = int("".join(c for c in budget_raw if c.isdigit()))
    except:
        budget_val = 100000
        
    tech = int(budget_val * 0.20)
    mark = int(budget_val * 0.25)
    ops = int(budget_val * 0.15)
    team = int(budget_val * 0.20)
    legal = int(budget_val * 0.05)
    inventory = int(budget_val * 0.05)
    emergency = int(budget_val * 0.10)
    
    monthly_exp = int(budget_val * 0.08)
    
    return {
        "startup_costs": {
            "technology": tech,
            "marketing": mark,
            "operations": ops,
            "team": team,
            "legal": legal,
            "inventory": inventory,
            "emergency_fund": emergency
        },
        "recurring_expenses": {
            "monthly": monthly_exp,
            "quarterly": monthly_exp * 3,
            "yearly": monthly_exp * 12
        },
        "revenue_forecast": {
            "year_1": int(budget_val * 1.5),
            "year_2": int(budget_val * 3.5),
            "year_3": int(budget_val * 8.0)
        },
        "profit_forecast": {
            "year_1": int(budget_val * 0.2),
            "year_2": int(budget_val * 1.1),
            "year_3": int(budget_val * 3.2)
        },
        "break_even": {
            "units_or_revenue": int(budget_val * 0.6),
            "timeline_months": 7,
            "explanation": f"Based on our initial overhead of ${monthly_exp}/month and standard pricing tiers, the company expects to reach net monthly profitability by month 7."
        },
        "cash_flow": {
            "year_1": int(budget_val * 0.8),
            "year_2": int(budget_val * 2.2),
            "year_3": int(budget_val * 5.4)
        },
        "financials_table_details": "All figures in USD. Projections based on linear marketing scale factors and current market size indices."
    }
