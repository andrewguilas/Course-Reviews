import tkinter
from gui.scene import Scene
from managers.course_manager import CourseManager
from models.course import Course
from models.review import Review

class NewReviewScene(Scene):
    def __init__(self):
        pass # TODO

    def build(self):
        self.frame = tkinter.Frame(self.root, name="new_review_scene")

        title = tkinter.Label(self.frame, text="New Review")
        title.grid(row=0, column=0, columnspan=2, pady=(20, 10))

        rating_text = tkinter.Label(self.frame, text="Rating (1-5)")
        rating_text.grid(row=1, column=0, sticky="e", padx=(10, 5), pady=5)
        self.rating_field = tkinter.Entry(self.frame)
        self.rating_field.grid(row=1, column=1, padx=(5, 10), pady=5, sticky="w")

        comment_frame = tkinter.Frame(self.frame)
        comment_frame.grid(row=2, column=1, padx=(5, 10), pady=5, sticky="w")
        comment_text = tkinter.Label(comment_frame, text="Comment")
        comment_text.grid(row=0, column=0, sticky="e", padx=(10, 5), pady=5)
        self.comment_field = tkinter.Text(comment_frame, height=5, width=40)
        self.comment_field.grid(row=0, column=1, padx=(10, 5), pady=5)

        add_button = tkinter.Button(self.frame, text="Add", command=self.create_review)
        add_button.grid(row=3, column=0, padx=(10, 5), pady=(10, 5), sticky="e")

        self.status_text = tkinter.Label(self.frame, text="", wraplength=400)
        self.status_text.grid(row=4, column=0, columnspan=2, pady=10)

        back_button = tkinter.Button(self.frame, text="Back", command=self.show_course_reviews_scene)
        back_button.grid(row=5, column=0, padx=(10, 5), pady=10, sticky="e")

        log_off_button = tkinter.Button(self.frame, text="Log Off", command=self.show_login_scene)
        log_off_button.grid(row=5, column=1, padx=(5, 10), pady=10, sticky="w")

    def show(self, app, course, authenticated_user):
        self.app = app
        self.root = self.app.root
        self.course = course
        self.authenticated_user = authenticated_user

        if not hasattr(self, 'frame'):
            self.build()

        self.frame.pack()
    
    def hide(self):
        self.frame.pack_forget()

    def create_review(self):
        self.highlight_field(self.rating_field, False)
        self.highlight_field(self.comment_field, False)

        rating_input = self.rating_field.get()
        comment_input = self.comment_field.get("1.0", tkinter.END)

        if not self.strip_string(rating_input):
            self.set_status("Error: Rating cannot be blank")
            self.highlight_field(self.rating_field, True)
            return
        
        if not rating_input.isnumeric:
            self.set_status("Error: Rating must be a number between 1 and 5")
            self.highlight_field(self.rating_field, True)
            return
        
        rating_input = int(rating_input)
        if rating_input < 1 or rating_input > 5:
            self.set_status("Error: Rating must be a number between 1 and 5")
            self.highlight_field(self.rating_field, True)
            return

        if self.course.get_user_review(self.authenticated_user):
            self.set_status("Error: You already reviewed this course")
            self.highlight_field(self.rating_field, True)
            return
        
        new_review = Review(rating_input, comment_input, self.authenticated_user)
        self.course.add_review(new_review)
        
        self.set_status(f"Success: Added review")
        self.clear_fields([self.rating_field, self.comment_field])
        self.set_status("")

    def set_status(self, text):
        self.status_text.config(text=text)

    def show_course_reviews_scene(self):
        self.hide()
        self.app.show_course_reviews_scene(self.course)

    def show_login_scene(self):
        self.hide()
        self.app.show_login_scene()
