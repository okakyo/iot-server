from fastapi import FastAPI,Header
import uvicorn
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
  return ""


if __name__=="__main__":
    uvicorn.run(app)
