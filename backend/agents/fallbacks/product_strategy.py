from typing import Dict, Any
from backend.agents.state import AgentState

def fallback_product_strategy(state: AgentState) -> Dict[str, Any]:
    return {
        "core_products": ["Core Web App Dashboard", "Automated Synchronization Engine", "Basic Report Builder"],
        "premium_products": ["AI Insight Analyst", "Custom Domain White-labeling", "Advanced API Integrations"],
        "future_line": ["Mobile Companion App (iOS & Android)", "Collaborative Team Workspaces"],
        "product_differentiation": "Unlike heavy systems that take weeks to deploy, this product features an 'instant-sync' logic that pulls client data and creates the workspace in under 3 minutes, combined with localized compliance templates.",
        "features": [
            "One-click data imports from CSV/APIs",
            "Responsive dashboard with real-time graphs",
            "Granular role-based user permissions",
            "Automated audit trails"
        ],
        "usp": f"The fastest, most compliant way to manage {state['industry']} operations in {state['country']} without enterprise bloat.",
        "roadmap": {
            "six_month": ["Beta launch with core sync", "First 100 pilot users feedback loops", "Integrate primary payment gate"],
            "twelve_month": ["Launch premium white-labeling tier", "API developer portal release", "SOC2 compliance audit"],
            "twenty_four_month": ["Multi-region translation & currency support", "Mobile native app release", "Enterprise team workspaces"]
        }
    }
