import serial
import time

# Set up serial communication
serial = serial.Serial('/dev/ttyS0', 9600) #connect Rx pin to GPIO14 and Tx pin to GPIO15

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
    data = serial.readline()

    # If there is data, print it to the console
    if data:
        print(data)

    time.sleep(1)
#--------------------------------------------