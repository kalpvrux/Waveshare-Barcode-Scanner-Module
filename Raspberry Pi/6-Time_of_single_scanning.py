import serial
import time

# Set up serial communication
serial = serial.Serial('/dev/ttyS0', 9600) #connect Rx pin to GPIO14 and Tx pin to GPIO15

def float_to_hex(time):
    # Ensure time is within the valid range (0 to 25.5)
    time = max(0, min(25.5, time))
    
    # Scale the time to the range 0 to 255 and round to the nearest integer
    scaled_time = round(time * 10)
    
    # Convert the scaled time to hex
    hex_code = scaled_time
    
    return hex_code

# Declare a specific time value
specific_time = 0.4  # 0.0-25.5s only

# Convert the specific time to hex
hex_representation = float_to_hex(specific_time)

Time_of_single_scanning = bytes([0x7E, 0x00, 0x08, 0x01, 0x00, 0x06, hex_representation # 0x00-0xFF：0-25.5 seconds
                            , 0xAB, 0xCD])

serial.write(Time_of_single_scanning)
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