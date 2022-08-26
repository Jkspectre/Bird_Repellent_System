#include<Servo.h>
Servo MX;
Servo MY;
void setup() {
  Serial.begin(9600);
   MX.attach(3);
   MY.attach(5);
   pinMode(4, OUTPUT);
   pinMode(7, OUTPUT);
}

void loop() {
 
 MX.write(30);
 delay(1000);
 digitalWrite(4, HIGH);
 MY.write(60);
 delay(1000);
  MX.write(60);
 delay(1000);
 MY.write(120);
 delay(1000);
 digitalWrite(7, HIGH);
 delay(2000);
 /*
  for (int i=0;i<150;i++){
    
    MX.write(i);
    Serial.print(i);
    delay(10);
    
  }
  delay(200);
  for (int i=150;i>=0;i--){
    
    MX.write(i);
    Serial.print(i);
    delay(10);
    
  }
  */
  /*
  delay(2000);
  MX.write(30);
  delay(2000);
  MX.write(90);
  delay(2000);
  MX.write(120);
  delay(2000);
  MX.write(60);
  delay(2000);
  MX.write(150);
  delay(2000);
  MX.write(15);
  delay(2000);
 */
}
