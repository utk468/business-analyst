# pyrefly: ignore [missing-import]
from langgraph.graph import StateGraph, END
from backend.agents.state import AgentState
from backend.agents import nodes

def build_workflow():

    workflow = StateGraph(AgentState)
    

    workflow.add_node("initiator", nodes.initiator_node)
    workflow.add_node("market_research", nodes.market_research_node)
    workflow.add_node("competitor_analysis", nodes.competitor_analysis_node)
    workflow.add_node("customer_research", nodes.customer_research_node)
    workflow.add_node("business_model", nodes.business_model_node)
    workflow.add_node("product_strategy", nodes.product_strategy_node)
    workflow.add_node("branding", nodes.branding_node)
    workflow.add_node("marketing", nodes.marketing_node)
    workflow.add_node("sales_strategy", nodes.sales_strategy_node)
    workflow.add_node("financial_planning", nodes.financial_planning_node)
    workflow.add_node("operations", nodes.operations_node)
    workflow.add_node("risk_assessment", nodes.risk_assessment_node)
    workflow.add_node("swot_analysis", nodes.swot_analysis_node)
    workflow.add_node("growth_strategy", nodes.growth_strategy_node)
    workflow.add_node("investor_readiness", nodes.investor_readiness_node)
    workflow.add_node("final_report", nodes.final_report_node)
    

    workflow.set_entry_point("initiator")
    

    parallel_nodes = [
        "market_research", "competitor_analysis", "customer_research",
        "business_model", "product_strategy", "branding", "marketing",
        "sales_strategy", "financial_planning", "operations",
        "risk_assessment", "swot_analysis", "growth_strategy", "investor_readiness"
    ]



    for node in parallel_nodes:
        workflow.add_edge("initiator", node)
        workflow.add_edge(node, "final_report")
        


    workflow.add_edge("final_report", END)
    
    return workflow.compile()




graph = build_workflow()
