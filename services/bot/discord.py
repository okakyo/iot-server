import discord 
from fastapi import APIRouter
import asyncio

router = APIRouter()
client = discord.client()

@router.on_event("startup")
async def startup_event():
    asyncio.create_task(client.start("token"))

