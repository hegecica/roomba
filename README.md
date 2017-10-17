# Roomba the RoboCar
#### DoNotSteal:

Our little beast, _ElectronicRoombaBeast_ has its own little GitHub repository. Please, please do not steal anything from here WITHOUT mentioning us somewhere in your project log and/or program code.
Thank you so much!

_RoboGroup8_
## Short description of codes:
4directions.html:
> Required by webMove.py; This file contains the html table with the control buttons.

followTheLine.py:
> Kinda self explanatory I guess. Works as intended. Sometimes it drives **Roomba** insane and goes off the table... _Maybe it wants to commit suicide?_

keyboardControl.py:
> In the newest version: You get to control **Roomba** with the keyboard. You can select the direction with the WASD keys, and voila, **Roomba** starts to run! If you want to stop it, just press X. Pretty simple, huh?

lineFollower.py:
> Newer version of the 'followTheLine' script, it uses roomba.py library, so it can be stored in separate file, making this whole thing MUCH more readable. And turns are redefined as well.
__**This file is not tested yet!!!**__

README.md:
> This file... Really? Do we have to explain this? ;)

roomba.py:
> Custom library. Includes the GPIO configuration and the functions for the motors.

webMove.py:
> CherryPy + Roomba + 4directions.html = You can control the _Beast_ from your browser! Woohoo!
Usage: You press a direction, Roomba starts to run for 1 sec. That's it. We don't really like to overcomplicate things.
