import tkinter
from managers.user_manager import UserManager
from models.user import User

def strip_string(string):
    return string.lower().strip().replace(" ", "")

class LoginScene:
    def __init__(self):
        self.ERROR_COLOR = 'pink'
        self.DEFAULT_COLOR = 'white'

        self.user_manager = UserManager()
        self.user_manager.add_user(User("admin", "pass")) # temp

    def log_in(self):
        self.highlight_field(self.username_field, False)
        self.highlight_field(self.password_field, False)
    
        username_input = self.username_field.get()
        password_input = self.password_field.get()

        if not strip_string(username_input):
            self.set_status("Error: Username cannot be blank")
            self.highlight_field(self.username_field, True)
            return
        
        if not strip_string(password_input):
            self.set_status("Error: Password cannot be blank")
            self.highlight_field(self.password_field, True)
            return

        user = self.user_manager.get_user(username_input)
        if not user:
            self.set_status("Error: User does not exist")
            self.highlight_field(self.username_field, True)
            return

        if not user.authenticate(password_input):
            self.password_field.delete(0, "end")
            self.set_status("Error: Incorrect password")
            self.highlight_field(self.password_field, True)
            return
        
        self.clear_fields()
        self.show_course_list_scene()

    def register(self):
        self.highlight_field(self.username_field, False)
        self.highlight_field(self.password_field, False)
    
        username_input = self.username_field.get()
        password_input = self.password_field.get()

        if not strip_string(username_input):
            self.set_status("Error: Username cannot be blank")
            self.highlight_field(self.username_field, True)
            return
        
        if not strip_string(password_input):
            self.set_status("Error: Password cannot be blank")
            self.highlight_field(self.password_field, True)
            return

        username_input = username_input.lower()

        if self.user_manager.get_user(username_input):
            self.set_status("Error: Username already used")
            self.highlight_field(self.username_field, True)
            return

        new_user = User(username_input, password_input)
        self.user_manager.add_user(new_user)

        self.set_status("Success: User created")
        self.password_field.delete(0, "end")

    def build(self):
        self.frame = tkinter.Frame(self.root, name="login_scene")

        title = tkinter.Label(self.frame, text="Login")
        title.grid(row=0, column=0, columnspan=2, pady=(20, 10))  # Center and add vertical padding

        username_text = tkinter.Label(self.frame, text="Username")
        username_text.grid(row=1, column=0, sticky="e", padx=(10, 5), pady=5)

        self.username_field = tkinter.Entry(self.frame)
        self.username_field.grid(row=1, column=1, padx=(5, 10), pady=5, sticky="w")

        password_text = tkinter.Label(self.frame, text="Password")
        password_text.grid(row=2, column=0, sticky="e", padx=(10, 5), pady=5)

        self.password_field = tkinter.Entry(self.frame, show="*")
        self.password_field.grid(row=2, column=1, padx=(5, 10), pady=5, sticky="w")
        self.password_field.bind('<Return>', lambda event: self.log_in())

        login_button = tkinter.Button(self.frame, text="Log In", command=self.log_in)
        login_button.grid(row=3, column=0, padx=(10, 5), pady=(10, 5))

        register_button = tkinter.Button(self.frame, text="Register", command=self.register)
        register_button.grid(row=3, column=1, padx=(5, 10), pady=(10, 5))

        self.status_text = tkinter.Label(self.frame, text="", wraplength=400)
        self.status_text.grid(row=4, column=0, columnspan=2, pady=(10, 20))  # Center and add space

    def show(self, app):
        self.app = app
        self.root = app.root

        if not hasattr(self, 'frame'):
            self.build()

        self.frame.pack(padx=20, pady=20)  # Padding around the entire scene

    def hide(self):
        self.frame.pack_forget()

    def clear_fields(self):
        self.username_field.delete(0, "end")
        self.password_field.delete(0, "end")

    def set_status(self, text):
        self.status_text.config(text=text)

    def highlight_field(self, field, is_error):
        color = self.ERROR_COLOR if is_error else self.DEFAULT_COLOR
        field.config(bg=color)

    def show_course_list_scene(self):
        self.hide()
        self.app.show_course_list_scene()
