from backend.agents.prompts.system_base import SYSTEM_INSTRUCTION_BASE

def get_operations_prompt(state: dict) -> str:
    return f"""{SYSTEM_INSTRUCTION_BASE}
You are the Operations Agent. Design operational structure, hiring, supply chain, and tech stack:
Idea: {state['startup_idea']}
Industry: {state['industry']}

Provide your analysis in the following JSON format:
{{
    "operational_structure": "Operational model overview (remote/hybrid, key offices).",
    "team_structure": "Roles and hierarchy design.",
    "hiring_plan": ["Immediate hire 1 (Role)", "Immediate hire 2", "Month 6 hire"],
    "vendor_strategy": ["Strategy for vendors", "Key tools needed"],
    "supply_chain_strategy": "Supply chain/logistics summary (or software distribution).",
    "technology_stack": ["Frontend/Backend/Cloud choices", "SaaS tools for operations"],
    "automation_opportunities": ["Automation flow 1 (e.g. CRM automated onboarding)", "Automation 2"],
    "operational_kpis": ["KPI 1 (e.g. ticket response time)", "KPI 2"]
}}
"""
