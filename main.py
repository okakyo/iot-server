from fastapi import FastAPI,Header
import uvicorn
import RPi.GPIO as GPIO


# 以下:ここに実装デバイス接続を行う(Global 変数)


SENSOR1-OUTPUT = 10
SENSOR1-INPUT =11 


SENSOR2-OUTPUT = 12
SENSOR2-INPUT =13



GPIO.setmode(GPIO.BCM)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(2,GPIO.IN)


app = FastAPI()




@app.get("/")
async def hello():
  return  "Hello World"


# ここにIoT データを送信するための実装を行う

@app.post("/sensor/check")
async def send_info(): 
  cultivation_id="0123"
  return {
      "cultivation_id":cultivation_id,    
      "pressure":"101300",    
      "hunudity":67,    
      "temperature":"32",    
      "illuminance":40,
      "soil_moisture":50,
    }

if __name__=="__main__":
    uvicorn.run(app)
