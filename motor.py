from machine import Pin, PWM
import utime

# Initialize the pin outside the function
servo_pin = Pin(16)
servo_pwm = PWM(servo_pin)
servo_pwm.freq(50)

def set_servo_angle(angle, pwm):
    duty = int((angle / 180) * 8000 + 1000)
    pwm.duty_u16(duty)

# Use the function
desired_angle = 120
set_servo_angle(desired_angle, servo_pwm)
utime.sleep(2)
                                                                                                                                                                                                           
                                                                                                                                                                                                           