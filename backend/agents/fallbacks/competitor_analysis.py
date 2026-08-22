from typing import Dict, Any
from backend.agents.state import AgentState

def fallback_competitor_analysis(state: AgentState) -> Dict[str, Any]:
    return {
        "competitors": [
            {
                "name": "Global incumbent Corp",
                "type": "Premium",
                "positioning": "The gold standard for enterprise buyers, highly secure but complex.",
                "products": ["Enterprise suite", "Custom integrations"],
                "pricing": "$150/user/month (annual commit)",
                "market_share_percent": 60,
                "pricing_level": 9,
                "quality_score": 8,
                "strengths": ["Huge market share", "Strong brand recognition", "Extensive feature set"],
                "weaknesses": ["Slow onboarding", "High pricing", "Clunky user interface"],
                "presence": "Global presence with over 10,000 customers.",
                "channels": ["Direct sales", "Enterprise PR", "Google Search Ads"],
                "differentiators": ["SOC2 certified", "Legacy integrations"]
            },
            {
                "name": "Quickstart LLC",
                "type": "Budget",
                "positioning": "Cheap and cheerful solution for hobbyists and freelancers.",
                "products": ["Basic app", "Community forum support"],
                "pricing": "Free tier, premium at $9/mo",
                "market_share_percent": 15,
                "pricing_level": 2,
                "quality_score": 4,
                "strengths": ["Low price barrier", "Simple setup", "Viral loops"],
                "weaknesses": ["Poor scaling limit", "Lacks advanced security", "No custom integrations"],
                "presence": "Strong community presence, mostly North America and Europe.",
                "channels": ["TikTok marketing", "Influencer sponsorship", "SEO"],
                "differentiators": ["Instant account creation", "Free tier"]
            },
            {
                "name": "Regional Pioneer Co",
                "type": "Direct",
                "positioning": "Localized provider specializing in domestic compliance.",
                "products": ["Standard tool", "Compliance consulting addon"],
                "pricing": "$35/mo per seat",
                "market_share_percent": 25,
                "pricing_level": 5,
                "quality_score": 7,
                "strengths": ["Regional compliance expertise", "Local support team"],
                "weaknesses": ["Slow product updates", "Limited capital"],
                "presence": f"Dominant in {state['country']}.",
                "channels": ["Regional trade shows", "B2B cold outreach"],
                "differentiators": ["100% compliant with local laws", "Native language customer support"]
            }
        ],
        "gap_analysis": "Incumbents are too expensive and complex for mid-market, whereas budget solutions lack the reliability and security features required. Local compliance is frequently ignored by international companies.",
        "differentiation_opportunities": [
            "Combine budget-friendly modular tiers with regional compliance standards.",
            "Incorporate automated onboarding to eliminate the typical 30-day setup period."
        ]
    }
