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


def fwdcycle():
    GPIO.output(ain1, GPIO.LOW)
    GPIO.output(ain2, GPIO.HIGH)
    GPIO.output(bin1, GPIO.HIGH)
    GPIO.output(bin2, GPIO.LOW)
    leftmotor.start(0)
    rightmotor.start(0)
    leftmotor.ChangeDutyCycle(40)
    rightmotor.ChangeDutyCycle(40)


def backward():
    GPIO.output(ain1, GPIO.HIGH)
    GPIO.output(ain2, GPIO.LOW)
    GPIO.output(bin1, GPIO.LOW)
    GPIO.output(bin2, GPIO.HIGH)
    leftmotor.start(0)
    rightmotor.start(0)
    leftmotor.ChangeDutyCycle(70)
    rightmotor.ChangeDutyCycle(70)


def turnleft():
    GPIO.output(ain1, GPIO.HIGH)
    GPIO.output(ain2, GPIO.LOW)
    GPIO.output(bin1, GPIO.HIGH)
    GPIO.output(bin2, GPIO.LOW)
    leftmotor.start(0)
    rightmotor.start(0)
    leftmotor.ChangeDutyCycle(0)
    rightmotor.ChangeDutyCycle(25)


def turnright():
    GPIO.output(ain1, GPIO.LOW)
    GPIO.output(ain2, GPIO.HIGH)
    GPIO.output(bin1, GPIO.LOW)
    GPIO.output(bin2, GPIO.HIGH)
    leftmotor.start(0)
    rightmotor.start(0)
    leftmotor.ChangeDutyCycle(25)
    rightmotor.ChangeDutyCycle(0)


def stop():
    rightmotor.stop(0)
    leftmotor.stop(0)


def main():
    while True:
        lsens = GPIO.input(left)
        csens = GPIO.input(cent)
        rsens = GPIO.input(rght)

        if lsens == 0 and csens == 0 and rsens == 0:
            stop()
        elif lsens == 0 and csens == 0 and rsens == 1:
            turnright()
        elif lsens == 0 and csens == 1 and rsens == 0:
            fwdcycle()
        elif lsens == 0 and csens == 1 and rsens == 1:
            turnright()
        elif lsens == 1 and csens == 0 and rsens == 0:
            turnleft()
        elif lsens == 1 and csens == 0 and rsens == 1:
            print("THIS SHOULD NEVER HAPPEN!!!")
        elif lsens == 1 and csens == 1 and rsens == 0:
            turnleft()
        elif lsens == 1 and csens == 1 and rsens == 1:
            fwdcycle()
        print(lsens, csens, rsens)


main()
