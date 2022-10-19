#include<Servo.h>
int pos=0;
Servo srv1;
Servo srv2;
char serialRead;

void setup() {
Serial.begin(9600);
srv1.attach(3);
srv2.attach(5);
pinMode(4, OUTPUT);
pinMode(7, OUTPUT);

}

void loop() {
  int con = 0;
  if(Serial.available()>0){
    int con=0;
    serialRead = Serial.read();
    if (serialRead == 'A'){
      pos = Serial.parseInt();
      srv1.write(pos);
      digitalWrite(4,HIGH);
      Serial.println(pos);
      delay(20);
      }
    if (serialRead == 'B'){
      pos = Serial.parseInt();
      srv2.write(pos);
      digitalWrite(7,HIGH);
      Serial.println(pos);
      delay(20);
    }
  }
  else{
    while(!Serial.available()){
    con++;
    delay(1000);
    Serial.println(con);
    if (con>2){  
  digitalWrite(4,LOW);
  digitalWrite(7,LOW);
  }
  }
}
}
