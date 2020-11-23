from fastapi import APIRouter
from bluetooth.ble import *

router= APIRouter()

@router.get("/")
async def findAllSensors():
    return ""


@router.get("/:deviceId")
async def findOneSensorByDeviceId():
    return ""

@router.post("/:deviceId")
async def registerSensor():
    return ""

@router.put("/:deviceId")
async def updateSensor():
    return ""

