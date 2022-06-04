//***************************Master or Receiver code*****************
/*This code was used for a video tutorial on the ForceTronics YouTube Channel
 * This code is free and open for anybody to use and modify at your own risk
*/

#include <SPI.h> //Call SPI library so you can communicate with the nRF24L01+
#include <nRF24L01.h> //nRF2401 libarary found at https://github.com/tmrh20/RF24/
#include <RF24.h> //nRF2401 libarary found at https://github.com/tmrh20/RF24/
#include <Servo.h>

Servo myServo;
Servo myServo2;
Servo myServo3;
Servo myServo4;
Servo ESC1;     // create servo object to control the ESC
Servo ESC2;     // create servo object to control the ESC


int servoPin = 5;//left wing
int servoPin2 = 3;//elevator
int servoPin3 = 6;//rudder
int servoPin4 = 2;//right wing
int ESCpin1 = 8;
int ESCpin2 = 1;

const uint8_t pinCE = 9; 
const uint8_t pinCSN = 10; 
RF24 wirelessSPI(pinCE, pinCSN);
const uint64_t rAddress = 0xB00B1E50C3LL;  

struct Signal {
  byte HLA;
  byte VLA;
  byte HRA;
  byte RT;

};

Signal Data; //create struct object
void setup() {
  wirelessSPI.begin();  //Start the nRF24 module
  wirelessSPI.setPALevel(RF24_PA_MIN);
  wirelessSPI.setDataRate(RF24_2MBPS);
  wirelessSPI.setChannel(124);
  wirelessSPI.openReadingPipe(1,rAddress);  //This is receiver or master so we need to be ready to read data from transmitters
  wirelessSPI.startListening();    // Start listening for messages
  Serial.begin(9600);  //serial port to display received data
  Serial.println("Network master is online...");
  myServo.attach(servoPin);
  myServo2.attach(servoPin2);
  myServo3.attach(servoPin3);
  myServo4.attach(servoPin4);
  ESC1.attach(ESCpin1);
  ESC2.attach(ESCpin2);

}

void loop() {
  if(wirelessSPI.available()){ //Check if recieved data
     wirelessSPI.read(&Data, sizeof(Signal)); //read packet of data and store it in struct object
     Serial.println("Received data packet from node: ");
     myServo.write((Data.HLA));
     myServo2.write((Data.VLA));
     myServo3.write((Data.HRA));
     myServo4.write(Data.HLA);
     ESC1.write(Data.RT);
     ESC2.write(Data.RT);


     
     //Serial.println((Data.RT)); //print node number or channel
         Serial.println((Data.HLA)); //print node number or channel
     Serial.println((Data.HRA)); //print node number or channel
          Serial.println((Data.RT)); //print node number or channel




  }
  //Serial.println("no value");
}
