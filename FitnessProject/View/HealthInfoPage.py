import tkinter as tk
from Control.logic import *
from SignInPage import SignInPage


class HealthInfoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # username_entry = controller.frames['SignInPage'].username_entry

        username_entry = SignInPage.get_username_entry(self)


        self.frame_photo_3 = tk.PhotoImage(file=r'/home/spring/Test101/FitnessProject/View/Images/Information.png')
        frame_label_3 = tk.Label(self, bd=0, bg='grey', image=self.frame_photo_3)
        frame_label_3.place(x=0, y=0)
        frame_label_3.bind('<B1-Motion>', controller.move_app)

        age_entry = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=7, bg='#141414', bd=0, fg='#939597')
        age_entry.insert(0, 'Age')
        age_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, age_entry, 'Age'))
        age_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, age_entry, 'Age'))
        age_entry.place(x=188, y=367)

        gender_entry = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=10, bg='#141414', bd=0, fg='#939597')
        gender_entry.insert(0, 'Gender')
        gender_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, gender_entry, 'Gender'))
        gender_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, gender_entry, 'Gender'))
        gender_entry.place(x=370, y=367)

        weight_entry = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=20, bg='#141414', bd=0, fg='#939597')
        weight_entry.insert(0, 'Weight')
        weight_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, weight_entry, 'Weight'))
        weight_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, weight_entry, 'Weight'))
        weight_entry.place(x=188, y=456)

        height_entry = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=20, bg='#141414', bd=0, fg='#939597')
        height_entry.insert(0, 'Height')
        height_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, height_entry, 'Height'))
        height_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, height_entry, 'Height'))
        height_entry.place(x=188, y=545)

        

        self.submit_box = tk.PhotoImage(file=r'/home/spring/Test101/FitnessProject/View/Images/Submit.png')
        submit_button = tk.Button(self, image=self.submit_box, bd=0, bg='#141414', activebackground='#141414',
                                  command=lambda: [Logic.add_health_info(username_entry.get(), gender_entry.get(), age_entry.get(), height_entry.get(), weight_entry.get()),controller.show_frame('HomePage'), Logic.display_health(username_entry.get(), posx =[267, 485], posy= [304, 372, 440])])
        submit_button.place(x=171, y=623)
        
