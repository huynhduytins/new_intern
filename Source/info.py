import csv
from tkinter import *
from tkinter import messagebox


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

    def __init__(self, master, s, ms=0):
        self.master = master
        self.s = s
        self.ms = ms
        self.master.title("employee information")
        self.master.geometry('550x600')
        self.listEmployee = []

    def readFile(self):
        with open('DsNhanVien.csv', mode='r') as md:
            for r in md:
                r = r.split(',')
                self.listEmployee.append(
                    InfoEmployee(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10]))

    def max_id(self):
        d = 0
        with open('DsNhanVien.csv', mode='r') as f1:
            for x in csv.reader(f1):
                d+=1
        return d+1


    def listToString(s):
        str1 = " "
        return (str1.join(s))

    def ID(self):
        return len(self.listEmployee) + 1

    def remove(self, em_code):
        f1 = open("DsNhanVien.csv", "r")
        with open("new.csv", "w", encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            for x in csv.reader(f1):
                if int(x[0]) != int(em_code):
                    writer.writerow(x)
        f1.close()
        f1 = open("new.csv", "r")
        with open("DsNhanVien.csv", "w", encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            for x in csv.reader(f1):
                writer.writerow(x)
        f1.close()
        self.master.destroy()

    def screen(self):

        label = {}

        l = ["ID", "Tên", "Tình trạng hôn nhân", "Số người con", "Trình độ văn hóa", "Lương căn bản",
             "Số ngày nghỉ có phép", "Số ngày nghỉ không phép", "Số ngày làm thêm", "Kết quả công việc",
             "Lương thực tế"]

        self.heading = Label(self.master, text="Personal Details", bg="light green", font=("Courier New", 10, 'bold'))
        self.heading.grid(row=0, column=1)
        Label(self.master, text="").grid(row=1, column=1)
        for i in range(2, len(l) + 2):
            Label(self.master, text="").grid(row=i * 2 + 1, column=0)
            label[i] = Label(self.master, text=l[i - 2])
            label[i].grid(row=i * 2, column=0)

        self.entry = {}
        for i in range(2, len(l) + 2):
            Label(self.master, text="").grid(row=i * 2 + 1, column=1, padx='100')
            self.entry[l[i - 2]] = Entry(self.master, justify='center')
            self.entry[l[i - 2]].grid(row=i * 2, column=1, padx='100')

        if self.s == "SAVE":
            d = self.max_id()
            self.entry["ID"].insert(0, str(d))
            self.entry["ID"].config(state="disable")

        if self.s == 'DELETE':
            self.display(self.ms)
            self.submit = Button(self.master, text="DELETE", fg="Black", font=("Courier New", 10, 'bold'),
                                 command=self.delete)
            self.submit.grid(row=28, column=1)

        elif self.s == 'MODIFY':
            self.display(self.ms)
            self.submit = Button(self.master, text="SAVE", fg="Black", font=("Courier New", 10, 'bold'),
                                 command=self.save)
            self.submit.grid(row=28, column=1)

        else:
            self.submit = Button(self.master, text="ADD", fg="Black", font=("Courier New", 10, 'bold'),
                                 command=self.save)
            self.submit.grid(row=28, column=1)

    def delete(self):
        rep = messagebox.askquestion('Delete', 'Delete this employee. Are you sure?')
        if rep == 'yes':
            self.remove(self.ms.em_code)
        else:
            pass

    def save(self):

        if self.entry["Tên"].get() == "":
            self.message("Tên", "Không được phép để trống")

        elif self.entry["Tình trạng hôn nhân"].get() == "":
            self.message("Tình trạng hôn nhân", "Không được phép để trống")
        elif self.entry["Tình trạng hôn nhân"].get() not in ["M", "S"]:
            self.message("Tình trạng hôn nhân", "Phai nhap tinh trang gia dinh tuong ung voi:\n"
                                                "                M = married\n"
                                                "                S = Single\n")

        elif self.entry["Số người con"].get() == "":
            self.message("Số người con", "Không được phép để trống")
        elif int(self.entry["Số người con"].get()) > 20:
            self.message("Số người con", "Số người con không được vượt quá 20")

        elif self.entry["Trình độ văn hóa"].get() == "":
            self.message("Trình dộ văn hóa", "Không được phép để trống")
        elif self.entry["Trình độ văn hóa"].get() not in ['C1', 'C2', 'C3', 'DH', 'CH']:
            self.message("Trình độ văn hóa", "Phải nhập trình độ văn hóa tương ứng với:\n"
                                             "            C1 = cấp 1\n"
                                             "            C2 = cấp 2\n"
                                             "            C3 = cấp 3\n"
                                             "            DH = đại học\n"
                                             "            CH = cao học\n")

        elif self.entry["Lương căn bản"].get() == "":
            self.message("Lương căn bản", "Không được phép để trống")
        elif int(self.entry["Lương căn bản"].get()) > 1000000:
            self.message("Lương căn bản", "Lương căn bản không lớn hơn 1000000")

        elif self.entry["Số ngày nghỉ có phép"].get() == "":
            self.message("Số ngày nghỉ có phép", "Không được phép để trống")
        elif int(self.entry["Số ngày nghỉ có phép"].get()) > 28:
            self.message("Số ngày nghỉ có phép", "Số ngày nghỉ có phép không lớn hơn 28 ngày")

        elif self.entry["Số ngày nghỉ không phép"].get() == "":
            self.message("Số ngày nghỉ không phép", "Không được phép để trống")
        elif int(self.entry["Số ngày nghỉ không phép"].get()) > 28:
            self.message("Số ngày nghỉ không phép", "Số ngày nghỉ không phép không lớn hơn 28 ngày")

        elif self.entry["Số ngày làm thêm"].get() == "":
            self.message("Số ngày làm thêm", "Không được phép để trống")
        elif int(self.entry["Số ngày làm thêm"].get()) > 28:
            self.message("Số ngày làm thêm", "Số ngày làm thêm không lớn hơn 28 ngày")

        elif self.entry["Kết quả công việc"].get() == "":
            self.message("Kết quả công việc", "Không được phép để trống")
        elif self.entry["Kết quả công việc"].get() not in ['T', 'TB', 'K']:
            self.message("Kết quả công việc", "Kết quả làm việc tương ứng với:\n"
                                              "           T = tốt\n"
                                              "          TB = đạt\n"
                                              "           K = kém\n")
        else:
            real_salary = int(self.entry["Lương căn bản"].get()) + (
                int(self.entry["Lương căn bản"].get()) * 0.05 if int(self.entry["Số người con"].get()) > 2 else 0) + \
                          (int(self.entry["Lương căn bản"].get()) * 0.1 if self.entry[
                                                                               "Trình độ văn hóa"].get() == 'CH' else 0) + \
                          int(self.entry["Lương căn bản"].get()) * 0.04 * int(
                self.entry["Số ngày làm thêm"].get()) - int(self.entry["Lương căn bản"].get()) * 0.05 * int(
                self.entry["Số ngày làm thêm"].get())

            self.entry["Lương thực tế"].delete(0, END)
            self.entry["Lương thực tế"].insert(0, real_salary)

            if self.s == "SAVE":
                with open("DsNhanVien.csv", "a", encoding='UTF8', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(
                        [self.entry["ID"].get(), self.entry["Tên"].get(), self.entry["Tình trạng hôn nhân"].get(),
                         self.entry["Số người con"].get(), self.entry["Trình độ văn hóa"].get(),
                         self.entry["Lương căn bản"].get(), self.entry["Số ngày nghỉ có phép"].get(),
                         self.entry["Số ngày nghỉ không phép"].get(),
                         self.entry["Số ngày làm thêm"].get(), self.entry["Kết quả công việc"].get(), real_salary])
                self.heading.config(text="successful")
                self.submit['state'] = DISABLED

            elif self.s == 'MODIFY':
                f1 = open("DsNhanVien.csv", "r")
                with open("new.csv", "w", encoding='UTF8', newline='') as f:
                    writer = csv.writer(f)
                    for x in csv.reader(f1):
                        if int(x[0]) == int(self.ms.em_code):
                            writer.writerow(
                                [self.entry["ID"].get(), self.entry["Tên"].get(),
                                 self.entry["Tình trạng hôn nhân"].get(),
                                 self.entry["Số người con"].get(), self.entry["Trình độ văn hóa"].get(),
                                 self.entry["Lương căn bản"].get(), self.entry["Số ngày nghỉ có phép"].get(),
                                 self.entry["Số ngày nghỉ không phép"].get(),
                                 self.entry["Số ngày làm thêm"].get(), self.entry["Kết quả công việc"].get(),
                                 real_salary])
                            continue
                        writer.writerow(x)
                f1.close()
                f1 = open("new.csv", "r")
                with open("DsNhanVien.csv", "w", encoding='UTF8', newline='') as f:
                    writer = csv.writer(f)
                    for x in csv.reader(f1):
                        writer.writerow(x)
                f1.close()
                self.heading.config(text="successful")
                self.submit['state'] = DISABLED

    def display(self, emp):
        self.entry["ID"].insert(0, emp.em_code)

        self.entry["Tên"].insert(0, emp.name)

        self.entry["Tình trạng hôn nhân"].insert(0, emp.marital_status)

        self.entry["Số người con"].insert(0, emp.num_children)

        self.entry["Trình độ văn hóa"].insert(0, emp.edu_level)

        self.entry["Lương căn bản"].insert(0, emp.base_salary)

        self.entry["Số ngày nghỉ có phép"].insert(0, emp.personal_leave)

        self.entry["Số ngày nghỉ không phép"].insert(0, emp.non_accept_leave)

        self.entry["Số ngày làm thêm"].insert(0, emp.OT)

        self.entry["Kết quả công việc"].insert(0, emp.work_result)

        self.entry["Lương thực tế"].insert(0, emp.real_salary)
        if self.s == "DELETE":
            self.entry["ID"].config(state="disable")
            self.entry["Tên"].config(state="disable")
            self.entry["Tình trạng hôn nhân"].config(state="disable")
            self.entry["Số người con"].config(state="disable")
            self.entry["Trình độ văn hóa"].config(state="disable")
            self.entry["Lương căn bản"].config(state="disable")
            self.entry["Số ngày nghỉ có phép"].config(state="disable")
            self.entry["Số ngày nghỉ không phép"].config(state="disable")
            self.entry["Số ngày làm thêm"].config(state="disable")
            self.entry["Kết quả công việc"].config(state="disable")
            self.entry["Lương thực tế"].config(state="disable")

    def message(self, text1, text2):
        messagebox.showinfo(text1, text2)


def displayDele(emp, s):
    root = Tk()
    e = App(root, s, emp)
    e.screen()
    root.mainloop()


def display(s):
    root = Tk()
    e = App(root, s)
    e.screen()
    root.mainloop()
