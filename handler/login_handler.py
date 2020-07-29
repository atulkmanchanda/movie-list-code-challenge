class LoginHandler:
    ### To validate the user #####
    def getUser(self, data):
        if data['username'] == 'admin' and data['password'] == 'admin':
            return True
        else:
            return False

