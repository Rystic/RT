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
            <script>
                var prevChar = null;

                function click(e) {
                   
                    var charCode = String.fromCharCode(e.keyCode);
                    sendKey(charCode);
                };

                function release(e)
                {
                    sendKey(null);
                };

                function sendKey(charCode)
                {
                    if (prevChar == charCode)
                    {
                        return;
                    }
                    prevChar = charCode;
                    console.log(charCode);
                    post('/memcacheput', {value: charCode});
                }
                
                function post(path, params, method) {
                    method = method || "post"; // Set method to post by default if not specified.

                    // The rest of this code assumes you are not using a library.
                    // It can be made less wordy if you use one.
                    var form = document.createElement("form");
                    form.setAttribute("method", method);
                    form.setAttribute("action", path);

                    for(var key in params) {
                        if(params.hasOwnProperty(key)) {
                            var hiddenField = document.createElement("input");
                            hiddenField.setAttribute("type", "hidden");
                            hiddenField.setAttribute("name", key);
                            hiddenField.setAttribute("value", params[key]);

                            form.appendChild(hiddenField);
                         }
                    }
                    document.body.appendChild(form);
                    form.submit();
                };
                document.onkeypress = click;
                document.onkeyup = release;
            </script>
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
        memcache.set(key='dir', value=self.request.get('value'))
        self.redirect('/')        

app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/memcacheput', MemCachePut)
], debug=True)
