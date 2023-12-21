#include <SoftwareSerial.h>
SoftwareSerial mySerial(11, 12);  //Rx=11, Tx=12

//Keyboard_Setting----------
#define US 0x00
#define Czech 0x01
#define France 0x02
#define Germany 0x03
#define Hungary 0x04
#define Italy 0x05
#define Japan 0x06
#define Spain 0x07
#define Turkey_F 0x08
#define Turkey_Q 0x09
//--------------------------

byte Keyboard_Setting[9] = {0x7E, 0x00, 0x08, 0x01, 0x00, 0x61, US, 0xAB, 0xCD};

void setup() {
  Serial.begin(115200);
  mySerial.begin(9600);
  
  mySerial.write(Keyboard_Setting, 9);
}

void loop() {
 if (mySerial.available()) {
    String receivedData = mySerial.readStringUntil('\n'); // Read entire data until newline character
    
    Serial.println(receivedData); // Print the data to Serial Monitor
  }
}
