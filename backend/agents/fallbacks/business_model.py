from typing import Dict, Any
from backend.agents.state import AgentState

def fallback_business_model(state: AgentState) -> Dict[str, Any]:
    return {
        "revenue_model": "A hybrid SaaS and transaction model. Standard features are billed on a recurring monthly/yearly SaaS framework, while heavy operations (like custom reports, international transactions, API calls) carry a micro-charge usage fee.",
        "pricing_model": "Three-tiered flat rate: Starter ($19/mo), Growth ($49/mo), and Enterprise (Custom quotes). Pro-rated annual payment receives a 20% discount.",
        "subscription_opportunities": [
            "Tiered seats: charge per active manager/operator.",
            "Add-on modular subscriptions: add compliance reports or AI assistance for $9/mo."
        ],
        "upselling_opportunities": [
            "Dedicated server hosting with 99.99% SLA uptime.",
            "White-labeled client portal for professional branding."
        ],
        "distribution_channels": [
            "Direct: SEO and content driving traffic to online portal.",
            "Partnership: Integration marketplace platforms (Shopify App Store, Slack Directory)."
        ],
        "marketplace_strategy": "List our core plugin/connector on major app directories to capture high-intent users looking for solutions.",
        "d2c_strategy": "Self-serve automated onboarding. Users configure their accounts in 3 steps, reducing sales touchpoint costs.",
        "b2b_opportunities": [
            "Offer bulk licensing for agency partners who manage multiple clients.",
            "Provide APIs for mid-market enterprises looking to build proprietary internal front-ends."
        ],
        "partnerships": [
            "Co-marketing campaigns with non-competing complementary SaaS players.",
            "Affiliate program paying 20% lifetime recurring commissions to agency recommenders."
        ]
    }
