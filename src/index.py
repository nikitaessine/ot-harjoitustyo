from tkinter import Tk
from service.equations import Equations
from ui.ui import UI


def main():
    """Pääohjelma, jossa luodaan oliot kaikelle
    tarvittavalle toiminnallisuudelle    
    """

    window = Tk()
    window.title("Matikkasovellus")
    equat = Equations()
    ui = UI(window, equat)
    ui.start()

    window.mainloop()

if __name__ == "__main__":
    main()
