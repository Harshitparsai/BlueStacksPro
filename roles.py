class Roles:
    def __init__(self,name="user1",resources=None):
        self.name = name
        if name == 'admin':
            self.access = ["read","write","execute"]
        else:
            self.access = ["read"]
        self.resources = resources

