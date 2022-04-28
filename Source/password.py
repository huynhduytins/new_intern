from tkinter import *


class App:

    def __init__(self, master, s):
        f = open("password.txt")
        self.s = s
        self.master = master
        self.username = 'admin123'
        self.password = f.read()

    def screen(self):
        self.master.geometry("300x250")
        self.master.title("LOGIN")
        self.label = Label(self.master, text=self.s, bg="grey", width="250", font=("Calibri", 13))
        self.label.pack()

        Label(self.master, text="").pack()

        Label(self.master, text="User name" if self.s == 'ADMIN LOGIN' else 'The old password').pack()
        self.un = Entry(self.master)
        self.show(self.un, self.s)
        self.un.pack()
        Label(self.master, text="").pack()

        Label(self.master, text="Password" if self.s == 'ADMIN LOGIN' else 'New password').pack()
        self.pw = Entry(self.master)
        self.pw.config(show="*")
        self.pw.pack()
        Label(self.master, text="").pack()

        self.button = Button(self.master, text='LOGIN' if self.s == 'ADMIN LOGIN' else 'CHANGE', height="2", width="10",
                             command=self.login if self.s == 'ADMIN LOGIN' else self.change)
        self.button.pack()

    def show(self, p, d):
        if d == 'CHANGE THE PASSWORD':
            p.config(show="*")
        else:
            pass

    def login(self):
        if self.un.get() == self.username and self.pw.get() == self.password:
            self.master.after(1000)
            self.master.destroy()
            import manage
            manage.manage()
        elif self.un.get() == '':
            self.label.config(text="please enter the USERNAME", fg='#FF0606')
        elif self.pw.get() == '':
            self.label.config(text="please enter the PASSWORD", fg='#FF0606')
        else:
            self.label.config(text="username or password is incorrect", fg='#FF0606')
            self.pw.delete(0, END)
            self.un.delete(0, END)


    def change(self):
        if self.un.get() == self.password and len(self.pw.get()) >= 8:
            self.label.config(text="CHANGE THE PASSWORD SUCCESSFUL", fg='#A1FF06')
            self.password = self.pw.get()
            f = open("md.txt", "w")
            f.write(self.password)
            self.master.after(1000)
            self.master.destroy()
        elif self.un.get() == '':
            self.label.config(text="please enter the old password", fg='#FF0606')
        elif self.pw.get() == '':
            self.label.config(text="please enter new password", fg='#FF0606')
        elif self.un.get() != self.password:
            self.label.config(text="the old password is incorrect", fg='#FF0606')
            self.pw.delete(0, END)
            self.un.delete(0, END)
        elif len(self.pw.get()) < 8:
            self.label.config(text="new password must above 8 characters", fg='#FF0606')
            self.pw.delete(0, END)
            self.un.delete(0, END)


def read(i):
    root = Tk()
    if i == 1:
        e = App(root, 'ADMIN LOGIN')
        e.screen()
    else:
        e = App(root, 'CHANGE THE PASSWORD')
        e.screen()
    root.mainloop()
