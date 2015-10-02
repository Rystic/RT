#include <DualVNH5019MotorShield.h>

DualVNH5019MotorShield md;

int forwardSpeed = 200;
int reverseSpeed = -200;
int fastfwdSpeed = 300;
int fastrevSpeed = -300;
int brakeMotors = 0;



void stopIfFault()
{
  if (md.getM1Fault())
  {
    Serial.println("M1 fault");
    while(1);
  }
  if (md.getM2Fault())
  {
    Serial.println("M2 fault");
    while(1);
  }
}

void setup()
{
  Serial.begin(9600);
  Serial.println("Dual VNH5019 Motor Shield");
  md.init();
}

void loop()
{

}

void serialEvent()
{
  while (Serial.available())
  {
    char inChar = (char) Serial.read();
    if(inChar == 'w')
    {
      md.setM1Speed(forwardSpeed);
      md.setM2Speed(forwardSpeed);
    }
    if(inChar == 's')
    {
      md.setM1Speed(reverseSpeed);
      md.setM2Speed(reverseSpeed);
    }
    if(inChar == 'd')
    {
      md.setM1Speed(forwardSpeed);
      md.setM2Speed(reverseSpeed);
    }
    if(inChar == 'a')
    {
      md.setM1Speed(reverseSpeed);
      md.setM2Speed(forwardSpeed);
    }
    if(inChar == 'e')
    {
      md.setM1Speed(brakeMotors);
      md.setM2Speed(brakeMotors);
    }
    if(inChar == 'E')
    {
      md.setM1Speed(brakeMotors);
      md.setM2Speed(brakeMotors);
    }
     if(inChar == 'W')
    {
      md.setM1Speed(fastfwdSpeed);
      md.setM2Speed(fastfwdSpeed);
    }
    if(inChar == 'S')
    {
      md.setM1Speed(fastrevSpeed);
      md.setM2Speed(fastrevSpeed);
    }
    if(inChar == 'D')
    {
      md.setM1Speed(fastfwdSpeed);
      md.setM2Speed(brakeMotors);
    }
    if(inChar == 'A')
    {
      md.setM1Speed(brakeMotors);
      md.setM2Speed(fastfwdSpeed);
    }  
    delay(1000);
  }
}



