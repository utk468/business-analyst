import logging 
import uuid 
from datetime import datetime 
from typing import List ,Dict ,Any ,Optional 

from motor .motor_asyncio import AsyncIOMotorClient 
from backend .config import settings 

logger =logging .getLogger ("startup_consultant.database")

class Database :
    def __init__ (self ):
        self .client :Optional [AsyncIOMotorClient ]=None 
        self .db =None 
        self .storage_type ="In-Memory" 
        self .is_connected =False 
        self.in_memory_reports: Dict[str, Dict[str, Any]] = {}

    async def connect (self ):
        url =settings .mongodb_url or "mongodb://localhost:27017"
        try :
            self .client =AsyncIOMotorClient (
            url ,
            serverSelectionTimeoutMS =2500 
            )
            await self .client .admin .command ('ping')
            self .db =self .client [settings .database_name ]
            self .is_connected =True 
            self .storage_type ="MongoDB"
            logger .info ("Successfully connected to MongoDB.")
        except Exception as e :
            self .is_connected =False 
            self .storage_type ="In-Memory"
            logger .warning (f"Failed to connect to MongoDB ({e}). Falling back to in-memory storage.")

    async def save_report (self ,report :Dict [str ,Any ])->str :
        if "id"not in report and "_id"not in report :
            report ["id"]=str (uuid .uuid4 ())
        elif "_id"in report and "id"not in report :
            report ["id"]=str (report ["_id"])

        if "created_at"not in report :
            report ["created_at"]=datetime .utcnow ().isoformat ()

        report_id =str (report .get ("_id")or report .get ("id"))

        if self .is_connected and self .db is not None :
            try :
                mongo_report =report .copy ()
                mongo_report ["_id"]=report_id 
                await self .db .reports .replace_one (
                {"_id":mongo_report ["_id"]},
                mongo_report ,
                upsert =True 
                )
                return report_id 
            except Exception as e :
                logger .error (f"Error saving report to MongoDB: {e}. Falling back to in-memory.")

        self .in_memory_reports [report_id ]=report .copy ()
        return report_id 

    async def get_reports (self )->List [Dict [str ,Any ]]:
        if self .is_connected and self .db is not None :
            try :
                cursor =self .db .reports .find ().sort ("created_at",-1 )
                reports =[]
                async for doc in cursor :
                    doc ["id"]=str (doc .get ("_id"))
                    if "_id"in doc :
                        del doc ["_id"]
                    reports .append (doc )
                return reports 
            except Exception as e :
                logger .error (f"Error fetching reports from MongoDB: {e}")

        reports_list =list (self .in_memory_reports .values ())
        reports_list .sort (key =lambda r :r .get ("created_at",""),reverse =True )
        result =[]
        for r in reports_list :
            doc =r .copy ()
            doc ["id"]=str (doc .get ("_id",doc .get ("id")))
            if "_id"in doc :
                del doc ["_id"]
            result .append (doc )
        return result 

    async def get_report (self ,report_id :str )->Optional [Dict [str ,Any ]]:
        if self .is_connected and self .db is not None :
            try :
                doc =await self .db .reports .find_one ({"_id":report_id })
                if not doc :
                    doc =await self .db .reports .find_one ({"id":report_id })
                if doc :
                    doc ["id"]=str (doc .get ("_id",doc .get ("id")))
                    if "_id"in doc :
                        del doc ["_id"]
                    return doc 
            except Exception as e :
                logger .error (f"Error fetching report {report_id } from MongoDB: {e}")

        doc =self .in_memory_reports .get (report_id )
        if doc :
            doc_copy =doc .copy ()
            doc_copy ["id"]=str (doc_copy .get ("_id",doc_copy .get ("id")))
            if "_id"in doc_copy :
                del doc_copy ["_id"]
            return doc_copy 
        return None 

    async def delete_report (self ,report_id :str )->bool :
        if self .is_connected and self .db is not None :
            try :
                result =await self .db .reports .delete_one ({"_id":report_id })
                if result .deleted_count >0 :
                    return True 
            except Exception as e :
                logger .error (f"Error deleting report {report_id } from MongoDB: {e}")

        if report_id in self .in_memory_reports :
            del self .in_memory_reports [report_id ]
            return True 
        return False 


db =Database ()
