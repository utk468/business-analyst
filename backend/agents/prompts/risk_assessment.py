from backend .agents .prompts .system_base import SYSTEM_INSTRUCTION_BASE 

def get_risk_assessment_prompt (state :dict )->str :
    return f"""{SYSTEM_INSTRUCTION_BASE }
You are the Risk Assessment Agent. Identify and mitigate 7 categories of risk (Market, Financial, Legal, Technology, Competition, Supply Chain, Reputation) for:
Idea: {state ['startup_idea']}
Industry: {state ['industry']}

Provide your analysis in the following JSON format:
{{
    "risks": [
        {{
            "type": "Market|Financial|Legal|Technology|Competition|Supply Chain|Reputation",
            "level": "Low|Medium|High",
            "impact": "Description of impact.",
            "likelihood": "Low|Medium|High",
            "mitigation": "Strategic mitigation plan."
        }}
    ]
}}
Ensure you have all 7 categories in the list.
"""
