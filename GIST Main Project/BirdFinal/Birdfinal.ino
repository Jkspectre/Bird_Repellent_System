#include<Servo.h>
int pos=0;
Servo srv;

void setup() {
Serial.begin(9600);
srv.attach(3);
pinMode(4, OUTPUT);

}

void loop() {
  int con = 0;
  if(Serial.available()>0){
    int  con=0;
      pos = Serial.parseInt();
      srv.write(pos);
      digitalWrite(4,HIGH);
      Serial.println(pos);
      delay(20);
  }
  
  else{
    while(!Serial.available()){
    con++;
    delay(1000);
    Serial.println(con);
    if (con>2){  
  digitalWrite(4,LOW);
  
}
    }
}
}
