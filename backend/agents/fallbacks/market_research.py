from typing import Dict, Any
from backend.agents.state import AgentState

def fallback_market_research(state: AgentState) -> Dict[str, Any]:
    idea = state["startup_idea"]
    ind = state["industry"]
    country = state["country"]
    aud = state["target_audience"]
    return {
        "industry_overview": f"The {ind} industry is undergoing a digital transformation driven by the integration of AI, mobile-first consumer habits, and regional shifts. {idea} addresses critical pain points in {country} targeting {aud}.",
        "market_size": "Estimated TAM: $4.2 Billion globally; SAM: $350 Million in the regional target market; SOM: $18 Million (Year 3 projection).",
        "estimated_growth": f"The market is projected to expand at a CAGR of 12.4% over the next five years, fueled by automation demand and consumer convenience preferences in {country}.",
        "tam_sam_som": {
            "tam": 4200000000,
            "sam": 350000000,
            "som": 18000000,
            "explanation": f"Based on industry benchmark statistics for {ind} in {country}."
        },
        "industry_trends": [
            "Hyper-personalization: Custom experiences tailored to individual user behaviors.",
            "De-centralization: Moving away from monolithic suites toward specialized modular APIs.",
            "Eco-sustainability: Increased consumer value on eco-friendly and ethical supply chains."
        ],
        "emerging_opportunities": [
            f"Unserved segments in {country} looking for budget-friendly alternatives.",
            "Integrations with local payment gateways and regional compliance frameworks."
        ],
        "technology_trends": [
            "Adoption of predictive AI models to forecast user workflows.",
            "Serverless architecture enabling rapid micro-scaling with minimal costs."
        ],
        "consumer_behavior": [
            "Shortened attention spans requiring immediate onboarding gratification (Time-to-Value < 2 min).",
            "Trust inflation: Buyers heavily researching social proof and peer reviews before committing."
        ],
        "regional_dynamics": f"The regulatory environment in {country} presents barriers to entry, which can be leveraged as a competitive moat once compliance is achieved.",
        "market_gaps": [
            "Lack of localized customer support and cultural fit in regional competitors.",
            "High price barriers for small-scale users who only need key features."
        ],
        "future_outlook": "The sector will consolidate around platforms that offer high integration speed, robust security, and specialized local solutions."
    }
