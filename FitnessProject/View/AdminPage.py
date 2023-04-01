import tkinter as tk
import sqlite3
from Control.logic import Logic



class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.frame_photo_4 = tk.PhotoImage(file=r'/home/spring/Test101/FitnessProject/View/Images/Home page (noti off).png')
        frame_label = tk.Label(self, bd=0, bg='grey', image=self.frame_photo_4)
        frame_label.place(x=0, y=0)
        frame_label.bind('<B1-Motion>', controller.move_app)

        self.stats_image = tk.PhotoImage(file=r'/home/spring/Test101/FitnessProject/View/Images/Statistics.png')
        stats_button = tk.Button(self, image=self.stats_image, border=0, bg='#212121', activebackground='#212121', command = lambda: [Logic.open_db()])
        stats_button.place(x=29, y=435.1)
        
        self.log_out_image = tk.PhotoImage(file=r'/home/spring/Test101/FitnessProject/View/Images/Log out.png')
        log_out_button = tk.Button(self, image=self.log_out_image, border=0, bg='#212121', activebackground='#212121', command=lambda: [Logic.delete_admin_leftover(self),controller.show_frame('SignInPage')])
        log_out_button.place(x=32, y=1012)
        
        
        
