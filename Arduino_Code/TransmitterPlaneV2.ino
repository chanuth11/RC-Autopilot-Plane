#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

const uint64_t pipeOut = 0xE9E8F0F0E1LL;//code
RF24 radio(7, 8);//CE,CSN pin

struct Signal {
  //byte throttle;
  //byte pitch;
  //byte roll;
  //byte yaw;
  byte ms;
  byte sm;
};

Signal data;

//Serial stuff
char nums[5];
int incomingBool = -1;
int sr = 90; // must be 0 - 180
int sp = 0; // must be 0 - 255

/*
void ResetData() {
  Center of the joysticks
}
*/

void setup(){
  //Start everything up
  radio.begin();
  radio.openWritingPipe(pipeOut);
  radio.stopListening(); //start the radio comunication for Transmitter
  //ResetData();
}

void loop(){
  // Control Stick Calibration
  //changed signs so that it would fit with the joysticks
  if (Serial.available() > 0) {
    incomingBool = Serial.read();
    if(incomingBool = 0){
      Serial.println("ServoControl-");
      delay(2000);
      Serial.readBytesUntil('\n', nums, 4);
      sr = atoi(nums);
      Serial.print("Number to display: ");
      Serial.println(nums);
      Serial.print("Input: ");
      Serial.println(sr);
      
    }else if (incomingBool = 1){
      Serial.println("MotorControl-");
      delay(2000);
      Serial.readBytesUntil('\n', nums, 4);
      sp = atoi(nums);
      Serial.print("Number to display: ");
      Serial.println(nums);
      Serial.print("Input: ");
      Serial.println(sp);
      
    }
  }
  data.ms = sr;
  data.sm = sp;
  /*
  data.throttle = trigger;
  data.roll = joysticklefty;
  data.pitch = joystickrightx;
  data.yaw = joystickrighty;
  
  radio.write(&data, sizeof(Signal));
  delay(1000);
  */
  for(int i = 0; i < 5; i++){
    nums[i] = '\0';
  }
  incomingBool = -1;
  radio.write(&data, sizeof(Signal));
  delay(5000);
  sr=90;
  sp=0;
  
}

  //data.throttle = mapJoystickValues( analogRead(A0), 524, 524, 1015, true );
  //data.roll = mapJoystickValues( analogRead(A1), 12, 524, 1020, true );
  //data.pitch = mapJoystickValues( analogRead(A2), 12, 524, 1020, true );
  //data.yaw = mapJoystickValues( analogRead(A3), 12, 524, 1020, true );
