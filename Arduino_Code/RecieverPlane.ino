#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <Servo.h>

const uint64_t pipeIn = 0xE9E8F0F0E1LL;
RF24 radio(8, 9); 

// Motor A connections
int enA = 19;
int in1 = 18;
int in2 = 17;
// Motor B connections
int enB = 14;
int in3 = 16;
int in4 = 15;

int ch_width_1 = 0;
int ch_width_2 = 0;
int ch_width_3 = 0;
int ch_width_4 = 0;

Servo ch2;
Servo ch3;
Servo ch4;
Servo ch5;

struct Signal{
  byte throttle;      
  byte pitch;
  byte roll;
  byte yaw;
};

Signal data;

void ResetData(){
  // Define the middle position for Potenciometers. (254/2=127)
  data.throttle = 127;
  data.pitch = 127;
  data.roll = 127;
  data.yaw = 127;
}

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
  
  //Set the pins for each PWM signal | Her bir PWM sinyal için pinler belirleniyor.
  ch2.attach(2);
  ch3.attach(3);
  ch4.attach(5);
  ch5.attach(6);
  
  //Configure the NRF24 module
  Serial.begin(9600);
  Serial.println("Startmain");
  ResetData();
  radio.begin();
  radio.openReadingPipe(0,pipeIn);
  radio.setPALevel(RF24_PA_MIN);
  radio.startListening();

}

unsigned long lastRecvTime = 0;

void recvData(){
  while ( radio.available() ) {
    Serial.println("start1");
    radio.read(&data, sizeof(Signal));
    lastRecvTime = millis();
  }
}

void loop(){
  Serial.println("Loop-");
  recvData();
  unsigned long now = millis();
  Serial.println("start");
  if ( now - lastRecvTime > 1000 ) {
  ResetData(); // Signal lost.. Reset data | Sinyal kayıpsa data resetleniyor
  }
  
  //data for motors already mapped
  Serial.println("start");
  Serial.println(data.throttle);
  Serial.println(data.pitch);
  Serial.println(data.yaw);
  Serial.println(data.roll);
  
  ch_width_1 = map(data.throttle, 0, 255, 1000, 2000);
  ch_width_2 = map(data.pitch,    0, 255, 1000, 2000);
  ch_width_3 = map(data.roll,     0, 255, 1000, 2000);
  ch_width_4 = map(data.yaw,      0, 255, 1000, 2000);
  
  analogWrite(enA, ch_width_1);
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  delay(20);
  analogWrite(enB, ch_width_1);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  delay(20);
      
  ch2.writeMicroseconds(ch_width_2);
  ch3.writeMicroseconds(ch_width_3);
  ch4.writeMicroseconds(ch_width_3);
  ch5.writeMicroseconds(ch_width_4);
}
