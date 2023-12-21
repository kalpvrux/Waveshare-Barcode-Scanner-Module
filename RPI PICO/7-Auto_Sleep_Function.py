from machine import UART
import time

# Set up serial communication
serial = UART(0,baudrate=9600)

# Auto_Sleep_Function
On = 0x80
Off = 0x00
Idle_time = 0x7F #  0x00 - 0x7F : (unit：100ms) for address 0x0007  And  0x00 - 0xFF : (unit：100ms) for address 0x0008

Auto_Sleep_Function = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x07, On + Idle_time, 0xAB, 0xCD])

serial.write(Auto_Sleep_Function)
time.sleep(0.1)  # Add a delay between commands
    
# Read data from the Barcode Scanner Module:
while True:
    # Read data from the UART
    data = serial.read()

    # If there is data, print it to the console
    if data:
        print(data)

    time.sleep(1)
#--------------------------------------------