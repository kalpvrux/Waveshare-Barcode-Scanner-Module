from machine import UART
import time

# Set up serial communication
serial = UART(0,baudrate=9600)

warning_tone = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x0A, 0x00 # 0x00：Buzzer 0x01-0xFF：Passive buzzer (freq=Value*20) 
                , 0xAB, 0xCD])

serial.write(warning_tone)
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