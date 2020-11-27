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


pressure=""
temperature=""
illuminance=""
solidMoisture=""

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
        global pressure, temperature,illuminance, solidMoisture
        data = data.decode(encoding='utf-8').split(":")
        if(data[0] =="pressure"):
          pressure =data[1]
        elif(data[0]=="temp"):
          temperature =data[1]
        elif(data[0] =="illuminance"):
          illuminance =data[1]
        elif(data[0]=="solid"):
          solidMoisture =data[1]


# TODO: メインの API サーバーから,ユーザーID, デバイスID 情報をもとにユーザー情報を取得するようにする


def main(): 
    try:
      peri = bluepy.btle.Peripheral()
      peri.connect(DEVICE_ADDRESS, bluepy.btle.ADDR_TYPE_PUBLIC)
      peri.withDelegate(MyDelegate(bluepy.btle.DefaultDelegate))
      
      nowDatetime = datetime.datetime.now()
      createdAt = nowDatetime.strftime('%Y/%m/%d-%H:%M:%S')
      while(pressure=="" or temperature=="" or illuminance =="" or solidMoisture==""):
          if peri.waitForNotifications(1.0):
              continue
      
    except Exception as e:
      logging.error(e)
      peri.disconnect()
    
    peri.disconnect()
    print(nowDatetime)
    print("データの取得完了")

    # TODO: humidity について、デバイスに接続して値を取得する必要がある
    device_db.child(SERVICE_UUID).child(PHONE_UDID).set({
      "createdAt":createdAt,
      "cultivationId":"xxxxxx",
      "humidity":{
        "value":"80",
      },
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
    # TODO:　ラズパイから Firebase に直接データを送信するようにして
    # getData = requests.post(BASE_URL)
    # print(getData)

if __name__ == "__main__":
    main()
