import random


class Equations:

    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.right_result = 0
        self.operat = ""
        #self.cheer = ""
        #self.cheer_if_wrong = ""
        self.operators = ["+", "-"]
        self.cheers = ["Hyvää työtä!",
                       "Hyvin opittu!",
                       "Oikein! Jatka samaan malliin :)"]

        self.cheers_if_wrong_answer = ["Väärin! Kokeile uudestaan",
                                       "Hups! Nyt jokin meni pieleen",
                                       "Melkein! Kokeile uudestaan"]

    def ask_result(self):
        while True:
            try:
                return int(input())
            except ValueError:
                print("Anna vain numeroita!")

    def equation_generator(self):

        self.num1 = random.randint(0, 10)
        self.num2 = random.randint(0, 10)

        self.operat = random.choice(self.operators)

    def plus(self):

        right_result = self.num1 + self.num2
        return right_result

    def minus(self):

        right_result = self.num1 - self.num2
        return right_result

    def result_checker(self, entry_value):
        print('result checkerii päästii')
        if self.operat == '+':
            print("entry value", entry_value)
            if entry_value == self.plus():
                return True
            return False

        else:
            print("entry value", entry_value)
            if entry_value == self.minus():
                return True
            return False

    def cheer_if_right_result(self):
        self.cheer = random.choice(self.cheers)
        return self.cheer

    def cheer_if_wrong_result(self):
        self.cheer_if_wrong = random.choice(self.cheers_if_wrong_answer)
        return self.cheer_if_wrong

    def __str__(self):
        return f"Paljonko on {self.num1} {self.operat} {self.num2}?"
