import network
import time

ssid = 'Televic Experience Center'
password = 'televic.001'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
#wlan.connect('BOOST', 'NoTorrent2023!')
wlan.connect(ssid, password)

while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)
    print(wlan.ifconfig())