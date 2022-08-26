#include <Servo.h>
//Servo motorY;
Servo motorX;
String serialData;
void setup() {
 Serial.begin(9600);
 while(!Serial){
  ;
 }
  motorX.attach(3);
 // motorY.attach(5);

}

void loop() {
  if (Serial.available() > 0) {
    serialData = Serial.read();
    motorX.write(serialData.toInt());
    //serialData = Serial.read();
    //motorY.write(serialData);
    
  }


}
