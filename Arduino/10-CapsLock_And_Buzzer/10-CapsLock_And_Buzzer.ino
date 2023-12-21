#include <SoftwareSerial.h>
SoftwareSerial mySerial(11, 12);  //Rx=11, Tx=12

//CapsLock_And_Buzzer-------
#define Dis 0x00  //CapsLock Disable
#define En 0x02   //CapsLock Enable
#define High 0x00 //High for idle and Low for busy
#define Low 0x01  //Low for busy and High for idle
//--------------------------

byte CapsLock_And_Buzzer[9] = {0x7E, 0x00, 0x08, 0x01, 0x00, 0x0C, Dis + High, 0xAB, 0xCD};

void setup() {
  Serial.begin(115200);
  mySerial.begin(9600);
  
  mySerial.write(CapsLock_And_Buzzer, 9);
}

void loop() {
 if (mySerial.available()) {
    String receivedData = mySerial.readStringUntil('\n'); // Read entire data until newline character
    
    Serial.println(receivedData); // Print the data to Serial Monitor
  }
}
