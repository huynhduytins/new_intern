from tkinter import *

from PIL import Image, ImageTk

root = Tk()


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("MANAGER")
        self.master.geometry("800x700")

        self.load = Image.open("background.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.img = Label(root, image=self.render)
        self.img.place(x=0, y=0)

        self.name = Label(self.master, text='ADMIN MANAGEMENT', fg='#FFFFFF', bd=0, bg='#03152D')
        self.name.config(font=("Courier New", 30))
        self.name.pack(pady=10)

    def button(self):
        button_dict = {}
        option = ["ADD A EMPLOYEE", "DELETE EMPLOYEE", "MODIFY EMPLOYEE", "SHOW THE LIST", "CHANGE THE PASSWORD"]
        for i in option:
            button_dict[i] = Button(self.master, height="2", width="20", text=i, font=(("Courier New"), 10, 'bold'),
                                    bg='#03152D', fg='#FFFFFF', command=i)
            button_dict[i].pack(pady="35")
        button_dict["ADD A EMPLOYEE"].config(command=self.add)
        button_dict["DELETE EMPLOYEE"].config(command=self.dele)
        button_dict["MODIFY EMPLOYEE"].config(command=self.modify)
        button_dict["SHOW THE LIST"].config(command=self.show)
        button_dict["CHANGE THE PASSWORD"].config(command=self.change)

    def add(self):
        import info
        info.display("SAVE")

    def dele(self):
        import search
        search.read("DELETE")

    def modify(self):
        import search
        search.read("MODIFY")

    def show(self):
        import show
        show.show()

    def change(self):
        import password
        password.read(0)


def manage():
    e = App(root)
    e.button()
    root.mainloop()
