#include <SoftwareSerial.h>
SoftwareSerial mySerial(11, 12);  //Rx=11, Tx=12

//Common_Setting------------
#define LED_Indicator_En 0x80
#define LED_Indicator_Dis 0x00

#define Buz_Indicator_En 0x40
#define Buz_Indicator_Dis 0x00

#define Target_light_Dis 0x00
#define Target_light_Com 0x10
#define Target_light_Keep 0x20

#define Light_Dis 0x00
#define Light_Com 0x04
#define Light_Keep 0x08

#define Manual_Mode 0x00
#define Command_Mode 0x01
#define Continous_Mode 0x02
#define Sensor_Mode 0x03
//--------------------------

byte Common_Setting[9] = {0x7E, 0x00, 0x08, 0x01, 0x00 , 0x00, LED_Indicator_En + Buz_Indicator_En + Target_light_Com + Light_Com + Command_Mode, 0xAB, 0xCD};

void setup() {
  Serial.begin(115200);
  mySerial.begin(9600);

  mySerial.write(Common_Setting, 9);
}

void loop() {
  if (mySerial.available()) {
    String receivedData = mySerial.readStringUntil('\n'); // Read entire data until newline character

    Serial.println(receivedData); // Print the data to Serial Monitor
  }
}
