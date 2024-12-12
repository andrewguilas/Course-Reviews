from gui.login_scene import LoginScene
from gui.course_list_scene import CourseList

def __main__():
    current_user = LoginScene().show()
    CourseList().show()

if __name__ == '__main__':
    __main__()
    