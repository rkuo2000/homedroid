/* This example shows how to use continuous mode to take
range measurements with the VL53L0X. It is based on
vl53l0x_ContinuousRanging_Example.c from the VL53L0X API.

The range readings are in units of mm. */

#include <Wire.h>
#include <VL53L0X.h>

const int motorL0 = D5;
const int motorL1 = D6;
const int motorR0 = D7;
const int motorR1 = D8;

VL53L0X sensor;
String inputString = "";
boolean stringComplete = false;
int distance;


void setup()
{
  pinMode(motorL0, OUTPUT);
  pinMode(motorL1, OUTPUT);
  pinMode(motorR0, OUTPUT);
  pinMode(motorR1, OUTPUT);
  stop();
  
  Serial.begin(9600);
  Wire.begin();
  inputString.reserve(200);

  sensor.init();
  sensor.setTimeout(500);

  // Start continuous back-to-back mode (take readings as
  // fast as possible).  To use continuous timed mode
  // instead, provide a desired inter-measurement period in
  // ms (e.g. sensor.startContinuous(100)).
  sensor.startContinuous();
  Serial.println("NodeMCU start...\n\r");
}

void loop()
{ 
  //Serial.print(sensor.readRangeContinuousMillimeters());
  distance = sensor.readRangeContinuousMillimeters();
  if (distance<50) 
  { 
    turnRight(); delay(100);
    forward();   delay(100);
  }
  //if (sensor.timeoutOccurred()) { Serial.print(" TIMEOUT"); }
  //Serial.println();
   
   while (Serial.available()) {
    char inChar = (char)Serial.read();
    inputString += inChar; 
    if (inChar == '\n') 
      stringComplete = true;
  } 
  
  if (stringComplete) 
  {
     Serial.println("UART:" + inputString);
     inputString.trim(); 
     if (inputString=="stop") stop();
     if (inputString=="forward") forward();   
     if (inputString=="backward") backward();      
     if (inputString=="turnRight") turnRight();
     if (inputString=="turnLeft") turnLeft();  
     inputString = "";
     stringComplete = false;
  }
     
}

void stop()
{
  digitalWrite(motorL0, LOW);
  digitalWrite(motorL1, LOW);
  digitalWrite(motorR0, LOW);
  digitalWrite(motorR1, LOW);
}

void forward()
{
  digitalWrite(motorL0, HIGH);
  digitalWrite(motorL1, LOW);
  digitalWrite(motorR0, HIGH);
  digitalWrite(motorR1, LOW);  
}

void backward()
{
  digitalWrite(motorL0, LOW);
  digitalWrite(motorL1, HIGH);
  digitalWrite(motorR0, LOW);
  digitalWrite(motorR1, HIGH);  
}

void turnRight()
{
  digitalWrite(motorL0, LOW);
  digitalWrite(motorL1, HIGH);
  digitalWrite(motorR0, HIGH);
  digitalWrite(motorR1, LOW);  
}

void turnLeft()
{
  digitalWrite(motorL0, HIGH);
  digitalWrite(motorL1, LOW);
  digitalWrite(motorR0, LOW);
  digitalWrite(motorR1, HIGH);  
}

