import cherrypy
import time
import roomba

file = open('4directions.html')
index_html = file.read()
file.close()


class MotorControl(object):
    @cherrypy.expose
    def index(self):
        return index_html

    @cherrypy.expose
    def stfwd(self):
        roomba.moveForward(100)
        time.sleep(1)
        roomba.stop()
        return index_html

    @cherrypy.expose
    def stback(self):
        roomba.moveBackward(100)
        time.sleep(1)
        roomba.stop()
        return index_html

    @cherrypy.expose
    def tleft(self):
        roomba.turnLeft(100)
        time.sleep(0.1)
        roomba.stop()
        return index_html

    @cherrypy.expose
    def tright(self):
        roomba.turnRight(100)
        time.sleep(0.1)
        roomba.stop()
        return index_html

    @cherrypy.expose
    def nomove(self):
        roomba.stop()
        return index_html


cherrypy.server.socket_host = "0.0.0.0"  # 0.0.0.0 =>  listen on all interfaces
cherrypy.quickstart(MotorControl())
