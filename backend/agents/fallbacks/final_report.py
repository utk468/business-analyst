from typing import Dict, Any
from backend.agents.state import AgentState

def fallback_final_report(state: AgentState) -> Dict[str, Any]:
    return {
        "executive_summary": "The proposed venture represents a high-potential startup designed to modernize operations inside the targeted industry. By solving the dual challenges of high complexity and slow regional compliance, our solution targets a high-growth market window. Backed by solid unit economics and a product-led scaling engine, this business model projects rapid cash flow viability within the first year.",
        "business_overview": f"The business operates in the {state['industry']} sector, targeting {state['target_audience']} in {state['country']}. It is positioned as an agile, compliance-first software provider designed to simplify operational bottlenecks.",
        "final_recommendations": [
            "Focus strictly on the primary target audience persona (Tech-Savvy Marcus) during beta testing to maximize onboarding alignment.",
            "Utilize SEO keyword targets early to build organic traffic before launch day, bypassing paid ad inflation.",
            "Maintain a lean operational headcount, using outsourcing and automations to preserve capital runway."
        ],
        "action_plan": [
            "Days 1-30: Complete MVP build, set up MongoDB local database configurations, and register beta participants.",
            "Days 31-90: Run beta tests, monitor support tickets, address usability friction, and push SEO content.",
            "Days 91+: Launch publicly, activate referral loops, and initiate outreach to angel investor groups."
        ],
        "conclusion": "With clear market gaps, high growth CAGR, and a highly capital-efficient operations roadmap, the founder is well-positioned to execute. Start execution immediately with MVP deployment."
    }
