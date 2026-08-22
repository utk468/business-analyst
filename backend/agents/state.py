from typing import Dict, List, Any, TypedDict

class AgentState(TypedDict):
    # user inputs 
    startup_idea: str
    industry: str
    country: str
    target_audience: str
    budget: str
    business_stage: str
    additional_information: str
    
    # Workflow Execution State
    current_agent: str
    progress: int
    logs: List[str]   
    
    # Outputs from specialized agents 14 agents 
    market_research: Dict[str, Any]
    competitor_analysis: Dict[str, Any]
    customer_research: List[Dict[str, Any]]
    business_model: Dict[str, Any]
    product_strategy: Dict[str, Any]
    branding: Dict[str, Any]
    marketing: Dict[str, Any]
    sales_strategy: Dict[str, Any]
    financial_planning: Dict[str, Any]
    operations: Dict[str, Any]
    risk_assessment: List[Dict[str, Any]]
    swot_analysis: Dict[str, Any]
    growth_strategy: Dict[str, Any]
    investor_readiness: Dict[str, Any]
    
    # Final consolidated report JSON 
    final_report: Dict[str, Any]
