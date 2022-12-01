from machine import Pin
from machine import UART                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
from machine import PWM
import time


led = Pin(25, Pin.OUT)
#asignamos una variable al led de la raspberry. 
uart = UART(0,9600)
#variable con los baudios que va a trabajar el modulo Bluetooth HC-05.
In1=Pin(14,Pin.OUT) 
In2=Pin(13,Pin.OUT)
In3=Pin(12,Pin.OUT)  
In4=Pin(11,Pin.OUT)
#variables In1 y In2 controlan el sentido de giro del motor A y In3 y In4 el del motor B.
EN_B= machine.PWM (machine.Pin(27))
EN_A= machine.PWM (machine.Pin(26))
#variables que regulan el pwm del motor A y B respectivamente.
EN_A.freq(10000)
EN_B.freq(10000)
#frecuencia con la que va a trabajar.
EN_A.duty_u16(65025)
EN_B.duty_u16(65025)
#velocidad maxima con la que va a trabajar los motores.
led.value(1)
#el led de la raspberry usado como indicador si la raspberry esta alimentada y el programa corriendo.
def forward():
    #funcion para que el robot se mueva hacia adelante.
    EN_B.duty_u16(65025)
    EN_A.duty_u16(65025)
    In1.value(1)
    In2.value(0)
    In3.value(0)
    In4.value(1)
    
def backward():
    #funcion para que el robot se mueva hacia atras.
    EN_B.duty_u16(65025)
    EN_A.duty_u16(65025)
    In1.value(0)
    In2.value(1)
    In3.value(1)
    In4.value(0)

def right():
    #funcion para que el robot se mueva hacia la derecha.
    EN_B.duty_u16(65025)
    EN_A.duty_u16(65025)
    In1.value(0)
    In2.value(1)
    In3.value(0)
    In4.value(1)

def left():
    #funcion para que el robot se mueva hacia la izquierda.
    EN_B.duty_u16(65025)
    EN_A.duty_u16(65025)    
    In1.value(1)
    In2.value(0)
    In3.value(1)
    In4.value(0)


def d1():
    #funcion para que el robot se mueva de forma diagonal hacia la derecha.
    EN_A.duty_u16(65025)
    EN_B.duty_u16(45025)
    In1.value(1)
    In2.value(0)
    In3.value(0)
    In4.value(1)
    


def d2():
    #funcion para que el robot se mueva de forma diagonal hacia la derecha, pero hacia atras.
    EN_A.duty_u16(65025)
    EN_B.duty_u16(45025)
    In1.value(0)
    In2.value(1)
    In3.value(1)
    In4.value(0)

def d3():
    #funcion para que el robot se mueva de forma diagonal hacia la izquierda.
    EN_B.duty_u16(65025)
    EN_A.duty_u16(45025)
    In1.value(1)
    In2.value(0)
    In3.value(0)
    In4.value(1)

def d4():
    #funcion para que el robot se mueva de forma diagonal hacia la izquierda, pero hacia atras.
    EN_B.duty_u16(65025)
    EN_A.duty_u16(45025)
    In1.value(0)
    In2.value(1)
    In3.value(1)
    In4.value(0)

    
while True:
        data = ""
        if uart.any()> 0: #comprobando si esta llegando informacion desde el Hc-05 a la raspberry
            data = uart.readline(1) #obtiene la informacion y la almacena en la variable data
            data = str(data) #convierte la informacion de bytes a formato str
            print (data)
        #ahora usando la aplicacion BLE arduino car conectada al Hc-05 se mandaran 9 datos
        #posibles, dependiendo la tecla que se toque en la app, los datos son: F B R L I J G H S
        # estos son los que se guardaran en la variale data.
        #el programa entrara al if o al elif el cual tenga como condicion que en data se encuentre
        #uno de estos valores.
        if("F" in data):
            print("Move forward")
            #si el valor de data es igual a F el programa entra en la funcion forward()
            forward()
        elif("B" in data):
            #si el valor de data es igual a B el programa entra en la funcion backward()
            print("Move backwards")           
            backward()
        elif("R" in data):
            #si el valor de data es igual a R el programa entra en la funcion right()
            print("Turn right")           
            right()
        elif("L" in data):
            #si el valor de data es igual a L el programa entra en la funcion left()
            print("Turn left")   
            left()
        elif("I" in data):
            #si el valor de data es igual a I el programa entra en la funcion d1()
            print("diagonal arriba derecha")
            d1()
        elif("J" in data):
            #si el valor de data es igual a J el programa entra en la funcion d2()
            print("diagonal abajo derecha")
            d2()
        elif("G" in data):
            #si el valor de data es igual a G el programa entra en la funcion d3()
            print("diagonal arriba izquierda")
            d3()
        elif("H" in data):
            #si el valor de data es igual a H el programa entra en la funcion d4()
            print("diagonal abajo izquierda")
            d4()
            
        elif ('S' in data):
            #si el valor de data es igual a S el programa le asignara a los In el valor 0
            # lo que parará los motores.
            print("Stop")
            In1.value(0)
            In2.value(0)
            In3.value(0)
            In4.value(0)
