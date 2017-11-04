import RPi.GPIO as GPIO
import time
import roomba

# Pins for the sensors
left = 10
cent = 9
rght = 11
sonarout = 98
sonarin = 99
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
    lsens = GPIO.input(left)
    csens = GPIO.input(cent)
    rsens = GPIO.input(rght)

    if lsens == 0 and csens == 0 and rsens == 0:
        return True
    else:
        return False


def main():
    while True:
        if distance() < 50:
            roomba.moveForward(100)
            if areWeClear() is False:
                roomba.moveBackward(100)
                time.sleep(0.5)
        else:
            roomba.softLeft(50)
    return True
