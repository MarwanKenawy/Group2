import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
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


# drive each motor using cytron driver (PWM = RPM)
def drive_motors(Omega1, Omega2, Omega3):
    max_pwm = 255  # considered that the max RPM of 
    max_speed =22  # considered that the max speed of motor is 22
    
    pwm1 = int((Omega1 / max_speed) * max_pwm)
    pwm2 = int((Omega2 / max_speed) * max_pwm)
    pwm3 = int((Omega3 / max_speed) * max_pwm)
    return pwm1,pwm2 ,pwm3


#
# positional PID Control
#
def simulate_robot_movement(Vx, Vy, omega, target_position=None):
    dt = 0.1
    total_time = 10
    num_steps = int(total_time / dt)

    x = 0
    y = 0
    theta = 0

    Kp = 0.5
    Ki = 0.1
    Kd = 0.2

    integral = 0
    previous_error = 0

    time = []
    x_data = []
    y_data = []
    theta_data = []  # Store the robot's orientation

    for step in range(num_steps):
        v1, v2, v3 = calculate_motor_velocities(Vx, Vy, omega)
        pwm1, pwm2, pwm3 = drive_motors(v1, v2, v3)

        if target_position is not None:
            error = math.sqrt((target_position[0] - x)**2 + (target_position[1] - y)**2)
            integral += error * dt
            derivative = (error - previous_error) / dt
            pid_output = Kp * error + Ki * integral + Kd * derivative

            pwm1 += pid_output
            pwm2 += pid_output
            pwm3 += pid_output

            previous_error = error

        x += (pwm1 + pwm2 + pwm3) * math.cos(math.radians(theta)) * dt
        y += (pwm1 + pwm2 + pwm3) * math.sin(math.radians(theta)) * dt
        theta += omega * dt

        time.append(step * dt)
        x_data.append(x)
        y_data.append(y)
        theta_data.append(theta)

    X_global = []
    Y_global = []

    for i in range(len(time)):
        X_local = x_data[i]
        Y_local = y_data[i]
        theta_i = theta_data[i]

        X_global.append(X_local * math.cos(math.radians(theta_i)) - Y_local * math.sin(math.radians(theta_i)))
        Y_global.append(X_local * math.sin(math.radians(theta_i)) + Y_local * math.cos(math.radians(theta_i)))

    return time, x_data, y_data, X_global, Y_global, theta_data



# Create an animation
def animate_robot_movement():
    #Example of values to make a simulation
    Vx = 5  
    Vy = 0
    omega = 45  

    target_position = [100, 100]  # Example target position

    time, x_data, y_data, X_global, Y_global, theta_data = simulate_robot_movement(Vx, Vy, omega, target_position)

    fig, ax = plt.subplots()

    def update(frame):
        ax.clear()
        ax.plot(X_global[:frame], Y_global[:frame], label='Robot Path')
        ax.set_xlabel('X (Global)')
        ax.set_ylabel('Y (Global)')
        ax.legend()

    ani = FuncAnimation(fig, update, frames=len(time), repeat=False, interval=100)
    plt.show()


animate_robot_movement()