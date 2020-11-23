import bluepy

scanner = bluepy.btle.Scanner(0)
devices = scanner.scan(3)      # 3秒間スキャンする

for device in devices:
    print('======================================================')
    print('address : %s' % device.addr)
    print('addrType: %s' % device.addrType)
    print('RSSI    : %s' % device.rssi)
    print('Adv data:')
    for (adtype, desc, value) in device.getScanData():
        print(' (%3s) %s : %s ' % (adtype, desc, value))
