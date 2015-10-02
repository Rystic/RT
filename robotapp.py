import sys
import webapp2
import cgi
import urllib
import datetime
from google.appengine.ext import webapp
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import memcache

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.out.write('<html><body>')

        self.response.out.write(memcache.get('dir'))
        self.response.out.write("""
          <form action="/memcacheput" method="post">
            <div><textarea name="content" rows="3" cols="60"></textarea></div>
            <div><input type="submit" value="Post instruction (w, a, s, d) "></div>
          </form>
        </body>
      </html>""")

    def post(self):
        url = 'http://robotapp-1041.appspot.com'
        f = urllib.urlopen(url)
        for line in f:
            self.response.out.write(line)

class MemCachePut(webapp2.RequestHandler):
    def post(self):
        memcache.set(key='dir', value=self.request.get('content'))
        self.redirect('/')        

app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/memcacheput', MemCachePut)
], debug=True)
