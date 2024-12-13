import tkinter
from gui.course_list_scene import CourseListScene
from managers.user_manager import UserManager
from models.user import User

def strip_string(string):
    return string.lower().strip().replace(" ", "")

class LoginScene:
    def __init__(self):
        self.user_manager = UserManager()
        self.user_manager.add_user(User("admin", "pass")) # temp

    def log_in(self):
        username_input = self.username_field.get()
        password_input = self.password_field.get()

        if not strip_string(username_input):
            self.set_status("Error: Username cannot be blank")
            return
        
        if not strip_string(password_input):
            self.set_status("Error: Password cannot be blank")
            return

        user = self.user_manager.get_user(username_input)
        if not user:
            self.set_status("Error: User does not exist")
            return

        if not user.authenticate(password_input):
            self.set_status("Error: Incorrect password")
            return
        
        CourseListScene().show()

    def register(self):
        username_input = self.username_field.get()
        password_input = self.password_field.get()

        if not strip_string(username_input):
            self.set_status("Error: Username cannot be blank")
            return
        
        if not strip_string(password_input):
            self.set_status("Error: Password cannot be blank")
            return

        username_input.lower()

        if self.user_manager.get_user(username_input):
            self.set_status("Error: Username already used")
            return

        new_user = User(username_input, password_input)
        self.user_manager.add_user(new_user)

        self.set_status("Success: User created")

    def show(self, root):
        title = tkinter.Label(root, text="Login")
        title.grid(row=0)

        username_text = tkinter.Label(root, text="Username")
        username_text.grid(row=1)

        self.username_field = tkinter.Entry(root)
        self.username_field.grid(row=1, column=1)

        password_text = tkinter.Label(root, text="Password")
        password_text.grid(row=2)

        self.password_field = tkinter.Entry(root, show="*")
        self.password_field.grid(row=2, column=1)

        login_button = tkinter.Button(root, text="Log In", command=self.log_in)
        login_button.grid(row=3)

        register_button = tkinter.Button(root, text="Register", command=self.register)
        register_button.grid(row=4)

        self.status_text = tkinter.Label(root)
        self.status_text.grid(row=5)

    def set_status(self, text):
        self.status_text.config(text=text)
