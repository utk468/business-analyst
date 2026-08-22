import os
import json
import logging
import uuid
from datetime import datetime
from typing import List, Dict, Any, Optional
# pyrefly: ignore [missing-import]
from motor.motor_asyncio import AsyncIOMotorClient
from backend.config import settings


logger = logging.getLogger("startup_consultant.database")

class Database:

    def __init__(self):
        self.client = None
        self.db = None
        self.use_fallback = False
        self.fallback_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "db_fallback.json")
        self.storage_type = "MongoDB"
        
    async def connect(self):
        try:
            self.client = AsyncIOMotorClient(
                settings.mongodb_url, 
                serverSelectionTimeoutMS=1500
            )
            
            await self.client.admin.command('ping')
            
            self.db = self.client[settings.database_name]
            self.storage_type = "MongoDB"
            logger.info("Successfully connected to MongoDB.")
            
        except Exception as e:
            logger.warning(f"Failed to connect to MongoDB: {e}. Falling back to local JSON database.")
            self.use_fallback = True
            self.storage_type = "Local File (JSON)"
            if not os.path.exists(self.fallback_file):
                with open(self.fallback_file, "w") as f:
                    json.dump([], f)



    def _read_fallback(self) -> List[Dict[str, Any]]:
        try:
            if os.path.exists(self.fallback_file):
                with open(self.fallback_file, "r") as f:
                    return json.load(f)
        except Exception as e:
            logger.error(f"Error reading fallback file: {e}")
        return []



    def _write_fallback(self, data: List[Dict[str, Any]]):
        try:
            with open(self.fallback_file, "w") as f:
                json.dump(data, f, indent=4, default=str)
        except Exception as e:
            logger.error(f"Error writing to fallback file: {e}")



    async def save_report(self, report: Dict[str, Any]) -> str:

        # Generate id if not exists
        if "id" not in report and "_id" not in report:
            report["id"] = str(uuid.uuid4())
        elif "_id" in report and "id" not in report:
            report["id"] = str(report["_id"])
            
        report["created_at"] = datetime.utcnow().isoformat()
        
        #here if fallback is ture
        if self.use_fallback:
    
            data = self._read_fallback()
            for i, r in enumerate(data):
                if r.get("id") == report["id"]:
                    data[i] = report
                    break
            else:
                data.append(report)
            self._write_fallback(data)
            return report["id"]

        else:
            # For MongoDB, ensure mongo-friendly formats
            mongo_report = report.copy()
            if "id" in mongo_report:
                mongo_report["_id"] = mongo_report["id"]
            
            result = await self.db.reports.replace_one(
                {"_id": mongo_report["_id"]}, 
                mongo_report, 
                upsert=True
            )
            return str(mongo_report["_id"])



    async def get_reports(self) -> List[Dict[str, Any]]:
        if self.use_fallback:
            data = self._read_fallback()
            # Sort by created_at descending
            data.sort(key=lambda x: x.get("created_at", ""), reverse=True)
            return data
        else:
            cursor = self.db.reports.find().sort("created_at", -1)
            reports = []
            async for doc in cursor:
                doc["id"] = str(doc.get("_id"))
                if "_id" in doc:
                    del doc["_id"]
                reports.append(doc)
            return reports



    async def get_report(self, report_id: str) -> Optional[Dict[str, Any]]:
        if self.use_fallback:
            data = self._read_fallback()
            for r in data:
                if r.get("id") == report_id:
                    return r
            return None
        else:
            doc = await self.db.reports.find_one({"_id": report_id})
            if doc:
                doc["id"] = str(doc.get("_id"))
                if "_id" in doc:
                    del doc["_id"]
                return doc
            return None

    async def delete_report(self, report_id: str) -> bool:
        if self.use_fallback:
            data = self._read_fallback()
            initial_len = len(data)
            data = [r for r in data if r.get("id") != report_id]
            if len(data) < initial_len:
                self._write_fallback(data)
                return True
            return False
        else:
            result = await self.db.reports.delete_one({"_id": report_id})
            return result.deleted_count > 0

# Global database instance
db = Database()
