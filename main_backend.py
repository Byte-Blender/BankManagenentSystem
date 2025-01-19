import csv
from tkinter import *
import pandas as pd
from tkinter import messagebox

filename = r".\database\customer.csv"
file2name = r".\database\employee_pword.csv"
filename3 = r".\database\customer_pword.csv"

#employee functions

def Cus_add_account(acc_name,age,gender,address,adhar_no,amount,password):
    df = pd.read_csv(filename)
    acc_no=191122+len(df)
    csvfile = open(filename, "a", newline='')
    csvfile2 = open(r".\database\customer_pword.csv","a", newline='')
    rows_2=[acc_name,password,acc_no]
    rows = [acc_no, acc_name, age, gender, address, adhar_no, amount]
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(rows)
    csvwriter2 = csv.writer(csvfile2)
    csvwriter2.writerow(rows_2)
    csvfile.close()
    csvfile2.close()

def cus_credit(acc_name,acc_no,amount_cr):
    df = pd.read_csv(filename)
    df.set_index("account no.", inplace=True)
    acc_number=int(acc_no)
    amount_credit=int(amount_cr)
    initial_bal = df.at[acc_number,'amount']
    new_bal = int(initial_bal)+amount_credit
    df.at[acc_number,'amount'] = new_bal
    df.to_csv(filename)
    messagebox.showinfo("","done")

def cus_debit(acc_name,acc_no,amount_db):
    df = pd.read_csv(filename)
    df.set_index("account no.", inplace=True)
    acc_number=int(acc_no)
    amount_credit=int(amount_db)
    initial_bal = df.at[acc_number,'amount']
    new_bal = int(initial_bal)-amount_credit
    df.at[acc_number,'amount'] = new_bal
    df.to_csv(filename)
    messagebox.showinfo("","done")

#customer options

def cus_transfer_money(amount,acco_no,pin,username):
#customer dataframe
    df = pd.read_csv(filename)
    df.set_index("account no.", inplace=True)

#customer password
    df2 = pd.read_csv(filename3)
    df2.set_index("username", inplace=True)
#getting variables
    act_passw=str(df2.at[username,'password'])
    from_acc=int(df2.at[username,'account no.'])

    if pin==act_passw:
        initial_bal_from = int(df.at[int(from_acc), 'amount'])

        initial_bal_to = int(df.at[int(acco_no), 'amount'])

        new_bal_from = int(initial_bal_from) - int(amount)

        new_bal_to = int(initial_bal_to) + int(amount)

        df.at[from_acc, 'amount'] = new_bal_from
        df.at[int(acco_no), 'amount'] = new_bal_to
        df.to_csv(filename)
        messagebox.showinfo("", "transfer successful")

    else:
        messagebox.showerror("","wrong password")

def cus_check_balance(win_name,pin,username):
    df = pd.read_csv(filename)
    df.set_index("account no.", inplace=True)

    df2 = pd.read_csv(filename3)
    df2.set_index("username", inplace=True)

    act_passw=str(df2.at[username,'password'])


    acc_no=int(df2.at[username,'account no.'])

    balance = df.at[acc_no,"amount"]
    if pin==act_passw:
        new_win=Tk()
        new_win.geometry("400x400")
        Label(new_win, text="your account balance is", bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=80, y=80)
        Label(new_win, text=balance, bg="#D1D0CE", font=("Comic Sans MS", 12)).place(x=80, y=150)
    else:
        messagebox.showerror("","incorrect password")

def cus_change_password(username,old_pa,new_pa):
    df2 = pd.read_csv(filename3)
    df2.set_index("username", inplace=True)
    print(df2)

    old_password = str(df2.at[username, 'password'])
    print(old_password)
    print(type(old_password))
    if old_pa==old_password:
        df2.at[username, 'password'] = new_pa
        print(df2)
        df2.to_csv(filename3)
        messagebox.showinfo("","password changed")

    else:
        messagebox.showerror("","unsuccessful , please check your password again")
