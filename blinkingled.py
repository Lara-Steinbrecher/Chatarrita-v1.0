from machine import Pin
import time

led = Pin(25, Pin.OUT)

while True:
    led.on()
    time.sleep_ms(500)
    led.off()
    time.sleep_ms(500)
