import tkinter
from gui.scene import Scene

class CourseReviewsScene(Scene):
    def __init__(self):
        self.displayed_reviews = []

    def build(self):
        self.frame = tkinter.Frame(self.root, name="course_reviews_scene")

        self.listbox = tkinter.Listbox(self.frame, width=50, height=15)
        self.listbox.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        back_button = tkinter.Button(self.frame, text="Back", command=self.show_course_list_scene)
        back_button.grid(row=1, column=0, padx=(5, 10), pady=10, sticky="w")

        new_review_button = tkinter.Button(self.frame, text="New Review", command=self.show_new_review_scene)
        new_review_button.grid(row=1, column=1, padx=(10, 5), pady=10, sticky="e")

        log_off_button = tkinter.Button(self.frame, text="Log Off", command=self.show_login_scene)
        log_off_button.grid(row=1, column=2, padx=(5, 10), pady=10, sticky="w")

    def show(self, app, course):
        self.app = app
        self.root = self.app.root

        if not hasattr(self, 'frame'):
            self.build()

        self.frame.pack()
        self.show_reviews(course)

    def hide(self):
        self.frame.pack_forget()

    def show_reviews(self, course):
        self.listbox.delete(0, "end")
        for review in course.getReviews():
            self.listbox.insert("end", review)

    def show_new_review_scene(self):
        self.hide()
        self.app.show_new_review_scene()

    def show_course_list_scene(self):
        self.hide()
        self.app.show_course_list_scene()
    
    def show_login_scene(self):
        self.hide()
        self.app.show_login_scene()