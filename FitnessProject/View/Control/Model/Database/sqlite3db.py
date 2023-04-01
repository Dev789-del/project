import sqlite3

#Create the database and connect to it 
connection = sqlite3.connect(r'/home/spring/Test101/FitnessProject/View/Control/Model/Database/Fitness.db')
cursor = connection.cursor() #cursor for database command

#Create a table for user info 
cursor.execute("DROP TABLE IF EXISTS user")
cursor.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, username CHAR, name CHAR, password CHAR, phone_number CHAR)")

#User table data dump
cursor.execute("INSERT INTO user (username, name, password, phone_number) VALUES ('admin', 'Tran Giang Son', '4gH2k3kDR', '035635466')")
cursor.execute("INSERT INTO user (username, name, password, phone_number) VALUES ('tensingnightco', 'Ho Cong Thanh', '14o35XoWU','012346456')")
cursor.execute("INSERT INTO user (username, name, password, phone_number) VALUES ('killerxkiller', 'Dinh Huy Thai Son', '8979wE7P2', '035573565')")
cursor.execute("INSERT INTO user (username, name, password, phone_number) VALUES ('spring317', 'Dao Xuan Quy', '7bM7R79Cp', '012346644')")
cursor.execute("INSERT INTO user (username, name, password, phone_number) VALUES ('fuyohaiyaaa', 'Phung Dam Quan', '64X5kIVoN', '035572435')")
cursor.execute("INSERT INTO user (username, name, password, phone_number) VALUES ('kiwiahihi', 'Nguyen Tran Duc Quy', 'p746BhrZ5', '012354533')")

connection.commit()

#Create a table for health info
cursor.execute("DROP TABLE IF EXISTS health")
cursor.execute("CREATE TABLE IF NOT EXISTS health (id INTEGER PRIMARY KEY AUTOINCREMENT, username CHAR, gender CHAR, age INT, height FLOAT, weight FLOAT, bmi FLOAT, bmr FLOAT, bodyfat FLOAT, lbm FLOAT)")

#Health table data dump
cursor.execute("INSERT INTO health (username, gender, age, height, weight, bmi, bmr, bodyfat, lbm) VALUES ('admin', '1', NULL, NULL, NULL, NULL, NULL, NULL, NULL)")
cursor.execute("INSERT INTO health (username, gender, age, height, weight, bmi, bmr, bodyfat, lbm) VALUES ('tensingnightco', '1', 20, 1.74, 65.7, 21.7, 1650, 13.7, 54.0)")
cursor.execute("INSERT INTO health (username, gender, age, height, weight, bmi, bmr, bodyfat, lbm) VALUES ('killerxkiller', '1', 25, 1.77, 63.7, 20.3, 1623, 11.9, 54.0)")
cursor.execute("INSERT INTO health (username, gender, age, height, weight, bmi, bmr, bodyfat, lbm) VALUES ('spring317', '1', 20, 1.75, 73.4, 24.0, 1743, 17.4, 57.4)")
cursor.execute("INSERT INTO health (username, gender, age, height, weight, bmi, bmr, bodyfat, lbm) VALUES ('fuyohaiyaaa', '1',  22, 1.69, 74.4, 26.0 , 1695, 20.8, 56.2)")
cursor.execute("INSERT INTO health (username, gender, age, height, weight, bmi, bmr, bodyfat, lbm) VALUES ('kiwiahihi', '1',  21, 1.76, 63.2, 20.4, 1642, 11.7, 53.5)")

connection.commit()

#Create a table for exercise info
cursor.execute("DROP TABLE IF EXISTS exercise")
cursor.execute("CREATE TABLE IF NOT EXISTS exercise (id INTEGER PRIMARY KEY AUTOINCREMENT, exername CHAR, effectarea CHAR, difficulty CHAR, note CHARC)")


#User table data dump
cursor.execute("INSERT INTO exercise (exername, effectarea, difficulty, note) VALUES ('push-ups', 'overall', 'easy', 'none')")
cursor.execute("INSERT INTO exercise (exername, effectarea, difficulty, note) VALUES ('triceps dips', 'arm', 'easy', 'chair required')")
cursor.execute("INSERT INTO exercise (exername, effectarea, difficulty, note) VALUES ('floor tricep dips', 'arm', 'medium', 'optional tool: mattress')")
cursor.execute("INSERT INTO exercise (exername, effectarea, difficulty, note) VALUES ('squats', 'leg', 'easy', 'none')")
cursor.execute("INSERT INTO exercise (exername, effectarea, difficulty, note) VALUES ('cat cow pose', 'shoulder & back', 'easy', 'none')")

connection.commit()

#Total changes to the database and terminate connection
print(connection.total_changes)
connection.close()




    





