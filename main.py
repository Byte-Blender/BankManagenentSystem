from tkinter import *
import csv
from tkinter import ttk
from tkinter import messagebox
import main_backend
import pandas as pd
import datetime

filename = r".\database\customer.csv"

strTime = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

df= pd.read_csv(filename)
df.set_index("account no.",inplace=True)
#login functions


def employee_log():
    global emp_var
    global emp_var2
    C1 = Canvas(root, bg="#D1D0CE", height=300, width=600)
    C1.place(relx=.5, rely=.5, anchor=CENTER)
    Label(C1, text="UserName",bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=300, y=75)
    emp_var=StringVar()
    emp_username = Entry(C1,textvariable=emp_var).place(x=400,y=80)
    Label(C1, text="Password", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=300, y=145)
    emp_var2=StringVar()
    emp_password = Entry(C1,textvariable = emp_var2,show="X").place(x=400, y=150)
    emp_login_lable = Label(C1, text="Please Login", bg="#D1D0CE", fg='black', font=("Comic Sans MS", 12)).place(x=1, y=1)
    Button(C1, text="Login", command=Ok, height=3, width=13).place(x=370, y=200)

def Ok():
    global uname
    uname=emp_var.get()
    password=emp_var2.get()
    x = 0
    if (uname == "" and password == ""):
        messagebox.showinfo("", "Blank Not allowed")
    elif x==0:
        with open(r'.\database\employee_pword.csv','r') as csv_file:
            csv_reader= csv.reader(csv_file)
            for row in csv_reader:
                if x==0:
                    for field in row:
                        if field==uname and row[1]==password and x==0:
                            messagebox.showinfo("", "Login Success")
                            write_file=[uname,",logged in on : ",strTime,"\n"]
                            with open(r'.\database\transaction.txt', 'a') as trans_file:
                                wr=trans_file.writelines(write_file)
                                trans_file.close()
                            emwin()
                            x=1
                            break
            if x==0:
                messagebox.showinfo("", "Incorrent Username and Password")

def cus_log():
    global cus_var
    global cus_var2
    C2 = Canvas(root, bg="#D1D0CE", height=300, width=600)
    C2.place(relx=.5, rely=.5, anchor=CENTER)
    Label(C2, text="UserName",bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=300, y=75)
    cus_var=StringVar()
    cus_username = Entry(C2,textvariable=cus_var).place(x=400,y=80)
    Label(C2, text="Password", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=300, y=145)
    cus_var2=StringVar()
    cus_password = Entry(C2,textvariable=cus_var2,show="X").place(x=400, y=150)
    Button(C2, text="Login", command=Ok2, height=3, width=13).place(x=370, y=200)
    cus_log_lable = Label(C2, text="Please Login", bg="#D1D0CE", fg='black', font=("Comic Sans MS", 12)).place(x=1, y=1)

