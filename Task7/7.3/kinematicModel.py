import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# Robot Constants
L = 0.2  # Distance between the two wheels (wheelbase)
R = 0.2  # Radius of the wheels

# Function to calculate wheel angular velocities
def calculate_wheel_angular_velocities(Vx, Vy, Omega):
    """
    Calculates the angular velocity of each wheel based on the linear velocity
    and angular velocity of the robot.
    """
    V1 = Vx + (L / 2) * Omega
    V2 = -0.5 * Vx + (L * np.sqrt(3) / 2) * Vy + (L / 2) * Omega
    V3 = -0.5 * Vx - (L * np.sqrt(3) / 2) * Vy + (L / 2) * Omega

    Omega1 = V1 / R
    Omega2 = V2 / R
    Omega3 = V3 / R

    return Omega1, Omega2, Omega3

# Function to drive each motor using a Cytron driver (PWM = RPM)
def drive_motors(Omega1, Omega2, Omega3):
    """
    Drives each motor using a Cytron driver.
    Assumes that the PWM value provided is proportional to the desired RPM.
    """
    # Code to drive the motors using Cytron driver
    # PWM1 = Omega1
    # PWM2 = Omega2
    # PWM3 = Omega3
    # ...

# Function for positional PID control
def positional_pid_control(current_position, target_position, dt):
    """
    Implements positional PID control to drive the robot to the target position.
    """
    Kp = 1.0  # Proportional gain
    Ki = 0.1  # Integral gain
    Kd = 0.5  # Derivative gain

    integral_error = np.array([0.0, 0.0])  # Initialize integral error
    previous_error = np.array([0.0, 0.0])  # Initialize previous error

    while True:
        # Calculate error
        error = target_position - current_position

        # Update integral error
        integral_error += error * dt

        # Calculate PID control output
        control_output = Kp * error + Ki * integral_error + Kd * (error - previous_error) / dt

        # Calculate wheel velocities
        Vx = control_output[0]
        Vy = control_output[1]
        Omega = 0.0  # Assume no angular velocity for simplicity

        Omega1, Omega2, Omega3 = calculate_wheel_angular_velocities(Vx, Vy, Omega)

        # Drive the motors
        drive_motors(Omega1, Omega2, Omega3)

        # Update previous error
        previous_error = error

        # Update current position
        current_position += np.array([Vx, Vy]) * dt

        # Check if target position reached
        if np.linalg.norm(error) < 0.01:
            break

        # Sleep for a small duration
        time.sleep(dt)

# Example usage
current_position = np.array([0.0, 0.0])  # Initial position
target_position = np.array([2.0, 3.0])  # Target position
dt = 0.1  # Control loop time step

positional_pid_control(current_position, target_position, dt)