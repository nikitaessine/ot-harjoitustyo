from tkinter import Tk, ttk, constants, StringVar
from equations import Equations
import random

class UI:
    def __init__(self, root, equations: Equations):
        self._root = root
        self.label_var = None
        self.label_cheer = None
        self.equations = equations
        #self.value = 0
        #self.right_result = 0
        self.answer = None

    def change_equation(self):
        self.equations.equation_generator()
        self.label_var.set(self.equations)
        self.label_cheer.set(self.result_checker())
        
    
    def get_entry_value(self):
        #value = 0
        value = self.answer.get()
       # print("value is ", value)
        return value 


    def start(self):
        self.equations.equation_generator()
        self.label_var = StringVar()
        self.label_cheer = StringVar()
        self.label_var.set(self.equations)

        heading_label = ttk.Label(master=self._root, text='Lasketaanpas vähän matikkaa!')
        label = ttk.Label(master=self._root, textvariable=self.label_var)
        self.answer = ttk.Entry(master=self._root)
        #self.answer.bind(self.get_entry_value())
        

        print("menee tähä")
        
        
        

        if self.result_checker() == self.get_entry_value():
            answer_label = ttk.Label(master=self._root, textvariable=self.label_cheer)
        else:
            answer_label = ttk.Label(master=self._root, textvariable=self.label_cheer)


    
        answer_button = ttk.Button(
            master=self._root,
            text="vastaa",
            command=lambda:[self.result_checker(),self.change_equation()]
        )

        '''
        new_equation_button = ttk.Button(
            master=self._root,
            text="seuraava",
            command=self.change_equation()

        )
        '''
        
        heading_label.grid(row=0,column=0)
        label.grid(row=1, column=0)
        self.answer.grid(row=2,column=0)
        answer_label.grid(row=3, column=0)
        answer_button.grid(row=4, column=0)
        #new_equation_button.grid(row=4, column=1)
        
    def result_checker(self):
        #print("entry value", self.get_entry_value())
        
        if self.equations.operat == '+':

            right_result = self.equations.plus()
            print("oikea vastaus", right_result)
            #print(random.choice(self.equations.cheers), self.right_result)
            #print(self.right_result)
            #print(self.value)
            value = self.get_entry_value()
            print("value", value)

            if right_result == value:
                
                print("meni oikeesttin iffiin")
                return random.choice(self.equations.cheers_if_wrong_answer)
               
            else:
                return random.choice(self.equations.cheers)
        
        else:

            right_result = self.equations.minus()
            print("meni miinukseen")
            #print(self.right_result)
            value = self.get_entry_value()
            print("value", value)

            if right_result == self.get_entry_value():
                print(random.choice(self.equations.cheers), right_result)

                return random.choice(self.equations.cheers_if_wrong_answer)
            else:
                return random.choice(self.equations.cheers)


        
    
    
    