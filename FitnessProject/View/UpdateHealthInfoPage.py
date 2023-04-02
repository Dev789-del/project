import tkinter as tk
from Control.logic import *
from SignInPage import SignInPage



class UpdateHealthInfoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # username_entry = controller.frames['SignInPage'].username_entry
        connect = sqlite3.connect(r'/home/spring/Test101/FitnessProject/View/Control/Model/Database/Fitness.db')
        cursor = connect.cursor()
        cursor.execute("SELECT username, gender, age, height, weight FROM health")
        results = cursor.fetchall()
        with open ("username.txt",'rb') as f:
            username = pickle.load(f)
        for result in results:
            if username == result[0]:
                gender = result[1]
                age = result[2]
                height = result[3]
                weight = result[4]



        self.frame_photo_3 = tk.PhotoImage(file=r'/home/spring/Test101/FitnessProject/View/Images/Information.png')
        frame_label_3 = tk.Label(self, bd=0, bg='grey', image=self.frame_photo_3)
        frame_label_3.place(x=0, y=0)
        frame_label_3.bind('<B1-Motion>', controller.move_app)

        age_entry = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=7, bg='#141414', bd=0, fg='#939597')
        age_entry.insert(0, age)
        age_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, age_entry, "age"))
        age_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, age_entry, "age"))
        age_entry.place(x=188, y=367)

        gender_entry = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=10, bg='#141414', bd=0, fg='#939597')
        gender_entry.insert(0, gender)
        gender_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, gender_entry, "gender"))
        gender_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, gender_entry, "gender"))
        gender_entry.place(x=370, y=367)

        weight_entry = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=20, bg='#141414', bd=0, fg='#939597')
        weight_entry.insert(0, weight)
        weight_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, weight_entry, "weight"))
        weight_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, weight_entry, "weight"))
        weight_entry.place(x=188, y=456)

        height_entry = tk.Entry(self, font=('iCiel Gotham Medium', 18), width=20, bg='#141414', bd=0, fg='#939597')
        height_entry.insert(0, height)
        height_entry.bind('<FocusIn>', lambda event: controller.on_entry_click(event, height_entry, height))
        height_entry.bind('<FocusOut>', lambda event: controller.on_focusout(event, height_entry, height))
        height_entry.place(x=188, y=545)

        

        self.submit_box = tk.PhotoImage(file=r'/home/spring/Test101/FitnessProject/View/Images/Submit.png')
        submit_button = tk.Button(self, image=self.submit_box, bd=0, bg='#141414', activebackground='#141414',
                                  command=lambda: [Logic.add_health_info(gender_entry.get(), age_entry.get(), height_entry.get(), weight_entry.get()),controller.show_frame('HomePage'), Logic.display_health(posx =[267, 485], posy= [304, 372, 440])])
        submit_button.place(x=171, y=623)
        
        connect.commit()
        connect.close()