from typing import Dict, Any
from backend.agents.state import AgentState

def fallback_investor_readiness(state: AgentState) -> Dict[str, Any]:
    return {
        "readiness_score": 78,
        "attractiveness_score": 83,
        "funding_stages": ["Pre-Seed", "Seed"],
        "investor_types": ["Angel Investors", "Micro VCs", "Industry Incubators"],
        "evaluations": {
            "market_potential": "Excellent. Targeting a growing sector with highly visible pain points and a strong CAGR index.",
            "scalability": "Strong. Software-led framework with low marginal costs per new client allows rapid scaling.",
            "competitive_advantage": "Medium. The speed of the onboarding loop and compliance focus represents a good starting moat, though competitors can copy features over time.",
            "revenue_potential": "Excellent. Recurring SaaS models blended with usage transaction fees yield high lifetime customer values.",
            "team_requirements": "The current team has solid technical capabilities, but will need specialized marketing leadership to scale past the founder sales stage.",
            "funding_potential": "High. Very appealing for pre-seed investors who value fast iteration, lean cost structures, and focused niche target markets."
        }
    }
