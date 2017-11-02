import RPi.GPIO as GPIO
import roomba

# Pins for the LIGHT sensors
left = 10
cent = 9
rght = 11
# GPIO general setup
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
# GPIO setup for LIGHT sensors
GPIO.setup(left, GPIO.IN)
GPIO.setup(cent, GPIO.IN)
GPIO.setup(rght, GPIO.IN)


def main():
    while True:
        lsens = GPIO.input(left)
        csens = GPIO.input(cent)
        rsens = GPIO.input(rght)

        if lsens == 0 and csens == 0 and rsens == 0:
            roomba.moveBackward(40)
        elif lsens == 0 and csens == 0 and rsens == 1:
            roomba.turnRight(30)
        elif lsens == 0 and csens == 1 and rsens == 0:
            roomba.moveForward(40)
        elif lsens == 0 and csens == 1 and rsens == 1:
            roomba.softRight(30)
        elif lsens == 1 and csens == 0 and rsens == 0:
            roomba.turnLeft(30)
        elif lsens == 1 and csens == 0 and rsens == 1:
            roomba.stop()
        elif lsens == 1 and csens == 1 and rsens == 0:
            roomba.softLeft(30)
        elif lsens == 1 and csens == 1 and rsens == 1:
            roomba.moveForward(40)


main()
