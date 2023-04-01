import tkinter as tk
from Control.logic import *


class SignInPage(tk.Frame):
    
    
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        
        self.frame_photo = tk.PhotoImage(file=r'/home/spring/Test101/FitnessProject/View/Images/Login (Eye close).png')
        frame_label = tk.Label(self, bd=0, bg='grey', image=self.frame_photo)
        frame_label.place(x=0, y=0)
        frame_label.bind('<B1-Motion>', controller.move_app)

        self.login_image = tk.PhotoImage(file=r'/home/spring/Test101/FitnessProject/View/Images/Login.png')
        login_button = tk.Button(self, image=self.login_image, borderwidth=0, bg='#141414', activebackground='#141414',
                                 command=lambda: sign_in())
        login_button.place(x=171, y=585)

        global username_entry
        username_entry = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=20, bg='#141414', bd=0, fg='#939597')
        username_entry.insert(0, 'Username')
        username_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, username_entry, 'Username'))
        username_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, username_entry, 'Username'))
        username_entry.place(x=188, y=418)

        password_entry = tk.Entry(self, show="*", font=('iCiel Gotham Medium', 18), width=20, bg='#141414', bd=0, fg='#939597')
        password_entry.insert(0, 'Password')
        password_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, password_entry, 'Password'))
        password_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, password_entry, 'Password'))
        password_entry.place(x=188, y=507)


        def sign_in():
            found = Logic.check_sign_in(username_entry.get(), password_entry.get())
            found2 = Logic.check_admin(username_entry.get(), password_entry.get())
            if found2:
                messagebox.showinfo(title="Login Success", message="You successfully logged in. Welcome Admin!")
                controller.show_frame('AdminPage')
            elif found:
                messagebox.showinfo(title="Login Success", message="You successfully logged in !")
            else:
                messagebox.showerror(title="Error", message="Incorect username or password!")

            found1 = Logic.check_health_info(username_entry.get())
            if not found1 and found:
                controller.show_frame('HealthInfoPage')
            elif found1 and found and not found2:
                controller.show_frame('HomePage')
                Logic.display_health(username_entry.get(), posx =[267, 485], posy= [304, 372, 440])
                
               
           
   
        def show_pw():
            hide_button = tk.Button(self, image=self.hide_image, command=hide_pw, activebackground='#141414', bd=0, bg='#141414')
            hide_button.place(x=498, y=517)
            password_entry.config(show='')

        def hide_pw():
            show_button = tk.Button(self, image=self.show_image, command=show_pw, activebackground='#141414', bd=0, bg='#141414')
            show_button.place(x=498, y=517)
            password_entry.config(show='*')

        
        self.show_image = tk.PhotoImage(file=r'/home/spring/Test101/FitnessProject/View/Images/Eye close.png')
        self.hide_image = tk.PhotoImage(file=r'/home/spring/Test101/FitnessProject/View/Images/Eye Open.png')

        show_button = tk.Button(self, image=self.show_image, command=show_pw, activebackground='#141414', bd=0, bg='#141414')
        show_button.place(x=498, y=517)

        self.sign_up_text = tk.PhotoImage(file=r'/home/spring/Test101/FitnessProject/View/Images/Sign up.png')
        sign_up_button = tk.Button(self, image=self.sign_up_text, border=0, bg='#141414', activebackground='#141414',
                                   command=lambda: controller.show_frame('SignUpPage'))
        sign_up_button.place(x=183, y=674)

        self.forgot_pw_text = tk.PhotoImage(file=r'/home/spring/Test101/FitnessProject/View/Images/Forgot password.png')
        forgot_pw_button = tk.Button(self, image=self.forgot_pw_text, border=0, bg='#141414', activebackground='#141414',
                                   command=lambda: messagebox.showinfo(title="Guidance", message="Please contact Admin for password recovery!"))
        forgot_pw_button.place(x=254, y=712)
        
        self.log_out_image = tk.PhotoImage(file=r'/home/spring/Test101/FitnessProject/View/Images/Log out.png')
        quit_button = tk.Button(self, image=self.log_out_image, border=0, bg='#212121', activebackground='#212121', command=lambda: Logic.quit_program(self))
        quit_button.place(x=32, y=1012)
    """def get_label(self):
        return label"""
    def get_username_entry(self):
        return username_entry
  
   
        