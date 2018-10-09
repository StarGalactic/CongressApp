'''
Copyright © 2017 Daniel Moon, Luke Moon, Michael Kricheldorf
All Rights Reserved. This code may not be reproduced or reused in any manner whatsoever
without the consent of the writer.
'''



import random
import tkinter as tk

root = tk.Tk()

#helv36 = tk.tkFont.Font(family='Helvetica',
#        size=36, weight='bold')
#parallel lists

elementNames = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon",
            "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium",
            "Aluminium", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon",
            "Potassium", "Calcium", "Scandium", "Titainiium", "Vanadium", "Chromium",
            "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium",
            "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium",
            "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium",
            "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin",
            "Antimony", "Tellurium", "Iodine", "Xenon", "Caesium", "Barium", "Lanthanum",
            "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium",
            "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium",
            "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium",
            "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead",
            "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium",
            "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium",
            "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium",
            "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium",
            "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium",
            "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Organesson"]

atomicNumber = []
for i in range(1, 119):
    atomicNumber.append(i)

atomicMass = [1.008, 4.0026, 6.94, 9.0122, 10.81, 12.011, 13.007, 15.999, 18.998,
              20.180, 22.990, 24.305, 26.982, 28.085, 30.974, 32.06, 35.45, 39.948,
              39.098, 40.078, 44.956, 47.867, 50.942, 51.996, 54.938, 55.845, 58.933,
              58.693, 63.546, 65.38, 69.723, 72.630, 74.922, 78.971, 79.904, 83.798,
              85.468, 87.62, 88.906, 91.224, 92.906, 95.95, 98, 101.07, 102.9, 106.42,
              107.87, 112.41, 114.82, 118.71, 121.76, 127.60, 126.90, 131.29, 132.91,
              137.33, 138.91, 140.12, 140.91, 144.24, 145, 150.36, 151.96, 157.25, 158.93,
              162.50, 164.93, 167.26, 168.93, 173.05, 174.97, 178.49, 180.95, 183.84,
              186.21, 190.23, 192.22, 195.08, 196.97, 200.59, 204.38, 207.2, 208.98,
              209, 210, 222, 223, 226, 227, 232.04, 231.04, 238.03, 237, 244, 243, 247,
              247, 251, 252, 257, 258, 259, 266, 267, 268, 269, 270, 277, 278, 281,
              282, 285, 286, 289, 290, 293, 294, 294]

funFacts = []

score = 0

questionPool = [atomicNumbers, atomicMass, funFacts]
currentQuestion = ""
currentAnswer = []
randomElement = 0
userAnswer = ""

def qAGen():
    # generates random "element", but actually the element's index, so (<atomicNumber> - 1)
    randomElement = random.randrange(118)
    # generates the actual element(the answer)
    currentAnswer = atomicNumber[randomElement]
    # generates the question using the randomElement index within one of the question pools
    currentQuestion = random.choice(questionPool)[randomElement]

def isCorrect():
    # just checks if the user's answer is the same as the actual answer (currentAnswer =? userAnswer)
    if userAnswer.lower() == currentAnswer.lower():
        return True
    elif userAnswer.lower() != currentAnswer.lower():
        return False

class Application(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.createWidgets()
    #def start(self):
    def createWidgets(self):
        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)   # HEY DAN! I don't know what all this tkinter nonsense means but make sure that the variable
        self.columnconfigure(0, weight=1)  # you use for user input transfers to the variable named "userAnswer" in my functions
        self.quit = tk.Button(self, text='Quit', command=self.quit)
        self.quit.grid(row=0, column=0,
            sticky=tk.N+tk.S+tk.E+tk.W)

#configures size of the window and initiates the running of the UI along with the title of the window
app = Application()
app.geometry =  '400x400-0+20'
app.master.title('Periodic_flash_cards')
app.mainloop()


'''
if __name__ == '__main__':
    main()
'''
