#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <Servo.h>

const uint64_t pipeIn = 0xE9E8F0F0E1LL;
RF24 radio(8, 9); 

// Motor A connections
int enA = 17;
int in1 = 19;
int in2 = 18;
// Motor B connections
int enB = 16;
int in3 = 15;
int in4 = 14;

//Servo objs
Servo ch2;
Servo ch3;
Servo ch4;
Servo ch5;

//Serial stuff
int sr = 90; // must be 0 - 180
int sp = 0; // must be 0 - 255

struct Signal{
  //byte throttle;      
  //byte pitch;
  //byte roll;
  //byte yaw;
  byte ms;
  byte sm;
};

Signal data;

void setup(){
  // Set all the motor control pins to outputs
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  
  // Turn off motors - Initial state
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  
  //Set the pins for each PWM signal
  ch2.attach(2);
  ch3.attach(3);
  ch4.attach(5);
  ch5.attach(6);

  //Servo start straight - Initial state
  ch2.write(90);
  ch3.write(90);
  ch4.write(90);
  ch5.write(90);

  //Serial stuff
  Serial.begin(9600);
  Serial.println("BEGIN");
  
  //Configure the NRF24 module
  radio.begin();
  radio.openReadingPipe(0,pipeIn);
  radio.startListening();//sets reciever

}
/*
unsigned long lastRecvTime = 0;

void recvData(){
  while ( radio.available() ) {
    Serial.println("start1");
    radio.read(&data, sizeof(Signal));
    lastRecvTime = millis();
  }
}
*/

void loop(){
  /*recvData();
  unsigned long now = millis();
  
  if ( now - lastRecvTime > 1000 ) {
  ResetData(); // Signal lost.. Reset data
  }*/

  //Serial.println("roundstart");
  if (radio.available()) {
    radio.read(&data, sizeof(Signal));
    Serial.println(data.sm);
    Serial.println(data.ms);

    sr = data.ms;
    sp = data.sm;
    
    ch2.write(sr);
    ch3.write(sr);
    ch4.write(sr);
    ch5.write(sr);
    if(sp >0){
      analogWrite(enA, sp);
      analogWrite(enB, sp);
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
      digitalWrite(in3, HIGH);
      digitalWrite(in4, LOW);
      delay(5000);
    
      digitalWrite(in1, LOW);
      digitalWrite(in2, LOW);
      digitalWrite(in3, LOW);
      digitalWrite(in4, LOW);
    }
    int sr = 90;
    int sp = 0;
  }
  
}

//fix motor running and make this work with servos
