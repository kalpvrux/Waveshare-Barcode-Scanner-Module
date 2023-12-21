import serial
import time

# Set up serial communication
serial = serial.Serial('/dev/ttyS0', 9600) #connect Rx pin to GPIO14 and Tx pin to GPIO15

# Keyboard_Setting
US = 0x00
Czech = 0x01
France = 0x02
Germany = 0x03
Hungary = 0x04
Italy = 0x05
Japan = 0x06
Spain = 0x07
Turkey_F = 0x08
Turkey_Q = 0x09

Keyboard_Setting = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x61, US, 0xAB, 0xCD])

SAVE_TO_FLASH = bytes([0x7E, 0x00, 0x09, 0x01, 0x00, 0x00, 0x00, 0xDE, 0xC8])

serial.write(Keyboard_Setting)
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