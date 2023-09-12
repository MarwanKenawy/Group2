import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# given
R = 20 
THETA1 = 0
THETA2 = 120
THETA3 = 240

#
# function to calculate the angular velocity on each motor
#
def calculate_motor_velocities(Vx, Vy, omega):
    vx1 = Vx - R * math.sin(math.radians(THETA1))
    vy1 = Vy - R * math.cos(math.radians(THETA1))
    v1 = math.sqrt(vx1**2 + vy1**2) + R * math.radians(omega)

    vx2 = Vx - R * math.sin(math.radians(THETA2))
    vy2 = Vy - R * math.cos(math.radians(THETA2))
    v2 = math.sqrt(vx2**2 + vy2**2) + R * math.radians(omega)

    vx3 = Vx - R * math.sin(math.radians(THETA3))
    vy3 = Vy - R * math.cos(math.radians(THETA3))
    v3 = math.sqrt(vx3**2 + vy3**2) + R * math.radians(omega)
    return v1, v2, v3



#
# positional PID Control
#
def simulate_robot_movement(Vx, Vy, omega, target_position=None):
    dt = 0.1 
    total_time = 10
    num_steps = int(total_time / dt)

    # Initials
    x = 0
    y = 0 
    theta = 0 

    # PID
    Kp = 0.5
    Ki = 0.1
    Kd = 0.2

    # PID variables
    integral = 0
    previous_error = 0 #error is initially set to 0

    time = []
    x_data = []
    y_data = []

    for step in range(num_steps):
        # Calculate motor velocity
        v1, v2, v3 = calculate_motor_velocities(Vx, Vy, omega)

        # Perform PID control
        if target_position is not None:
            error = math.sqrt((target_position[0] - x)**2 + (target_position[1] - y)**2)
            integral += error * dt
            derivative = (error - previous_error) / dt

            # PID control output
            pid_output = Kp * error + Ki * integral + Kd * derivative

            # Update velocities based on PID control output
            v1 += pid_output
            v2 += pid_output
            v3 += pid_output

            previous_error = error

        # Update robot state
        x += (v1 + v2 + v3) * math.cos(math.radians(theta)) * dt
        y += (v1 + v2 + v3) * math.sin(math.radians(theta)) * dt
        theta += omega * dt

        # Store data
        time.append(step * dt)
        x_data.append(x)
        y_data.append(y)

    return time, x_data, y_data
