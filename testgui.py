from tkinter import Tk, Label, Button, Entry, StringVar, Text, IntVar
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        master["bg"] = "orchid4"

        self.label = Label(master, text="Enter the Name You Want Printed:")
        self.label.pack()

        self.name = ""
        self.name_length = 0

        self.name_entry_text = StringVar()
        self.name_label_text = StringVar()
        self.name_label_text.set("Name:")
        self.name_length_text = StringVar()
        self.name_length_text.set("Length:")


        self.name_entry = Entry(master, textvariable=self.name_entry_text)
        self.name_entry.pack()

        self.submit_button = Button(master, text="Print The Name", command=self.submit_name)
        self.submit_button.pack()

        self.name_label = Label(master, textvariable = self.name_label_text)
        self.name_label.pack()
        self.length_label = Label(master, textvariable = self.name_length_text)
        self.length_label.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def submit_name(self):
        self.name = self.name_entry.get()
        self.name_length = len(self.name)
        print(self.name)
        print(self.name_length)
        self.name_label_text.set("Name: " + self.name)
        self.name_length_text.set("Length: " + str(self.name_length))

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
