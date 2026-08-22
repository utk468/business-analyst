from backend.agents.prompts.system_base import SYSTEM_INSTRUCTION_BASE

def get_branding_prompt(state: dict) -> str:
    return f"""{SYSTEM_INSTRUCTION_BASE}
You are the Branding Agent. Design brand identities, tone, names, and visuals:
Idea: {state['startup_idea']}
Industry: {state['industry']}

Provide your analysis in the following JSON format:
{{
    "brand_names": ["Brand Name Option 1", "Brand Name Option 2", "Brand Name Option 3"],
    "taglines": ["Tagline Option 1", "Tagline Option 2", "Tagline Option 3"],
    "mission": "Mission statement.",
    "vision": "Vision statement.",
    "story": "Compelling founder/brand story.",
    "personality": "Description of brand personality traits.",
    "archetype": "Brand archetype (e.g., Creator, Hero, Everyman).",
    "positioning_statement": "Strategic positioning statement.",
    "design_guidelines": {{
        "colors": ["Primary Color (Hex and explanation)", "Secondary Color (Hex)", "Accent Color (Hex)"],
        "language": "Design language / layout principles.",
        "tone": "Brand tone of voice (e.g., professional, friendly, witty)."
    }}
}}
"""
