from google.appengine.ext import ndb
import hashlib      #we need this to safely store passwords
import logging

class User(ndb.Model):
    email = ndb.StringProperty()
    password = ndb.StringProperty()

    @staticmethod
    def checkToken(token):
        user = User.get_by_id(long(token))
        return user

    def setPassword(self, password):
        self.password = hashlib.md5(password).hexdigest()
        self.put()

    def checkPassword(self, password):
        if not password:
            return False
        logging.info("self.pass: {}, hashed pass: {}".format(self.password, hashlib.md5(password).hexdigest()))
        if self.password == hashlib.md5(password).hexdigest():
            return True

        return False