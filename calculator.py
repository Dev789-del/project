import math


class Calculator:
    """**
    * @Descriptions: Calculator class contain all the function for calculating statistics for users
    **"""
    def round_down(self, n, decimals=0):
        """**
    *
    * float round_down(self, n, decimals=0):
    *   muliplier = 10 ** decimals
    *   return math.floor(n * multiplier) / multiplier
    *
    **"""
        multiplier = 10 ** decimals
        return math.floor(n * multiplier) / multiplier

    def calculate_BMI(self, weight, height):
        """**
        *
        * float calculate_BMI(self, weight, height):
        *    self.BMI = weight / (height ** 2)
        *    return Calculator.round_down(sef, self.BMI, 2)
        *
        *"""
        self.BMI = weight / (height ** 2)
        return Calculator.round_down(self, self.BMI, 2)

    def calculate_body_fat(self, age, weight, height, gender):
        """**
        *
        * float calculate_body_fat(self, age, weight, height, gender):
        *    self.BMI = Calcualtor.calculate_BMI(weight, height)
        * if age < 18:
        *    self.body_fat = ((1.51 * self.BMI) - (0.7 * age) - (3.6 * gender) + 1.4)

        * else:
        *    self.body_fat = ((1.2 * self.BMI) - (0.23 * age) - (10.8 * gender) - 5.4)

        * return Calculator.round_down(self, self.body_fat, 2)
        *
        *"""
        self.BMI = Calculator().calculate_BMI(weight, height)

        if age < 18:
            self.body_fat = ((1.51 * self.BMI) - (0.7 * age) - (3.6 * gender) + 1.4)

        else:
            self.body_fat = ((1.2 * self.BMI) - (0.23 * age) - (10.8 * gender) - 5.4)

        return Calculator.round_down(self, self.body_fat, 2)

    def calculate_LBM(self, weight, height, gender):
        """**
        *
        * float calculate_LBM (self, weight, heigt, gender):
        *    if gender == 1:
        *       self.LBM = 0.407 * weight + 0.267 * height - 19.2
        *    else:
        *       self.LBM = 0.252 * weight + 0.473 * height - 48.3
        *
        * return Calculator.round_down(self, self.LBM, 2)
        *
        *
        """
        if gender == 1:
            self.LBM = 0.407 * weight + 0.267 * height - 19.2
        else:
            self.LBM = 0.252 * weight + 0.473 * height - 48.3

        return Calculator.round_down(self, self.LBM, 2)

    def calculate_BMR(self, weight, age, height, gender):
        """**
        * float calculate_BMR(self, weight, age, height, gender):
        *   if gender == 1:
        *       self.BMR = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
        *   else:
        *       self.BMR = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
        *
        *   return Calculator.round_down(self, self.BMR, 2)
        *       
        *"""
        if gender == 1:
            self.BMR = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
        else:
            self.BMR = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)

        return Calculator.round_down(self, self.BMR, 2)


