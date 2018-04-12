from tkinter import Tk, Label, Button, Entry, StringVar
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="Enter the Name You Want Printed")
        self.label.pack()

        self.name = StringVar()

        self.name_box = Entry(master, textvariable=self.name)
        self.name_box.pack()


        self.greet_button = Button(master, text="Print The Name", command=self.print_name)
        self.greet_button.pack()


    def print_name(self):
        print(self.name_box.get())

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
