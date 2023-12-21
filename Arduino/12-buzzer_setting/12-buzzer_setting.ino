#include <SoftwareSerial.h>
SoftwareSerial mySerial(11, 12);  //Rx=11, Tx=12

//buzzer_setting------------
#define Dis_music 0x02 // Disable start music
#define En_music 0x00  // Enable start music
#define Open_T 0x04    // Open warning tone of decoding 
#define Close_T 0x00   // Close warning tone of decoding
//--------------------------

byte buzzer_setting[9] = {0x7E, 0x00, 0x08, 0x01, 0x00, 0x0E, Dis_music + Close_T, 0xAB, 0xCD};

void setup() {
  Serial.begin(115200);
  mySerial.begin(9600);
  
  mySerial.write(buzzer_setting, 9);
}

void loop() {
 if (mySerial.available()) {
    String receivedData = mySerial.readStringUntil('\n'); // Read entire data until newline character
    
    Serial.println(receivedData); // Print the data to Serial Monitor
  }
}
