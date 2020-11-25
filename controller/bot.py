import discord 
from fastapi import APIRouter
import asyncio
import logging
from services.bot import discord

router = APIRouter()

"""
- センサーより取得したデータを送信する
"""
@router.get("/sensor")
async def sendData():
    try:
        print("Done")
    except Exception as e:
        logging.error(e)

    return ""

"""
- Discord より入力されたコマンドをもとにラズパイを操作する

"""
@router.post("/message/push")
async def pushMessage():
    return ""