from typing import Dict, Any
from backend.agents.state import AgentState

def fallback_swot(state: AgentState) -> Dict[str, Any]:
    return {
        "strengths": [
            "Highly flexible, modern tech stack that permits rapid prototyping.",
            "Cost-efficiency: low startup costs due to remote model.",
            "Direct understanding of target audience pain points."
        ],
        "weaknesses": [
            "No established brand presence or trust equity yet.",
            "Limited early marketing capital compared to incumbents.",
            "Small initial team creates execution bottle-necks."
        ],
        "opportunities": [
            "Serving high-growth startups seeking custom operations tooling.",
            "Creating templates for emerging compliance regulations.",
            "Partnering with accelerators/incubators for bulk sales."
        ],
        "threats": [
            "Aggressive counter-measures by dominant global players.",
            "Rapidly shifting technological frameworks (AI deprecating older solutions).",
            "Slowing capital availability in early venture capital stages."
        ],
        "strategic_recommendations": [
            "SO Strategy: Pitch the modern tech stack and custom templates to growth startups in incubator partnerships.",
            "WO Strategy: Build a robust affiliate program to bypass the need for a massive marketing budget.",
            "ST Strategy: Leverage product development velocity to release features before larger slow-moving players can react.",
            "WT Strategy: Minimize weaknesses and avoid threats."
        ]
    }
