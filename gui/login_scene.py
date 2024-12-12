from managers.UserManager import UserManager
from models.User import User

class LoginScene:
    def show():
        user_manager = UserManager()

        while True:
            print("\n\nLogin Scene")
            
            username_input = input("Enter username: ")
            password_input = input("Enter password: ")
            option_input = int(input("1: Login\n2: Register\nSelect option: "))

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
