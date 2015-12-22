import webapp2
import os

from google.appengine.ext.webapp.template import render
from google.appengine.api import memcache
from google.appengine.ext import ndb

name_string = 'name'

# -- Pages --

class MainPage(webapp2.RequestHandler):
    def get(self):
        tmpl = os.path.join(os.path.dirname(__file__), 'templates/robots.html')
        self.response.write(render(tmpl, {'active_robots' : getActiveRobotNames()}))

class RegisterRobotPage(webapp2.RequestHandler):
    def post(self):
        active_robots = getActiveRobotNames()
        name = self.request.get(name_string)
        if active_robots.count(name) == 0:
            setNameInMemcache(name)
            robot = RobotEntity()
            robot.name = name
            robot_key = robot.put()

class PollActiveRobotsPage(webapp2.RequestHandler):
    def post(self):
        active_robots = getActiveRobotKeys()
        self.response.write("""<html><body><p>""")
        no_robots = True
        tmpl = os.path.join(os.path.dirname(__file__), 'templates/robot_info_block.html')
        for key in active_robots:
            name = key.get().name
            if memcache.get(name) is None:
                key.delete()
            else:
                no_robots = False
                self.response.write(render(tmpl, {'name' : name}))
        if no_robots:
            self.response.write("""no robots""")
        self.response.write("""</p></body></html>""")

class ControlPage(webapp2.RequestHandler):
    def post(self):
        name = self.request.get(name_string)
        tmpl = os.path.join(os.path.dirname(__file__), 'templates/control.html')
        self.response.write(render(tmpl, {name_string : name}))

class HeartBeatPage(webapp2.RequestHandler):
    def post(self):
        name = self.request.get(name_string)
        setNameInMemcache(name)

# -- Non-pages --
                     
class RobotEntity(ndb.Model):
    name = ndb.StringProperty()

def getActiveRobotNames():
    return getActiveRobots(False)

def getActiveRobotKeys():
    return getActiveRobots(True)

def getActiveRobots(returnKeys):
    active_robots = [];
    qry = RobotEntity.query()
    for item in qry.iter(keys_only=returnKeys):
        if returnKeys:
            active_robots.append(item)
        else:
            active_robots.append(item.name)
    return active_robots

def setNameInMemcache(name):
    memcache.set(key=name, value=0, time=5)
    

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/register', RegisterRobotPage),
    ('/pollactiverobots', PollActiveRobotsPage),
    ('/control', ControlPage),
    ('/heartbeat', HeartBeatPage),
], debug=True)
