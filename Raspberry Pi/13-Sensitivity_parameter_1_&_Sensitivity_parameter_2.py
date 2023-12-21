import serial
import time

# Set up serial communication
serial = serial.Serial('/dev/ttyS0', 9600) #connect Rx pin to GPIO14 and Tx pin to GPIO15

Sensitivity_parameter_1 = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x0F, 0x00 # 0x00-0xFF： Higher the value, lower the sensitivity, default 0x32
                            , 0xAB, 0xCD])
Sensitivity_parameter_2 = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x10, 0x00 #0x00-0xFF：Higher the value, lower the sensitivity, default 0x0A
                            , 0xAB, 0xCD])

serial.write(Sensitivity_parameter_1)
time.sleep(0.1)  # Add a delay between commands
serial.write(Sensitivity_parameter_2)

# Read data from the Barcode Scanner Module:
while True:
    # Read data from the UART
    data = serial.readline()

    # If there is data, print it to the console
    if data:
        print(data)

    time.sleep(1)
#--------------------------------------------