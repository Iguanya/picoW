 # Connect to network
import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
#wlan.connect('Wireless Network', 'The Password')
wlan.connect('BOOST', 'NoTorrent2023!')
# Should be connected and have an IP address
wlan.status() # 3 == success
wlan.ifconfig()
status = wlan.ifconfig()
print(wlan.ifconfig())
print( 'ip = ' + status[0] )

# Get IP address for google.com
import socket
ai = socket.getaddrinfo("google.com", 80)
addr = ai[0][-1]

 # Create a socket and make a HTTP request
s = socket.socket()
s.connect(addr)
s.send(b"POST / HTTP/1.0\r\n\r\n")
# Print the response
print(s.recv(512))