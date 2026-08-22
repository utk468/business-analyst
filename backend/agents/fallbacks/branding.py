from typing import Dict, Any
from backend.agents.state import AgentState


def fallback_branding(state: AgentState) -> Dict[str, Any]:
    return {
        "brand_names": ["Business Strategy Solutions", "AeroConsult", "Stratis Business Tools"],
        "taglines": ["Simplifying Complexity", "Enterprise Power, Startup Speed", "Operational Intelligence, Unlocked"],
        "mission": "To democratize high-level business intelligence, providing accessible, secure, and intuitive tools that empower startups and growing businesses to focus on their vision.",
        "vision": "To become the global operating system for early-stage and mid-market organizations, fostering growth through simple design and smart data automation.",
        "story": "Founded by industry experts who grew tired of watching startups burn capital trying to configure complex enterprise software, we built this tool in a garage to offer a plug-and-play alternative.",
        "brand_personality": "Authoritative yet approachable, efficient, and forward-looking.",
        "archetype": "The Creator (improving systems, fostering innovation, structure and control).",
        "positioning_statement": f"For {state['target_audience']} who are frustrated by slow and expensive tools, our solution provides immediate, compliant operational intelligence in {state['country']}.",
        "design_guidelines": {
            "colors": [
                "Deep Space Blue (#0B192C) - Represents trust, stability, and depth.",
                "Aqua Teal (#008DDA) - Highlights tech-forwardness, clarity, and precision.",
                "Neon Coral (#FF4E88) - Call to actions and high energy accents."
            ],
            "language": "Clean, grid-based layout with high contrast, generous whitespace, rounded borders (12px radius), and smooth hover scaling.",
            "tone": "Confident, clean, and plain-spoken. Avoid unnecessary buzzwords; speak to the actual user benefit."
        }
    }
