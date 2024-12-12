class UserManager:
    users = []

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def add_user(self, user):
        self.users.append(user)
