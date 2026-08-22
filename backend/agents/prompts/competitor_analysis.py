from backend.agents.prompts.system_base import SYSTEM_INSTRUCTION_BASE

def get_competitor_analysis_prompt(state: dict, search_results: str = "") -> str:
    return f"""{SYSTEM_INSTRUCTION_BASE}
You are the Competitor Analysis Agent. Analyze direct, indirect, premium, budget, and international competitors for:
Idea: {state['startup_idea']}
Industry: {state['industry']}
Country/Region: {state['country']}

Recent Web Search Findings on Competitors:
{search_results}

CRITICAL INSTRUCTION: You must provide real, authentic competitor profiles. Do NOT make up fake competitor names or mock positionings. Research and identify actual operating companies in {state['country']} or globally from the search results, and outline their real products, authentic pricing strategies, and genuine strengths and weaknesses.

Provide your analysis in the following JSON format:
{{
    "competitors": [
        {{
            "name": "Competitor Name",
            "type": "Direct|Indirect|Premium|Budget|International",
            "positioning": "Brand positioning summary.",
            "products": ["Product/service 1", "Product/service 2"],
            "pricing": "Pricing model or estimate (e.g. subscription $10/mo, premium, low-cost).",
            "market_share_percent": 15,
            "pricing_level": 7,
            "quality_score": 8,
            "strengths": ["Strength 1", "Strength 2"],
            "weaknesses": ["Weakness 1", "Weakness 2"],
            "presence": "Market share / geographic presence description.",
            "channels": ["Marketing channel 1", "Marketing channel 2"],
            "differentiators": ["Key differentiator 1"]
        }}
    ],
    "gap_analysis": "Summary of gaps in current competitor offerings.",
    "differentiation_opportunities": ["Opportunity 1 to stand out", "Opportunity 2 to stand out"]
}}
Generate at least 3-4 realistic competitors.
"""
