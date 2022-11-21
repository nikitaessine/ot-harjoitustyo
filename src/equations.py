import random

class Equations:

    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.right_result = 0
        self.operators = ["+", "-"]
        self.cheers = ["Hyvää työtä!", 
                        "Hyvin opittu!", 
                        "Oikein! Jatka samaan malliin :)"]
        self.cheers_if_wrong_answer = ["Väärin! Kokeile uudestaan", 
                                        "Hups! Nyt jokin meni pieleen", 
                                        "Melkein! Kokeile uudestaan"]
    

    def askResult(self):
        while True:
            try:
                return int(input())
            except ValueError:
                print("Anna vain numeroita!")
    
    def equation_generator(self):

        self.num1 = random.randint(0,10)
        self.num2 = random.randint(0,10)

        operat = random.choice(self.operators)

        print(f"Paljonko on {self.num1} {operat} {self.num2}?")
    

        if operat == "+":
            self.plus()
        else:
            self.minus()
        
        self.result_checker()

    def result_checker(self):

        user_result = self.askResult()

        if self.right_result == user_result:
            print(random.choice(self.cheers))
        else:
            print(random.choice(self.cheers_if_wrong_answer))

    def plus(self):
        
        self.right_result = self.num1 + self.num2
        return self.right_result
    
    def minus(self):

        self.right_result =  self.num1 - self.num2
        return self.right_result