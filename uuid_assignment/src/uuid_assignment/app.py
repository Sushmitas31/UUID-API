import uuid
import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/uuid")
def get_uuid():
    """
    This endpoint generates and returns a version 4 UUID string without delay.
    """
    return {"uuid": str(uuid.uuid4())}


@app.get("/async-uuid")
async def get_async_uuid():
    """
    This endpoint generates and returns a version 4 UUID string with 3 seconds delay in non-blocking way.
    """
    await asyncio.sleep(3)
    return {"uuid": str(uuid.uuid4())}
