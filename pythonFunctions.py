# This file contains our functions for the robocar
import gpioPinout


def fwdcycle():
    GPIO.output(ain1, GPIO.LOW)
    GPIO.output(ain2, GPIO.HIGH)
    GPIO.output(bin1, GPIO.LOW)
    GPIO.output(bin2, GPIO.HIGH)
    leftmotor.start(0)
    rightmotor.start(0)
    leftmotor.ChangeDutyCycle(40)
    rightmotor.ChangeDutyCycle(40)


def stop():
    rightmotor.stop(0)
    leftmotor.stop(0)


def main():
    fwdcycle()
    time.sleep(1)
    stop()


main()
