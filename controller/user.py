from fastapi import APIRouter
from bluetooth.ble import *

router= APIRouter()

@router.get("/")
async def chat():
    return ""