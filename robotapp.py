import webapp2
import os

from google.appengine.ext.webapp.template import render
from google.appengine.api import memcache

class MainPage(webapp2.RequestHandler):
    def get(self):
        tmpl = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.write(render(tmpl, {'value' : memcache.get('d1')}))

class RTPage(webapp2.RequestHandler):
    def get(self):
        value = memcache.get('d1')
        self.response.out.write("""<html><body><p>""")
        self.response.out.write(value)
        self.response.out.write("""</p></body></html>""");
        
    def post(self):
        memcache.set(key='d1', value=self.request.get('value'))

class AnthonyBotPage(webapp2.RequestHandler):
    def get(self):
        value = memcache.get('d2')
        self.response.out.write("""<html><body><p>""")
        self.response.out.write(value)
        self.response.out.write("""</p></body></html>""");
        
    def post(self):
        memcache.set(key='d2', value=self.request.get('value'))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/rt', RTPage),
    ('/anthonybot', AnthonyBotPage),
], debug=True)
