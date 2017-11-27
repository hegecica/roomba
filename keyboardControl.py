import sys
import termios
import tty
import roomba


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def main():
    direction = ''
    while direction != "\x03":
        direction = getch()
        if direction == 'w':
            roomba.moveForward(100)
        elif direction == 's':
            roomba.moveBackward(100)
        elif direction == 'a':
            roomba.turnLeft(100)
        elif direction == 'd':
            roomba.turnRight(100)
        elif direction == 'x':
            roomba.stop()
        elif direction == "\x03":
            print('Exiting.. Bye!')
        else:
            print('INVALID:', direction)
    roomba.stop()


main()
