import tkinter
from gui.login_scene import LoginScene
import sv_ttk

def __main__():
    root = tkinter.Tk()
    root.geometry('1200x720')
    sv_ttk.set_theme("light")

    login_scene = LoginScene()
    login_scene.show(root)

    root.mainloop()

if __name__ == '__main__':
    __main__()
