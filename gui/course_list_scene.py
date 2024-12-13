
import tkinter
from managers.course_manager import CourseManager
from models.course import Course

def strip_string(string):
    return string.lower().strip().replace(" ", "")

class CourseListScene:
    def __init__(self):
        self.displayed_courses = []

        self.course_manager = CourseManager()
        self.course_manager.add_course(Course("CS", "1110", "Intro to Programming"))
        self.course_manager.add_course(Course("CS", "2100", "Data Structures and Algorithms 1"))
        self.course_manager.add_course(Course("CS", "2130", "Computer Systems and Organization 1"))

    def build(self):
        self.frame = tkinter.Frame(self.root, name="course_list_scene")

        search_query = tkinter.StringVar()
        search_query.trace_add("write", lambda name, index, mode, sv=search_query: self.filter_courses(search_query.get()))

        self.search_field = tkinter.Entry(self.frame, textvariable=search_query)
        self.search_field.grid(row=0)
        self.search_field.focus()

        self.listbox = tkinter.Listbox(self.frame)
        self.listbox.grid(row=1)

        new_course_button = tkinter.Button(self.frame, text="New Course", command=self.show_new_course_scene)
        new_course_button.grid(row=2)

        log_off_button = tkinter.Button(self.frame, text="Log Off", command=self.show_login_scene)
        log_off_button.grid(row=2, column=1)

    def show(self, app):
        self.app = app
        self.root = self.app.root

        if not hasattr(self, 'frame'):
            self.build()

        self.filter_courses("")
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()

    def filter_courses(self, search_query):
        search_query = strip_string(search_query)

        if search_query == "":
            self.displayed_courses = self.course_manager.get_courses()
        else:
            self.displayed_courses = []
            for course in self.course_manager.get_courses():
                if (search_query in strip_string(str(course))):
                    self.displayed_courses.append(course)

        self.show_courses()

    def show_courses(self):
        self.listbox.delete(0, "end")
        for course in self.displayed_courses:
            self.listbox.insert("end", course)

    def show_new_course_scene(self):
        self.hide()
        self.app.show_new_course_scene()

    def show_login_scene(self):
        self.hide()
        self.app.show_login_scene()
