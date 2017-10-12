import time
import RPi.GPIO as GPIO
# Pins for the LEFT motor
ain1 = 17
ain2 = 27
pwma = 22
# Pins for the RGHT motor
bin1 = 16
bin2 = 20
pwmb = 21

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


def fwdcycle():
    GPIO.output(ain1, GPIO.LOW)
    GPIO.output(ain2, GPIO.HIGH)
    GPIO.output(bin1, GPIO.HIGH)
    GPIO.output(bin2, GPIO.HIGH)
    leftmotor.start(0)
    rightmotor.start(0)
    leftmotor.ChangeDutyCycle(40)
    rightmotor.ChangeDutyCycle(40)
    print('FWD')


def stop():
    rightmotor.stop(0)
    leftmotor.stop(0)
    print('STOP')


def main():
    fwdcycle()
    time.sleep(1)
    stop()


main()
