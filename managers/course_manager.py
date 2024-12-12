class CourseManager:
    courses = []

    def get_courses(self):
        return self.courses

    def add_course(self, course):
        self.courses.append(course)
