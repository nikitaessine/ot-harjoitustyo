from tkinter import ttk, StringVar
import random
from service.equations import Equations


class UI:
    """Käyttöliittymästä vastaava luokka"""

    def __init__(self, root, equations: Equations):
        """Luokan konstruktori
        Args:
            root: Tkrinter-elementti, jonka sisälle käyttöliittymä alustetaan
            label_var: Generoitu lauseke
            equations: Equations-luokan olio
            answer: Tähän talletetaan käyttäjän syöttämä luku
            cheer_label: Kannustusviesti
        """
        self._root = root
        self.label_var = None
        self.equations = equations
        self.answer = None
        self.cheer_label = None

    def start(self):
        """Käyttöliittymän komponenttien luonti"""
        self.equations.equation_generator()
        self.label_var = StringVar()
        self.label_var.set(self.equations)

        heading_label = ttk.Label(
            master=self._root, text='Lasketaanpas vähän matikkaa!')
        label = ttk.Label(master=self._root, textvariable=self.label_var)
        self.answer = ttk.Entry(master=self._root)
        self.cheer_label = ttk.Label(
            master=self._root, text='Tsemppiä tehtäviin :)')


        check_button = ttk.Button(
            master=self._root,
            text="tarkasta",
            command=lambda: [self.user_cheer(self.equations.result_checker(
                self.entry_value())), self.clear_text()]
        )

        next_button = ttk.Button(
            master=self._root,
            text="seuraava",
            command=lambda: [self.change_equation(), self.clear_text()]
        )

        heading_label.grid(row=0, column=0)
        label.grid(row=1, column=0)
        self.answer.grid(row=2, column=0)
        self.cheer_label.grid(row=3, column=0)
        check_button.grid(row=4, column=0)
        next_button.grid(row=4, column=1)


    def change_equation(self):
        """Kutsuu Equations-luokan olion metoda, joka vaihtaa lausekkeen

           Asettaa merkkijonon label-komponenttiin 

        """
        print('change equationis ollaa')
        self.equations.equation_generator()
        self.label_var.set(self.equations)

    def entry_value(self):
        """Tallettaa käyttäjän syöttämän luvun
        
        Returns:
            Käyttäjän syöttämä luku
        """
        value = self.answer.get()
        return value

    def user_cheer(self, boolean):
        """Kannustaa käyttäjää vastauksesta riippuen
        
        Args:
            boolean: True, jos oikea vastaus
        """
        cheer = ''
        print(boolean)
        if boolean == True:
            cheer = self.equations.cheer_if_right_result()
        else:
            cheer = self.equations.cheer_if_wrong_result()
        self.cheer_label.config(text=cheer)

    def clear_text(self):
        """Tyhjentää tekstikentän"""
        self.answer.delete(0)
