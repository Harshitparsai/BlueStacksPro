from roles import Roles

class Users:
    def __init__(self,uname,password,roles,resourses):
        self.uname = uname
        self.password = password
        self.roles = []
        for role in roles:
            self.roles.append(Roles(role,resourses))


