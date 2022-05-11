import csv
from tkinter import messagebox
from tkinter import *
import random
from tkinter import ttk
import tkinter as tk
from csv import DictWriter
import os
from csv import DictReader
import ctypes, sys

def keeper_password():
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    if is_admin():
        win = tk.Tk()
        win.title("Password Genrator (By Ranjan)")
        win.geometry("350x400")

        site_name_label = ttk.Label(win, text='Site Name : ')
        site_name_label.grid(row=0, column=0, sticky=tk.W)

        site_var = tk.StringVar()
        site_name_box = ttk.Entry(win, width=16, textvariable=site_var)
        site_name_box.grid(row=0, column=1, pady=5)
        site_name_box.focus()


        user_name_label = ttk.Label(win, text='User Name : ')
        user_name_label.grid(row=1, column=0, sticky=tk.W)

        user_name_var = tk.StringVar()
        user_name_box = ttk.Entry(win, width=16, textvariable=user_name_var)
        user_name_box.grid(row=1, column=1, pady=5)

        password_label = ttk.Label(win, text='Pswrd Length : ')
        password_label.grid(row=2, column=0, sticky=tk.W)

        password_length_var = tk.IntVar()
        password_length_box = ttk.Entry(win, width=16, textvariable=password_length_var)
        password_length_box.grid(row=2, column=1, pady=5)

        password_label = ttk.Label(win, text='Password \n (Use this \n when you write password \n manually) : ')
        password_label.grid(row=3, column=0, sticky=tk.W)

        password_var = tk.StringVar()
        password_name_box = ttk.Entry(win, width=16, textvariable=password_var)
        password_name_box.grid(row=3, column=1, pady=5)

        mode_label = ttk.Label(win, text='Select Mode : ')
        mode_label.grid(row=4, column=0, sticky=tk.W)

        mode_var = tk.StringVar()  
        mode=ttk.Combobox(win,width=8, textvariable=mode_var, state='readonly')   
        mode['values']=('Encryption','Decryption')                                   
        mode.grid(row=4,column=1)
        mode.current(0)

        label = ttk.Label(win, text='')
        label.grid(row=4, column=0)#, sticky=tk.W)

        label = ttk.Label(win, text='')
        label.grid(row=5, column=0, sticky=tk.W)

        label = ttk.Label(win, text='')
        label.grid(row=6, column=0, sticky=tk.W)

        def password_generator():
            al="asdfghjklpoiuytrewqzxcvbnmASDFGHJKLPOIUYTREWQZXCVBNM!@#$%^&*1234567890"
            password=""
            nu=password_length_var.get()
            if nu <= 9:
                messagebox.showerror("","Password Length is must be 10 Or above 10")
                return 0
            else:    
                for i in range(0,nu):
                    password=password+random.choice(al)
            return password   

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

        def generate_pass():
            if mode_var.get() == "Encryption":
                password = encyp_decryp(password_generator(),mode_var.get())
                sitename = site_var.get()
                if user_name_var.get() != "":
                    if len(user_name_var.get()) >3:
                        username = encyp_decryp(user_name_var.get(),mode_var.get())
                        with open(r'C:\\Windows\\SysWOW64\\information.csv', 'a') as f:
                            dict_writer=DictWriter(f,fieldnames=['Site','Username','Password'])
                            if os.stat(r'C:\\Windows\\SysWOW64\\information.csv').st_size==0:
                                dict_writer.writeheader()
                            dict_writer.writerow({
                                'Site':sitename,
                                'Username':username,
                                'Password':password            
                            })
                            site_name_box.delete(0, tk.END)    
                            password_name_box.delete(0, tk.END)
                            password_length_box.delete(0,tk.END)
                            user_name_box.delete(0,tk.END)
                            site_name_box.focus()
                            messagebox.showwarning("","Support Ranjan :-)")  
                    else :
                        messagebox.showerror("error","Username is too small")
                else:
                    messagebox.showerror("","....Put The Username....")     
            else :
                messagebox.showerror("","You Are Saving Password So Select '....Encryption....'") 
                

        def get_info():
            if mode_var.get() == "Decryption":
                count=0
                data=csv.reader(open(r'C:\\Windows\\SysWOW64\\information.csv','r'))
                site=site_var.get()
                for i in data:
                    if site in i:
                        count +=1
                        username=i[1]
                        password=i[2]        
                if count > 0:
                    messagebox.showwarning("sucess",f"{encyp_decryp(username,mode_var.get())}    {encyp_decryp(password,mode_var.get())}")
                else:
                    messagebox.showerror("sucess","!!...Not found...!!!")
            else:
                messagebox.showerror("","You Are Searching For Data So Select '....Decryption....'")   

        def Encryption_And_Save():
            if mode_var.get() == "Encryption":
                if password_var.get() != "" :
                    password = encyp_decryp(password_var.get(),mode_var.get())
                    sitename=site_var.get()
                    if user_name_var.get() != "":
                        if len(user_name_var.get()) >3:
                            username=encyp_decryp(user_name_var.get(),mode_var.get())
                            with open(r'C:\\Windows\\SysWOW64\\information.csv', 'a') as f:
                                dict_writer=DictWriter(f,fieldnames=['Site','Username','Password'])
                                if os.stat(r'C:\\Windows\\SysWOW64\\information.csv').st_size==0:
                                    dict_writer.writeheader()
                                dict_writer.writerow({
                                    'Site':sitename,
                                    'Username':username,
                                    'Password':password            
                                })
                                site_name_box.delete(0, tk.END)    
                                password_name_box.delete(0, tk.END)
                                password_length_box.delete(0,tk.END)
                                user_name_box.delete(0,tk.END)
                                site_name_box.focus()
                                messagebox.showwarning("","Support Ranjan :-)")  
                        else :
                            messagebox.showerror("error","Username is too small")        
    
                    else:
                        messagebox.showerror("Error","....Put The Username....")
                else:
                    messagebox.showerror("Error","Your Password Box Is Empty")             
            else :
                messagebox.showerror("Error","You Are Saving Password So Select '....Encryption....'")   
                            

        genrate_button=ttk.Button(win,text='Genrate Password',command=generate_pass) 
        genrate_button.grid(row=7,column=1) 


        label = ttk.Label(win, text='')
        label.grid(row=8, column=0, sticky=tk.W)

        site_name_label = ttk.Label(win, text='Use it when you write your \n password manually : ')
        site_name_label.grid(row=9, column=0, sticky=tk.W)

        Encryption_And_Save_button=ttk.Button(win,text='Encryption And Save',command=Encryption_And_Save) 
        Encryption_And_Save_button.grid(row=9,column=1) 

        label = ttk.Label(win, text='')
        label.grid(row=10, column=1, sticky=tk.W)

        search_button=ttk.Button(win,text='Search',command=get_info) 
        search_button.grid(row=11,column=1)         

        win.mainloop()
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)    