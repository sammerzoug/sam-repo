class Testclass:
    age = 0
    sex = " "
    def __init__(self, age, sex):
        self.age = age
        self.sex = sex

    def fox(self):
        print("Your age is " + self.age + "\nYou are a " + self.sex)
