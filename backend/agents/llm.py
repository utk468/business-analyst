# pyrefly: ignore [missing-import]
import httpx
import logging
from backend.config import settings

logger = logging.getLogger("startup_consultant.llm")




async def call_grok(prompt: str, system_message: str = "You are a professional business consultant.") -> str:


    if not settings.groq_api_key:
        raise ValueError("API Key not configured in .env file")
        
    api_key = settings.groq_api_key
    
    # Auto-detect Groq vs xAI Grok
    if api_key.startswith("gsk_"):
        url = "https://api.groq.com/openai/v1/chat/completions"
        model = "llama-3.3-70b-versatile"
        logger.info("Groq key detected (starts with gsk_). Routing to Groq endpoint with Llama 3.3.")
    else:
        url = "https://api.x.ai/v1/chat/completions"
        model = "grok-beta"
        logger.info("xAI key detected. Routing to Grok endpoint.")
        

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }


    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }
    


    async with httpx.AsyncClient(timeout=20.0) as client:
        
        response = await client.post(url, headers=headers, json=payload)

        response.raise_for_status()
        
        result_json = response.json()
        
        content = result_json["choices"][0]["message"]["content"]
        
        content = content.strip()

        if content.startswith("```json"):
            content = content[7:]

        if content.endswith("```"):
            content = content[:-3]

        return content.strip()
