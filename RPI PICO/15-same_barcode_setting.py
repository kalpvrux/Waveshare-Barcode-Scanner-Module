from machine import UART
import time

# Set up serial communication
serial = UART(0,baudrate=9600)

# Same_barcode_setting
En_delay = 0x80
Dis_delay = 0x00

Delay_time = 4  # 0：infinity And 0.1-12.7s

def float_to_hex(time):
    # Ensure time is within the valid range (0 to 25.5)
    time = max(0, min(25.5, time))
    
    # Scale the time to the range 0 to 255 and round to the nearest integer
    scaled_time = round(time * 10)
    
    # Convert the scaled time to hex
    hex_code = scaled_time
    
    return hex_code

# Convert the specific time to hex
hex_representation = float_to_hex(Delay_time)

same_barcode_setting = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x13, En_delay + hex_representation, 0xAB, 0xCD])

SAVE_TO_FLASH = bytes([0x7E, 0x00, 0x09, 0x01, 0x00, 0x00, 0x00, 0xDE, 0xC8])

serial.write(same_barcode_setting)
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