import tkinter
from gui.login_scene import LoginScene
from gui.course_list_scene import CourseListScene
from gui.new_course_scene import NewCourseScene

class App():
    def __init__(self):
        self.login_scene = LoginScene()
        self.course_list_scene = CourseListScene()
        self.new_course_scene = NewCourseScene()

    def start(self):
        self.root = tkinter.Tk()
        self.root.geometry('1200x720')

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
