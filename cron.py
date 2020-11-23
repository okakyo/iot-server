import bluepy
import binascii

HANDLE_A_BUTTON = 0x002a
devadr = "30:ae:a4:ee:8d:66"   # 実際にはmicro:bit のアドレスを記述

exflag = False

class MyDelegate(bluepy.btle.DefaultDelegate):
    def __init__(self, params):
        bluepy.btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        global exflag
        print(data)

def main():
    peri = bluepy.btle.Peripheral()
    peri.connect(devadr, bluepy.btle.ADDR_TYPE_PUBLIC)
    peri.withDelegate(MyDelegate(bluepy.btle.DefaultDelegate))

    # ボタン notify を要求
    peri.writeCharacteristic(HANDLE_A_BUTTON + 1, b'\x01\x00')

    print( "Notification を待機。A or B ボタン長押しでプログラム終了")
    while exflag == False:
        if peri.waitForNotifications(1.0):
            continue
    peri.disconnect()

if __name__ == "__main__":
    main()
