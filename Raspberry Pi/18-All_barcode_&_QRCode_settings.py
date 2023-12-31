import serial
import time

# Set up serial communication
serial = serial.Serial('/dev/ttyS0', 9600) #connect Rx pin to GPIO14 and Tx pin to GPIO15

# CodeBar
En_CodeBar = 0x01
Dis_CodeBar = 0x00
Start_Stop_char = 0x00  # 0x00 for Disable Start/Stop character And 0x02 for Enable Start/Stop character


EAN13 = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x2E, 0x01 # 0x00-0x01：Disable-Enable
        , 0xAB, 0xCD])
EAN8 = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x2F, 0x01 # 0x00-0x01：Disable-Enable
        , 0xAB, 0xCD])
UPCA = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x30, 0x01 # 0x00-0x01：Disable-Enable
        , 0xAB, 0xCD])
UPCE0 = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x31, 0x01 # 0x00-0x01：Disable-Enable
        , 0xAB, 0xCD])
UPCE1 = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x32, 0x01 # 0x00-0x01：Disable-Enable
        , 0xAB, 0xCD])

Code128 = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x33, 0x01 # 0x00-0x01：Disable-Enable
            , 0xAB, 0xCD])
Code128_min_length = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x34, 0x06 #0x00-0xFF：0-255
                        , 0xAB, 0xCD])
Code128_max_length = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x35, 0xFF #0x00-0xFF：0-255
                        , 0xAB, 0xCD])

Code39 = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x36, 0x01 #0x00-0x01：Disable-Enable
            , 0xAB, 0xCD])
Code39_min_length = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x37, 0x00 #0x00-0xFF：0-255
                    , 0xAB, 0xCD])
Code39_max_length = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x38, 0xFF #0x00-0xFF：0-255
                    , 0xAB, 0xCD])
 
Code93 = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x39, 0x01 #0x00-0x01：Disable-Enable
            , 0xAB, 0xCD])
Code93_min_length = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x3A, 0x00 #0x00-0xFF：0-255
                    , 0xAB, 0xCD])
Code93_max_length = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x3B, 0xFF #0x00-0xFF：0-255
                    , 0xAB, 0xCD])

CodeBar = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x3C, En_CodeBar + Start_Stop_char, 0xAB, 0xCD])
CodeBar_min_length = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x3D, 0x00 #0x00-0xFF：0-255
                    , 0xAB, 0xCD])
CodeBar_max_length = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x3E, 0xFF #0x00-0xFF：0-255
                        , 0xAB, 0xCD])

QR_code = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x3F, 0x01 #0x00-0x01：Disable-Enable
            , 0xAB, 0xCD])

Interleaved_2of5 = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x40, 0x01 #0x00-0x01：Disable-Enable
                    , 0xAB, 0xCD])
Interleaved_2of5_min_length = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x41, 0x00 #0x00-0xFF：0-255
                                , 0xAB, 0xCD])
Interleaved_2of5_max_length = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x42, 0xFF #0x00-0xFF：0-255
                                , 0xAB, 0xCD])

Industrial_25 = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x43, 0x01 #0x00-0x01：Disable-Enable
                , 0xAB, 0xCD])
Industrial_25_min_length = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x44, 0x00 #0x00-0xFF：0-255
                            , 0xAB, 0xCD])
Industrial_25_max_length = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x45, 0xFF #0x00-0xFF：0-255
                            , 0xAB, 0xCD])

Matrix_2_of_5 = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x46, 0x01#0x00-0x01：Disable-Enable
                , 0xAB, 0xCD])
Matrix_2_of_5_min_length = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x47, 0x00 #0x00-0xFF：0-255
                            , 0xAB, 0xCD])
Matrix_2_of_5_max_length = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x48, 0xFF #0x00-0xFF：0-255
                            , 0xAB, 0xCD])

Code11 = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x49, 0x01 #0x00-0x01：Disable-Enable
        , 0xAB, 0xCD])
Code11_min_length = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x4A, 0x00 #0x00-0xFF：0-255
                    , 0xAB, 0xCD])
Code11_max_length = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x4B, 0xFF #0x00-0xFF：0-255
                    , 0xAB, 0xCD])

MSI = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x4C, 0x01 #0x00-0x01：Disable-Enable
        , 0xAB, 0xCD])
MSI_min_length = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x4D, 0x00 #0x00-0xFF：0-255
                    , 0xAB, 0xCD])
MSI_max_length = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x4E, 0xFF #0x00-0xFF：0-255
                    , 0xAB, 0xCD])

RSS_14 = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x4F, 0x01 #0x00-0x01：Disable-Enable
            , 0xAB, 0xCD])
Limited_RSS = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x50, 0x01#0x00-0x01：Disable-Enable
                , 0xAB, 0xCD])
Expanded_RSS = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x51, 0x01#0x00-0x01：Disable-Enable
                , 0xAB, 0xCD])
RSS_min_length = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x52, 0x00 #0x00-0xFF：0-255
                , 0xAB, 0xCD])
RSS_max_length = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x53, 0xFF #0x00-0xFF：0-255
                    , 0xAB, 0xCD])

DM = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x54, 0x01 #0x00-0x01：Disable-Enable
        , 0xAB, 0xCD])

PDF417 = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x55, 0x01 #0x00-0x01：Disable-Enable
            , 0xAB, 0xCD])

SAVE_TO_FLASH = bytes([0x7E, 0x00, 0x09, 0x01, 0x00, 0x00, 0x00, 0xDE, 0xC8])

serial.write(MSI)
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