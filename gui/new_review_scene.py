import tkinter
from gui.scene import Scene
from managers.course_manager import CourseManager
from models.course import Course

class NewReviewScene(Scene):
    def __init__(self):
        pass # TODO

    def build(self):
        pass # TODO

    def show(self, app):
        self.app = app
        self.root = self.app.root

        if not hasattr(self, 'frame'):
            self.build()

        self.frame.pack()
    
    def hide(self):
        self.frame.pack_forget()

    def create_review(self):
        pass # TODO

    def set_status(self, text):
        self.status_text.config(text=text)

    def show_course_reviews_scene(self):
        self.hide()
        self.app.show_course_reviews_scene()

    def show_login_scene(self):
        self.hide()
        self.app.show_login_scene()
