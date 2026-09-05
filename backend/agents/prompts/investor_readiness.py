from backend .agents .prompts .system_base import SYSTEM_INSTRUCTION_BASE 

def get_investor_readiness_prompt (state :dict ,search_results :str ="")->str :
    country =state .get ('country','Global')

    return f"""{SYSTEM_INSTRUCTION_BASE }
You are the Investor Readiness Agent. Evaluate investment readiness and funding strategy for:
Idea: {state ['startup_idea']}
Industry: {state ['industry']}
Target Country: {country }
Budget / Capital: {state ['budget']}
Stage: {state ['business_stage']}

Live Venture & Investor Intelligence (Crunchbase, Tracxn, Startup India schemes, Inc42):
{search_results }

Provide your analysis in the following JSON format:
{{
    "readiness_score": 75,
    "attractiveness_score": 80,
    "funding_stages": ["Pre-Seed", "Seed (Local & Global)"],
    "investor_types": ["Angel Networks in {country }", "Sector-Specific Micro VCs", "Government Grants / Seed Schemes"],
    "evaluations": {{
        "market_potential": "Market capacity and venture scalability evaluation.",
        "scalability": "Unit economics and regional expansion potential.",
        "competitive_advantage": "Moat, defensive IP, and proprietary advantage.",
        "revenue_potential": "Revenue predictability and payback timelines.",
        "team_requirements": "Key leadership hires required for institutional funding.",
        "funding_potential": "Current venture capital appetite in {country } and relevant startup schemes."
    }}
}}
Ensure the scores are integers between 0 and 100.
"""
