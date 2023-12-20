import RPi.GPIO as GPIO
import time

# Setup
motor1A = 26  # GPIO pin connected to Motor1A on motor driver
motor1B = 16  # GPIO pin connected to Motor1B on motor driver
motor2A = 20  # GPIO pin connected to Enable1 on motor driver
motor2B = 21  # GPIO pin connected to Enable1 on motor driver
sensor_pin = 4
# Use GPIO numbering
GPIO.setmode(GPIO.BCM)  # Use Broadcom SOC channel numbering

# Define the GPIO pin
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(motor1A, GPIO.OUT)
GPIO.setup(motor1B, GPIO.OUT)
GPIO.setup(motor2A, GPIO.OUT)
GPIO.setup(motor2B, GPIO.OUT)

# Function to control the motor
def motor_forward():
    GPIO.output(motor1A, GPIO.HIGH)
    GPIO.output(motor1B, GPIO.LOW)
    GPIO.output(motor2A, GPIO.HIGH)
    GPIO.output(motor2B, GPIO.LOW)

def motor_backward():
    GPIO.output(motor1A, GPIO.LOW)
    GPIO.output(motor1B, GPIO.HIGH)
    GPIO.output(motor2A, GPIO.LOW)
    GPIO.output(motor2B, GPIO.HIGH)

def motor_stop():
    GPIO.output(motor1B, GPIO.LOW)
    GPIO.output(motor1A, GPIO.LOW)
    GPIO.output(motor2A, GPIO.LOW)
    GPIO.output(motor2B, GPIO.LOW)

def motor_spin_right():
    GPIO.output(motor1B, GPIO.HIGH)
    GPIO.output(motor1A, GPIO.LOW)
    GPIO.output(motor2A, GPIO.HIGH)
    GPIO.output(motor2B, GPIO.LOW)

def motor_spin_left():
    GPIO.output(motor1B, GPIO.LOW)
    GPIO.output(motor1A, GPIO.HIGH)
    GPIO.output(motor2A, GPIO.LOW)
    GPIO.output(motor2B, GPIO.HIGH)



def measure_pulse(pin):
    # Measure the time of the high pulse
    start_time = time.time()
    while GPIO.input(pin) == 0:
        start_time = time.time()

    end_time = time.time()
    while GPIO.input(pin) == 1:
        end_time = time.time()

    duration = end_time - start_time
    return duration

"""
try:
    while True:
        pulse_duration = measure_pulse(sensor_pin)
        # Convert pulse duration to distance (in cm or inches)
        # The scaling factor 58.2 cm or 148.2 inches is based on the speed of sound.
        # You may need to adjust the scaling factor based on your specific sensor's datasheet.
        distance = pulse_duration * 1000000 / 147 # 148.2  # Distance in cm
        print("Distance: {:.2f} cm".format(distance))

        if distance < 9.0:
            motor_backward()
        if distance > 20.0:
            motor_forward()
        time.sleep(0.25)
except KeyboardInterrupt:
    GPIO.cleanup()
"""
if __name__ == "__main__":
    motor_spin_right()
    #motor_forward()
    time.sleep(0.25)
    GPIO.cleanup()
