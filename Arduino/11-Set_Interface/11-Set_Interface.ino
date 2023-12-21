#include <SoftwareSerial.h>
SoftwareSerial mySerial(11, 12);  //Rx=11, Tx=12

//Set_Interface-------------
#define UART_Output 0x00
#define USB_Output 0x01
#define USB_Virtual_Port 0x03
//--------------------------

byte Set_Interface[9] = {0x7E, 0x00, 0x08, 0x01, 0x00, 0x0D, USB_Output, 0xAB, 0xCD};

void setup() {
  Serial.begin(115200);
  mySerial.begin(9600);
  
  mySerial.write(Set_Interface, 9);
}

void loop() {
 if (mySerial.available()) {
    String receivedData = mySerial.readStringUntil('\n'); // Read entire data until newline character
    
    Serial.println(receivedData); // Print the data to Serial Monitor
  }
}
