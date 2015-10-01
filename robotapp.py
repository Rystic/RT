import sys
import webapp2
import cgi
import urllib
import datetime
from google.appengine.ext import webapp
from google.appengine.ext import ndb
from google.appengine.api import users

guestbook_key = ndb.Key('Guestbook', 'default_guestbook')

class Greeting(ndb.Model):
  author = ndb.UserProperty()
  content = ndb.TextProperty()
  date = ndb.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):

    content = ndb.TextProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
    
    def get(self):
        self.response.out.write('<html><body>')
        
        greetings = ndb.gql('SELECT * '
                        'FROM Greeting '
                        'WHERE ANCESTOR IS :1 '
                        'ORDER BY date DESC LIMIT 1',
                        guestbook_key)

        for greeting in greetings:
              self.response.out.write(greeting.content)

        self.response.out.write("""
          <form action="/sign" method="post">
            <div><textarea name="content" rows="3" cols="60"></textarea></div>
            <div><input type="submit" value="Post instruction (w, a, s, d)"></div>
          </form>
        </body>
      </html>""")

    def post(self):
        url = 'http://robotapp-1041.appspot.com'
        f = urllib.urlopen(url)
        for line in f:
            self.response.out.write(line)

class Guestbook(webapp2.RequestHandler):
    def post(self):
        greeting = Greeting(parent=guestbook_key)

        if users.get_current_user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        greeting.put()
        self.redirect('/')        

app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/sign', Guestbook)
], debug=True)
