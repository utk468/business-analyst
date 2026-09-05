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
        self .storage_type ="MongoDB"
        self .is_connected =False 

    async def connect (self ):
        try :
            self .client =AsyncIOMotorClient (
            settings .mongodb_url ,
            serverSelectionTimeoutMS =2500 
            )
            await self .client .admin .command ('ping')
            self .db =self .client [settings .database_name ]
            self .is_connected =True 
            logger .info ("Successfully connected to MongoDB.")
        except Exception as e :
            self .is_connected =False 
            logger .error (f"Failed to connect to MongoDB: {e }")
            raise e 

    async def save_report (self ,report :Dict [str ,Any ])->str :

        if "id"not in report and "_id"not in report :
            report ["id"]=str (uuid .uuid4 ())
        elif "_id"in report and "id"not in report :
            report ["id"]=str (report ["_id"])

        report ["created_at"]=datetime .utcnow ().isoformat ()

        mongo_report =report .copy ()
        if "id"in mongo_report :
            mongo_report ["_id"]=mongo_report ["id"]

        await self .db .reports .replace_one (
        {"_id":mongo_report ["_id"]},
        mongo_report ,
        upsert =True 
        )
        return str (mongo_report ["_id"])

    async def get_reports (self )->List [Dict [str ,Any ]]:
        cursor =self .db .reports .find ().sort ("created_at",-1 )
        reports =[]
        async for doc in cursor :
            doc ["id"]=str (doc .get ("_id"))
            if "_id"in doc :
                del doc ["_id"]
            reports .append (doc )
        return reports 

    async def get_report (self ,report_id :str )->Optional [Dict [str ,Any ]]:
        doc =await self .db .reports .find_one ({"_id":report_id })
        if not doc :
            doc =await self .db .reports .find_one ({"id":report_id })
        if doc :
            doc ["id"]=str (doc .get ("_id",doc .get ("id")))
            if "_id"in doc :
                del doc ["_id"]
            return doc 
        return None 

    async def delete_report (self ,report_id :str )->bool :
        result =await self .db .reports .delete_one ({"_id":report_id })
        return result .deleted_count >0 


db =Database ()
