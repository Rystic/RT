import webapp2
import os

from google.appengine.ext.webapp.template import render
from google.appengine.api import memcache
from google.appengine.ext import ndb

heartbeat_timeout = 5;

class MainPage(webapp2.RequestHandler):
    def get(self):
        tmpl = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.write(render(tmpl, {'value' : memcache.get('d1')}))

class RegisterRobotPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""<html><body><p>""")
        self.response.out.write(getActiveRobots())
        self.response.out.write("""</p></body></html>""")
        
    def post(self):
        active_robots = getActiveRobots()
        name = self.request.get('name')
        if active_robots.count(name) == 0:
            robot = RobotEntity()
            robot.name = name
            robot_key = robot.put()

class HeartBeatPage(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('name')
        memcache.set(key=name, value=0, time=heartbeat_timeout)
                     
class RobotEntity(ndb.Model):
    name = ndb.StringProperty()

def getActiveRobots():
    active_robots = [];
    qry = RobotEntity.query()
    for key in qry.iter(keys_only=True):
        active_robots.append(key.get().name)
    return active_robots
    

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/register', RegisterRobotPage),
    ('/heartbeat', HeartBeatPage),
], debug=True)
