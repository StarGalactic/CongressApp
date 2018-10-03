from tkinter import *
root = Tk()

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.init_window()
    def init_window(self):
        self.master.title("UI")
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Exit", command = self.exit)
        menu.add_cascade(label="File", menu=file)
    def exit(self):
        exit()

root.geometry("400x400")
app = Window(root)
root.mainloop()
