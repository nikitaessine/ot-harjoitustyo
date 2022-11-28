from equations import Equations
from tkinter import Tk
from ui import UI

def main():

    window = Tk()
    window.title("Matikkasovellus")
    equat = Equations()
    ui = UI(window,equat)
    ui.start()

    window.mainloop()

    #print("Hei! lasketaanpas vähän matikkaa")


if __name__ == "__main__":
    main()