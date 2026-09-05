import logging 
import asyncio 
import httpx 
from typing import List ,Optional 
from pydantic import BaseModel 
from fastapi import APIRouter ,HTTPException 
from backend .config import settings 

logger =logging .getLogger ("startup_consultant.chatbot")

router =APIRouter (prefix ="/api/chat",tags =["Chatbot"])


class ChatMessage (BaseModel ):
    role :str 
    content :str 


class ChatRequest (BaseModel ):
    message :str 
    history :Optional [List [ChatMessage ]]=[]
    context :Optional [dict ]=None 


class ChatResponse (BaseModel ):
    reply :str 
    status :str ="success"


DEFAULT_SYSTEM_PROMPT ="""You are an elite Business Strategy Advisor.
CRITICAL INSTRUCTION:
- Never refer to yourself as ChatGPT, OpenAI, or any external AI model name.
- Do NOT use generic intro greetings like "I'm ChatGPT" or "As an AI".
- Jump straight into sharp, actionable, structured strategic insights.

Your objective is to provide high-caliber, practical, and highly structured strategic advice to entrepreneurs, founders, and business leaders.

When answering:
1. Provide actionable, data-driven frameworks (e.g., TAM/SAM/SOM, CAC/LTV, Lean Canvas, Unit Economics, GTM playbooks).
2. Keep explanations crystal clear, professional, structured with concise headings, bullet points, and high-impact takeaways.
3. If relevant, highlight potential risks, competitive advantages (moats), and next actionable steps.
4. Format all responses in clean, readable Markdown.
"""

SUGGESTIONS =[
"Evaluate my SaaS idea",
"Calculate CAC vs LTV",
"Zero-budget GTM hacks",
"Angel investor checklist",
"Defensible market moat"
]


@router .get ("/suggestions")
async def get_suggestions ():
    return {"suggestions":SUGGESTIONS }


@router .post ("",response_model =ChatResponse )
async def chat_endpoint (request :ChatRequest ):
    user_msg =request .message .strip ()
    if not user_msg :
        raise HTTPException (status_code =400 ,detail ="Message cannot be empty.")

    api_key =settings .groq_api_key 


    messages =[{"role":"system","content":DEFAULT_SYSTEM_PROMPT }]


    if request .context :
        ctx_str =", ".join ([f"{k }: {v }"for k ,v in request .context .items ()if v ])
        if ctx_str :
            messages .append ({
            "role":"system",
            "content":f"Context regarding the user's business idea: {ctx_str }"
            })


    if request .history :
        for msg in request .history [-8 :]:
            if msg .role in ["user","assistant"]:
                messages .append ({"role":msg .role ,"content":msg .content })


    messages .append ({"role":"user","content":user_msg })


    if not api_key :

        fallback_reply =(
        f"**Strategy Advisor Note:** Groq API key is not currently detected in `.env`.\n\n"
        f"Here is initial strategic feedback for **'{user_msg }'**:\n"
        f"- **Value Proposition:** Ensure your core offering solves a hair-on-fire pain point with 10x ROI for users.\n"
        f"- **Target Market:** Pinpoint a tight beachhead segment before expanding horizontally.\n"
        f"- **Unit Economics:** Aim for an LTV/CAC ratio of >= 3.0x with < 12 months payback period.\n"
        f"- **Next Step:** Add your `GROQ_API_KEY` to `.env` to unlock live deep multi-turn AI consultations!"
        )
        return ChatResponse (reply =fallback_reply ,status ="offline_fallback")


    if api_key .startswith ("gsk_"):
        url ="https://api.groq.com/openai/v1/chat/completions"
        model =settings .groq_model or "openai/gpt-oss-120b"
    else :
        url ="https://api.x.ai/v1/chat/completions"
        model ="grok-beta"

    headers ={
    "Authorization":f"Bearer {api_key }",
    "Content-Type":"application/json"
    }

    payload ={
    "model":model ,
    "messages":messages ,
    "temperature":0.5 ,
    "max_tokens":3500 
    }


    for attempt in range (4 ):
        try :
            if attempt >=1 and "openai/gpt-oss-120b"in model and "groq.com"in url :
                payload ["model"]="openai/gpt-oss-20b"

            async with httpx .AsyncClient (timeout =45.0 )as client :
                resp =await client .post (url ,headers =headers ,json =payload )

                if resp .status_code ==429 and attempt <3 :
                    await asyncio .sleep (2.0 *(attempt +1 ))
                    continue 

                resp .raise_for_status ()
                data =resp .json ()
                reply_text =data ["choices"][0 ]["message"]["content"].strip ()


                import re 
                reply_text =re .sub (r"^(?:I(?:'m| am) (?:ChatGPT|an AI|your elite AI)[^\n\.\!]*[\n\.\!]\s*)+","",reply_text ,flags =re .IGNORECASE ).strip ()
                return ChatResponse (reply =reply_text ,status ="success")

        except httpx .HTTPStatusError as e :
            if e .response .status_code ==429 and attempt <3 :
                await asyncio .sleep (2.0 *(attempt +1 ))
                continue 
            logger .error (f"Chat API HTTP error: {e }")
            raise HTTPException (status_code =502 ,detail =f"LLM Provider Error: {str (e )}")
        except Exception as e :
            logger .error (f"Chat error: {e }")
            if attempt >=3 :
                raise HTTPException (status_code =500 ,detail =f"Chat generation failed: {str (e )}")
            await asyncio .sleep (1.5 )

    raise HTTPException (status_code =500 ,detail ="Failed to retrieve AI consultant response.")
