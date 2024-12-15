import tkinter
from gui.scene import Scene
from managers.course_manager import CourseManager
from models.course import Course

class NewCourseScene(Scene):
    def __init__(self):
        self.course_manager = CourseManager()

    def build(self):
        self.frame = tkinter.Frame(self.root, name="new_course_scene")

        title = tkinter.Label(self.frame, text="New Course")
        title.grid(row=0, column=0, columnspan=2, pady=(20, 10))

        mnemonic_text = tkinter.Label(self.frame, text="Mnemonic")
        mnemonic_text.grid(row=1, column=0, sticky="e", padx=(10, 5), pady=5)

        self.mnemonic_field = tkinter.Entry(self.frame)
        self.mnemonic_field.grid(row=1, column=1, padx=(5, 10), pady=5, sticky="w")

        number_text = tkinter.Label(self.frame, text="Number")
        number_text.grid(row=2, column=0, sticky="e", padx=(10, 5), pady=5)

        self.number_field = tkinter.Entry(self.frame)
        self.number_field.grid(row=2, column=1, padx=(5, 10), pady=5, sticky="w")

        title_text = tkinter.Label(self.frame, text="Title")
        title_text.grid(row=3, column=0, sticky="e", padx=(10, 5), pady=5)

        self.title_field = tkinter.Entry(self.frame)
        self.title_field.grid(row=3, column=1, padx=(5, 10), pady=5, sticky="w")
        self.title_field.bind('<Return>', lambda event: self.create_course())

        create_button = tkinter.Button(self.frame, text="Create", command=self.create_course)
        create_button.grid(row=4, column=0, padx=(10, 5), pady=(10, 5), sticky="e")

        self.status_text = tkinter.Label(self.frame, text="", wraplength=400)
        self.status_text.grid(row=5, column=0, columnspan=2, pady=10)

        back_button = tkinter.Button(self.frame, text="Back", command=self.show_course_list_scene)
        back_button.grid(row=6, column=0, padx=(10, 5), pady=10, sticky="e")

        log_off_button = tkinter.Button(self.frame, text="Log Off", command=self.show_login_scene)
        log_off_button.grid(row=6, column=1, padx=(5, 10), pady=10, sticky="w")

    def show(self, app):
        self.app = app
        self.root = self.app.root

        if not hasattr(self, 'frame'):
            self.build()

        self.frame.pack()
    
    def hide(self):
        self.frame.pack_forget()

    def create_course(self):
        self.highlight_field(self.mnemonic_field, False)
        self.highlight_field(self.number_field, False)
        self.highlight_field(self.title_field, False)

        mnemonic_input = self.strip_string(self.mnemonic_field.get())
        number_input = self.number_field.get()
        title_input = self.title_field.get()

        if not self.strip_string(mnemonic_input):
            self.set_status("Error: Course mnemonic cannot be blank")
            self.highlight_field(self.mnemonic_field, True)
            return
        
        if not mnemonic_input.isalpha():
            self.set_status("Error: Course mnemonic must only contain letters (A-Z)")
            self.highlight_field(self.mnemonic_field, True)
            return
        
        if len(mnemonic_input) < 2 or len(mnemonic_input) > 4:
            self.set_status("Error: Course mnemonic length must be between 2 and 4")
            self.highlight_field(self.mnemonic_field, True)
            return

        if not self.strip_string(number_input):
            self.set_status("Error: Course number cannot be blank")
            self.highlight_field(self.number_field, True)
            return
        
        if not number_input.isnumeric:
            self.set_status("Error: Course number must only contain numbers")
            self.highlight_field(self.number_field, True)
            return
        
        if len(number_input) != 4:
            self.set_status("Error: Course number must be between 1000 and 9999")
            self.highlight_field(self.number_field, True)
            return
        
        if not self.strip_string(title_input):
            self.set_status("Error: Course title cannot be blank")
            self.highlight_field(self.title_field, True)
            return
        
        if len(title_input) > 50:
            self.set_status("Error: Course title cannot be longer than 50 characters")
            self.highlight_field(self.title_field, True)
            return

        if self.course_manager.get_course(mnemonic_input, number_input, title_input):
            self.set_status("Error: Course already exists")
            self.highlight_field(self.title_field, True)
            return
        
        mnemonic_input = mnemonic_input.upper()
        new_course = Course(mnemonic_input, number_input, title_input)
        self.course_manager.add_course(new_course)
        
        self.set_status(f"Success: Added {new_course}")
        self.clear_fields([self.mnemonic_field, self.number_field, self.title_field])

    def set_status(self, text):
        self.status_text.config(text=text)

    def show_course_list_scene(self):
        self.hide()
        self.app.show_course_list_scene()

    def show_login_scene(self):
        self.hide()
        self.app.show_login_scene()
