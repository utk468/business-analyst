from backend .agents .prompts .system_base import SYSTEM_INSTRUCTION_BASE 

def get_customer_research_prompt (state :dict )->str :
    return f"""{SYSTEM_INSTRUCTION_BASE }
You are the Customer Research Agent. Generate at least 3 distinct customer personas for:
Idea: {state ['startup_idea']}
Industry: {state ['industry']}
Target Audience: {state ['target_audience']}
Country: {state ['country']}

Provide your analysis in the following JSON format:
{{
    "personas": [
        {{
            "name": "Persona Name (e.g. Tech-Savvy Tina)",
            "age": 28,
            "income": "Average income level",
            "profession": "Profession",
            "location": "Location context (urban/suburban)",
            "goals": ["Goal 1", "Goal 2"],
            "pain_points": ["Pain point 1", "Pain point 2"],
            "buying_behavior": "Description of buying behavior.",
            "digital_habits": ["Habit 1", "Habit 2"],
            "social_media": ["Platform 1", "Platform 2"],
            "purchase_triggers": ["Trigger 1", "Trigger 2"]
        }}
    ]
}}
"""
