import time
from machine import Pin

pin = Pin("LED", Pin.OUT)

 # Wait for USB to become ready

while True:
    pin.on()
    print("Hello, Pi Pico!")
    time.sleep(1)
    pin.off()
    time.sleep(1)