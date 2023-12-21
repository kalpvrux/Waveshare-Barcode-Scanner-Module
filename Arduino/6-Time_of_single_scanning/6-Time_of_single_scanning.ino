#include <SoftwareSerial.h>
SoftwareSerial mySerial(11, 12);  //Rx=11, Tx=12

float specificTime = 2.0; // 0.0-25.5s only
int hexRepresentation;

void setup() {
  Serial.begin(115200);
  mySerial.begin(9600);

  hexRepresentation = floatToHex(specificTime);
  byte Time_of_single_scanning[9] = {0x7E, 0x00, 0x08, 0x01, 0x00, 0x06, hexRepresentation, 0xAB, 0xCD};

  mySerial.write(Time_of_single_scanning, 9);
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
