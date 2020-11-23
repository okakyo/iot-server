import bluepy
import binascii

HANDLE_A_BUTTON = 0x002a
devadr = "30:ae:a4:ee:8d:66"   # 実際にはmicro:bit のアドレスを記述

exflag = False

pressure=""
temperature=""
illuminance=""
solidMoisture=""


class MyDelegate(bluepy.btle.DefaultDelegate):
    def __init__(self, params):
        bluepy.btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        global pressure, temperature,illuminance, solidMoisture
        data = str(data).replace("'","")
        if(cHandle ==42):
          pressure =data.split(":")[1]
        elif(cHandle ==45):
          temperature =data.split(":")[1]
        elif(cHandle ==47):
          illuminance =data.split(":")[1]
        elif(cHandle ==49):
          solidMoisture =data.split(":")[1]

def main():
    peri = bluepy.btle.Peripheral()
    peri.connect(devadr, bluepy.btle.ADDR_TYPE_PUBLIC)
    peri.withDelegate(MyDelegate(bluepy.btle.DefaultDelegate))

    
    while(pressure=="" or temperature=="" or illuminance =="" or solidMoisture==""):
        if peri.waitForNotifications(1.0):
            continue
    print("全データを取得")
    print(pressure)
    print(temperature)
    print(illuminance)
    print(solidMoisture)

    peri.disconnect()

if __name__ == "__main__":
    main()
