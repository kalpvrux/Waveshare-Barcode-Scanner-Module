#include <SoftwareSerial.h>
SoftwareSerial mySerial(11, 12);  //Rx=11, Tx=12

byte Sensitivity_parameter_1[9] = {0x7E, 0x00, 0x08, 0x01, 0x00, 0x0F, 0x32 /*0x00-0xFF： Higher the value, lower the sensitivity, default 0x32*/, 0xAB, 0xCD};
byte Sensitivity_parameter_2[9] = {0x7E, 0x00, 0x08, 0x01, 0x00, 0x10, 0x0A /*0x00-0xFF：Higher the value, lower the sensitivity, default 0x0A*/, 0xAB, 0xCD};

void setup() {
  Serial.begin(115200);
  mySerial.begin(9600);
  
  mySerial.write(Sensitivity_parameter_1, 9);
//  mySerial.write(Sensitivity_parameter_2, 9);
  
}

void loop() {
 if (mySerial.available()) {
    String receivedData = mySerial.readStringUntil('\n'); // Read entire data until newline character
    
    Serial.println(receivedData); // Print the data to Serial Monitor
  }
}
