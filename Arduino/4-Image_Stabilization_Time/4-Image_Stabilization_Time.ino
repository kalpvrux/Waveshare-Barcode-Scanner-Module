#include <SoftwareSerial.h>
SoftwareSerial mySerial(11, 12);  //Rx=11, Tx=12

float specificTime = 1.0; // 0.0-25.5s only
int hexRepresentation;
byte Image_Stabilization_Time[9] = {0x7E, 0x00, 0x08, 0x01, 0x00, 0x04, hexRepresentation /*0x00-0xFF：0-25.5 seconds*/, 0xAB, 0xCD};

void setup() {
  Serial.begin(115200);
  mySerial.begin(9600);
  
  hexRepresentation = floatToHex(specificTime);
  mySerial.write(Image_Stabilization_Time, 9);
}

void loop() {
  if (mySerial.available()) {
    String receivedData = mySerial.readStringUntil('\n'); // Read entire data until newline character

    Serial.println(receivedData); // Print the data to Serial Monitor
  }
}

int floatToHex(float time) {
  // Ensure time is within the valid range (0 to 25.5)
  time = max(0.0, min(25.5, time));

  // Scale the time to the range 0 to 255 and round to the nearest integer
  int scaledTime = round(time * 10);

  return scaledTime;
}
