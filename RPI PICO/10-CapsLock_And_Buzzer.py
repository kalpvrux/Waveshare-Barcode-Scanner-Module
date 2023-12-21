from machine import UART
import time

# Set up serial communication
serial = UART(0,baudrate=9600)

# CapsLock_And_Buzzer
Dis = 0x00  # CapsLock Disable
En = 0x02  # CapsLock Enable
High = 0x00  # High for idle and Low for busy
Low = 0x01  # Low for busy and High for idle

CapsLock_And_Buzzer = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x0C, Dis + Low, 0xAB, 0xCD])

serial.write(CapsLock_And_Buzzer)
time.sleep(0.1)  # Add a delay between commands

SAVE_TO_FLASH = bytes([0x7E, 0x00, 0x09, 0x01, 0x00, 0x00, 0x00, 0xDE, 0xC8])
serial.write(SAVE_TO_FLASH)
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