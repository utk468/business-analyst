from typing import Dict, Any
from backend.agents.state import AgentState

def fallback_sales_strategy(state: AgentState) -> Dict[str, Any]:
    return {
        "funnel": {
            "awareness": "SEO content, social media posts, and micro-tools bring users to the landing page.",
            "interest": "Interactive demo videos, pricing calculators, and free trials capture email addresses.",
            "decision": "Email drip sequences, customer testimonials, and direct sales calls address objections.",
            "action": "Easy checkout, instant workspace provisioning, and automated setup tours onboard the customer."
        },
        "lead_generation": "Combining inbound SEO traffic with outbound LinkedIn cold messages targeting operations managers.",
        "conversion_strategy": "Deploying exit-intent popups offering discounts, maintaining clean UI pricing comparisons, and installing live-chat widgets on checkout pages.",
        "customer_acquisition_plan": "Self-serve acquisition for startups/growth tiers; personalized sales pipeline with customized proposals for Enterprise accounts.",
        "retention_plan": "Quarterly business reviews for top accounts, proactive outreach if account activity decreases, and product feedback integrations.",
        "customer_success": "Providing a 24-hour setup guarantee, video knowledge libraries, and immediate live chat assistance.",
        "kpis": [
            "Customer Acquisition Cost (CAC) targeted < $50 for self-serve.",
            "Lifetime Value to CAC ratio (LTV:CAC) > 3.5x within Year 1.",
            "Monthly Net Revenue Retention (NRR) > 105%."
        ]
    }
