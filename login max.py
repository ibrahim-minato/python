import tkinter as tk
import os
import json
import sys



def account():
     if os.path.exists('account.json'):
         with open('account.json','r') as f:
                json.load(f)
     else:
         account = {}

     def create_account():
         username = entry1.get()
         password = entry2.get()
         account[username] =password

         with open('account.json','w') as f:
             json.dump(account,f)
             result_label.config(text='Account saved!')

     root=tk.Tk()
     root.title('Create Account')
     root.geometry('500x500')

     tk.Label(root, text='USERNAME:').grid(row=0,column=0,pady=5)
     entry1 =tk.Entry(root)
     entry1.grid(row=0,column=1,pady=5)

     tk.Label(root, text='PASSWORD:').grid(row=1, column=0, pady=5)
     entry2 = tk.Entry(root)
     entry2.grid(row=1, column=1, pady=5)

     tk.Button(root, text='Create', command=create_account).grid()

     result_label = tk.Label(root, text='')
     result_label.grid()



def login():
    try:
        username = entry3.get()
        password = entry4.get()
        if username and password == account[username]:
            result_label.config(text='You have successfuly login')
        else:
            result_label.config(text='in valid password')
    except KeyError:
        result_label.config(text='Username not found')

        create = entry5.get()
        if create =='yes':
            result_label.config(text='')
        else:
            sys.exit()

root=tk.Tk()
root.title(' LOGIN')
root.geometry('500x500')

tk.Label(root, text='USERNAME:').grid(row=0,column=0,pady=5)
entry3 =tk.Entry(root)
entry3.grid(row=0,column=1,pady=5)

tk.Label(root, text='PASSWORD:').grid(row=1, column=0, pady=5)
entry4 = tk.Entry(root)
entry4.grid(row=1, column=1, pady=5)

tk.Button(root, text='login', command=login).grid()

tk.Label(root, text='Create a new account').grid()
entry5 = tk.Entry(root)
entry5.grid()

tk.Button(root, text='create', command=account).grid()

result_label = tk.Label(root, text='')
result_label.grid()

root.mainloop()

