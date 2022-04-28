from tkinter import *


class InfoEmployee:

    def __init__(self, em_code, name, marital_status, num_children, edu_level, base_salary, personal_leave=0,
                 non_accept_leave=0, OT=0, work_result='None', real_salary=0):
        self.em_code = em_code
        self.name = name
        self.marital_status = marital_status
        self.num_children = num_children
        self.edu_level = edu_level
        self.base_salary = base_salary
        self.personal_leave = personal_leave
        self.non_accept_leave = non_accept_leave
        self.OT = OT
        self.work_result = work_result
        self.real_salary = real_salary


class App:
    listEmployee = []

    def __init__(self, master, s):
        self.master = master
        self.s = s

    def screen(self):
        self.master.geometry("300x250")
        self.master.title("SEARCH")
        self.label = Label(self.master, text="PLEASE ENTER THE ID", bg="grey", width="250", font=("Calibri", 13))
        self.label.pack()

        Label(self.master, text="").pack(pady=20)

        self.un = Entry(self.master, width=20, justify='center')
        self.un.pack()

        Label(self.master, text="").pack()

        Label(self.master, text="").pack()

        self.button = Button(self.master, text='SEARCH', height="1", width="10", command=self.search)
        self.button.pack()

    def readFile(self, file):
        self.listEmployee = []
        with open(file, mode='r') as md:
            for r in md:
                r = r.split(',')
                self.listEmployee.append(
                    InfoEmployee(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10]))

    def findEm(self, em_code):

        if (len(self.listEmployee) > 0):
            for em in self.listEmployee:
                if (em.em_code == em_code):
                    return em
        return None

    def search(self):

        self.readFile("DsNhanVien.csv")
        print(self.listEmployee)

        emp = self.un.get()

        if emp == '':
            self.label.config(text="PLEASE ENTER THE ID", fg='#FF0606')

        elif self.s == 'DELETE':
            em = self.findEm(emp)
            if em == None:
                self.label.config(text="THE ID DOES NOT EXIST", fg='#FF0606')
                self.un.delete(0, END)
            else:
                print(em.name)
                self.master.destroy()
                import info
                info.displayDele(em, 'DELETE')
        else:
            em = self.findEm(emp)
            if em == None:
                self.label.config(text="THE ID DOES NOT EXIST", fg='#FF0606')
                self.un.delete(0, END)
            else:
                print(em.name)
                self.master.destroy()
                import info
                info.displayDele(em, 'MODIFY')


def read(s):
    root = Tk()
    e = App(root, s)
    e.screen()
    root.mainloop()
