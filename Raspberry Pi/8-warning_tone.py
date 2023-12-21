import serial
import time

# Set up serial communication
serial = serial.Serial('/dev/ttyS0', 9600) #connect Rx pin to GPIO14 and Tx pin to GPIO15

warning_tone = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x0A, 0x00 # 0x00：Buzzer 0x01-0xFF：Passive buzzer (freq=Value*20) 
                , 0xAB, 0xCD])

serial.write(warning_tone)
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