/*#include <Servo.h>
String serialData; 
int servoPin = 9;
char recievedData [14];
int servoPos; 
Servo myServo; 
Servo myServo2;
void setup() {
    // put your setup code here, to run once:
    Serial.begin(9600);
    myServo.attach(servoPin);
}

void loop() {
  // put your main code here, to run repeatedly: 
    

  
  if(Serial.available() > 0){

      serialData = Serial.readString();  

      serialData.toCharArray(recievedData, 14); 


      for(int i = 0; i < 14; i++){
          Serial.print(recievedData[i]); 
      }

       Serial.println(); 

  }      
}
*/
/*This code was used for a video tutorial on the ForceTronics YouTube Channel
 * This code is free and open for anybody to use and modify at your own risk
*/
#include <SPI.h> //Call SPI library so you can communicate with the nRF24L01+
#include <nRF24L01.h> //nRF2401 libarary found at https://github.com/tmrh20/RF24/
#include <RF24.h> //nRF2401 libarary found at https://github.com/tmrh20/RF24/
const uint8_t pinCE = 9; 
const uint8_t pinCSN = 10;
RF24 wirelessSPI(pinCE, pinCSN);  
const uint64_t wAddress = 0xB00B1E50C3LL;  

String serialData; 
char recievedData[15];
byte ToDecimal = 48;
struct Signal {
  byte HLA;
  byte VLA;
  byte HRA;
  byte RT;
};
Signal Data; //create struct object

int myTimeout = 5; 

void setup() {

Serial.setTimeout(myTimeout);
  Serial.begin(9600);
  wirelessSPI.begin();  //Start the nRF24 module
  wirelessSPI.setPALevel(RF24_PA_MIN);
  wirelessSPI.setDataRate(RF24_2MBPS);
  wirelessSPI.setChannel(124);
  wirelessSPI.openWritingPipe(wAddress); //open writing or transmit pipe
  wirelessSPI.stopListening(); //go into transmit mode
}

void loop() {
  
    if(Serial.available() > 0){

      serialData = Serial.readString();  

      serialData.toCharArray(recievedData, 9); 
      
      byte val1 = ((byte(recievedData[0]))-48)*10 + ((byte(recievedData[1]))-48);
      if (val1 <= 9){
        Data.HLA = map(val1, 0, 9, 90, 0);
      }
      else{ 
        Data.HLA = map(val1, 10, 19, 90, 180);}
      
      byte val2 = ((byte(recievedData[2]))-48)*10 + ((byte(recievedData[3]))-48);
      if (val2 <= 9) {
        Data.VLA = map(val2, 0, 9, 90, 180); 
      }
      else{
        Data.VLA = map(val2, 10, 19, 90, 0); 
      }
      
      byte val3 = ((byte(recievedData[4]))-48)*10 + ((byte(recievedData[5]))-48);
      if (val3 <= 9) {
        Data.HRA = map(val3, 0, 9, 90, 0); 
      }
      else{
        Data.HRA = map(val3, 10, 19, 90, 180); 
      }    
      byte val4 = ((byte(recievedData[6]))-48)*10 + ((byte(recievedData[7]))-48);

      if (val4 <= 9) {
        Data.HRA = map(val4, 0, 9, 0, 50); 
      }
      else{
        Data.HRA = map(val4, 11, 19, 50, 100); 
      }  
      
      Serial.setTimeout(myTimeout);


     wirelessSPI.write(&Data, sizeof(Signal));
       
  }
}
