import serial
import time

# Set up serial communication
serial = serial.Serial('/dev/ttyS0', 9600) #connect Rx pin to GPIO14 and Tx pin to GPIO15

# Switch_of_all_barcodes
Disable_all_barcodes = 0x00
Enable_all_barcodes = 0x02
Enable_default_barcodes = 0x04

Scan_area = 0x00  # 0x00 for Whole area and 0x08 for Center area

Switch_of_all_barcodes = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x2C, Disable_all_barcodes + Scan_area, 0xAB, 0xCD])

SAVE_TO_FLASH = bytes([0x7E, 0x00, 0x09, 0x01, 0x00, 0x00, 0x00, 0xDE, 0xC8])

serial.write(Switch_of_all_barcodes)
time.sleep(0.1)  # Add a delay between commands
# serial.write(SAVE_TO_FLASH)

# Read data from the Barcode Scanner Module:
while True:
    # Read data from the UART
    data = serial.readline()

    # If there is data, print it to the console
    if data:
        print(data)

    time.sleep(1)
#--------------------------------------------