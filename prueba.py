from machine import Pin
from machine import UART
from machine import PWM
import time

led = Pin(25, Pin.OUT)

uart = UART(0,9600)

In1=Pin(14,Pin.OUT) 
In2=Pin(13,Pin.OUT)
In3=Pin(12,Pin.OUT)  
In4=Pin(11,Pin.OUT)
EN_A= Pin(8, Pin.OUT)
EN_B= Pin(9, Pin.OUT)
EN_B.value(1)
EN_A.value(1)
print ("a")

while True:
    In1.value(1)
    In3.value(1)
