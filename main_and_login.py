import csv
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import tkinter as tk
from csv import DictWriter
from csv import DictReader
from os import path
import password_genrator_keeper
import ctypes, sys

def encyp_decryp(text,mode):
    key="abcdefghijklmnopqrstuvwxyzASDFGHJKLPOIUYTREWQZXCVBNM1234567890_+-/.!?@#$%^&*=,`~"
    value = "?/_,.!@#$%^&*-=+`~0987321456qpwoeirutyalskdjfhgzmxncbvASDFGHJKLPOIUYTREWQZXCVBNM"
    encryption = dict(zip(key,value))
    decryption = dict(zip(value,key))
    crypto_msg=''
    if mode == "Encryption":
        for i in text:
            crypto_msg=crypto_msg+encryption[i]
    elif mode == "Decryption":
        for i in text:
            crypto_msg=crypto_msg+decryption[i]
    else:
        print("Chosse Write Option...!!!")           
    return crypto_msg 

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    if path.exists("C:\\Windows\\login.csv"):
        root = tk.Tk()
        root.title("log In")
        root.geometry("250x200")

        username_label = ttk.Label(root, text='Username : ')
        username_label.grid(row=1, column=0, sticky=tk.W)

        password_label = ttk.Label(root, text='Password : ')
        password_label.grid(row=2, column=0, sticky=tk.W)

        user_name_var = tk.StringVar()
        user_name_box = ttk.Entry(root, width=16, textvariable=user_name_var)
        user_name_box.grid(row=1, column=1, pady=5)

        password_var = tk.StringVar()
        password_box = ttk.Entry(root, width=16, textvariable=password_var,show='*')
        password_box.grid(row=2, column=1, pady=5)

        def login():
            username = user_name_var.get()
            password = password_var.get()
            with open('C:\\Windows\\login.csv','r') as f:
                csv_reader=DictReader(f)
                for i in csv_reader:
                    if i['username'] == encyp_decryp(username,"Encryption") and i['password'] == encyp_decryp(password,"Encryption") :
                        root.destroy() 
                        password_genrator_keeper.keeper_password()               
                    else:
                        messagebox.showerror("","Acess Denied")       
        search_button = ttk.Button(root, text='Login', command=login)
        search_button.grid(row=3, column=1)
        root.mainloop()
    else:
        win = tk.Tk()
        win.title("Set Your Login Details")
        win.geometry("250x200")

        username_label = ttk.Label(win, text='Username : ')
        username_label.grid(row=1, column=0, sticky=tk.W)

        password_label = ttk.Label(win, text='Password : ')
        password_label.grid(row=2, column=0, sticky=tk.W)

        user_name_var = tk.StringVar()
        user_name_box = ttk.Entry(win, width=16, textvariable=user_name_var)
        user_name_box.grid(row=1, column=1, pady=5)

        password_var = tk.StringVar()
        password_box = ttk.Entry(win, width=16, textvariable=password_var)
        password_box.grid(row=2, column=1, pady=5)   

        def add():
            username = encyp_decryp(user_name_var.get(),"Encryption")
            password = encyp_decryp(password_var.get(),"Encryption")
            with open('C:\\Windows\\login.csv','a') as f:
                dict_writer=DictWriter(f,fieldnames=['username','password'])
                dict_writer.writeheader()
                dict_writer.writerow({
                    'username':username,
                    'password':password            
                }) 
                win.destroy()

        search_button = ttk.Button(win, text='add', command=add)
        search_button.grid(row=3, column=1)
        
        win.mainloop()    
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)        