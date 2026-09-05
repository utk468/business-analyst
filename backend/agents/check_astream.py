import asyncio 
import sys 

sys .path .append (r'c:\Users\ASUS\Desktop\BUSINESS_ANALYSIS')

from backend .agents .graph import graph 

async def main ():
    state ={
    "startup_idea":"SaaS for micro-SaaS marketing",
    "industry":"Marketing Tech",
    "country":"United States",
    "target_audience":"Micro-SaaS Founders",
    "budget":"$1000/mo",
    "business_stage":"Idea",
    "additional_information":"None",
    "current_agent":"Initiator",
    "progress":0 ,
    "logs":[]
    }
    print ("Invoking graph...")
    try :
        async for output in graph .astream (state ):
            print ("Received raw output:",type (output ),repr (output ))
    except Exception as e :
        import traceback 
        traceback .print_exc ()

if __name__ =="__main__":
    asyncio .run (main ())
