from backend.agents.prompts.system_base import SYSTEM_INSTRUCTION_BASE

def get_product_strategy_prompt(state: dict) -> str:
    return f"""{SYSTEM_INSTRUCTION_BASE}
You are the Product Strategy Agent. Design core, premium, and future product lines with a roadmap:
Idea: {state['startup_idea']}
Industry: {state['industry']}

Provide your analysis in the following JSON format:
{{
    "core_products": ["Core Product/Feature 1", "Core Product/Feature 2"],
    "premium_products": ["Premium tier feature 1", "Premium tier feature 2"],
    "future_line": ["Future line expansion 1", "Future line expansion 2"],
    "product_differentiation": "Details on why this product stands out.",
    "features": ["Key technical/functional feature 1", "Key feature 2"],
    "usp": "Unique Selling Proposition statement.",
    "roadmap": {{
        "six_month": ["Milestone 1", "Milestone 2"],
        "twelve_month": ["Milestone 1", "Milestone 2"],
        "twenty_four_month": ["Milestone 1", "Milestone 2"]
    }}
}}
"""
