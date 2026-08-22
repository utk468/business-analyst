from typing import Dict, Any
from backend.agents.state import AgentState

def fallback_marketing(state: AgentState) -> Dict[str, Any]:
    return {
        "organic": {
            "objectives": "Generate 1,000 monthly organic signups within 6 months.",
            "execution": ["Write high-quality problem-solving blog posts", "Participate actively in industry forums", "Build free mini-tools (e.g. ROI Calculators)"],
            "results": "Low customer acquisition cost (CAC) and sustained traffic generation.",
            "budget_share_percent": 10
        },
        "content": {
            "objectives": "Establish domain authority in the industry space.",
            "execution": ["Weekly industry reports and newsletters", "Infographics outlining industry stats", "Video guides showing workflow hacks"],
            "results": "High newsletter opt-ins and brand trust.",
            "budget_share_percent": 15
        },
        "seo": {
            "objectives": "Rank in the top 3 spots for high-intent long-tail keywords.",
            "execution": ["On-page optimization targeting low-competition keywords", "Creating comprehensive 'Ultimate Guides' to build backlinks"],
            "results": "Consistent inflow of high-converting transactional traffic.",
            "budget_share_percent": 15
        },
        "social_media": {
            "instagram": {
                "objectives": "Build visual brand presence and brand lifestyle.",
                "execution": ["Carousels showing tips & tricks", "Behind-the-scenes founder reels", "User spotlight posts"],
                "results": "Strong community affinity and brand warmth.",
                "budget_share_percent": 10
            },
            "linkedin": {
                "objectives": "Engage business stakeholders and decision makers.",
                "execution": ["Publish thought leadership pieces from founders", "Case studies demonstrating ROI", "Announcing product launches"],
                "results": "B2B warm outreach channels and strategic inquiries.",
                "budget_share_percent": 15
            },
            "youtube": {
                "objectives": "Provide detailed educational walkthroughs.",
                "execution": ["Detailed video tutorials", "Interviews with industry consultants", "Competitor teardowns"],
                "results": "Search-based traffic and reduced customer support inquiries.",
                "budget_share_percent": 10
            }
        },
        "email": {
            "objectives": "Convert 15% of trial signups to premium tiers.",
            "execution": ["5-part automated onboarding sequences", "Weekly product update updates", "Targeted customer discount codes"],
            "results": "High trial-to-paid conversions and automated nurturing.",
            "budget_share_percent": 5
        },
        "influencer": {
            "objectives": "Leverage established industry voices for quick trust.",
            "execution": ["Sponsor newsletters of top tech curators", "Partner with industry creators for product reviews"],
            "results": "Rapid reach expansion and high signups surges.",
            "budget_share_percent": 10
        },
        "community": {
            "objectives": "Create a community of brand advocates.",
            "execution": ["Set up a dedicated Discord/Slack for users", "Host monthly virtual roundtable discussions"],
            "results": "Direct customer feedback loop and high product retention.",
            "budget_share_percent": 5
        },
        "referral": {
            "objectives": "Drive 20% of new acquisitions from existing users.",
            "execution": ["Double-sided referral bonuses (free usage credits)", "Aesthetic affiliate dashboard for easy link sharing"],
            "results": "Viral growth coefficient (K-factor > 0.2).",
            "budget_share_percent": 5
        },
        "pr": {
            "objectives": "Get featured in top-tier tech publications.",
            "execution": ["Pitch funding announcements", "Publish data-driven industry reports", "Submit to ProductHunt"],
            "results": "High authority backlinks and corporate validation.",
            "budget_share_percent": 0
        }
    }
