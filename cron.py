import bluepy
import requests
import os,sys
import firebase_admin
from firebase_admin import db
from plugins import FirebasePlugin
import datetime
import logging

SERVICE_UUID="4fafc201-1fb5-459e-8fcc-c5c9c331914b"
DEVICE_ADDRESS ="30:ae:a4:ee:8d:66"

PLANT_ID = "xxxxxx"

pressure=""
temperature=""
illuminance=""
solidMoisture=""
humidity=""

firebase_admin.initialize_app(FirebasePlugin,{
  "databaseURL": "https://speak-vegetable.firebaseio.com"
})
device_db = db.reference("/device_data")

# BLE の通信方法: Notify 
# データ受信方法:  devKey:value
# devKey: pressure, temp, illuminance, solid , humid
# value に値を送信する
class MyDelegate(bluepy.btle.DefaultDelegate):
    def __init__(self, params):
        bluepy.btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        global pressure, temperature,illuminance, solidMoisture,humidity
        data = data.decode(encoding='utf-8').split(":")
        if(data[0] =="pressure"):
          pressure =data[1]
          print(pressure)
        elif(data[0]=="temp"):
          temperature =data[1]
          print(temperature)
        elif(data[0] =="illuminance"):
          illuminance =data[1]
          print(illuminance)
        elif(data[0]=="solid"):
          solidMoisture =data[1]
          print(solidMoisture)
        elif(data[0]=="humidity"):
          if (data[1]!="nan"):
            humidity=data[1]
            humidity =int(float(humidity)*100/255)
            print(humidity)
          else :
            print("取得できませんでした")
# TODO: メインの API サーバーから,ユーザーID, デバイスID 情報をもとにユーザー情報を取得するようにする


def main():
    print()
    print("=====================================")
    print()
    print("Start BLE Connection to the IoT Devices!")
    print(datetime.datetime.now())
    print()
    print("=====================================")
    print()
    try:
      peri = bluepy.btle.Peripheral()
      peri.connect(DEVICE_ADDRESS, bluepy.btle.ADDR_TYPE_PUBLIC)
      peri.withDelegate(MyDelegate(bluepy.btle.DefaultDelegate))
      
      nowDatetime = datetime.datetime.now()
      createdAt = nowDatetime.strftime('%Y/%m/%d-%H:%M:%S')
      print("Collecting",end="")
      while(pressure=="" or temperature=="" or illuminance =="" or solidMoisture=="" or humidity==""):
          print(".",end="")
          if peri.waitForNotifications(1.0):
              continue
    except Exception as e:
      logging.error(e)
      peri.disconnect()
    peri.disconnect()
    print()
    print("Collected all sensor data:")
    print()
    print("=====================================")
    print()
    print("Temperature:{}℃".format(temperature))
    print("Humidity:{}%".format(humidity))
    print("Pressure:{}Pa".format(pressure))
    print()
    print("=====================================")
    print("Success in collecting the device data !!!")
    print("Now Updating")
    
    # TODO: humidity について、デバイスに接続して値を取得する必要がある
    device_db.child(SERVICE_UUID).set({
      "createdAt":createdAt,
      "humidity":{
        "value": humidity,
      },
      "plantId":PLANT_ID,
      "pressure":{
       "value": pressure,
       },
      "illuminance":{
        "value":illuminance,
      },
      "solid_moisture":{
        "value":solidMoisture,
      },
      "temperature":{
        "value":temperature,
      }
    })
    print("Done !")

    # TODO:　ラズパイから Firebase に直接データを送信するようにして
if __name__ == "__main__":
    main()
