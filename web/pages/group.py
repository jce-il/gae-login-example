from google.appengine.ext.webapp import template
import webapp2
import json
from models.user import User
from models.group import Group

class AllGroupsHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect('/')
        return

class GroupHandler(webapp2.RequestHandler):
    def get(self, group):
        template_params = {}
        user = None
        if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
            user = User.checkToken(self.request.cookies.get('our_token'))

        if not user:
            self.redirect('/')

        template_params['email'] = user.email

        group = Group.get_by_id(int(group))
        if group.admin != user.key and user.key not in group.members:
            template_params['no_access'] = True
        else:
            template_params['group_title'] = group.title
            template_params['group_admin'] = group.admin.get().email

        html = template.render('web/templates/group.html', template_params)
        self.response.write(html)

app = webapp2.WSGIApplication([
	('/groups/(.*)', GroupHandler),
], debug=True)
