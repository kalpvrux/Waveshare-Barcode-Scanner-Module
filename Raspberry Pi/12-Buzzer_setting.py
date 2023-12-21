import serial
import time

# Set up serial communication
serial = serial.Serial('/dev/ttyS0', 9600) #connect Rx pin to GPIO14 and Tx pin to GPIO15

# Buzzer_setting
Dis_music = 0x02  # Disable start music
En_music = 0x00  # Enable start music
Open_T = 0x04  # Open warning tone of decoding
Close_T = 0x00  # Close warning tone of decoding

Buzzer_setting = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x0E, En_music + Open_T, 0xAB, 0xCD])

serial.write(Buzzer_setting)
time.sleep(0.1)  # Add a delay between commands

SAVE_TO_FLASH = bytes([0x7E, 0x00, 0x09, 0x01, 0x00, 0x00, 0x00, 0xDE, 0xC8])
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