import random


class Equations:
    """Luokka, jonka avulla luodaan lauseke ja tehdään
    matemaattinen toiminnallisuus, palautetaan kannustusviestit

    Attributes:
        num1: Lausekkeen ensimmöinen numero
        num2: Lausekkeen toinen numero
        right_result: Lausekkeen oikea vastaus
        operat: Lausekkeen operaattori
        operators: Mahdolliset operaattorit
        cheers: Kannustusviesti, jos oikea vastaus
        cheers_if_wrong_answer: Kannustusviesti, jos väärä vastaus
    """

    def __init__(self):
        """Luokan konstruktori, joka luo lausekkeen

        Args:
            num1: Lausekkeen ensimmöinen numero
            num2: Lausekkeen toinen numero
            right_result: Lausekkeen oikea vastaus
            operat: Lausekkeen operaattori
            operators: Mahdolliset operaattorit
            cheers: Kannustusviesti, jos oikea vastaus
            cheers_if_wrong_answer: Kannustusviesti, jos väärä vastaus

        """
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
        """Tarkistaa onko vastaus annettu numeroina
        Args:
            int(input()): Käyttäjän syöttämä vastaus        
        """
        while True:
            try:
                return int(input())
            except ValueError:
                print("Anna vain numeroita!")

    def equation_generator(self):
        """Luo lausekkeen numeroista 0 ja 10 väliltä"""

        self.num1 = random.randint(0, 10)
        self.num2 = random.randint(0, 10)

        self.operat = random.choice(self.operators)

    def plus(self):
        """Laskee generoidun lausekkeen vastauksen

        Returns:
            Oikea vastaus
        """

        right_result = self.num1 + self.num2
        return right_result

    def minus(self):
        """Laskee generoidun lausekkeen vastauksen

        Returns:
            Oikea vastaus
        """

        right_result = self.num1 - self.num2
        return right_result

    def result_checker(self, entry_value):
        """Tarkistaa antoiko käyttäjä oikean vastauksen

        Args: 
            entry_value: Käyttäjän syöttämä luku

        Returns:
            True, jos oikea vastaus ja käyttäjän syöttämä luku ovat samat
        """
        if self.operat == '+':
            if entry_value == self.plus():
                return True
            return False

        else:
            if entry_value == self.minus():
                return True
            return False

    def cheer_if_right_result(self):
        """Antaa kannustusviestin, jos vastaus oikein

        Returns:
            Palauttaa kannsutusviestin        
        """
        self.cheer = random.choice(self.cheers)
        return self.cheer

    def cheer_if_wrong_result(self):
        """Antaa kannustusviestin, jos vastaus väärin

        Returns:
            Palauttaa kannsutusviestin        
        """
        self.cheer_if_wrong = random.choice(self.cheers_if_wrong_answer)
        return self.cheer_if_wrong

    def __str__(self):
        """Muodostaa lausekkeesta merkkijonomuotoisen esityksen

        Returns:
            Merkkijono, joka kertoo matemaattisen lausekkeen
        """
        return f"Paljonko on {self.num1} {self.operat} {self.num2}?"
