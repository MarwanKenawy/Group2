
# Driving the Kinematic model for the
omni wheel configuration

---

# Omni wheel configuration :

---

The omni wheel configuration is a type of wheeled robot design that utilizes special wheels called omni wheels or mecanum wheels. These wheels have small rollers or rollers arranged at an angle around their circumference, allowing for both forward and sideways movement without the need for steering or turning the wheels. To drive the kinematic model for the omni wheel configuration, we can use a mathematical representation known as the mecanum drive kinematics.

The main advantage of omni-wheels is their ability to move in any direction without requiring complicated steering mechanisms. By controlling the speed and direction of rotation of each wheel independently, the robot can achieve smooth translations and rotations.

Omni-wheels find applications in various fields, including robotics, automation, and mobile platforms where precise and agile motion is required. They are often used in robotic platforms such as AGVs (Automated Guided Vehicles), robotic arms, and omnidirectional mobile robots.

# Local kinematics equations :

---

![WhatsApp Image 2023-09-11 at 21.47.57.jpg](Driving%20the%20Kinematic%20model%20for%20the%20omni%20wheel%20con%206620bc5b708c48afadaa71c054953628/WhatsApp_Image_2023-09-11_at_21.47.57.jpg)

$$
V_{1X} = -V_1 \cos \alpha
$$

$$
V_{1Y} = V_1 \sin \alpha
$$

where 

$$
\alpha = 90 - \phi
$$

---

$$
V_{2X} = -V_2 \cos \alpha
$$

$$
V_{2Y} = -V_2 \sin \alpha
$$

---

$$
V_{3X} = V_3 , V_{3Y} = 0
$$

So ,

$$
V_X = V_3 - V_1 \cos \alpha - V_2 \cos \alpha
$$

$$
V_Y = V_1 \sin \alpha - V_2 \sin \alpha
$$

$$
V_\theta = \frac{V_1 + V_2 + V_3}{R}
$$

$V_{i(1,2,3)} = \omega .r$  where   $r$ = radius of wheel 

## Describing the dynamics with matrices :

Let’s assume that $\phi$ = 30 $\degree$ So $\alpha$ = 60 $\degree$ .So, $\sin \alpha = \frac{\sqrt3}{2}$ and $\cos \alpha = \frac{1}{2}$.

Therefore the matrix should be : 
```math
 \begin{bmatrix}
 V_{X}\\V_{Y}\\V_\theta
 \end{bmatrix}

 =
  \begin{bmatrix}
  -\cos \alpha &  -\cos \alpha & 1\\\sin \alpha &  -\sin \alpha & 0\\\frac{1}{R} &  \frac{1}{R} & \frac{1}{R}\\
    \end{bmatrix} 
   
  
    \begin{bmatrix} V_{1}\\V_{2}\\V_3 \end{bmatrix}

```
and then we substitute with previous givens.

# Global kinematics equations :

![WhatsApp Image 2023-09-12 at 13.39.30.jpg](Driving%20the%20Kinematic%20model%20for%20the%20omni%20wheel%20con%206620bc5b708c48afadaa71c054953628/WhatsApp_Image_2023-09-12_at_13.39.30.jpg)

We need to transform the local frame to the  global frame and in order to do that we need to decomposite local velocities into global velocities.

So, 

$$
V_{xg} = V_{xl} \cos \theta -V_{yl}\sin \theta
$$

$$
V_{yg} = V_{xl} \sin \theta +V_{yl}\cos \theta
$$

$$
\omega = \omega
$$

