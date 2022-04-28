import csv

from tkinter import *

class App:

    def __init__(self, root, l, num_row, num_collumn):
        self.master = root
        self.master.title("LIST EMPLOYEE")
        self.label = Label(self.master, text="PLEASE ENTER THE ID", bg="grey", width="250", font=("Calibri", 13))
        for i in range(num_row):
            for j in range(num_collumn):
                self.e = Entry(self.master, width=15,
                               font=('Courier New', 10, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, l[i][j])
                self.e.config(state="disable")


def show():
    l = []
    f1 = open("DsNhanVien.csv", "r")
    for x in csv.reader(f1):
        l.append(x)
    f1.close()
    f1 = open("DsNhanVien.csv", "r")
    num_row = sum(1 for line in f1)
    num_collumn = 11

    f1.close()

    root = Tk()
    t = App(root,l,num_row,num_collumn)
    root.mainloop()
