#include <Keyboard.h>  
#include <Mouse.h>
//variables:
const int LEDpin = 9;
const int buttonpin = 2;
int state;


void setup() {
  // set pins:
  Serial.begin(9600);
  pinMode(LEDpin, OUTPUT);
  pinMode(buttonpin,INPUT_PULLUP);
}

void loop() {
  //read button state:
  state = digitalRead(buttonpin);
  // put your main code here, to run repeatedly:
  if(state == HIGH) { //Means button not pressed
    digitalWrite(LEDpin,LOW);
  }
  else{ //this means button is pressed
    Serial.print("button is pressed");
    Keyboard.write('Q');
    digitalWrite(LEDpin,HIGH);
  }

}
