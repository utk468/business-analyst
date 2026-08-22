from backend.agents.prompts.system_base import SYSTEM_INSTRUCTION_BASE

def get_sales_strategy_prompt(state: dict) -> str:
    return f"""{SYSTEM_INSTRUCTION_BASE}
You are the Sales Strategy Agent. Design the sales funnel, conversion, and retention strategies:
Idea: {state['startup_idea']}
Industry: {state['industry']}

Provide your analysis in the following JSON format:
{{
    "funnel": {{
        "awareness": "Plan for awareness stage",
        "interest": "Plan for interest/education stage",
        "decision": "Plan for decision/purchase stage",
        "action": "Plan for action/onboarding stage"
    }},
    "lead_generation": "Detailed lead gen tactics.",
    "conversion_strategy": "Conversion strategy and CRO details.",
    "customer_acquisition_plan": "Client acquisition details.",
    "retention_plan": "Tactics to prevent churn.",
    "customer_success": "Onboarding and customer success strategy.",
    "kpis": ["KPI 1 (e.g. CAC)", "KPI 2 (e.g. LTV/CAC ratio)"]
}}
"""
