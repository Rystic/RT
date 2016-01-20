import webapp2
import os

from google.appengine.ext.webapp.template import render
from google.appengine.api import memcache
from google.appengine.ext import ndb

name_string = 'name'
robot_names = ['rt', 'anthonybot']

# -- Pages --

class MainPage(webapp2.RequestHandler):
    def get(self):
        tmpl = os.path.join(os.path.dirname(__file__), 'templates/robots.html')
        self.response.write(render(tmpl, {'active_robots' : getActiveRobotNames()}))

class RegisterRobotPage(webapp2.RequestHandler):
    def post(self):
        name = self.request.get(name_string)
        setNameInMemcache(name)

class PollActiveRobotsPage(webapp2.RequestHandler):
    def post(self):
        self.response.write("""<html><body><p>""")
        no_robots = True
        tmpl = os.path.join(os.path.dirname(__file__), 'templates/robot_info_block.html')
        for name in robot_names:
            if memcache.get(name) is not None:
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

def setNameInMemcache(name):
    memcache.set(key=name, value=0, time=5)

def getActiveRobotNames():
    active_robots = []
    for name in robot_names:
         if memcache.get(name) is not None:
             active_robots.append(name)
    return active_robots

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/register', RegisterRobotPage),
    ('/pollactiverobots', PollActiveRobotsPage),
    ('/control', ControlPage),
    ('/heartbeat', HeartBeatPage),
], debug=True)
