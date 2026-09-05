import os 
import uuid 
import json 
import logging 
import asyncio 
from contextlib import asynccontextmanager 

from fastapi import FastAPI ,BackgroundTasks ,HTTPException ,Request 

from fastapi .middleware .cors import CORSMiddleware 

from fastapi .responses import StreamingResponse 

from fastapi .staticfiles import StaticFiles 
from backend .config import settings 
from backend .database import db 
from backend .agents .graph import graph 
from backend .chatbot import router as chatbot_router 


logging .basicConfig (
level =logging .INFO ,
format ="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger =logging .getLogger ("startup_consultant.main")

active_tasks ={}


@asynccontextmanager 
async def lifespan (app :FastAPI ):
    await db .connect ()
    yield 


app =FastAPI (
title ="AI Startup Consultant API",
description ="Multi-agent strategic business consulting powered by LangGraph & Grok",
version ="1.0.0",
lifespan =lifespan 
)

app .add_middleware (
CORSMiddleware ,
allow_origins =["*"],
allow_credentials =True ,
allow_methods =["*"],
allow_headers =["*"],
)

app .include_router (chatbot_router )


@app .get ("/api/status")
async def get_status ():
    return {
    "status":"online",
    "storage":db .storage_type ,
    "grok_active":bool (settings .groq_api_key ),
    "database_connected":bool (db .is_connected )
    }


NODE_METADATA ={
"initiator":("Initiator",2 ),
"market_research":("Market Research Agent",10 ),
"competitor_analysis":("Competitor Analysis Agent",20 ),
"customer_research":("Customer Research Agent",30 ),
"business_model":("Business Model Agent",40 ),
"product_strategy":("Product Strategy Agent",50 ),
"branding":("Branding Agent",60 ),
"marketing":("Marketing Agent",70 ),
"sales_strategy":("Sales Strategy Agent",80 ),
"financial_planning":("Financial Planning Agent",85 ),
"operations":("Operations Agent",90 ),
"risk_assessment":("Risk Assessment Agent",93 ),
"swot_analysis":("SWOT Analysis Agent",95 ),
"growth_strategy":("Growth Strategy Agent",97 ),
"investor_readiness":("Investor Readiness Agent",99 ),
"final_report":("Final Report Generator Agent",100 )
}


async def run_analysis_task (task_id :str ,inputs :dict ):
    task_info =active_tasks .get (task_id )

    if not task_info :
        return 

    queue =task_info ["queue"]

    state ={
    "startup_idea":inputs .get ("startup_idea",""),
    "industry":inputs .get ("industry",""),
    "country":inputs .get ("country",""),
    "target_audience":inputs .get ("target_audience",""),
    "budget":inputs .get ("budget",""),
    "business_stage":inputs .get ("business_stage",""),
    "additional_information":inputs .get ("additional_information",""),
    "current_agent":"Initiator",
    "progress":0 ,
    "logs":["[System] Spawning 15 business agents for detailed consulting workflow..."]
    }

    await queue .put ({
    "progress":2 ,
    "current_agent":"Initiator",
    "logs":list (state ["logs"]),
    "completed":False 
    })

    completed_nodes =set ()


    try :
        async for output in graph .astream (state ):
            for node_name ,node_output in output .items ():

                if not isinstance (node_output ,dict ):
                    continue 

                completed_nodes .add (node_name )

                agent_name ,progress_val =NODE_METADATA .get (node_name ,(node_name ,state ["progress"]))

                state ["current_agent"]=agent_name 

                state ["progress"]=min (99 ,int ((len (completed_nodes )/16 )*100 ))

                if "node_logs"in node_output :
                    state ["logs"].extend (node_output ["node_logs"])

                if node_name =="final_report":
                    state ["final_report"]=node_output ["final_report"]
                    state ["progress"]=100 
                elif node_name =="initiator":
                    pass 
                else :
                    state [node_name ]=node_output .get (node_name ,{})

            await queue .put ({
            "progress":state ["progress"],
            "current_agent":state ["current_agent"],
            "logs":list (state ["logs"]),
            "completed":False 
            })

        final_report =state .get ("final_report")

        if not final_report :
            raise ValueError ("LangGraph completed execution but did not generate a final report.")

        report_id =await db .save_report (final_report )

        task_info ["report_id"]=report_id 
        task_info ["completed"]=True 

        await queue .put ({
        "progress":100 ,
        "current_agent":"Finalized",
        "logs":list (state ["logs"])+["[System] Strategy compilation stored in database. Processing complete."],
        "completed":True ,
        "report_id":report_id 
        })

    except Exception as e :
        logger .exception (f"Error executing graph for task {task_id }")
        err_msg =f"LangGraph execution error: {str (e )}"
        task_info ["error"]=err_msg 

        await queue .put ({
        "progress":state .get ("progress",0 ),
        "current_agent":"Error",
        "logs":list (state .get ("logs",[]))+[f"[System Error] {err_msg }"],
        "completed":True ,
        "error":err_msg 
        })


@app .post ("/api/analyze")
async def analyze_startup (inputs :dict ,background_tasks :BackgroundTasks ):
    task_id =str (uuid .uuid4 ())

    active_tasks [task_id ]={
    "id":task_id ,
    "queue":asyncio .Queue (),
    "completed":False ,
    "report_id":None ,
    "error":None 
    }
    background_tasks .add_task (run_analysis_task ,task_id ,inputs )

    return {"task_id":task_id }


@app .get ("/api/analyze/stream/{task_id}")
async def stream_analysis_progress (task_id :str ):
    if task_id not in active_tasks :
        raise HTTPException (status_code =404 ,detail ="Task session not found")

    task_info =active_tasks [task_id ]
    queue =task_info ["queue"]

    async def event_stream ():
        try :
            while True :
                payload =await queue .get ()
                yield f"data: {json .dumps (payload )}\n\n"

                if payload .get ("completed"):
                    if task_id in active_tasks :
                        del active_tasks [task_id ]
                    break 
        except asyncio .CancelledError :
            logger .info (f"SSE stream client cancelled task session: {task_id }")
            pass 

    return StreamingResponse (event_stream (),media_type ="text/event-stream")


@app .get ("/api/reports")
async def list_reports ():
    reports =await db .get_reports ()

    briefs =[]
    for r in reports :
        briefs .append ({
        "id":r .get ("id"),
        "created_at":r .get ("created_at"),
        "metadata":r .get ("metadata",{}),
        "executive_summary":r .get ("executive_summary","")[:250 ]+"..."if r .get ("executive_summary")else ""
        })
    return briefs 


@app .get ("/api/reports/{report_id}")
async def get_report_details (report_id :str ):
    report =await db .get_report (report_id )
    if not report :
        raise HTTPException (status_code =404 ,detail ="Report not found")
    return report 


@app .delete ("/api/reports/{report_id}")
async def delete_report (report_id :str ):
    success =await db .delete_report (report_id )
    if not success :
        raise HTTPException (status_code =404 ,detail ="Report not found")
    return {"status":"deleted"}


frontend_dir =os .path .join (os .path .dirname (os .path .dirname (os .path .abspath (__file__ ))),"frontend")
if not os .path .exists (frontend_dir ):
    os .makedirs (frontend_dir ,exist_ok =True )


app .mount ("/",StaticFiles (directory =frontend_dir ,html =True ),name ="frontend")
