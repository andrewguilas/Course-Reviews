import tkinter
from managers.course_manager import CourseManager
from models.course import Course

def strip_string(string):
    return string.lower().strip().replace(" ", "")

class NewCourseScene():
    def __init__(self):
        self.ERROR_COLOR = 'pink'
        self.DEFAULT_COLOR = 'white'
    
        self.course_manager = CourseManager()

    def show(self, app):
        self.app = app
        self.root = self.app.root

        self.frame = tkinter.Frame(self.root)

        title = tkinter.Label(self.frame, text="New Course")
        title.grid(row=0)

        mnemonic_text = tkinter.Label(self.frame, text="Mnemonic")
        mnemonic_text.grid(row=1)

        self.mnemonic_field = tkinter.Entry(self.frame)
        self.mnemonic_field.grid(row=1, column=1)

        number_text = tkinter.Label(self.frame, text="Number")
        number_text.grid(row=2)

        self.number_field = tkinter.Entry(self.frame)
        self.number_field.grid(row=2, column=1)

        title_text = tkinter.Label(self.frame, text="Title")
        title_text.grid(row=3)

        self.title_field = tkinter.Entry(self.frame)
        self.title_field.grid(row=3, column=1)

        create_button = tkinter.Button(self.frame, text="Create", command=self.create_course)
        create_button.grid(row=4)

        self.status_text = tkinter.Label(self.frame)
        self.status_text.grid(row=5)

        back_button = tkinter.Button(self.frame, text="Back", command=self.show_course_list_scene)
        back_button.grid(row=6)

        self.frame.pack()
    
    def hide(self):
        for element in self.root.winfo_children():
            element.destroy()

    def set_status(self, text):
        self.status_text.config(text=text)

    def create_course(self):
        self.highlight_field(self.mnemonic_field, False)
        self.highlight_field(self.number_field, False)
        self.highlight_field(self.title_field, False)
        
        mnemonic_input = self.mnemonic_field.get()
        number_input = self.number_field.get()
        title_input = self.title_field.get()

        if not strip_string(mnemonic_input):
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

        if not strip_string(number_input):
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
        
        if not strip_string(title_input):
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
        
        new_course = Course(mnemonic_input, number_input, title_input)
        self.course_manager.add_course(new_course)
        
        self.set_status(f"Success: Added {new_course}")
        self.clear_fields()

    def clear_fields(self):
        self.mnemonic_field.delete(0, "end")
        self.number_field.delete(0, "end")
        self.title_field.delete(0, "end")

    def highlight_field(self, field, is_error):
        color = self.ERROR_COLOR if is_error else self.DEFAULT_COLOR
        field.config(bg=color)

    def show_course_list_scene(self):
        self.hide()
        self.app.show_course_list_scene()
