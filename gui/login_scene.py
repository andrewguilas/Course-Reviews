from managers.user_manager import UserManager
from models.user import User

class LoginScene:
    def show():
        user_manager = UserManager()

        while True:
            print("\n\nLogin")
            
            username_input = input("Enter username: ")
            password_input = input("Enter password: ")
            option_input = int(input("1. Login\n3: Register\n9. Exit\nSelect option: "))

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
                case 9:
                    pass #TODO
