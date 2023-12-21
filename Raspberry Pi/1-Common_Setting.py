import serial
import time

# Common_Setting
LED_Indicator_En = 0x80
LED_Indicator_Dis = 0x00
Buz_Indicator_En = 0x40
Buz_Indicator_Dis = 0x00
Target_light_Dis = 0x00
Target_light_Com = 0x10
Target_light_Keep = 0x20
Light_Dis = 0x00
Light_Com = 0x04
Light_Keep = 0x08
Manual_Mode = 0x00
Command_Mode = 0x01
Continous_Mode = 0x02
Sensor_Mode = 0x03

common_setting = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x00, LED_Indicator_En + Buz_Indicator_En + Target_light_Com + Light_Com + Command_Mode, 0xAB, 0xCD])

# Set up serial communication
serial = serial.Serial('/dev/ttyS0', 9600) #connect Rx pin to GPIO14 and Tx pin to GPIO15

serial.write(common_setting)
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