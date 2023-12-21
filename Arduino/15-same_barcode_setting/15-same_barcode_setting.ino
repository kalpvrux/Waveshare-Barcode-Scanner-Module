#include <SoftwareSerial.h>
SoftwareSerial mySerial(11, 12);  //Rx=11, Tx=12

//same_barcode_setting------
#define En_delay 0x80
#define Dis_delay 0x00
#define Delay_time 0x00 //0x00：infinity And 0x01-0x7F：0.1-12.7s；
//--------------------------

byte same_barcode_setting[9] = {0x7E, 0x00, 0x08, 0x01, 0x00, 0x13, Dis_delay + Delay_time, 0xAB, 0xCD};

void setup() {
  Serial.begin(115200);
  mySerial.begin(9600);
  
  mySerial.write(same_barcode_setting, 9);
  
}

void loop() {
 if (mySerial.available()) {
    String receivedData = mySerial.readStringUntil('\n'); // Read entire data until newline character
    
    Serial.println(receivedData); // Print the data to Serial Monitor
  }
}
