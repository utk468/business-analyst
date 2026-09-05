from backend .agents .prompts .system_base import SYSTEM_INSTRUCTION_BASE 

def get_swot_prompt (state :dict )->str :
    return f"""{SYSTEM_INSTRUCTION_BASE }
You are the SWOT Analysis Agent. Conduct a SWOT analysis and recommend actions:
Idea: {state ['startup_idea']}
Industry: {state ['industry']}

Provide your analysis in the following JSON format:
{{
    "strengths": ["Strength 1", "Strength 2", "Strength 3"],
    "weaknesses": ["Weakness 1", "Weakness 2", "Weakness 3"],
    "opportunities": ["Opportunity 1", "Opportunity 2", "Opportunity 3"],
    "threats": ["Threat 1", "Threat 2", "Threat 3"],
    "strategic_recommendations": [
        "SO Strategy: Use strengths to capture opportunities.",
        "WO Strategy: Overcome weaknesses by pursuing opportunities.",
        "ST Strategy: Use strengths to avoid threats.",
        "WT Strategy: Minimize weaknesses and avoid threats."
    ]
}}
"""
