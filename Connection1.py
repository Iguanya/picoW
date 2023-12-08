import network
import time

ssid = 'BOOST'
password = 'NoTorrent2023!'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)
    print(wlan.ifconfig())
    
# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 1 :
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)
    if wlan.status() != 1:
        raise RuntimeError('network connection failed')
    else:
        print('connected')
        status = wlan.ifconfig()
        print( 'ip = ' + status[0] )