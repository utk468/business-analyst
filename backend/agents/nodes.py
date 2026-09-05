import json 
import logging 
from typing import Dict ,Any ,List 
from backend .config import settings 
from backend .agents .state import AgentState 
from backend .agents import prompts 
from backend .agents .search import search_multi_source_intelligence 
from backend .agents .llm import call_grok 

logger =logging .getLogger ("startup_consultant.nodes")


def _parse_agent_json (raw_text :str )->Any :
    """Parse JSON with multi-layered fallback and repair."""
    try :
        return json .loads (raw_text )
    except Exception :
        pass 

    try :
        import json_repair 
        return json_repair .loads (raw_text )
    except Exception as e :
        logger .warning (f"json_repair also failed: {e }")
        raise ValueError (f"Could not parse response as valid JSON: {raw_text [:200 ]}")



async def run_agent_node (
state :AgentState ,
agent_name :str ,
prompt_text :str 
)->tuple [Dict [str ,Any ],List [str ]]:
    """
    Run agent node logic directly through Grok AI.
    Args:
        state (AgentState): The current state of the graph.
        agent_name (str): The name of the agent.
        prompt_text (str): The prompt to send to the agent.
    Returns:
        tuple[Dict[str, Any], List[str]]: The response from the agent and the logs.
    """
    node_logs =[f"[{agent_name }] Initializing agent operations..."]

    if not settings .groq_api_key :
        err =f"Missing GROQ_API_KEY. Grok AI is required for {agent_name } analysis."
        logger .error (err )
        node_logs .append (f"[{agent_name }] Error: {err }")
        raise RuntimeError (err )

    try :
        node_logs .append (f"[{agent_name }] Contacting Groq AI backend...")

        raw_response =await call_grok (prompt_text ,f"You are the {agent_name } agent.")
        parsed =_parse_agent_json (raw_response )

        node_logs .append (f"[{agent_name }] Grok AI returned detailed analysis successfully.")
        return parsed ,node_logs 

    except Exception as e :
        logger .error (f"Grok API call failed for {agent_name }: {e }")
        node_logs .append (f"[{agent_name }] Grok AI generation failed: {str (e )}")
        raise RuntimeError (f"{agent_name } analysis failed: {str (e )}")from e 


async def initiator_node (state :AgentState )->Dict [str ,Any ]:
    return {"node_logs":["[System] Routing startup briefing to 14 consulting agents in parallel..."]}


async def market_research_node (state :AgentState )->Dict [str ,Any ]:
    search_context =await search_multi_source_intelligence (
    industry =state ['industry'],
    country =state ['country'],
    topic ="market size industry growth trends GDP statistics",
    preferred_sources =["tracxn","data_gov_in","crunchbase"]
    )

    prompt =prompts .get_market_research_prompt (state ,search_context )
    output ,node_logs =await run_agent_node (state ,"Market Research Agent",prompt )
    return {"market_research":output ,"node_logs":node_logs }


async def competitor_analysis_node (state :AgentState )->Dict [str ,Any ]:
    search_context =await search_multi_source_intelligence (
    industry =state ['industry'],
    country =state ['country'],
    topic ="top competitors startups funding rounds valuation",
    preferred_sources =["tracxn","crunchbase","inc42","startup_india"]
    )

    prompt =prompts .get_competitor_analysis_prompt (state ,search_context )
    output ,node_logs =await run_agent_node (state ,"Competitor Analysis Agent",prompt )
    return {"competitor_analysis":output ,"node_logs":node_logs }


async def customer_research_node (state :AgentState )->Dict [str ,Any ]:
    prompt =prompts .get_customer_research_prompt (state )
    output ,node_logs =await run_agent_node (state ,"Customer Research Agent",prompt )
    personas =output .get ("personas")if isinstance (output ,dict )else output 
    return {"customer_research":personas ,"node_logs":node_logs }


async def business_model_node (state :AgentState )->Dict [str ,Any ]:
    prompt =prompts .get_business_model_prompt (state )
    output ,node_logs =await run_agent_node (state ,"Business Model Agent",prompt )
    return {"business_model":output ,"node_logs":node_logs }


async def product_strategy_node (state :AgentState )->Dict [str ,Any ]:
    prompt =prompts .get_product_strategy_prompt (state )
    output ,node_logs =await run_agent_node (state ,"Product Strategy Agent",prompt )
    return {"product_strategy":output ,"node_logs":node_logs }


