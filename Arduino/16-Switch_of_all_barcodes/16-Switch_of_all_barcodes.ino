#include <SoftwareSerial.h>
SoftwareSerial mySerial(11, 12);  //Rx=11, Tx=12

//Switch_of_all_barcodes----
#define Disable_all_barcodes 0x00
#define Enable_all_barcodes 0x02
#define Enable_default_barcodes 0x04
#define Scan_area 0x00 // 0x00 for Whole area and 0x08 for Center area
//--------------------------

byte Switch_of_all_barcodes[9] = {0x7E, 0x00, 0x08, 0x01, 0x00, 0x2C, Disable_all_barcodes + Scan_area, 0xAB, 0xCD};

void setup() {
  Serial.begin(115200);
  mySerial.begin(9600);
  
  mySerial.write(Switch_of_all_barcodes, 9);
  
}

void loop() {
 if (mySerial.available()) {
    String receivedData = mySerial.readStringUntil('\n'); // Read entire data until newline character
    
    Serial.println(receivedData); // Print the data to Serial Monitor
  }
}
