from backend .agents .prompts .system_base import SYSTEM_INSTRUCTION_BASE 

def get_competitor_analysis_prompt (state :dict ,search_results :str ="")->str :
    country =state .get ('country','Global')

    return f"""{SYSTEM_INSTRUCTION_BASE }
You are the Competitor Analysis Agent. Analyze direct, indirect, premium, budget, and regional competitors for:
Idea: {state ['startup_idea']}
Industry: {state ['industry']}
Target Country/Region: {country }

Live Multi-Source Data Feeds (Tracxn, Crunchbase, Inc42, Startup India):
{search_results }

CRITICAL INSTRUCTION:
You must provide real, authentic competitor profiles verified from live startup databases (Tracxn, Crunchbase, Inc42, Startup India).
Identify actual operating companies in {country } and internationally, and outline their real products, verified funding stage (if found in Tracxn/Crunchbase/Inc42), authentic pricing models in local currency, and genuine strengths and weaknesses.

Provide your analysis in the following JSON format:
{{
    "competitors": [
        {{
            "name": "Competitor Name",
            "type": "Direct|Indirect|Premium|Budget|International",
            "positioning": "Brand positioning summary.",
            "products": ["Product/service 1", "Product/service 2"],
            "pricing": "Pricing model in local currency.",
            "market_share_percent": 15,
            "pricing_level": 7,
            "quality_score": 8,
            "strengths": ["Strength 1", "Strength 2"],
            "weaknesses": ["Weakness 1", "Weakness 2"],
            "presence": "Market share / geographic presence description in {country }.",
            "channels": ["Marketing channel 1", "Marketing channel 2"],
            "differentiators": ["Key differentiator 1"]
        }}
    ],
    "gap_analysis": "Summary of gaps in current competitor offerings based on market intelligence.",
    "differentiation_opportunities": ["Opportunity 1 to stand out", "Opportunity 2 to stand out"]
}}
Generate at least 3-4 realistic, verified competitors.
"""
