from managers.course_manager import CourseManager

class CourseListScene:
    def show():
        course_manager = CourseManager()

        while True:
            print("\n\nCourse List")

            for course in course_manager.get_courses():
                print(course)

            option_input = int(input("1. Search\n2. Add Course\n3. My Reviews\n9. Log Out "))

            match option_input:
                case 1:
                    pass #TODO
                case 2:
                    pass #TODO
                case 3:
                    pass #TODO
                case 9:
                    pass #TODO

        
