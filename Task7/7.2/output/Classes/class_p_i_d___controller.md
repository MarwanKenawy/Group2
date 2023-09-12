---
title: PID_Controller
summary: PID Controller class for flow meter control. 

---

# PID_Controller



PID Controller class for flow meter control. 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[PID_Controller](Classes/class_p_i_d___controller.md#function-pid-controller)**(double kp, double ki, double kd, double Target_Rate)<br>Constructor.  |
| double | **[calc](Classes/class_p_i_d___controller.md#function-calc)**(double input)<br>Calculate the PID output.  |

## Public Functions Documentation

### function PID_Controller

```cpp
inline PID_Controller(
    double kp,
    double ki,
    double kd,
    double Target_Rate
)
```

Constructor. 

**Parameters**: 

  * **kp** Proportional gain 
  * **ki** Integral gain 
  * **kd** Derivative gain 
  * **Target_Rate** Target flow rate (CFM) 


### function calc

```cpp
inline double calc(
    double input
)
```

Calculate the PID output. 

**Parameters**: 

  * **input** Current flow rate 


**Return**: PID output 

-------------------------------

Updated on 2023-09-12 at 14:02:54 +0300