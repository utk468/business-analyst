import json
import logging
from typing import Dict, Any, List
from backend.config import settings
from backend.agents.state import AgentState
from backend.agents import prompts
from backend.agents.search import search_web
from backend.agents.llm import call_grok
from backend.agents import fallbacks

logger = logging.getLogger("startup_consultant.nodes")


# Helper: Run Agent Node Logic
async def run_agent_node(
    state: AgentState, 
    agent_name: str, 
    prompt_text: str, 
    fallback_data_generator
) -> tuple[Dict[str, Any], List[str]]:
    """
    Run agent node logic.
    Args:
        state (AgentState): The current state of the graph.
        agent_name (str): The name of the agent.
        prompt_text (str): The prompt to send to the agent.
        fallback_data_generator (function): A function to generate fallback data.
    Returns:
        tuple[Dict[str, Any], List[str]]: The response from the agent and the logs.
    """
    node_logs = [f"[{agent_name}] Initializing agent operations..."]
    
    if settings.groq_api_key:
        try:
            node_logs.append(f"[{agent_name}] Contacting Groq AI backend...")
            
            raw_response = await call_grok(prompt_text, f"You are the {agent_name} agent.")
            # Validate JSON string
            parsed = json.loads(raw_response)
            
            node_logs.append(f"[{agent_name}] Grok AI returned detailed analysis successfully.")
            
            return parsed, node_logs

        except Exception as e:
            node_logs.append(f"[{agent_name}] Grok API call/parse failed: {str(e)}. Triggering backup consulting engine...")
            
            logger.exception(f"Grok API call failed for {agent_name}")

            fallback_res = fallback_data_generator(state)

            return fallback_res, node_logs
    else:
        node_logs.append(f"[{agent_name}] Running local consulting engines (no Grok API key found)...")
        import asyncio
        await asyncio.sleep(0.5)
        fallback_res = fallback_data_generator(state)
        return fallback_res, node_logs








async def initiator_node(state: AgentState) -> Dict[str, Any]:
    return {"node_logs": ["[System] Routing startup briefing to 14 consulting agents in parallel..."]}



async def market_research_node(state: AgentState) -> Dict[str, Any]:

    # Run web search query for industry context
    query = f"{state['industry']} industry size trends growth 2025 2026 {state['country']}"

    search_context = await search_web(query)
    
    prompt = prompts.get_market_research_prompt(state, search_context)
    
    output, node_logs = await run_agent_node(state, "Market Research Agent", prompt, fallbacks.fallback_market_research)
    
    return {"market_research": output, "node_logs": node_logs}





async def competitor_analysis_node(state: AgentState) -> Dict[str, Any]:
    # Run web search query for competitors
    query = f"top competitors companies services in {state['industry']} {state['country']}"
    search_context = await search_web(query)
    
    prompt = prompts.get_competitor_analysis_prompt(state, search_context)
    output, node_logs = await run_agent_node(state, "Competitor Analysis Agent", prompt, fallbacks.fallback_competitor_analysis)
    
    return {"competitor_analysis": output, "node_logs": node_logs}



async def customer_research_node(state: AgentState) -> Dict[str, Any]:
    prompt = prompts.get_customer_research_prompt(state)
    output, node_logs = await run_agent_node(state, "Customer Research Agent", prompt, lambda s: {"personas": fallbacks.fallback_customer_research(s)})
    
    personas = output.get("personas") if isinstance(output, dict) else output
    if not personas:
        personas = fallbacks.fallback_customer_research(state)
        
    return {"customer_research": personas, "node_logs": node_logs}




async def business_model_node(state: AgentState) -> Dict[str, Any]:
    prompt = prompts.get_business_model_prompt(state)
    output, node_logs = await run_agent_node(state, "Business Model Agent", prompt, fallbacks.fallback_business_model)
    return {"business_model": output, "node_logs": node_logs}




async def product_strategy_node(state: AgentState) -> Dict[str, Any]:
    prompt = prompts.get_product_strategy_prompt(state)
    output, node_logs = await run_agent_node(state, "Product Strategy Agent", prompt, fallbacks.fallback_product_strategy)
    return {"product_strategy": output, "node_logs": node_logs}



async def branding_node(state: AgentState) -> Dict[str, Any]:
    prompt = prompts.get_branding_prompt(state)
    output, node_logs = await run_agent_node(state, "Branding Agent", prompt, fallbacks.fallback_branding)
    return {"branding": output, "node_logs": node_logs}



