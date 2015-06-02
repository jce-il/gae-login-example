from google.appengine.ext import ndb

class Group(ndb.Model):
    title = ndb.StringProperty()
    admin = ndb.KeyProperty()
    members = ndb.KeyProperty(repeated=True)

    def getMembers(self):
        members = []
        for member in self.members:
            members.append({"email":member.get().email})

        return members


    @staticmethod
    def getAdminGroups(user):
        q = Group.query(Group.admin == user.key)
        groups_arr = []
        for group in q:
            groups_arr.append({
                "title": group.title,
                "id": group.key.id(),
                "admin": True
            })

        return groups_arr

    @staticmethod
    def getUserGroups(user):
        q = Group.query(Group.members == user.key)
        groups_arr = []
        for group in q:
            groups_arr.append({
                "title": group.title,
                "id": group.key.id(),
                "admin": False
            })

        return groups_arr

    @staticmethod
    def getAllGroups(user):
        arr_a = Group.getAdminGroups(user)
        arr_b = Group.getUserGroups(user)

        return arr_a + arr_b