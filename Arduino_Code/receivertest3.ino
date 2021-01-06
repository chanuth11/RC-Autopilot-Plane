#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(8, 9);  // CE, CSN
const byte address[6] = "00001";

void setup(){
 
  Serial.begin(9600);
  Serial.println("Start");
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.startListening();
}

void loop(){
    char text[32]={0};
    radio.read(&text, sizeof(text));
    Serial.println(text);
    delay(1000);
}
