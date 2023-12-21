#include <SoftwareSerial.h>
SoftwareSerial mySerial(11, 12);  //Rx=11, Tx=12

byte Exposure_High[9] = {0x7E, 0x00, 0x08, 0x01, 0x00, 0x11, 0x00 /*Exposure data-High bits 0x00~0xFF*/, 0xAB, 0xCD};
byte Exposure_Low[9] = {0x7E, 0x00, 0x08, 0x01, 0x00, 0x12, 0x00 /*Exposure data-Low bits 0x00~0xFF*/, 0xAB, 0xCD};

void setup() {
  Serial.begin(115200);
  mySerial.begin(9600);
  
  mySerial.write(Exposure_High, 9);
//  mySerial.write(Exposure_Low, 9);
  
}

void loop() {
 if (mySerial.available()) {
    String receivedData = mySerial.readStringUntil('\n'); // Read entire data until newline character
    
    Serial.println(receivedData); // Print the data to Serial Monitor
  }
}
