#include <SoftwareSerial.h>
char bt;
SoftwareSerial EEBlue(0,1); // RX | TX
int outPin1 = 13;     //motor1 
int outPin2 = 12;    //motor1 
int outPin3 = 11;   //motor2 
int outPin4 = 10;   //motor2 
int SPEED = 10

void setup()
{
  pinMode(outPin1,OUTPUT); 
  pinMode(outPin2,OUTPUT); 
  pinMode(outPin3,OUTPUT); 
  pinMode(outPin4,OUTPUT); 

  Serial.begin(9600);
  EEBlue.begin(9600);  //Default Baud for comm, it may be different for your Module. 
  Serial.println("The bluetooth gates are open.\n Connect to HC-05 from any other bluetooth device with 1234 as pairing key!.");
 
}
 
void loop()
{

  // Feed any data from bluetooth to Terminal.
  if (EEBlue.available()){
    Serial.write(EEBlue.read());
    SPEED = Serial.read();

  }
  // Feed all data from termial to bluetooth
  if (Serial.available()){
    bt = (Serial.read());
    Serial.print(bt);
    Serial.print("\n");Serial.print("----\n");
   if(bt == '0')        //move forwards 
    { 
     Serial.print("Inside F\n");
      analogWrite(outPin1,SPEED); 
      analogWrite(outPin2,0); 
      analogWrite(outPin3,SPEED); 
      analogWrite(outPin4,0); 
      delay(1000);
    } 
    else if (bt == '1')       //move backwards 
    {Serial.print("Inside B\n"); 
      analogWrite(outPin1,0); 
      analogWrite(outPin2,SPEED); 
      analogWrite(outPin3,0); 
      analogWrite(outPin4,SPEED); 
      delay(1000);
    } 
    else if (bt == '4')     //stop!! 
    {    Serial.print("Inside S\n");
      analogWrite(outPin1,0); 
      analogWrite(outPin2,0); 
      analogWrite(outPin3,0); 
      analogWrite(outPin4,0); 
      delay(1000);
    } 
    else if (bt == '2')    //right 
    {Serial.print("Inside R\n");
      analogWrite(outPin1,SPEED); 
      analogWrite(outPin2,0); 
      analogWrite(outPin3,0); 
      analogWrite(outPin4,0); 
      delay(1000);
    } 
    else if (bt == '3')     //left 
    { Serial.print("Inside L\n");
      analogWrite(outPin1,0); 
      analogWrite(outPin2,0); 
      analogWrite(outPin3,SPEED); 
      analogWrite(outPin4,0); 
      delay(1000);
    } else {
     Serial.print("none");
    }
      analogWrite(outPin1,0); 
      analogWrite(outPin2,0); 
      analogWrite(outPin3,0); 
      analogWrite(outPin4,0); 
  }
}