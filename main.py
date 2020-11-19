from fastapi import FastAPI,Header
import uvicorn
import RPi.GPIO as GPIO
import asyncio
import datetime

app = FastAPI()

@app.get("/")
async def hello():
  return  "Hello World"

# ここにIoT データを送信するための実装を行う


"""
PSoC デバイスからデータを取得し、送信する


@return {
  raspi_device_id:string,
  user_id:string,
  datetime: string,
  data:{
    psoc_device_id_key: DeviceData,
  }

"""
@app.post("/sensors/check")
async def send_info(): 
  
  cultivation_id=0

  pressureData = 300
  humidityData = 32
  temperatureData = 50
  illuminanceData = 40
  solidMoistureData = 35
  nowDatetime = datetime.datetime.now()

  return {
    "raspi_device_id":"s-5u2",
    "user_id":"start",
    "datetime":nowDatetime,
    "data":{
        "psoc_device_id-0":{
        "cultivation_id": cultivation_id,
        "pressure":pressureData,
        "humidity":humidityData,
        "illuminance":illuminanceData,
        "solid_moisture":solidMoistureData,
        }
      }
    }


if __name__=="__main__":
    uvicorn.run(app)
