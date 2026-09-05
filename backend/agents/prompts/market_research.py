from backend .agents .prompts .system_base import SYSTEM_INSTRUCTION_BASE 
from backend .agents .currency_helper import get_country_currency_info 

def get_market_research_prompt (state :dict ,search_results :str ="")->str :
    country =state .get ('country','Global')
    curr =get_country_currency_info (country )

    return f"""{SYSTEM_INSTRUCTION_BASE }
You are the Market Research Agent. Your task is to perform an in-depth market research analysis for the following startup idea:
Idea: {state ['startup_idea']}
Industry: {state ['industry']}
Target Country/Region: {country } (Local Currency: {curr ['name']} - {curr ['code']} / {curr ['symbol']})
Target Audience: {state ['target_audience']}
Budget: {state ['budget']}
Stage: {state ['business_stage']}
Additional Info: {state ['additional_information']}

Recent Web Search Findings:
{search_results }

CRITICAL LOCALIZATION INSTRUCTION:
You must provide real, authentic business intelligence specifically for {country }. Extract actual figures, local market sizes (TAM/SAM/SOM denominated in {curr ['code']} {curr ['symbol']}), CAGRs, and real trends. If exact regional numbers are missing, construct highly realistic, professional estimations modeled on real-world industry benchmarks in {country }.

Provide your analysis in the following JSON format:
{{
    "industry_overview": "Detailed overview of the industry state, regional market challenges, and landscape in {country }.",
    "market_size": "Estimated market size for {country } (TAM, SAM, SOM in {curr ['code']} {curr ['symbol']}).",
    "estimated_growth": "Market growth projections in {country }, including expected CAGR percentage.",
    "tam_sam_som": {{
        "tam": 5000000000,
        "sam": 500000000,
        "som": 50000000,
        "explanation": "Brief explanation of how the TAM, SAM, and SOM values were estimated based on industry data in {country }."
    }},
    "industry_trends": ["Trend 1 with regional explanation", "Trend 2 with regional explanation", "Trend 3 with regional explanation"],
    "emerging_opportunities": ["Opportunity 1 in {country }", "Opportunity 2 in {country }"],
    "technology_trends": ["Tech trend 1", "Tech trend 2"],
    "consumer_behavior": ["Behavior trend in {country } 1", "Behavior trend in {country } 2"],
    "regional_dynamics": "Specific dynamics relative to {country } (regulations, consumer habits, digital adoption).",
    "market_gaps": ["Gap 1: Unmet need in {country }", "Gap 2: Unmet need in {country }"],
    "future_outlook": "Synthesis of where the market in {country } is going over the next 5 years."
}}
"""
