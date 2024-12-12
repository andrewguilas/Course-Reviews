from managers.user_manager import UserManager
from models.user import User

class LoginScene:
    def show(self):
        user_manager = UserManager()
        user_manager.add_user(User("admin", "pass"))

        while True:
            print("\n\nLogin")
            
            username_input = input("Enter username: ")
            password_input = input("Enter password: ")

            try:
                option_input = int(input("1. Login\n2. Register\n3. Exit\nEnter option: "))
            except ValueError:
                print("Invalid input")
                continue

            match option_input:
                case 1:
                    user = user_manager.get_user(username_input)
                    if not user:
                        print("User does not exist")
                        continue

                    if not user.authenticate(password_input):
                        print("Incorrect password")
                        continue
                    
                    print("Logged in")
                    return user
                case 2:
                    new_user = User(username_input, password_input)
                    user_manager.add_user(new_user)
                    print("User created")
                case 3:
                    pass #TODO
                case _:
                    print("Invalid input")
                    continue
                