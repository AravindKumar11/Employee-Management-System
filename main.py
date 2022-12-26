from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from data_base import Database

data_base = Database("Employees.db")
root = Tk()
root.title("Employee Management System")
root.geometry("1350x700+0+0")
root.config(bg="grey")

name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()

entries_frame = Frame(root, bg="grey")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Employee Management System", font=("TimesNewRoman",20,"bold", "italic"),bg="white",fg="red")
title.grid(row=0, columnspan=20, padx=450, pady=20, sticky="W")

lblName = Label(entries_frame, text="Name", font=("TimesNewRoman", 16), bg="grey",fg="black")
lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("TimesNewRoman", 16), width=20, bg="white",fg="black")
txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblAge = Label(entries_frame, text="Age", font=("TimesNewRoman", 16), bg="grey",fg="black")
lblAge.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtAge = Entry(entries_frame, textvariable=age, font=("TimesNewRoman", 16), width=20, bg="white",fg="black")
txtAge.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lbldoj = Label(entries_frame, text="D.O.J", font=("TimesNewRoman", 16), bg="grey",fg="black")
lbldoj.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtDoj = Entry(entries_frame, textvariable=doj, font=("TimesNewRoman", 16), width=20, bg="white",fg="black")
txtDoj.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblEmail = Label(entries_frame, text="Email", font=("TimesNewRoman", 16), bg="grey",fg="black")
lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtEmail = Entry(entries_frame, textvariable=email, font=("TimesNewRoman", 16), width=20, bg="white",fg="black")
txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblGender = Label(entries_frame, text="Gender", font=("TimesNewRoman", 16), bg="grey",fg="black")
lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
comboGender = ttk.Combobox(entries_frame, textvariable=gender, font=("TimesNewRoman", 16), width=19, state="readonly")
comboGender['values'] = ("Male", "Female")
comboGender.grid(row=3, column=1, padx=10, sticky="w")

lblContact = Label(entries_frame, text="Contact No", font=("TimesNewRoman", 16), bg="grey",fg="black")
lblContact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtContact = Entry(entries_frame, textvariable=contact, font=("TimesNewRoman", 16), width=20, bg="white",fg="black")
txtContact.grid(row=3, column=3, padx=10, sticky="w")

lblAddress = Label(entries_frame, text="Address", font=("TimesNewRoman", 16), bg="grey",fg="black")
lblAddress.grid(row=4, column=0, padx=10, pady=10, sticky="w")

txtAddress = Text(entries_frame, width=55, height=4, font=("TimesNewRoman", 16), bg="white",fg="black")
txtAddress.grid(row=5, column=0, columnspan=4, padx=10, sticky="w")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[7])

def displayAll():
    tv.delete(*tv.get_children())
    for row in data_base.fetch():
        tv.insert("", END, values=row)

def add_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Details missing","Please fill all the details")
        return
    data_base.insert(txtName.get(),txtAge.get(), txtDoj.get(), txtEmail.get(), comboGender.get(), txtContact.get(), txtAddress.get(1.0, END))
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    displayAll()

def update_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Details missing","Please fill all the details")
        return
    data_base.update(row[0],txtName.get(), txtAge.get(), txtDoj.get(), txtEmail.get(), comboGender.get(), txtContact.get(),txtAddress.get(1.0, END))
    messagebox.showinfo("Success", "Record Updated")
    clearAll()
    displayAll()

def delete_employee():
    data_base.delete(row[0])
    clearAll()
    displayAll()

def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0, END)


# Inserting Buttons

btn_frame = Frame(entries_frame, bg="grey")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_employee, text="Add", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="brown", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_employee, text="Update", width=15, font=("Calibri", 16, "bold"),
                fg="white", bg="green",bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_employee, text="Delete", width=15, font=("Calibri", 16, "bold"),
                fg="white", bg="red",bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear All", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="orange",bd=0).grid(row=0, column=3, padx=10)

# Creating Table to view details

tree_frame = Frame(root, bg="red")
tree_frame.place(x=10, y=440, width=1345, height=255)
style = ttk.Style()
style.configure("my_style.Treeview", font=('TimesNewRoman', 14),rowheight=50)
style.configure("my_style.Treeview.Heading", font=('TimesNewRoman', 14))
tv = ttk.Treeview(tree_frame, columns=("1", "2", "3", "4", "5", "6", "7", "8"), style="my_style.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=20)
tv.heading("2", text="Name")
tv.column("2", width=120)
tv.heading("3", text="Age")
tv.column("3", width=30)
tv.heading("4", text="D.O.J")
tv.column("4", width=40)
tv.heading("5", text="Email")
tv.heading("6", text="Gender")
tv.column("6", width=30)
tv.heading("7", text="Contact")
tv.column("7", width=70)
tv.heading("8", text="Address")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

displayAll()
root.mainloop()