from machine import UART
import time

# Set up serial communication
serial = UART(0,baudrate=9600)

# Setting_code
Close = 0x02  # Close Setting code
Open = 0x00  # Open Setting code
With = 0x01  # Output content of Setting code
Without = 0x00  # Without content of Setting code

Setting_code = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x03, Close + Without, 0xAB, 0xCD])

serial.write(Setting_code)

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