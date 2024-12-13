class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, password_input):
        return password_input == self.password
