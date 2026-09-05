import logging 
import asyncio 
import warnings 
from typing import List ,Dict ,Any ,Optional 

warnings .filterwarnings ("ignore")


from duckduckgo_search import DDGS 

logger =logging .getLogger ("startup_consultant.search")


INTELLIGENCE_SOURCES ={
"tracxn":{
"name":"Tracxn",
"domain":"tracxn.com",
"description":"Funding rounds, sectors, startups, investors, and founder intelligence"
},
"startup_india":{
"name":"Startup India (DPIIT)",
"domain":"startupindia.gov.in",
"description":"Official DPIIT-recognized startups, government schemes, and state hub data"
},
"crunchbase":{
"name":"Crunchbase",
"domain":"crunchbase.com",
"description":"Global venture funding rounds, investors, and company profiles"
},
"inc42":{
"name":"Inc42 DataLabs",
"domain":"inc42.com",
"description":"Startup tracking, funding deals, and company intelligence"
},
"data_gov_in":{
"name":"Open Government Data (Data.gov.in)",
"domain":"data.gov.in",
"description":"Official government open datasets, economic statistics, and industry registers"
}
}


def _run_ddg_search (query :str ,max_results :int )->list :
    """
    Synchronous worker function to execute the DDG search with fast timeout.
    """
    try :
        with DDGS (timeout =3.0 )as ddgs :
            return list (ddgs .text (query ,max_results =max_results ))
    except Exception as e :
        logger .debug (f"DDG query failed for '{query }': {e }")
        return []


async def search_web (query :str ,max_results :int =3 )->str :
    """
    Asynchronously search the web.
    """
    try :
        results =await asyncio .wait_for (
        asyncio .to_thread (_run_ddg_search ,query ,max_results ),
        timeout =3.5 
        )

        if not results :
            return ""

        search_str =""
        for i ,r in enumerate (results ):
            search_str +=f"{i +1 }. Title: {r .get ('title')}\nURL: {r .get ('href')}\nSnippet: {r .get ('body')}\n\n"

        return search_str 

    except Exception as e :
        logger .warning (f"Search error/timeout: {e }")
        return ""


async def search_source (source_key :str ,industry :str ,country :str ,query :str ,max_results :int =2 )->str :
    """
    Search a specific platform with live DuckDuckGo query.
    """
    source_info =INTELLIGENCE_SOURCES .get (source_key )
    if not source_info :
        return await search_web (query ,max_results )

    name =source_info ["name"]
    domain =source_info ["domain"]
    targeted_query =f"site:{domain } {industry } {country }"

    try :
        results =await asyncio .wait_for (
        asyncio .to_thread (_run_ddg_search ,targeted_query ,max_results ),
        timeout =3.0 
        )

        if not results :
            return ""

        formatted =f"=== Source: {name } ({domain }) ===\n"
        for i ,r in enumerate (results ):
            formatted +=f"[{i +1 }] {r .get ('title')}\nURL: {r .get ('href')}\nData Snippet: {r .get ('body')}\n\n"

        return formatted 

    except Exception as e :
        logger .warning (f"Source search failed for {source_key }: {e }")
        return ""


async def search_multi_source_intelligence (
industry :str ,
country :str ,
topic :str ="market competitors funding",
preferred_sources :Optional [List [str ]]=None ,
max_results_per_source :int =2 
)->str :
    """
    Aggregates live data across Tracxn, Crunchbase, Startup India, Inc42, and Data.gov.in.
    """
    if not preferred_sources :
        is_india =any (k in (country or "").lower ()for k in ["india","bharat","delhi","bangalore","mumbai","in"])
        if is_india :
            preferred_sources =["tracxn","startup_india","crunchbase","inc42","data_gov_in"]
        else :
            preferred_sources =["crunchbase","tracxn","data_gov_in"]

    tasks =[]
    for src in preferred_sources :
        q =f"{industry } {topic } {country }"
        tasks .append (search_source (src ,industry ,country ,q ,max_results =max_results_per_source ))

    try :
        results =await asyncio .wait_for (
        asyncio .gather (*tasks ,return_exceptions =True ),
        timeout =4.0 
        )
    except Exception as e :
        logger .warning (f"Multi-source intelligence gather timed out: {e }")
        results =[]

    aggregated_intelligence ="### Live Intelligence Ingested from Multi-Source Datasets:\n\n"
    has_results =False 
    for r in results :
        if isinstance (r ,str )and r .strip ():
            aggregated_intelligence +=r +"\n---\n\n"
            has_results =True 

    if not has_results :
        return ""

    return aggregated_intelligence 
