
import httpx 
import logging 
import re 
import asyncio 
import random 
from backend .config import settings 

logger =logging .getLogger ("startup_consultant.llm")


_LLM_SEMAPHORE =asyncio .Semaphore (2 )
_FALLBACK_MODEL ="openai/gpt-oss-20b"


def _extract_retry_after (response :httpx .Response ,attempt :int )->float :
    """Extract wait time from response headers or message body."""

    retry_header =response .headers .get ("retry-after")
    if retry_header :
        try :
            return float (retry_header )+0.5 
        except (ValueError ,TypeError ):
            pass 


    try :
        match =re .search (r"try again in ([\d\.]+)s",response .text ,re .IGNORECASE )
        if match :
            return float (match .group (1 ))+0.75 
    except Exception :
        pass 


    base_wait =min (30.0 ,(2 **attempt )*2.5 )
    return base_wait +random .uniform (0.2 ,1.0 )


async def _execute_chat_request (url :str ,headers :dict ,payload :dict ,retries :int =6 )->str :
    current_payload =dict (payload )

    for attempt in range (retries ):
        try :

            if attempt >=2 and current_payload .get ("model")!=_FALLBACK_MODEL and "groq.com"in url :
                original_model =current_payload .get ("model")
                current_payload ["model"]=_FALLBACK_MODEL 
                logger .info (f"Switching from {original_model } to {_FALLBACK_MODEL } to avoid Groq TPM limits.")

            async with httpx .AsyncClient (timeout =60.0 )as client :
                response =await client .post (url ,headers =headers ,json =current_payload )

                if response .status_code ==429 :
                    wait_time =_extract_retry_after (response ,attempt )
                    logger .warning (
                    f"Rate limited (429) by Groq on {current_payload .get ('model')}. "
                    f"Retrying in {wait_time :.1f}s (attempt {attempt +1 }/{retries })..."
                    )
                    await asyncio .sleep (wait_time )
                    continue 

                response .raise_for_status ()

                result_json =response .json ()
                content =result_json ["choices"][0 ]["message"]["content"]

                content =content .strip ()


                if "```json"in content :
                    content =content .split ("```json",1 )[1 ].split ("```",1 )[0 ]
                elif "```"in content :
                    content =content .split ("```",1 )[1 ].split ("```",1 )[0 ]

                content =content .strip ()


                json_match =re .search (r'(\{.*\}|\[.*\])',content ,re .DOTALL )
                if json_match :
                    content =json_match .group (0 ).strip ()

                return content 

        except httpx .HTTPStatusError as e :
            if e .response .status_code ==429 and attempt <retries -1 :
                wait_time =_extract_retry_after (e .response ,attempt )
                logger .warning (f"Rate limited (429) on attempt {attempt +1 }. Retrying in {wait_time :.1f}s...")
                await asyncio .sleep (wait_time )
                continue 
            raise e 
        except Exception as e :
            if attempt <retries -1 :
                wait_time =(attempt +1 )*1.5 +random .uniform (0.1 ,0.5 )
                logger .warning (f"Request error: {e }. Retrying in {wait_time :.1f}s...")
                await asyncio .sleep (wait_time )
                continue 
            raise e 

    raise RuntimeError ("Exceeded maximum retries for Groq API call. Rate limits were consistently reached.")


async def call_grok (prompt :str ,system_message :str ="You are a professional business consultant.")->str :
    if not settings .groq_api_key :
        raise ValueError ("API Key not configured in .env file")

    api_key =settings .groq_api_key 


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
    "messages":[
    {"role":"system","content":f"{system_message } You MUST reply ONLY with valid, parseable JSON matching the required structure without any markdown commentary outside the JSON block."},
    {"role":"user","content":prompt }
    ],
    "temperature":0.2 
    }

    async with _LLM_SEMAPHORE :

        await asyncio .sleep (0.5 )
        return await _execute_chat_request (url ,headers ,payload )
