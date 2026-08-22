from backend.agents.prompts.system_base import SYSTEM_INSTRUCTION_BASE

def get_investor_readiness_prompt(state: dict) -> str:
    return f"""{SYSTEM_INSTRUCTION_BASE}
You are the Investor Readiness Agent. Evaluate funding readiness:
Idea: {state['startup_idea']}
Industry: {state['industry']}
Budget: {state['budget']}
Stage: {state['business_stage']}

Provide your analysis in the following JSON format:
{{
    "readiness_score": 75,
    "attractiveness_score": 80,
    "funding_stages": ["Pre-Seed", "Seed"],
    "investor_types": ["Angel Investors", "Micro VCs"],
    "evaluations": {{
        "market_potential": "Market size and dynamic evaluation.",
        "scalability": "Scalability potential.",
        "competitive_advantage": "Moat and barrier to entry evaluation.",
        "revenue_potential": "Revenue forecast credibility.",
        "team_requirements": "Key hires needed to look investable.",
        "funding_potential": "Synthesis of investor sentiment."
    }}
}}
Ensure the scores are integers between 0 and 100.
"""
