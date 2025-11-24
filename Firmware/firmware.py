
from machine import Pin
import time

# Initialize GPIO 25 as an output pin
led = Pin(25, Pin.OUT)

while True:
    led.value(1)      # Turn LED ON
    time.sleep(0.5)   # Wait for 0.5 seconds
    led.value(0)      # Turn LED OFF
