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
              20.180, 22.990, 24.305, 26.982, 28.085, 30.974, 32.06, ]

funFacts = []

score = 0

questionPool = [atomicNumbers, atomicMass, funFacts]
currentQuestion = []
currentAnswer = []

# CONTINUE HERE FOR MOGULDORF
'''
def qGen():

'''
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
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
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
