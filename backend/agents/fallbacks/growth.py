from typing import Dict, Any
from backend.agents.state import AgentState

def fallback_growth(state: AgentState) -> Dict[str, Any]:
    return {
        "roadmap": {
            "ninety_days": ["Finalize MVP dashboard", "Run closed beta with 20 companies", "Establish primary social handles"],
            "six_months": ["Public launch", "Execute SEO keyword content push", "Achieve $5K Monthly Recurring Revenue (MRR)"],
            "one_year": ["Release V2 developer APIs", "Build internationalization templates", "Reach $30K MRR"],
            "three_years": ["Establish secondary office", "Launch B2B reseller program", "Position for Series A round or strategic buyout"]
        },
        "scaling_strategy": "We will employ a product-led growth model where free-tier documents/outputs include a 'Powered by Business Strategy' watermark, turning users into marketing nodes.",
        "international_expansion_opportunities": [
            "English-speaking markets (UK, Australia) to leverage identical codebase.",
            "Developing Latin American localization as tech-hubs scale in Brazil and Mexico."
        ],
        "partnership_opportunities": [
            "Incubator sponsorship: offering 1 year free to portfolio founders.",
            "System integrations partners who earn consulting fees for deploying our tool."
        ],
        "acquisition_opportunities": [
            "AeroConsult (niche plugin provider) to integrate document parsing engines.",
            "Consolidating smaller regional tool builders in secondary markets."
        ]
    }
