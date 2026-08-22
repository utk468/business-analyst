from typing import List, Dict, Any
from backend.agents.state import AgentState

def fallback_customer_research(state: AgentState) -> List[Dict[str, Any]]:
    return [
        {
            "name": "Tech-Savvy Marcus",
            "age": 32,
            "income": "$85,000/year",
            "profession": "Software engineer & Side-Hustler",
            "location": "Urban Metro Center",
            "goals": ["Automate repetitive business administration", "Find reliable tools that grow with his revenue"],
            "pain_points": ["Wasting 10 hours a week on bookkeeping", "Clunky APIs that require constant maintenance"],
            "buying_behavior": "Researches ProductHunt, checks Reddit reviews, and starts with free trials.",
            "digital_habits": ["Uses Slack and Notion daily", "Listens to tech podcasts during commutes"],
            "social_media": ["Twitter/X", "LinkedIn", "Reddit"],
            "purchase_triggers": ["A recommendation on a trusted developer forum", "Frustration with a system outage on a competitor's app"]
        },
        {
            "name": "Pragmatic Elena",
            "age": 45,
            "income": "$62,000/year",
            "profession": "Operations Manager",
            "location": "Suburban Tech Hub",
            "goals": ["Improve team output without adding headcount", "Provide simple reports to senior leadership"],
            "pain_points": ["Resistance to change from older staff", "Lack of clear metrics on team performance"],
            "buying_behavior": "Requests sales demos, compares pricing tables, prefers yearly invoicing.",
            "digital_habits": ["Reads HBR, checks LinkedIn newsletters", "Relies heavily on desktop email"],
            "social_media": ["LinkedIn", "Facebook"],
            "purchase_triggers": ["Exceeding operational budget due to inefficiency", "Direct recommendation from another operations director"]
        },
        {
            "name": "Budget-Conscious Sam",
            "age": 23,
            "income": "$38,000/year",
            "profession": "Freelance designer",
            "location": "Remote / Nomad",
            "goals": ["Look professional to clients on a shoestring budget", "Keep expenses consolidated in one tool"],
            "pain_points": ["Unpredictable cash flow makes monthly subscriptions stressful", "No legal or accounting background"],
            "buying_behavior": "Uses coupon codes, joins affiliate programs, searches for 'appsumo lifetime deals'.",
            "digital_habits": ["Watches YouTube tutorials, uses Figma", "Works out of co-working spaces"],
            "social_media": ["Instagram", "Pinterest", "TikTok"],
            "purchase_triggers": ["Hitting a usage limit on a free plan", "Landing a major project that requires upgrading client-facing portals"]
        }
    ]
