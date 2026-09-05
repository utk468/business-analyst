from backend .agents .prompts .system_base import SYSTEM_INSTRUCTION_BASE 

def get_business_model_prompt (state :dict )->str :
    return f"""{SYSTEM_INSTRUCTION_BASE }
You are the Business Model Agent. Design the revenue architecture, pricing model, and distribution channels for:
Idea: {state ['startup_idea']}
Industry: {state ['industry']}
Budget: {state ['budget']}
Stage: {state ['business_stage']}

Provide your analysis in the following JSON format:
{{
    "revenue_model": "Comprehensive explanation of how the business makes money.",
    "pricing_model": "Detailed pricing structure (e.g. freemium, tiered flat rate).",
    "subscription_opportunities": ["SaaS subscription option", "Premium service plan"],
    "upselling_opportunities": ["Upsell option 1", "Upsell option 2"],
    "distribution_channels": ["Channel 1 (Direct)", "Channel 2 (Partnerships)"],
    "marketplace_strategy": "Marketplace Strategy description or N/A.",
    "d2c_strategy": "D2C Strategy description or N/A.",
    "b2b_opportunities": ["B2B opportunities description"],
    "partnerships": ["Strategic partnership 1", "Strategic partnership 2"]
}}
"""
