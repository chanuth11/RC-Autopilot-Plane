#include <SPI.h>
#include <SoftwareSerial.h> 
#include "TinyGPS++.h"

String lat2;
String lon2;

TinyGPSPlus gps;
SoftwareSerial SoftSerial(4, 5); 

/*-----------------------------Setup---------------------------------*/
void setup() {
  String destination;
  Serial.begin(9600);
  SoftSerial.begin(9600);
  delay(3000); 
}


/*-----------------------------Main Loop---------------------------------*/
void loop() {

  String entry_1;
  //Get Starting GPS Coordinates
  while (SoftSerial.available() > 0)
  gps.encode(SoftSerial.read());
    if (gps.location.isUpdated())
    {
      lat2 = (String(gps.location.lat(),5));
      lon2 = (String(gps.location.lng(),5));

      Serial.println(lat2 + "," + lon2);
      delay(500); 
    }
    
  
}
