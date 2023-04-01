import math
class Calculator:
    def calculate_BMI(self, weight, height):
        self.BMI = weight / (height ** 2)
        return math.floor(self.BMI*(10**2))/10**2

    def calculate_body_fat(self, age, weight, height, gender):
        self.BMI = Calculator().calculate_BMI(weight, height)

        if gender == 1:
            self.body_fat = ((1.2 * self.BMI) + (0.23 * age) - 16.2)

        else:
            self.body_fat = ((1.2 * self.BMI) + (0.23 * age) - 5.4)

        return math.floor(self.body_fat*(10**2))/10**2

    def calculate_LBM(self, weight, height, gender):
        if gender == 1:
            self.LBM = 0.32810 * weight + 0.33929 *(height*100) - 29.5336
        else:
            self.LBM = 0.29569 * weight + 0.41813 * (height*100 )- 43.2933

        return math.floor(self.LBM * (10**2))/10**2

    def calculate_BMR(self, weight, age, height, gender):
        if gender == 1:
            self.BMR = 88.362 + (13.397 * weight) + (4.799 * (height*100)) - (5.677 * age)
        else:
            self.BMR = 447.593 + (9.247 * weight) + (3.098 * (height*100)) - (4.33 * age)

        return math.floor(self.BMR*(10**2))/10**2


