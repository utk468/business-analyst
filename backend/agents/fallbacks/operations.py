from typing import Dict, Any
from backend.agents.state import AgentState

def fallback_operations(state: AgentState) -> Dict[str, Any]:
    return {
        "operational_structure": "Remote-first workforce with hot-desking options in regional tech hubs to minimize fixed overhead costs.",
        "team_structure": "Chief Executive Officer (Strategy/Sales), Chief Technology Officer (Product development), 2 Developers, 1 Customer Support specialist, and outsourced bookkeeping.",
        "hiring_plan": [
            "Month 1: Senior Full-Stack Developer",
            "Month 2: Content marketer / SEO writer",
            "Month 6: Customer success specialist",
            "Month 12: Lead growth salesperson"
        ],
        "vendor_strategy": [
            "Hosting: Amazon Web Services (AWS) or Vercel",
            "CRM: HubSpot or Pipedrive",
            "Communications: Slack & Google Workspace"
        ],
        "supply_chain_strategy": "100% digital cloud delivery. Scaled hosting nodes dynamically deploy via containerization (Docker/Kubernetes).",
        "technology_stack": [
            "Frontend: React.js with Vite and Vanilla CSS",
            "Backend: Python (FastAPI) and LangGraph agent workflow",
            "Database: MongoDB (Atlas) for unstructured JSON documentation",
            "CI/CD: GitHub Actions"
        ],
        "automation_opportunities": [
            "Automated setup emails triggered instantly on database registration.",
            "Slack chatbot alerts when high-value accounts trigger custom thresholds.",
            "AI-summarized customer support tickets categorized automatically."
        ],
        "operational_kpis": [
            "First response support ticket duration < 30 minutes.",
            "Monthly application uptime SLA > 99.9%.",
            "Time-to-deploy core features < 5 days."
        ]
    }
