#include <SoftwareSerial.h>

SoftwareSerial barcodeSerial(11, 12);  // RX, TX pins

void setup() {
  Serial.begin(9600);
  barcodeSerial.begin(9600);  // Set baud rate according to your module's specifications
}

void loop() {
  if (barcodeSerial.available()) {
    String receivedData = barcodeSerial.readStringUntil('\n'); // Read entire data until newline character
    
    Serial.println(receivedData); // Print the data to Serial Monitor
  }
}
