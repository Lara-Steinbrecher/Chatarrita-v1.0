from machine import Pin
from machine import UART
from machine import PWM
import time

led = Pin(25, Pin.OUT)

uart = UART(0,9600)

In1=Pin(16,Pin.OUT) 
In2=Pin(17,Pin.OUT)
In3=Pin(18,Pin.OUT)  
In4=Pin(19,Pin.OUT)
EN_A= PWM (Pin(14))
EN_B= PWM (Pin(15))
EN_A.freq(1500)
EN_B.freq(1500)
EN_A.duty_u16(65025)
EN_B.duty_u16(65025)

while True:
        data = ""
        if uart.any()> 0: #Checking if data available
            data = uart.readline(1)
            data = str(data)#Getting data
             #Converting bytes to str type
            print (data)
        if("F" in data):
            print("Move forward")
            In1.value(1)
            In3.value(1)
        elif("B" in data):
            print("Move backwards")
            In2.value(1)
            In4.value(1)
        elif("R" in data):
            print("Turn right")
            In3.value(1)
        elif("L" in data):
            print("Turn left")
            In1.value(1)
        elif ('S' in data):
            print("Stop")
            In1.value(0)
            In2.value(0)
            In3.value(0)
            In4.value(0)
