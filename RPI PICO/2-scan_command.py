from machine import UART
import time

scan_command = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x02, 0x01 # Enable 0x01 and Disable 0x00
               ,0xAB, 0xCD])

# Set up serial communication
serial = UART(0,baudrate=9600)

serial.write(scan_command)
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