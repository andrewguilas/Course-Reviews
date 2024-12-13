import tkinter
from gui.login_scene import LoginScene

def __main__():
    root = tkinter.Tk()
    root.geometry('1200x720')
    
    LoginScene().show(root)
    
    root.mainloop()

if __name__ == '__main__':
    __main__()
