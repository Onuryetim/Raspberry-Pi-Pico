## Raspberry Pi Pico - HC05 Röle Led Kontrol
## Written By Onur

from machine import UART, Pin

rxData = bytes()

uart = UART(0, baudrate = 9600, tx=Pin(0), rx=Pin(1))
in1 = Pin(3, Pin.OUT)
in2 = Pin(6, Pin.OUT)


in1.value(1) 
in2.value(1) 

uart.write("Haberleşme Sağlandı.")


while True:
    if uart.any() > 0:
        rxData = uart.read(1);
        
        if "0" in rxData:
               uart.write("Led 1 Açıldı")
               print("Led 1 Açıldı")
               in1.value(0)
               in2.value(1)
               
               
        elif "1" in rxData:
               uart.write("Led 2 Açıldı")
               print("Led 2 Açıldı")
               in1.value(1)
               in2.value(0)
               
        if "2" in rxData:
               uart.write("Led 1 ve Led 2 açıldı")
               print("Led 1 ve Led 2 açıldı")
               in1.value(0)
               in2.value(0)
               
               
        elif "3" in rxData:
               uart.write("Led 1 ve Led 2 kapandı")
               print("Led 1 ve Led 2 kapandı")
               in1.value(1)
               in2.value(1)
 