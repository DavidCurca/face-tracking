#include<Servo.h>

Servo serX;
Servo serY;

String serialData;

void setup() {
  serX.attach(9);
  serY.attach(10);
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  if(Serial.available() > 0){
    serialEvent();
  }
}

void serialEvent() {
  serialData = Serial.readString();
  String X = "",Y = "";
  for(int i = 0; i <= serialData.length()-1; i++){
    if(i < serialData.indexOf(" ")){
      X += serialData.charAt(i);
    }else if(i > serialData.indexOf(" ")){
      Y += serialData.charAt(i);
    }
  }
  Serial.println(X.toInt());
  Serial.println(Y.toInt());
  serX.write(X.toInt());
  serY.write(Y.toInt());
}
