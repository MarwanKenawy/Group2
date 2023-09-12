#include <PID_v1.h>
// Define motor control, flow meter pin
#define Motor_pin 6
#define flowMeter_pin A1//analog pin
double flowRate = 0;
// Define PID parametersdouble now=millis();
double kp =1.5 ;// Proportional gain
double ki =1.3 ; // Integral gain 
double kd =0.5 ; // Derivative gain 
double Target_Rate=90;//CFM
double input,output; 
 // Initialize PID controller
PID pid(&input,&output,&Target_Rate,kp,ki,kd,DIRECT);
void setup() {
  Serial.begin(9600);
  // Set up pin modes
  pinMode(flowMeter_pin,INPUT);
  pinMode(Motor_pin,OUTPUT);
  // Initialize PID controller
  pid.SetMode(AUTOMATIC);
  pid.SetSampleTime(1000); //milliseconds  
}
void loop() {
  // Read flow meter value and convert it  to CFM
  int flowMeterValue=analogRead(flowMeter_pin);
  flowRate=map(flowMeterValue,0,1023,0,150); // flowRate=flowMeterValue*150/1023.(0 and 1023):corresponding to the voltage range of 0 to 5V,(0, 150):Min ,Max flowrate.Assuming a linear calibration
  // Update PID input value
  input=flowRate;
  pid.Compute();// Compute PID output
  double motorspeed = map(output,0,255,0,255);//(Min,Max) output Range,(Min,Max) speed Range.speed=pid_out*255/255.
  // Write the motor output based on the PID output
   analogWrite(Motor_pin,motorspeed);
                 /*if (flowRate== Target_Rate) {  
                analogWrite(Motor_pin,motorspeed); // adjust the motor based on PID output
                }
                 else { 
                  analogWrite(Motor_pin,0); // turn off the suction cleaner
                   }*/
  Serial.print("Flow rate:");
  Serial.print(flowRate);
 Serial.print("PID output:");
 Serial.print(output);
  Serial.print("motor speed:");
  Serial.println(motorspeed);
  delay(1000); 
}
