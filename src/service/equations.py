import random


class Equations:

    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.right_result = 0
        self.operat = ""
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

        # if self.operat == "+":
        # self.plus()
        # else:
        # self.minus()

        # self.result_checker()

    def plus(self):

        right_result = self.num1 + self.num2
        return right_result

    def minus(self):

        right_result = self.num1 - self.num2
        return right_result

    def __str__(self):
        return f"Paljonko on {self.num1} {self.operat} {self.num2}?"
