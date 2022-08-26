#include<Servo.h>
int pos=0;
Servo srv;

void setup() {
Serial.begin(9600);
srv.attach(3);
pinMode(4, OUTPUT);

}

void loop() {
  while(Serial.available()>0){
    pos = Serial.parseInt();
    if(pos=pos){
      srv.write(pos);
      digitalWrite(4,HIGH);
      Serial.println(pos);
      //delay(80);
      
    }
    delay(15);
    
  }
  //digitalWrite(4,LOW);
}
