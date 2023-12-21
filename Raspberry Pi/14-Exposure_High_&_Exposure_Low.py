import serial
import time

# Set up serial communication
serial = serial.Serial('/dev/ttyS0', 9600) #connect Rx pin to GPIO14 and Tx pin to GPIO15

# Same_barcode_setting
En_delay = 0x80
Dis_delay = 0x00
Delay_time = 0x00  # 0x00：infinity And 0x01-0x7F：0.1-12.7s

# Switch_of_all_barcodes
Disable_all_barcodes = 0x00
Enable_all_barcodes = 0x02
Enable_default_barcodes = 0x04
Scan_area = 0x00  # 0x00 for Whole area and 0x08 for Center area

# CodeBar
En_CodeBar = 0x01
Dis_CodeBar = 0x00
Start_Stop_char = 0x00  # 0x00 for Disable Start/Stop character And 0x02 for Enable Start/Stop character

# Extra_Function
Add_End_Char = 0x01
Without_End_Char = 0x00
Add_Suffix = 0x02
Without_Suffix = 0x00
Add_Code_ID = 0x04
Without_Code_ID = 0x00
Add_Prefix = 0x08
Without_Prefix = 0x00
Add_RF = 0x10
Without_RF = 0x00
CR = 0x00  # End_Char_Suffix_Type
CRLF = 0x20  # End_Char_Suffix_Type
TAB = 0x40  # End_Char_Suffix_Type
none = 0x60  # End_Char_Suffix_Type

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

# Prefix_And_Suffix_length
Prefix_Length = 0x00  # 0x00-0x0F : 0 - 15
Suffix_Length = 0x00  # 0x00-0x0F : 0 - 15

# Data_intercept_setting
All = 0x00  # Send all Data
M_Data = 0x01  # Send first M Data
N_Data = 0x02  # Send last N Data
None_data = 0x03  # Don’t send the first M+ the last N Data

Exposure_High = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x11, 0x00 #Exposure data-High bits 0x00~0xFF
                , 0xAB, 0xCD])
Exposure_Low = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x12, 0x00 # Exposure data-Low bits 0x00~0xFF
                , 0xAB, 0xCD])
SAVE_TO_FLASH = bytes([0x7E, 0x00, 0x09, 0x01, 0x00, 0x00, 0x00, 0xDE, 0xC8])

serial.write(Exposure_High)
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