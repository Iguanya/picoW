import network
import ubinascii

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.config(pm = 0xa11140)
status = wlan.ifconfig()
mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()


# Other things you can query
print(mac)
print(wlan.config('channel'))
print(wlan.config('essid'))
print(wlan.config('txpower'))
print('connected')
print(wlan.ifconfig())
print( 'ip = ' + status[0] )