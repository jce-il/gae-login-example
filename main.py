from google.appengine.ext.webapp import template
import webapp2
import json
from models.user import User

class MainHandler(webapp2.RequestHandler):
    def get(self):

        html = template.render('templates/index.html', {})
        self.response.write(html)

class LoginHandler(webapp2.RequestHandler):
    def get(self):

        html = template.render('templates/index.html', {})
        self.response.write(html)

class RegisterHandler(webapp2.RequestHandler):
    def get(self):

        html = template.render('templates/index.html', {})
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LoginHandler),
    ('/register', RegisterHandler)
], debug=True)
