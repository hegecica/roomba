# This file stores the GPIO configuration
# for our RoboCar. Please don't edit it
# unless it's REALLY necessary. Thank you ;)

import RPi.GPIO as GPIO
# Pins for the LEFT motor
ain1 = 17
ain2 = 27
pwma = 22
# Pins for the RGHT motor
bin1 = 16
bin2 = 20
pwmb = 21
# Pins for the LIGHT sensors
left = 10
cent = 9
rght = 11
# GPIO general setup
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
# GPIO setup for LEFT motor
GPIO.setup(ain1, GPIO.OUT)
GPIO.setup(ain2, GPIO.OUT)
GPIO.setup(pwma, GPIO.OUT)
leftmotor = GPIO.PWM(pwma, 50)
# GPIO setup for RGHT motor
GPIO.setup(bin1, GPIO.OUT)
GPIO.setup(bin2, GPIO.OUT)
GPIO.setup(pwmb, GPIO.OUT)
rightmotor = GPIO.PWM(pwmb, 50)
# GPIO setup for LIGHT sensors
GPIO.setup(left, GPIO.IN)
GPIO.setup(cent, GPIO.IN)
GPIO.setup(rght, GPIO.IN)
