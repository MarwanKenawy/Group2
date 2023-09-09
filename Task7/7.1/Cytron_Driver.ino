//define Motor pins
#define MotorSpeed 8
#define MotorDir 9

double SpeedVal_original = 0, SpeedVal_filtered = 0;
double smoothing_factor = 0.9;

void setup() {
  //Declaration of pins mode
  pinMode(MotorSpeed, OUTPUT);
  pinMode(MotorDir, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  //clockwise direction
  digitalWrite(MotorDir, LOW);
  SpeedVal_filtered = 0;

  //loop increases to max speed
  for(SpeedVal_original = 0;SpeedVal_original<=255;SpeedVal_original++)
  {
    //Simple Exponential filter (Smoothing filter)
    SpeedVal_filtered = smoothing_factor * SpeedVal_filtered + (1 - smoothing_factor) * SpeedVal_original;
    
    analogWrite(MotorSpeed, SpeedVal_filtered);
    Serial.print("SpeedVal before filter: ");
    Serial.println(SpeedVal_original);
    Serial.print("SpeedVal after filter: ");
    Serial.println(SpeedVal_filtered);
    delay(50);
  }
  analogWrite(MotorSpeed, 0);
  SpeedVal_filtered = 0;

  //anticlockwise direction
  digitalWrite(MotorDir, HIGH);

  //loop increases to max speed
  for(SpeedVal_original = 0;SpeedVal_original<=255;SpeedVal_original++)
  {
    //Simple Exponential filter (Smoothing filter)
    SpeedVal_filtered = smoothing_factor * SpeedVal_filtered + (1 - smoothing_factor) * SpeedVal_original;
    analogWrite(MotorSpeed, SpeedVal_filtered);
    Serial.print("SpeedVal: ");
    Serial.println(SpeedVal_filtered);
    delay(50);
  }
  analogWrite(MotorSpeed, 0);
}
