import discord
import asyncio
import logging
import os,sys

client = discord.client()
loop = asyncio.get_event_loop()


async def startup_data():
    try:
        loop.run_until_complete(client.start("NzgwNTExMTg1Njc3ODQ0NTcw.X7wJrw.SttcbuyLPT6SXkx4Rq6p2JjFd_8"))
    except KeyboardInterrupt:
        loop.run_until_complete(client.logout())
        # cancel all tasks lingering
    finally:
        loop.close()

async def sendMessage(message:str):
    
    logging.info(message)


