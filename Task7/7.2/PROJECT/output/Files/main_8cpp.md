---
title: input/main.cpp
summary: Flow Meter Control using PID. 

---

# input/main.cpp

Flow Meter Control using PID. 

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[PID_Controller](Classes/class_p_i_d___controller.md)** <br>PID Controller class for flow meter control.  |

## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[setup](Files/main_8cpp.md#function-setup)**()<br>Setup function.  |
| void | **[loop](Files/main_8cpp.md#function-loop)**()<br>Loop function.  |

## Attributes

|                | Name           |
| -------------- | -------------- |
| double | **[kp](Files/main_8cpp.md#variable-kp)**  |
| double | **[ki](Files/main_8cpp.md#variable-ki)**  |
| double | **[kd](Files/main_8cpp.md#variable-kd)**  |
| double | **[Target_Rate](Files/main_8cpp.md#variable-target-rate)**  |
| [PID_Controller](Classes/class_p_i_d___controller.md)(kp, ki, kd, Target_Rate) | **[pid](Files/main_8cpp.md#variable-pid)**  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[Motor_pin](Files/main_8cpp.md#define-motor-pin)**  |
|  | **[flowMeter_pin](Files/main_8cpp.md#define-flowmeter-pin)**  |


## Functions Documentation

### function setup

```cpp
void setup()
```

Setup function. 

### function loop

```cpp
void loop()
```

Loop function. 


## Attributes Documentation

### variable kp

```cpp
double kp = 1.5;
```


Proportional gain 


### variable ki

```cpp
double ki = 1.3;
```


Integral gain 


### variable kd

```cpp
double kd = 0.5;
```


Derivative gain 


### variable Target_Rate

```cpp
double Target_Rate = 90.0;
```


Target flow rate (CFM) 


### variable pid

```cpp
PID_Controller(kp, ki, kd, Target_Rate) pid;
```



## Macros Documentation

### define Motor_pin

```cpp
#define Motor_pin 6
```


Motor control pin 


### define flowMeter_pin

```cpp
#define flowMeter_pin A1
```


Flow meter pin 


## Source code

```cpp

// Define motor control and flow meter pin
#define Motor_pin 6 
#define flowMeter_pin A1 
class PID_Controller {
public:
  PID_Controller(double kp, double ki, double kd, double Target_Rate)
      : kp(kp), ki(ki), kd(kd), Target_Rate(Target_Rate) {
    error = 0;
    integral = 0;
    derivative = 0;
    previnput = 0;
  }

  double calc(double input) {
    error = Target_Rate - input;
    integral += error;
    derivative = input - previnput;
    previnput = input;
    double output = kp * error + ki * integral + kd * derivative;
    return output;
  }

private:
  double kp; 
  double ki; 
  double kd; 
  double Target_Rate; 
  double error; 
  double integral; 
  double derivative; 
  double previnput; 
};

// Define PID gains and setpoint (Target_Rate)
double kp = 1.5; 
double ki = 1.3; 
double kd = 0.5; 
double Target_Rate = 90.0; 
// Create a PID controller
PID_Controller pid(kp, ki, kd, Target_Rate);

void setup() {
  Serial.begin(9600);
  // Set up pin modes
  pinMode(flowMeter_pin, INPUT);
  pinMode(Motor_pin, OUTPUT);
}

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
```


-------------------------------

Updated on 2023-09-12 at 14:02:54 +0300
