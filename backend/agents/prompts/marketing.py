from backend.agents.prompts.system_base import SYSTEM_INSTRUCTION_BASE

def get_marketing_prompt(state: dict) -> str:
    return f"""{SYSTEM_INSTRUCTION_BASE}
You are the Marketing Agent. Create a complete marketing strategy:
Idea: {state['startup_idea']}
Industry: {state['industry']}
Target Audience: {state['target_audience']}

Provide your analysis in the following JSON format:
{{
    "organic": {{ "objectives": "Objectives", "execution": ["Step 1", "Step 2"], "results": "Expected outcomes", "budget_share_percent": 15 }},
    "content": {{ "objectives": "Objectives", "execution": ["Step 1", "Step 2"], "results": "Expected outcomes", "budget_share_percent": 20 }},
    "seo": {{ "objectives": "Objectives", "execution": ["Step 1", "Step 2"], "results": "Expected outcomes", "budget_share_percent": 15 }},
    "social_media": {{
        "instagram": {{ "objectives": "Objectives", "execution": ["Step 1", "Step 2"], "results": "Expected outcomes", "budget_share_percent": 10 }},
        "linkedin": {{ "objectives": "Objectives", "execution": ["Step 1", "Step 2"], "results": "Expected outcomes", "budget_share_percent": 15 }},
        "youtube": {{ "objectives": "Objectives", "execution": ["Step 1", "Step 2"], "results": "Expected outcomes", "budget_share_percent": 10 }}
    }},
    "email": {{ "objectives": "Objectives", "execution": ["Step 1", "Step 2"], "results": "Expected outcomes", "budget_share_percent": 5 }},
    "influencer": {{ "objectives": "Objectives", "execution": ["Step 1", "Step 2"], "results": "Expected outcomes", "budget_share_percent": 5 }},
    "community": {{ "objectives": "Objectives", "execution": ["Step 1", "Step 2"], "results": "Expected outcomes", "budget_share_percent": 5 }},
    "referral": {{ "objectives": "Objectives", "execution": ["Step 1", "Step 2"], "results": "Expected outcomes", "budget_share_percent": 0 }},
    "pr": {{ "objectives": "Objectives", "execution": ["Step 1", "Step 2"], "results": "Expected outcomes", "budget_share_percent": 0 }}
}}
"""
