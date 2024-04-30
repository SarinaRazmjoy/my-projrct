list1 = []


class person:
    def __init__(self, name, family, age, national_code, start):
        self.name = name
        self.family = family
        self.age = age
        self.national_code = national_code
        self.start = start
        
    def report_card1(self):
        global x
        x = self.name + " " + self.family + "\n age:" + \
            str(self.age) + "\n national_code:" + \
            str(self.national_code) + "\n start:" + str(self.start) + "\n "
        return x
    # print('------------------')


class person_lessons:

    def __init__(self, riazi, physics, olomComputer, tarikh):
        self.riazi = riazi
        self.physics = physics
        self.olomComputer = olomComputer
        self.tarikh = tarikh
        

    def report_card2(self):
        global y
        y = "riazi: " + str(self.riazi) + "\n physics: " + str(self.physics) + \
            "\n olomComputer: " + \
            str(self.olomComputer) + "\n tarikh: " + \
            str(self.tarikh) + "\n " + "___________" + "\n "
        return y
