import tkinter
from gui.login_scene import LoginScene
from gui.course_list_scene import CourseListScene
from gui.new_course_scene import NewCourseScene
from gui.course_reviews_scene import CourseReviewsScene
from gui.new_review_scene import NewReviewScene

class App():
    def __init__(self):
        self.login_scene = LoginScene()
        self.course_list_scene = CourseListScene()
        self.new_course_scene = NewCourseScene()
        self.course_reviews_scene = CourseReviewsScene()
        self.new_review_scene = NewReviewScene()

        self.authenticated_user = None

        self.STYLES = {
            "*Font": "Arial 14",
            "*Label.Font": "Arial 16 bold",
            "*Button.Font": "Arial 16", 
            "*Entry.Font": "Arial 16",
            "*Button.Background": "#001F54",
            "*Button.Foreground": "white",
            "*Button.ActiveBackground": "#003B88", # hover
            "*Button.ActiveForeground": "white", # hover
            "*Entry.Background": "#f5f5f5",
            "*Entry.Foreground": "black",
            "*Label.Foreground": "#333333",
            "*Toplevel*Background": "white",
            "*padx": 10,
            "*pady": 10,
        }

    def start(self):
        self.root = tkinter.Tk()
        self.root.title("Course Reviews")
        self.root.geometry('1200x720')
        self.apply_styles()

        self.show_login_scene()

        self.root.mainloop()

    def show_login_scene(self):
        self.authenticated_user = None
        self.login_scene.show(self)

    def show_course_list_scene(self, *args):
        if len(args) > 0: 
            self.authenticated_user = args[0]
        self.course_list_scene.show(self)

    def show_new_course_scene(self):
        self.new_course_scene.show(self)

    def show_course_reviews_scene(self, course):
        self.course_reviews_scene.show(self, course, self.authenticated_user)

    def show_new_review_scene(self, course):
        self.new_review_scene.show(self, course, self.authenticated_user)

    def apply_styles(self):
        for name, value in self.STYLES.items():
            self.root.option_add(name, value)

if __name__ == '__main__':
    App().start()
