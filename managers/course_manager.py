class CourseManager:
    courses = []

    def get_courses(self):
        return self.courses

    def add_course(self, course):
        self.courses.append(course)

    def get_course(self, mnemonic, number, title):
        for course in self.courses:
            if course.mnemonic == mnemonic and course.number == number and course.title == title:
                return course