def Ok2():
    global uname2
    uname2 = cus_var.get()
    password2 = cus_var2.get()
    x = 0
    if (uname2 == "" and password2 == ""):
        messagebox.showinfo("", "Blank Not allowed")
    elif x == 0:
        with open('.\database\customer_pword.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if x == 0:
                    for field in row:
                        if field == uname2 and row[1] == password2 and x == 0:
                            messagebox.showinfo("", "Login Success")
                            cuwin()
                            x = 1
                            break
            if x==0:
                messagebox.showinfo("", "Incorrent Username and Password")

#user window

def emwin():
    try:
        root.destroy()
    except Exception as e:
        pass
    emw=Tk()
    emw.title("employee window")
    emw.configure(bg='#151B54')
    emw.geometry('800x600')
    Button(emw, text="main menu", command=lambda: [emwin(),emw.destroy()],bg = "yellow", fg = "black",activebackground='#FFD700').place(x=10, y=10)
    emc = Canvas(emw, bg="#D1D0CE", height=300, width=600)
    emc.place(relx=.5, rely=.5, anchor=CENTER)
    def Add_account():
        def Back_add_acc():
            try:
                password = e16_var.get()
                acc_name = e11_var.get()
                age = e12_var.get()
                gender = e13_var.get()
                address = e14_var.get()
                adhar_no = e15_var.get()
                amount = e17_var.get()
                if (acc_name=='' or age=='' or gender=='' or address=="" or adhar_no=='' or amount==''):
                    messagebox.showinfo("", "blank not allowed")
                else:
                    main_backend.Cus_add_account(acc_name,age,gender,address,adhar_no,amount,password)
                    write2_file=[uname," ,added a new account on ",strTime," with account name ",acc_name,"\n"]
                    with open(r'.\database\transaction.txt', 'a') as trans_file:
                        wr = trans_file.writelines(write2_file)
                        trans_file.close()
                    messagebox.showinfo("", "account created")
            except Exception as e:
                messagebox.showerror("error", "some unknown error has occured")
                print(e)
        emc1 = Canvas(emc, bg="#D1D0CE", height=300, width=600)
        emc1.place(relx=.5, rely=.5, anchor=CENTER)
        Label(emc1, text="Please enter all the details", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=10, y=5)
        e11_var=StringVar()
        e11 = Entry(emc1,textvariable=e11_var).place(x=400, y=40)
        Label(emc1, text=" Account Name", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=250, y=37)
        Label(emc1, text="Age", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=300, y=62)
        e12_var=StringVar()
        e12 = Entry(emc1,textvariable=e12_var).place(x=400, y=65)
        Label(emc1, text="Gender", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=300, y=87)
        e13_var = StringVar()
        e13 = Entry(emc1,textvariable=e13_var).place(x=400, y=90)
        Label(emc1, text="Address", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=300, y=112)
        e14_var = StringVar()
        e14 = Entry(emc1,textvariable=e14_var).place(x=400, y=115)
        Label(emc1, text="Adhar card", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=300, y=137)
        e15_var=StringVar()
        e15 = Entry(emc1,textvariable=e15_var).place(x=400, y=140)
        Label(emc1, text="Set password", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=300, y=162)
        e16_var=StringVar()
        e16 = Entry(emc1,textvariable=e16_var).place(x=400, y=165)
        e17_var = StringVar()

        e17 = Entry(emc1, textvariable=e17_var).place(x=400, y=190)
        Label(emc1, text="opening ammount",bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=250, y=187)

        Label(emc1, text="in Rs",bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=530, y=187)
        Button(emc1, text="Confirm", command=Back_add_acc, height=3, width=13).place(x=400, y=240)

    def Credit_debit():
        def credit():
            def credited():
                try:
                    acc_name=e21_var.get()
                    acc_no=e22_var.get()
                    amount_cr=e24_var.get()
                    print(acc_no,acc_name,amount_cr)
                    main_backend.cus_credit(acc_name,acc_no,amount_cr)
                    write2_file=["employee : ",uname," ,credited ",amount_cr," to account number ",acc_no," on",strTime,"\n"]

                    with open(r'.\database\transaction.txt', 'a') as trans_file:

                        wr = trans_file.writelines(write2_file)
                        trans_file.close()
                    emwin()


                except Exception as e:
                    print(e)
                    messagebox.showerror("","unable to process your request")

            emc201 = Canvas(emc, bg="#D1D0CE", height=300, width=600)
            emc201.place(relx=.5, rely=.5, anchor=CENTER)

            Label(emc201, text="Please enter account details", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=10, y=5)
            Label(emc201, text="Account name", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=230, y=65)
            e21_var=StringVar()
            e21 = Entry(emc201,textvariable=e21_var).place(x=400, y=70)
            Label(emc201, text="enter account number", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=230, y=110)
            e22_var=StringVar()
            e22 = Entry(emc201,textvariable=e22_var).place(x=400, y=115)

            Label(emc201, text="enter amount to credit", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=230, y=200)
            e24_var=StringVar()
            e24 = Entry(emc201,textvariable=e24_var).place(x=400, y=205)
            Button(emc201, text="Confirm", command=credited, height=3, width=13).place(x=370, y=240)

        def debit():
            def debited():
                try:
                    acc_name=e25_var.get()
                    acc_no=e26_var.get()
                    amount_db=e28_var.get()
                    print(acc_no,acc_name,amount_db)
                    main_backend.cus_debit(acc_name,acc_no,amount_db)
                    write2_file = ["employee : ", uname, " ,debited ", amount_db, " from account number ", acc_no, " on ", strTime, "\n"]

                    with open(r'.\database\transaction.txt', 'a') as trans_file:

                        wr = trans_file.writelines(write2_file)
                        trans_file.close()
                    emwin()

                except Exception as e:
                    print(e)
                    messagebox.showerror("","unable to process your request")

            emc202 = Canvas(emc, bg="#D1D0CE", height=300, width=600)
            emc202.place(relx=.5, rely=.5, anchor=CENTER)

            Label(emc202, text="Please enter account details", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=10, y=5)
            Label(emc202, text="Account name", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=230, y=65)
            e25_var=StringVar()
            e25 = Entry(emc202,textvariable=e25_var).place(x=400, y=70)
            Label(emc202, text="enter account number", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=230, y=110)

            e26_var=StringVar()
            e26 = Entry(emc202,textvariable=e26_var).place(x=400, y=115)

            Label(emc202, text="enter amount to debit", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=230, y=200)
            e28_var=StringVar()

            e28 = Entry(emc202,textvariable=e28_var).place(x=400, y=205)
            Button(emc202, text="Confirm", command=debited, height=3, width=13).place(x=370, y=240)

        emc2 = Canvas(emc, bg="#D1D0CE", height=300, width=600)
        emc2.place(relx=.5, rely=.5, anchor=CENTER)
        Label(emc2, text="Please select your option", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=10, y=10)


        Button(emc2, text="Debit", command=debit, bg="yellow", fg="black", activebackground='#FFD700').place(
            x=100, y=200)
        Button(emc2, text="Credit", command=credit, bg="yellow", fg="black", activebackground='#FFD700').place(
            x=250, y=200)




    def cus_details():
        emc3=Canvas(emcl, bg="#D1D0CE", height=1000, width=2000).place(relx=.5, rely=.5, anchor=CENTER)

        search_var=StringVar()

        def confirmed():
            try:
                search=search_var.get()
                search_info= df.loc[int(search)]
                Label(emc3, text=search_info, bg="yellow", font=("Comic Sans MS", 20)).place(x=100,y=250)
                messagebox.showinfo("", "account found")


            except Exception as e:
                messagebox.showerror("", "account not found")


        Label(emc3, text="Enter Account number to search", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=10, y=5)
        search_entry = Entry(emc3,textvariable= search_var).place(x=250,y=37)


        Button(emc3, text="Confirm", command=confirmed, height=3, width=13).place(x=400, y=140)


    def all_transaction():
        all_trans = Tk()
        all_trans.geometry("600x400")
        Label(all_trans, text="TRANSACTION AND ACTIVITY", bg="yellow", font=("Comic Sans MS", 20)).place(x=10, y=10)

        with open(r'.\database\transaction.txt','r') as trans_file:
            t=trans_file.readlines()

        scrollbar = Scrollbar(all_trans)
        scrollbar.pack(side=RIGHT,fill=Y)

        listbox = Listbox(all_trans,yscrollcommand=scrollbar.set,font=100,width=100)
        for i in t:
            listbox.insert(END,i)

        listbox.place(relx=.5,rely=.5,anchor=CENTER)
        scrollbar.config(command=listbox.yview)




    emcl = Label(emc, text="EMPLOYEE ACCOUNT", bg='#D1D0CE', fg='black', font=("bold", 20)).place(x=170, y=0)
    Button(emc, text="ADD ACCOUNT", command=Add_account,bg = "yellow", fg = "black",activebackground='#FFD700').place(x=100, y=100)
    Button(emc, text="CUSTOMER DETAILS", command=cus_details,bg = "yellow", fg = "black",activebackground='#FFD700').place(x=100, y=200)
    Button(emc, text="DEBIT/CREDIT", command=Credit_debit,bg = "yellow", fg = "black",activebackground='#FFD700').place(x=400, y=100)
    Button(emc, text="TRANSACTIONS and ACTIVITY", command=all_transaction,bg = "yellow", fg = "black",activebackground='#FFD700').place(x=400, y=200)


def cuwin():
    try:
        root.destroy()
    except Exception as e:
        pass

    cuw=Tk()
    cuw.title("Customer window")
    cuw.configure(bg='#151B54')
    cuw.geometry('800x600')
    Button(cuw, text="main menu", command=lambda: [cuwin(),cuw.destroy()],bg = "yellow", fg = "black",activebackground='#FFD700').place(x=10, y=10)

    cuc = Canvas(cuw, bg="#D1D0CE", height=300, width=600)

    def Transfer_money():
        def Confirmed():
            try:
                amount_var=e3_var.get()
                acc_no_var=e4_var.get()
                pin_var=e6_var.get()

                main_backend.cus_transfer_money(amount_var,acc_no_var,pin_var,uname2)

            except Exception as e:
                messagebox.showerror("","error , please check your details")


        cut = Canvas(cuw, bg="#D1D0CE", height=300, width=600)
        cut.place(relx=.5, rely=.5, anchor=CENTER)
        Label(cut, text="Please enter all the details", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=10, y=10)

        Label(cut, text="enter amount", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=230, y=65)
        e3_var=StringVar()
        e3 = Entry(cut,textvariable=e3_var).place(x=400, y=70)
        Label(cut, text="enter account number", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=230, y=110)
        e4_var = StringVar()
        e4 = Entry(cut,textvariable=e4_var).place(x=400, y=115)

        Label(cut, text="enter your pin", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=230, y=200)
        e6_var = StringVar()
        e6 = Entry(cut,textvariable=e6_var).place(x=400, y=205)
        Button(cut, text="Confirm", command=Confirmed, height=3, width=13).place(x=370, y=240)

    def check_balance():
        def check_balance_confirm():
            pin=e7_var.get()

            main_backend.cus_check_balance(cub,pin,uname2)
        cub = Canvas(cuw, bg="#D1D0CE", height=300, width=600)
        cub.place(relx=.5, rely=.5, anchor=CENTER)
        Label(cub, text="CHECKING BALANCE", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=10, y=10)
        Label(cub, text="enter your pin", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=80, y=80)
        e7_var=StringVar()
        e7 = Entry(cub,textvariable=e7_var).place(x=200, y=85)
        Button(cub, text="Confirm", command=check_balance_confirm, height=3, width=13).place(x=130, y=150)

    def Change_pin():
        def confirmed():
            old_P=str(e8_var.get())
            new_p=str(e10_var.get())
            main_backend.cus_change_password(uname2,old_P,new_p)
        cucp = Canvas(cuw, bg="#D1D0CE", height=300, width=600)
        cucp.place(relx=.5, rely=.5, anchor=CENTER)
        Label(cucp, text="CHANGE PIN", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=10, y=10)
        Label(cucp, text="enter your old pin", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=80, y=80)
        e8_var=StringVar()
        e8 = Entry(cucp,textvariable=e8_var).place(x=220, y=85)
        Label(cucp, text="enter new pin", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=80, y=180)
        e10_var = StringVar()
        e10 = Entry(cucp,textvariable=e10_var).place(x=220, y=185)
        Button(cucp, text="Confirm", command=confirmed, height=3, width=13).place(x=150, y=220)


    cuc.place(relx=.5, rely=.5, anchor=CENTER)
    cucl = Label(cuc, text="CUSTOMER ACCOUNT", bg='#D1D0CE', fg='black', font=("bold", 20)).place(x=170, y=0)
    Button(cuc, text="TRANSFER MONEY", command=Transfer_money,bg = "yellow", fg = "black",activebackground='#FFD700').place(x=100, y=100)
    Button(cuc, text="CHECK BALANCE", command=check_balance,bg = "yellow", fg = "black",activebackground='#FFD700').place(x=250, y=200)
    Button(cuc, text="CHANGE PIN", command=Change_pin,bg = "yellow", fg = "black",activebackground='#FFD700').place(x=400, y=100)


#_main_

root =Tk()
root.geometry('800x600')
root.title("welcome to iBank")
root.configure(bg='#151B54')

C = Canvas(root, bg="yellow",height=300, width=600)

C.place(relx=.5,rely=.5,anchor=CENTER)
cl= Label(C, text = "I BANK",bg='yellow',fg='black',font = ("bold",30)).place(x=220,y=0)

l = Label(C, text = "Please select your option",bg='yellow',fg='black',font = ("Comic Sans MS",12)).place(x=90,y=60)

b = Button(C, text = "Employee", bg = "yellow", fg = "black",activebackground='#FFD700',command = employee_log, font = ("Comic Sans MS",8))
b.place(x=90,y=200)

b1 = Button(C, text = "Customer", bg = "yellow", fg = "black",activebackground='#FFD700',command = cus_log, font = ("Comic Sans MS",8))
b1.place(x=400,y=200)


root.mainloop()
