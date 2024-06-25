#include <Servo.h>

Servo myservo;


void setup(){
  Serial.begin(9600);
  myservo.attach(9);
}

void loop(){
  int val;
  while(Serial.available()>0){
    val = Serial.parseInt();
    if(val != 0){
      Serial.println(val);
      myservo.write(val);
    }
    delay(5);
  }
}
