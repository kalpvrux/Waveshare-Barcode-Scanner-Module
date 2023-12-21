#include <SoftwareSerial.h>
SoftwareSerial mySerial(11, 12);  //Rx=11, Tx=12

byte Duration_of_warning_tone[9] = {0x7E, 0x00, 0x08, 0x01, 0x00, 0x0B, 0x00 /*0x00-0xFF；0-255ms*/, 0xAB, 0xCD};

void setup() {
  Serial.begin(115200);
  mySerial.begin(9600);
  
  mySerial.write(Duration_of_warning_tone, 9);
}

void loop() {
 if (mySerial.available()) {
    String receivedData = mySerial.readStringUntil('\n'); // Read entire data until newline character
    
    Serial.println(receivedData); // Print the data to Serial Monitor
  }
}
