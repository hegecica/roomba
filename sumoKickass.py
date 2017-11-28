import RPi.GPIO as GPIO
import time
import roomba

# Pins for the sensors
left = 10
cent = 9
rght = 11
sonarout = 14
sonarin = 15
# GPIO general setup
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
# GPIO setup for the sensors
GPIO.setup(left, GPIO.IN)
GPIO.setup(cent, GPIO.IN)
GPIO.setup(rght, GPIO.IN)
GPIO.setup(sonarout, GPIO.OUT)
GPIO.setup(sonarin, GPIO.IN)


def distance():
    pingtime = 0
    echotime = 0
    GPIO.output(sonarout, GPIO.LOW)
    GPIO.output(sonarout, GPIO.HIGH)
    pingtime = time.time()
    time.sleep(0.00001)
    GPIO.output(sonarout, GPIO.LOW)
    while GPIO.input(sonarin) == 0:
        pingtime = time.time()
    while GPIO.input(sonarin) == 1:
        echotime = time.time()
    if (echotime is not None) and (pingtime is not None):
        elapsedtime = echotime - pingtime
        distance = elapsedtime * 17000
    else:
        distance = 0
    return distance


def areWeClear():

    csens = GPIO.input(cent)

    if csens == 0:
        return True


def main():
    while True:
        if areWeClear() is not True:
            while areWeClear() is not True:
                roomba.moveBackward(100)
        else:
            while distance() < 50:
                if areWeClear() is not True:
                    break
                roomba.moveForward(100)
            while distance() >= 50:
                roomba.softLeft(35)
                time.sleep(0.1)


main()
