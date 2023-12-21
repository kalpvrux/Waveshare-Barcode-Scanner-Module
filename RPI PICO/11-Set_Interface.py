from machine import UART
import time

# Set up serial communication
serial = UART(0,baudrate=9600)

# Set_Interface
UART_Output = 0x00
USB_Output = 0x01
USB_Virtual_Port = 0x03

Set_Interface = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x0D, UART_Output, 0xAB, 0xCD])
SAVE_TO_FLASH = bytes([0x7E, 0x00, 0x09, 0x01, 0x00, 0x00, 0x00, 0xDE, 0xC8])

serial.write(Set_Interface)
time.sleep(0.1)  # Add a delay between commands
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