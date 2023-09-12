/**
 * @file main.cpp
 * @brief Flow Meter Control using PID
 */

// Define motor control and flow meter pin
#define Motor_pin 6 /**< Motor control pin */
#define flowMeter_pin A1 /**< Flow meter pin */

/**
 * @class PID_Controller
 * @brief PID Controller class for flow meter control
 */
class PID_Controller {
public:
  /**
   * @brief Constructor
   * @param kp Proportional gain
   * @param ki Integral gain
   * @param kd Derivative gain
   * @param Target_Rate Target flow rate (CFM)
   */
  PID_Controller(double kp, double ki, double kd, double Target_Rate)
      : kp(kp), ki(ki), kd(kd), Target_Rate(Target_Rate) {
    error = 0;
    integral = 0;
    derivative = 0;
    previnput = 0;
  }

  /**
   * @brief Calculate the PID output
   * @param input Current flow rate
   * @return PID output
   */
  double calc(double input) {
    error = Target_Rate - input;
    integral += error;
    derivative = input - previnput;
    previnput = input;
    double output = kp * error + ki * integral + kd * derivative;
    return output;
  }

private:
  double kp; /**< Proportional gain */
  double ki; /**< Integral gain */
  double kd; /**< Derivative gain */
  double Target_Rate; /**< Target flow rate (CFM) */
  double error; /**< Error term */
  double integral; /**< Integral term */
  double derivative; /**< Derivative term */
  double previnput; /**< Previous input value */
};

// Define PID gains and setpoint (Target_Rate)
double kp = 1.5; /**< Proportional gain */
double ki = 1.3; /**< Integral gain */
double kd = 0.5; /**< Derivative gain */
double Target_Rate = 90.0; /**< Target flow rate (CFM) */

// Create a PID controller
PID_Controller pid(kp, ki, kd, Target_Rate);

/**
 * @brief Setup function
 */
void setup() {
  Serial.begin(9600);
  // Set up pin modes
  pinMode(flowMeter_pin, INPUT);
  pinMode(Motor_pin, OUTPUT);
}

/**
 * @brief Loop function
 */
void loop() {
  // Read flow meter value and convert it to CFM
  int flowMeterValue = analogRead(flowMeter_pin);
  double flowRate = map(flowMeterValue, 0, 1023, 0, 150); // (0, 1023) corresponds to the voltage range of 0 to 5V, (0, 150) represents the flow rate range

  // Compute motor speed using PID controller
  double pid_out = pid.calc(flowRate);

  // Scale PID output to motor speed range
  double motorspeed = map(pid_out, 0, 255, 0, 255); //(Min,Max) output Range, (Min,Max) speed Range.

  // Write the motor output based on the PID output
  analogWrite(Motor_pin, motorspeed);

  Serial.print("Flow rate: ");
  Serial.print(flowRate);
  Serial.print(" PID output: ");
  Serial.print(pid_out);
  Serial.print(" Motor speed: ");
  Serial.println(motorspeed);
  delay(1000);
}