async def branding_node (state :AgentState )->Dict [str ,Any ]:
    prompt =prompts .get_branding_prompt (state )
    output ,node_logs =await run_agent_node (state ,"Branding Agent",prompt )
    return {"branding":output ,"node_logs":node_logs }


async def marketing_node (state :AgentState )->Dict [str ,Any ]:
    prompt =prompts .get_marketing_prompt (state )
    output ,node_logs =await run_agent_node (state ,"Marketing Agent",prompt )
    return {"marketing":output ,"node_logs":node_logs }


async def sales_strategy_node (state :AgentState )->Dict [str ,Any ]:
    prompt =prompts .get_sales_strategy_prompt (state )
    output ,node_logs =await run_agent_node (state ,"Sales Strategy Agent",prompt )
    return {"sales_strategy":output ,"node_logs":node_logs }


async def financial_planning_node (state :AgentState )->Dict [str ,Any ]:
    prompt =prompts .get_financial_planning_prompt (state )
    output ,node_logs =await run_agent_node (state ,"Financial Planning Agent",prompt )
    return {"financial_planning":output ,"node_logs":node_logs }


async def operations_node (state :AgentState )->Dict [str ,Any ]:
    prompt =prompts .get_operations_prompt (state )
    output ,node_logs =await run_agent_node (state ,"Operations Agent",prompt )
    return {"operations":output ,"node_logs":node_logs }


async def risk_assessment_node (state :AgentState )->Dict [str ,Any ]:
    prompt =prompts .get_risk_assessment_prompt (state )
    output ,node_logs =await run_agent_node (state ,"Risk Assessment Agent",prompt )
    risks =output .get ("risks")if isinstance (output ,dict )else output 
    return {"risk_assessment":risks ,"node_logs":node_logs }


async def swot_analysis_node (state :AgentState )->Dict [str ,Any ]:
    prompt =prompts .get_swot_prompt (state )
    output ,node_logs =await run_agent_node (state ,"SWOT Analysis Agent",prompt )
    return {"swot_analysis":output ,"node_logs":node_logs }


async def growth_strategy_node (state :AgentState )->Dict [str ,Any ]:
    prompt =prompts .get_growth_prompt (state )
    output ,node_logs =await run_agent_node (state ,"Growth Strategy Agent",prompt )
    return {"growth_strategy":output ,"node_logs":node_logs }


async def investor_readiness_node (state :AgentState )->Dict [str ,Any ]:
    search_context =await search_multi_source_intelligence (
    industry =state ['industry'],
    country =state ['country'],
    topic ="investors venture capital seed funds grants schemes",
    preferred_sources =["crunchbase","tracxn","startup_india"]
    )

    prompt =prompts .get_investor_readiness_prompt (state ,search_context )
    output ,node_logs =await run_agent_node (state ,"Investor Readiness Agent",prompt )
    return {"investor_readiness":output ,"node_logs":node_logs }


async def final_report_node (state :AgentState )->Dict [str ,Any ]:
    prompt =prompts .get_final_report_prompt (state )
    output ,node_logs =await run_agent_node (state ,"Final Report Generator Agent",prompt )

    final_report ={
    "metadata":{
    "startup_idea":state ["startup_idea"],
    "industry":state ["industry"],
    "country":state ["country"],
    "target_audience":state ["target_audience"],
    "budget":state ["budget"],
    "business_stage":state ["business_stage"],
    "additional_information":state ["additional_information"]
    },
    "executive_summary":output .get ("executive_summary",""),
    "business_overview":output .get ("business_overview",""),
    "final_recommendations":output .get ("final_recommendations",[]),
    "action_plan":output .get ("action_plan",[]),
    "conclusion":output .get ("conclusion",""),
    "market_research":state .get ("market_research",{}),
    "competitor_analysis":state .get ("competitor_analysis",{}),
    "customer_research":state .get ("customer_research",[]),
    "business_model":state .get ("business_model",{}),
    "product_strategy":state .get ("product_strategy",{}),
    "branding":state .get ("branding",{}),
    "marketing":state .get ("marketing",{}),
    "sales_strategy":state .get ("sales_strategy",{}),
    "financial_planning":state .get ("financial_planning",{}),
    "operations":state .get ("operations",{}),
    "risk_assessment":state .get ("risk_assessment",[]),
    "swot_analysis":state .get ("swot_analysis",{}),
    "growth_strategy":state .get ("growth_strategy",{}),
    "investor_readiness":state .get ("investor_readiness",{})
    }

    node_logs .append ("[System] Workflow complete. Final report compiled.")
    return {"final_report":final_report ,"node_logs":node_logs }
