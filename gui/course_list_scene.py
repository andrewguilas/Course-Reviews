from managers.course_manager import CourseManager
from models.course import Course

class CourseListScene:
    displayed_courses = []

    def show(self):
        course_manager = CourseManager()
        course_manager.add_course(Course("CS", "1110", "Intro to Programming"))
        course_manager.add_course(Course("CS", "2100", "Data Structures and Algorithms 1"))
        course_manager.add_course(Course("CS", "2130", "Computer Systems and Organization 1"))

        self.filter_courses("")

        while True:
            print("\n\nCourse List")
            self.show_courses()
            try:
                option_input = int(input("1. Search\n2. Add Course\n3. My Reviews\n4. Log Out\nEnter option: "))
            except ValueError:
                print("Invalid input")
                continue

            match option_input:
                case 1:
                    search_query = input("Enter keyword: ")
                    self.filter_courses(search_query)
                case 2:
                    pass #TODO
                case 3:
                    pass #TODO
                case 4:
                    pass #TODO
                case _:
                    print("Invalid input")
                    continue

    def filter_courses(self, search_query):
        course_manager = CourseManager()
        search_query = strip_string(search_query)

        if search_query == "":
            self.displayed_courses = course_manager.get_courses()
            return

        self.displayed_courses = []
        for course in course_manager.get_courses():
            if (search_query in strip_string(str(course))):
                self.displayed_courses.append(course)

    def show_courses(self):
        for course in self.displayed_courses:
            print(course)

def strip_string(string):
    return string.lower().strip().replace(" ", "")
