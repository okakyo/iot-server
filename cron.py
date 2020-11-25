import bluepy
import requests
import os,sys
import firebase_admin
from firebase_admin import db
from plugins import FirebasePlugin
devadr = "30:ae:a4:ee:8d:66"   # 実際にはmicro:bit のアドレスを記述
BASE_URL = "https://example.com"

pressure=""
temperature=""
illuminance=""
solidMoisture=""

firebase_admin.initialize_app(FirebasePlugin,{
  "databaseURL": "https://speak-vegetable.firebaseio.com"
})
deviceDb = db.reference("/device_data")

# BLE の通信方法: Notify 
# データ受信方法:  devKey:value
# devKey: pressure, temp, illuminance, solid , humid
# value に値を送信する
class MyDelegate(bluepy.btle.DefaultDelegate):
    def __init__(self, params):
        bluepy.btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        global pressure, temperature,illuminance, solidMoisture
        data = data.decode(encoding='utf-8').replace("'","").split(":")
        if(data[0] =="pressure"):
          pressure =data[1]
        elif(data[0]=="temp"):
          temperature =data[1]
        elif(data[0] =="illuminance"):
          illuminance =data[1]
        elif(data[0]=="solid"):
          solidMoisture =data[1]

def main():
    peri = bluepy.btle.Peripheral()
    charas = peri.getCharacteristics()
    peri.connect(devadr, bluepy.btle.ADDR_TYPE_PUBLIC)
    peri.withDelegate(MyDelegate(bluepy.btle.DefaultDelegate))

    
    while(pressure=="" or temperature=="" or illuminance =="" or solidMoisture==""):
        if peri.waitForNotifications(1.0):
            continue
    print("全データを取得")
    print("気圧:",pressure)
    print("気温:",temperature)
    print("照度:",illuminance)
    print("土壌:",solidMoisture)
    print(charas)
    peri.disconnect()
    
    
    # TODO:　ラズパイから Firebase に直接データを送信するようにして
    # getData = requests.post(BASE_URL)
    # print(getData)

if __name__ == "__main__":
    main()
