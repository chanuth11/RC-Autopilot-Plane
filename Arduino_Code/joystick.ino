#include <Servo.h>
char serialData; 
int servoPin = 9; 
int servoPos; 
Servo myServo; 


void setup() {
    // put your setup code here, to run once:
    Serial.begin(9600);
    myServo.attach(servoPin);
}

void loop(){
  // put your main code here, to run repeatedly: 
  if(Serial.available() > 0){
    serialData = Serial.read(); 
    
    if(serialData == '1'){
        myServo.write(180); 
    }else if(serialData == '2'){
        myServo.write(170); 
    }else if(serialData == '3'){
        myServo.write(160); 
    }else if(serialData == '4'){
        myServo.write(150); 
    }else if(serialData == '5'){
        myServo.write(140); 
    }else if(serialData == '6'){
        myServo.write(130); 
    }else if(serialData == '7'){
        myServo.write(120); 
    }else if(serialData == '8'){
        myServo.write(110); 
    }else if(serialData == '9'){
        myServo.write(90); 
    }else if(serialData == 'A'){
        myServo.write(0); 
    }else if(serialData == 'B'){
        myServo.write(10); 
    }else if(serialData == 'C'){
        myServo.write(20); 
    }else if(serialData == 'D'){
        myServo.write(50); 
    }else if(serialData == 'E'){
        myServo.write(70); 
    }else if(serialData == 'F'){
        myServo.write(80); 
    }

  }
}
    
    
    //else if(serialData == '3'){
//        myServo.write(60); 
//    }else if(serialData == '4'){
//        myServo.write(50); 
//    }else if(serialData == '5'){
//        myServo.write(40); 
//    }else if(serialData == '6'){
//        myServo.write(30); 
//    }else if(serialData == '7'){
//        myServo.write(20); 
//    }else if(serialData == '8'){
//        myServo.write(10); 
//    }else if(serialData == '9'){
//        myServo.write(0); 
//    }else if(serialData == 'A'){
//        myServo.write(100); 
//    }else if(serialData == 'B'){
//        myServo.write(110); 
//    }else if(serialData == 'C'){
//        myServo.write(120); 
//    }else if(serialData == 'D'){
//        myServo.write(130); 
//    }else if(serialData == 'E'){
//        myServo.write(140); 
//    }else if(serialData == 'F'){
//        myServo.write(150); 
//    }else if(serialData == 'G'){
//        myServo.write(160); 
//    }else if(serialData == 'H'){
//        myServo.write(170); 
//    }else if(serialData == 'I'){
//        myServo.write(180); 
//    }
//  
      
