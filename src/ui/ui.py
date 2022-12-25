from tkinter import ttk, StringVar
import random
from service.equations import Equations


class UI:
    def __init__(self, root, equations: Equations):
        self._root = root
        self.label_var = None
        self.equations = equations
        #self.value = 0
        #self.right_result = 0
        self.answer = None
        #self.answer_label = None
        self.cheer_label = None

    def start(self):
        self.equations.equation_generator()
        self.label_var = StringVar()
        self.label_var.set(self.equations)

        heading_label = ttk.Label(
            master=self._root, text='Lasketaanpas vähän matikkaa!')
        label = ttk.Label(master=self._root, textvariable=self.label_var)
        self.answer = ttk.Entry(master=self._root)
        self.cheer_label = ttk.Label(
            master=self._root, text='Tsemppiä tehtäviin :)')

        print("menee tähä")

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

        #new_equation_button.grid(row=4, column=1)

    def change_equation(self):
        print('change equationis ollaa')
        self.equations.equation_generator()
        self.label_var.set(self.equations)
        # self.label_cheer.set(self.equations.result_checker(self.entry_value))

    def entry_value(self):
        print('entry values ollaa')
        value = self.answer.get()
        print(value)
        return value

    def user_cheer(self, boolean):
        print('user cheeris ollaa')
        cheer = ''
        print(boolean)
        if boolean == True:
            cheer = self.equations.cheer_if_right_result()
        else:
            cheer = self.equations.cheer_if_wrong_result()
        print('cheeer', cheer)
        self.cheer_label.config(text=cheer)

    def clear_text(self):
        self.answer.delete(0)
