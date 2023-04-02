import sqlite3
from .Model.calculator import Calculator
from tkinter import messagebox
import tkinter as tk 
import subprocess
import pickle
class Logic:
    stats_position = []
    stat_admin_position = []
    def check_sign_in(username, password):
        conn1 = sqlite3.connect(r'/home/spring/Test101/FitnessProject/View/Control/Model/Database/Fitness.db')
        cursor1 = conn1.cursor()
        cursor1.execute("SELECT username, password FROM user")
        results = cursor1.fetchall()
        for result in results:
            if username == result[0] and password == result[1]:
                return True
            elif username == 'Username':
                return False
        return False

    def check_admin(username, password):
        connect = sqlite3.connect(r'/home/spring/Test101/FitnessProject/View/Control/Model/Database/Fitness.db')
        cursor = connect.cursor()
        cursor.execute("SELECT username, password FROM user")
        results = cursor.fetchall()
        for result in results:
            if username == "admin" and password == result[1]:
                return True
        return False

    def check_health_info(username):
        conn2 = sqlite3.connect(r'/home/spring/Test101/FitnessProject/View/Control/Model/Database/Fitness.db')
        cursor2 = conn2.cursor()
        cursor2.execute("SELECT username FROM health")
        results = cursor2.fetchall()

        for result in results:
            if username == result[0]:
                return True
        return False

    def calculate_stats(user_name):
        conn3 = sqlite3.connect(r'/home/spring/Test101/FitnessProject/View/Control/Model/Database/Fitness.db')
        cursor3 = conn3.cursor()
        cursor3.execute("SELECT username, gender, age, height, weight FROM health")
        results = cursor3.fetchall()
        calculator = Calculator()

        for result in results:
            if user_name == result[0]:
                query = "UPDATE health SET bmi = ?, bmr = ?, bodyfat = ?, lbm = ? WHERE username = ?"
                bmi = calculator.calculate_BMI(float(result[4]), float(result[3]))
                bmr = calculator.calculate_BMR(float(result[4]), float(result[2]), float(result[3]), float(result[1]))
                bodyfat = calculator.calculate_body_fat(float(result[2]), float(result[4]), float(result[3]),
                                                        float(result[1]))
                lbm = calculator.calculate_LBM(float(result[4]), float(result[3]), float(result[1]))
                cursor3.execute(query, (bmi, bmr, bodyfat, lbm, user_name))
                conn3.commit()
                break

        conn3.close()

    def check_signup(username, name,phone_number, password, cf_password):
        conn2 = sqlite3.connect(r'/home/spring/Test101/FitnessProject/View/Control/Model/Database/Fitness.db')
        cursor2 = conn2.cursor()
        cursor2.execute("SELECT username FROM user")
        results = cursor2.fetchall()

        found = False
        for result in results:
            if username == result[0]:

                found = True
                break
            elif username == 'Username':
                found = False
            else:
                found = False
        if len(password) < 6:
            messagebox.showerror(title = "Error", message = "Password must has at least 6 characters!")
        else:
            if password == cf_password:
                if not found:
                    cursor2.execute("INSERT INTO user (username, name, password, phone_number) VALUES (?, ?, ?, ?)",
                                    (username, name, password, phone_number))
                    messagebox.showinfo("Success", "New account created successfully")
                else:
                    messagebox.showerror(title="Error", message = "Username existed!")
            else:
                messagebox.showerror(title="Error", message="Password does not match!")

        conn2.commit()
        conn2.close()

    def add_health_info( gender, age, height, weight):
        conn3 = sqlite3.connect(r'/home/spring/Test101/FitnessProject/View/Control/Model/Database/Fitness.db')
        cursor3 = conn3.cursor()
        cursor3.execute("SELECT username, age, height, weight FROM health")
        results = cursor3.fetchall()
        found = False
        with open("username.txt",'rb') as f:
            username = pickle.load(f)
        for result in results:
            if username == result[0]:
                
                found = True
                break
            else:
                found = False

        if not found:
            query = "INSERT INTO health (username, gender, age, height, weight) VALUES (?, ?, ?, ?, ?)"
            if gender == "1" or gender == "0":

                params = username, gender, age, height, weight

                # print(username)
                cursor3.execute(query, params)

                messagebox.showinfo("Success", "Submission successfully")
            else:
                messagebox.showerror(title="Error", message="Gender must be 1 for male and 0 for woman.")

        conn3.commit()
        Logic.calculate_stats(username)

        conn3.close()

    def display_health(posx, posy):
        conn4 = sqlite3.connect(r'/home/spring/Test101/FitnessProject/View/Control/Model/Database/Fitness.db')
        cursor4 = conn4.cursor()
        cursor4.execute("SELECT username, height, weight, bmi, bmr, bodyfat, lbm FROM health")
        results = cursor4.fetchall()
        with open("username.txt", 'rb') as f:
               username = pickle.load(f)
        print(username)
        
        for result in results:
            if username == result[0]:
                height = str(result[1])
                weight = str(result[2])
                bmi = str(result[3])
                bmr = str(result[4])
                bodyfat = str(result[5])
                lbm = str(result[6])
                # return [height, weight, bmi, bmr, bodyfat, lbm]

        health_info = [height + "m", weight + "kg", bmi + "kg/m2", bmr, bodyfat + "%", lbm + "lbf"]
        idx = 0
         
        for y in posy:
            for x in posx:
                info = tk.Label(bd=0, highlightthickness=0, borderwidth=0, font=('iCiel Gotham Medium', 15), text=health_info[idx], fg='#F5DF4D',
                                bg='#212121')
                info.place(x=x, y=y)
                Logic.stats_position.append(info)
                idx += 1


        idx = 0
        
    
    def delete_leftover(self):
        for position in Logic.stats_position:
            position.destroy()

    def delete_admin_leftover(self):
        for position in Logic.stat_admin_position:
            position.destroy()    
        
    def quit_program(frame):
            frame.quit()
    
    """def open_db():
        db_browser_path = r'/usr/bin/sqlitebrowser/usr/share/man/man1/sqlitebrowser.1.gz'
        db_file_path = r'/home/spring/Test101/FitnessProject/View/Control/Model/Database/Fitness.db'

        subprocess.Popen(db_browser_path, db_file_path)"""
   

    

    
            
            

            

           
            


        
        

    


