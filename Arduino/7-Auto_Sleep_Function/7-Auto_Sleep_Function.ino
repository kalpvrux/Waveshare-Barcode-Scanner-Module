#include <SoftwareSerial.h>
SoftwareSerial mySerial(11, 12);  //Rx=11, Tx=12

//Auto_Sleep_Function-------
#define On 0x80
#define Off 0x00
//--------------------------
#define Idle_time 0x00 /*0x00 - 0x7F : (unit：100ms) for address 0x0007*/ /*0x00 - 0xFF : (unit：100ms) for address 0x0008*/

byte Auto_Sleep_Function[9] = {0x7E, 0x00, 0x08, 0x01, 0x00, 0x07, Off + Idle_time, 0xAB, 0xCD};

void setup() {
  Serial.begin(115200);
  mySerial.begin(9600);
  
  mySerial.write(Auto_Sleep_Function, 9);
}

void loop() {
 if (mySerial.available()) {
    String receivedData = mySerial.readStringUntil('\n'); // Read entire data until newline character
    
    Serial.println(receivedData); // Print the data to Serial Monitor
  }
}
