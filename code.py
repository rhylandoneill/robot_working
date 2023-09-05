import time
import board
import pwmio

from adafruit_motor import motor

right_motor_forward = board.GP12
right_motor_backward = board.GP13
left_motor_forward = board.GP16
left_motor_backward = board.GP17

pwm_La = pwmio.PWMOut(right_motor_forward, frequency=10000)
pwm_Lb = pwmio.PWMOut(right_motor_backward, frequency=10000)
pwm_Lc = pwmio.PWMOut(left_motor_forward, frequency=10000)
pwm_Ld = pwmio.PWMOut(left_motor_backward, frequency=10000)

Right_Motor = motor.DCMotor(pwm_La, pwm_Lb)
Right_Motor_speed = 0
Left_Motor = motor.DCMotor(pwm_Lc, pwm_Ld)
Left_Motor_speed = 0

while True:
    Right_Motor_speed = -1
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(2)
    Right_Motor_speed = 1
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(2)

    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(2)
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(2)
