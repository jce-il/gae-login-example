from google.appengine.ext.webapp import template
import webapp2
import json
from models.user import User
from models.group import Group

class GetGroups(webapp2.RequestHandler):
    def get(self):
        group = Group.get_by_id(int(self.request.get('group')))
        user = None
        if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
            user = User.checkToken(self.request.cookies.get('our_token'))

        if not user or (group.admin != user.key and user.key not in group.members):
            self.error(403)
            self.response.write('access denied')
            return

        members = group.getMembers()
        self.response.write(json.dumps({"status": "OK", "members": members}))


app = webapp2.WSGIApplication([
    ('/api/members', GetGroups)
], debug=True)
