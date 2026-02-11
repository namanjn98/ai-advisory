import asyncio
import time
from typing import Dict, List, Any

import httpx

from .config import OPENROUTER_BASE_URL


async def query_model(
    model_id: str,
    model_name: str,
    messages: List[Dict[str, str]],
    token: str,
    timeout: int = 60,
) -> Dict[str, Any]:
    """Query a single model via OpenRouter API."""
    start = time.time()

    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.post(
                OPENROUTER_BASE_URL,
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": model_id,
                    "messages": messages,
                },
            )
            response.raise_for_status()
            data = response.json()

            elapsed = time.time() - start
            return {
                "success": True,
                "name": model_name,
                "id": model_id,
                "content": data["choices"][0]["message"]["content"],
                "elapsed": elapsed,
            }

    except httpx.TimeoutException:
        return {
            "success": False,
            "name": model_name,
            "id": model_id,
            "error": "Request timed out",
            "elapsed": time.time() - start,
        }
    except httpx.HTTPStatusError as e:
        return {
            "success": False,
            "name": model_name,
            "id": model_id,
            "error": f"HTTP {e.response.status_code}: {e.response.text}",
            "elapsed": time.time() - start,
        }
    except Exception as e:
        return {
            "success": False,
            "name": model_name,
            "id": model_id,
            "error": str(e),
            "elapsed": time.time() - start,
        }


async def query_all_models(
    models: List[Dict[str, str]],
    messages: List[Dict[str, str]],
    token: str,
) -> List[Dict[str, Any]]:
    """Query all models concurrently."""
    tasks = [
        query_model(
            model_id=model["id"],
            model_name=model["name"],
            messages=messages,
            token=token,
        )
        for model in models
    ]
    return await asyncio.gather(*tasks)
