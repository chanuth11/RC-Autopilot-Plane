//communication 1 way
//firstly download library https://github.com/nRF24/RF24

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
RF24 radio(7, 8); // CE, CSN
const byte address[6] = "00001";
int led_pin = 3;
boolean button_state = 0;

void setup() {
pinMode(led_pin, OUTPUT);
Serial.begin(9600);
radio.begin();
radio.openReadingPipe(0, address);   //Setting the address at which we will receive the data
radio.setPALevel(RF24_PA_MIN);       //You can set this as minimum or maximum depending on the distance between the transmitter and receiver.
radio.startListening();              //This sets the module as receiver
}

void loop()
{
if (radio.available())              //Looking for the data.
{
char text[32] = "";                 //Saving the incoming data
radio.read(&text, sizeof(text));    //Reading the data
   //Reading the data


Serial.println(text);

delay(5);
}
}
