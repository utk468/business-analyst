from typing import List, Dict, Any
from backend.agents.state import AgentState

def fallback_risk_assessment(state: AgentState) -> List[Dict[str, Any]]:
    return [
        {
            "type": "Market",
            "level": "Medium",
            "impact": "Slow adoption due to economic downturns.",
            "likelihood": "Medium",
            "mitigation": "Target sectors that are counter-cyclical (e.g., cost saving automations)."
        },
        {
            "type": "Financial",
            "level": "High",
            "impact": "Running out of capital before self-sustainability.",
            "likelihood": "Low",
            "mitigation": "Maintain a strict 12-month runway emergency reserve and defer expensive hires until revenue targets are hit."
        },
        {
            "type": "Legal",
            "level": "Medium",
            "impact": "Data privacy lawsuits or compliance shifts in target region.",
            "likelihood": "Medium",
            "mitigation": "Encrypt all customer records at rest and consult local data counsel early to obtain GDPR/SOC2 alignment."
        },
        {
            "type": "Technology",
            "level": "Low",
            "impact": "Server outages or security breaches.",
            "likelihood": "Low",
            "mitigation": "Deploy on multiple AWS availability zones with automated daily database backups."
        },
        {
            "type": "Competition",
            "level": "High",
            "impact": "Incumbents matching product features and slashing prices.",
            "likelihood": "High",
            "mitigation": "Build proprietary integrations and maintain superior customer service that creates a high switching cost."
        },
        {
            "type": "Supply Chain",
            "level": "Low",
            "impact": "Third-party APIs changing endpoints or shutting down.",
            "likelihood": "Medium",
            "mitigation": "Write modular code wrappers that allow switching core data providers with minimal code changes."
        },
        {
            "type": "Reputation",
            "level": "Low",
            "impact": "Negative reviews online damaging customer trust.",
            "likelihood": "Low",
            "mitigation": "Proactive customer success outreach, rapid resolution of public bugs, and active monitoring of mentions."
        }
    ]
