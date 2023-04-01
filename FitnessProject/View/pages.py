import tkinter as tk
from tkinter import messagebox
import sqlite3
import ctypes
"""import pyglet"""
from SignInPage import *
from SignUpPage import *
from HealthInfoPage import *
from HomePage import *
from AdminPage import *

"""pyglet.font.add_file('GOTHAM-MEDIUM.OTF')"""


class SampleApp(tk.Tk):
    """Create a windows for all the display layers: SignInPage, SignUpPage, """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        """ctypes.windll.shcore.SetProcessDpiAwareness(1)"""

        self.geometry('1920x1080')
        """self.state('zoomed')"""
        self.title("UwU Gymnastics")
        """self.wm_attributes('-transparentcolor', 'grey')"""
        self.attributes('-fullscreen', True)
        self.overrideredirect(False)
        self.resizable(height=False, width=False)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
    
        self.frames = {}
        for F in (SignInPage, SignUpPage, AdminPage, HealthInfoPage, HomePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame("SignInPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def move_app(self, e):
        self.geometry(f'+{e.x_root}+{e.y_root}')

    def on_entry_click(self, e, entry, default_text):
        if entry.get() == default_text:
            entry.delete(0, "end")
            entry.insert(0, '')
            entry.config(fg='#939597')

    def on_focusout(self, e, entry, default_text):
        if entry.get() == '':
            entry.insert(0, default_text)
            entry.config(fg='#939597')

   

class AbsPage:
    pass


class ChestPage:
    pass





class ChatPage:
    pass


class PersonalSettings:
    pass


class Exit:
    pass


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
