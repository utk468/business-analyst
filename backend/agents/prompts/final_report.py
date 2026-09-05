from backend .agents .prompts .system_base import SYSTEM_INSTRUCTION_BASE 

def get_final_report_prompt (state :dict )->str :
    return f"""{SYSTEM_INSTRUCTION_BASE }
You are the Final Report Generator Agent. Create an Executive Summary and compile/harmonize the entire report.
Use the data gathered by the previous 14 agents in the state.

Provide your analysis in the following JSON format:
{{
    "executive_summary": "High-impact, premium 2-3 paragraph pitch and executive summary.",
    "business_overview": "A synthesis of the business structure, stage, region, and target market.",
    "final_recommendations": ["Core recommendation 1", "Core recommendation 2", "Core recommendation 3"],
    "action_plan": ["Immediate action (Day 1-30)", "Medium-term action (Day 31-90)", "Long-term action (Day 91+)"],
    "conclusion": "Final encouraging, highly professional concluding statement."
}}
"""
