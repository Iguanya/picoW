import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
#wlan.connect('Televic Experience Center', 'televic.001')
wlan.connect('BOOST', 'NoTorrent2023!')

# Make GET request
import urequests
r = urequests.get("http://www.google.com")
print(r.content)
r.close()