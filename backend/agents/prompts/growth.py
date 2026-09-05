from backend .agents .prompts .system_base import SYSTEM_INSTRUCTION_BASE 

def get_growth_prompt (state :dict )->str :
    return f"""{SYSTEM_INSTRUCTION_BASE }
You are the Growth Strategy Agent. Develop roadmaps, scaling plans, and partnership/acquisition insights:
Idea: {state ['startup_idea']}
Industry: {state ['industry']}

Provide your analysis in the following JSON format:
{{
    "roadmap": {{
        "ninety_days": ["Objective 1", "Objective 2"],
        "six_months": ["Objective 1", "Objective 2"],
        "one_year": ["Objective 1", "Objective 2"],
        "three_years": ["Objective 1", "Objective 2"]
    }},
    "scaling_strategy": "Tactical growth engine / viral loops details.",
    "international_expansion_opportunities": ["Expansion target 1", "Expansion target 2"],
    "partnership_opportunities": ["Partner category 1", "Partner category 2"],
    "acquisition_opportunities": ["Acquisition target ideas / Consolidation ideas"]
}}
"""
