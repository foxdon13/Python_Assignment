class Person:
    def __init__(self, age):
        if int(age) < 0:
            self.age = 0
            print("Age is not valid, setting age to 0")
        else:
            self.age = int(age)

    def yearPasses(self, year_pass):
        self.age = self.age + year_pass

    def amIOld(self):

        if self.age > 0 and self.age < 13:
            print("You are young.")
        elif self.age > 13 and self.age <= 19:
            print("You are a teenager")
        else:
            print("You are old.")


person1 = Person(-9)
person1.amIOld()
