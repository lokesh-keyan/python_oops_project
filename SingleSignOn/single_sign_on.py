import random

class SingleSignOnRegistry:
    def register_new_session(self, credentials):
        pass

    def is_valid(self, token):
        pass

    def unregister(self, token):
        pass

class SSOToken:
    def __init__(self):
        self.id = random.randrange(100000)

    def __eq__(self, o):
        return self.id == o.guid
    
    def __repr__(self, o):
        return str(self.id)