async def marketing_node(state: AgentState) -> Dict[str, Any]:
    prompt = prompts.get_marketing_prompt(state)
    output, node_logs = await run_agent_node(state, "Marketing Agent", prompt, fallbacks.fallback_marketing)
    return {"marketing": output, "node_logs": node_logs}



async def sales_strategy_node(state: AgentState) -> Dict[str, Any]:
    prompt = prompts.get_sales_strategy_prompt(state)
    output, node_logs = await run_agent_node(state, "Sales Strategy Agent", prompt, fallbacks.fallback_sales_strategy)
    return {"sales_strategy": output, "node_logs": node_logs}




async def financial_planning_node(state: AgentState) -> Dict[str, Any]:
    prompt = prompts.get_financial_planning_prompt(state)
    output, node_logs = await run_agent_node(state, "Financial Planning Agent", prompt, fallbacks.fallback_financial_planning)
    return {"financial_planning": output, "node_logs": node_logs}



async def operations_node(state: AgentState) -> Dict[str, Any]:
    prompt = prompts.get_operations_prompt(state)
    output, node_logs = await run_agent_node(state, "Operations Agent", prompt, fallbacks.fallback_operations)
    return {"operations": output, "node_logs": node_logs}




async def risk_assessment_node(state: AgentState) -> Dict[str, Any]:

    prompt = prompts.get_risk_assessment_prompt(state)
    
    output, node_logs = await run_agent_node(state, "Risk Assessment Agent", prompt, lambda s: {"risks": fallbacks.fallback_risk_assessment(s)})
    
    risks = output.get("risks") if isinstance(output, dict) else output
    if not risks:
        risks = fallbacks.fallback_risk_assessment(state)
        
    return {"risk_assessment": risks, "node_logs": node_logs}




async def swot_analysis_node(state: AgentState) -> Dict[str, Any]:
    prompt = prompts.get_swot_prompt(state)
    output, node_logs = await run_agent_node(state, "SWOT Analysis Agent", prompt, fallbacks.fallback_swot)
    return {"swot_analysis": output, "node_logs": node_logs}



async def growth_strategy_node(state: AgentState) -> Dict[str, Any]:
    prompt = prompts.get_growth_prompt(state)
    output, node_logs = await run_agent_node(state, "Growth Strategy Agent", prompt, fallbacks.fallback_growth)
    return {"growth_strategy": output, "node_logs": node_logs}




async def investor_readiness_node(state: AgentState) -> Dict[str, Any]:
    prompt = prompts.get_investor_readiness_prompt(state)
    output, node_logs = await run_agent_node(state, "Investor Readiness Agent", prompt, fallbacks.fallback_investor_readiness)
    return {"investor_readiness": output, "node_logs": node_logs}




async def final_report_node(state: AgentState) -> Dict[str, Any]:
    
    prompt = prompts.get_final_report_prompt(state)
    
    output, node_logs = await run_agent_node(state, "Final Report Generator Agent", prompt, fallbacks.fallback_final_report)
    

    final_report = {
        "metadata": {
            "startup_idea": state["startup_idea"],
            "industry": state["industry"],
            "country": state["country"],
            "target_audience": state["target_audience"],
            "budget": state["budget"],
            "business_stage": state["business_stage"],
            "additional_information": state["additional_information"]
        },
        "executive_summary": output.get("executive_summary", ""),
        "business_overview": output.get("business_overview", ""),
        "final_recommendations": output.get("final_recommendations", []),
        "action_plan": output.get("action_plan", []),
        "conclusion": output.get("conclusion", ""),
        "market_research": state.get("market_research", {}),
        "competitor_analysis": state.get("competitor_analysis", {}),
        "customer_research": state.get("customer_research", []),
        "business_model": state.get("business_model", {}),
        "product_strategy": state.get("product_strategy", {}),
        "branding": state.get("branding", {}),
        "marketing": state.get("marketing", {}),
        "sales_strategy": state.get("sales_strategy", {}),
        "financial_planning": state.get("financial_planning", {}),
        "operations": state.get("operations", {}),
        "risk_assessment": state.get("risk_assessment", []),
        "swot_analysis": state.get("swot_analysis", {}),
        "growth_strategy": state.get("growth_strategy", {}),
        "investor_readiness": state.get("investor_readiness", {})
    }
    
    node_logs.append("[System] Workflow complete. Final report compiled.")
    return {"final_report": final_report, "node_logs": node_logs}
