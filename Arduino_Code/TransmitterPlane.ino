#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

const uint64_t pipeOut = 0xE9E8F0F0E1LL;//code
RF24 radio(8, 9);//CE,CSN pin

struct Signal {
  byte throttle;
  byte pitch;
  byte roll;
  byte yaw;
};

Signal data;

void ResetData() {
  data.throttle = 127; // Motor Stop (254/2=127)
  data.pitch = 127; // Center
  data.roll = 127; // Center
  data.yaw = 127; // Center
}

void setup(){
  //Start everything up
  radio.begin();
  radio.openWritingPipe(pipeOut);
  radio.stopListening(); //start the radio comunication for Transmitter
  ResetData();
}

//Joystick center and its borders
int mapJoystickValues(int val, int lower, int middle, int upper, bool reverse){
  val = constrain(val, lower, upper);
  if ( val < middle )
  val = map(val, lower, middle, 0, 128);
  else
  val = map(val, middle, upper, 128, 255);
  return ( reverse ? 255 - val : val );
}

void loop(){
  // Control Stick Calibration
  //changed signs so that it would fit with the joysticks
  data.throttle = mapJoystickValues( analogRead(A0), 524, 524, 1015, true );

  data.roll = mapJoystickValues( analogRead(A1), 12, 524, 1020, true );

  data.pitch = mapJoystickValues( analogRead(A2), 12, 524, 1020, true );

  data.yaw = mapJoystickValues( analogRead(A3), 12, 524, 1020, true );

  radio.write(&data, sizeof(Signal));
   delay(1000);
}
