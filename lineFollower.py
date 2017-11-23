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

        print(lsens, csens, rsens)

        if lsens == 0 and csens == 0 and rsens == 0:
            roomba.moveBackward(100)
            print("BCK")
        elif lsens == 0 and csens == 0 and rsens == 1:
            roomba.turnRight(30)
            print("RGHT")
        elif lsens == 0 and csens == 1 and rsens == 0:
            roomba.moveForward(100)
            print("FWD")
        elif lsens == 0 and csens == 1 and rsens == 1:
            roomba.softRight(25)
            print("SRGHT")
        elif lsens == 1 and csens == 0 and rsens == 0:
            roomba.turnLeft(30)
            print("LEFT")
        elif lsens == 1 and csens == 0 and rsens == 1:
            roomba.stop()
        elif lsens == 1 and csens == 1 and rsens == 0:
            roomba.softLeft(25)
            print("SLEFT")
        elif lsens == 1 and csens == 1 and rsens == 1:
            roomba.moveForward(100)
            print("FWD")


main()
