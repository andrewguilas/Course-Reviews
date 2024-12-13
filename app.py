import tkinter
from gui.login_scene import LoginScene
from gui.course_list_scene import CourseListScene
from gui.new_course_scene import NewCourseScene

class App():
    def __init__(self):
        self.login_scene = LoginScene()
        self.course_list_scene = CourseListScene()
        self.new_course_scene = NewCourseScene()

    def apply_styles(self):
        self.root.option_add("*Font", "Arial 14")             # Set default font for all widgets
        self.root.option_add("*Label.Font", "Arial 16 bold")  # Labels will have bold font
        self.root.option_add("*Button.Font", "Arial 14")      # Buttons font size
        self.root.option_add("*Entry.Font", "Arial 14")       # Entry fields font size
        self.root.option_add("*Button.Background", "#001F54")  # Buttons background color
        self.root.option_add("*Button.Foreground", "white")  # Buttons text color
        self.root.option_add("*Button.ActiveBackground", "#003B88")  # Buttons hover color
        self.root.option_add("*Button.ActiveForeground", "white")   # Buttons hover text color
        self.root.option_add("*Entry.Background", "#f5f5f5")  # Light gray entry background
        self.root.option_add("*Entry.Foreground", "black")    # Entry text color
        self.root.option_add("*Label.Foreground", "#333333")  # Dark gray for labels
        self.root.option_add("*Toplevel*Background", "white")  # Background color for all windows
        self.root.option_add("*padx", 10)  # Padding inside widgets
        self.root.option_add("*pady", 10)  # Padding inside widgets

    def start(self):
        self.root = tkinter.Tk()
        self.root.title("Course Reviews")
        self.root.geometry('1200x720')
        self.apply_styles()

        self.show_login_scene()

        self.root.mainloop()

    def show_login_scene(self):
        self.login_scene.show(self)

    def show_course_list_scene(self):
        self.course_list_scene.show(self)

    def show_new_course_scene(self):
        self.new_course_scene.show(self)

if __name__ == '__main__':
    App().start()
