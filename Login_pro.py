import tkinter as tk
import os
import json
import sys

# Load accounts if file exists
if os.path.exists('account.json'):
    with open('account.json', 'r') as f:
        accounts = json.load(f)
else:
    accounts = {}

def create_account_window():
    def create_account():
        username = entry1.get()
        password = entry2.get()
        if username and password:
            accounts[username] = password
            with open('account.json', 'w') as f:
                json.dump(accounts, f)
            result_label.config(text='Account saved!')
        else:
            result_label.config(text='Please enter username and password')

    acc_win = tk.Toplevel(root)
    acc_win.title('Create Account')
    acc_win.geometry('300x200')

    tk.Label(acc_win, text='USERNAME:').grid(row=0, column=0, pady=5)
    entry1 = tk.Entry(acc_win)
    entry1.grid(row=0, column=1, pady=5)

    tk.Label(acc_win, text='PASSWORD:').grid(row=1, column=0, pady=5)
    entry2 = tk.Entry(acc_win, show='*')
    entry2.grid(row=1, column=1, pady=5)

    tk.Button(acc_win, text='Create', command=create_account).grid(row=2, column=0, columnspan=2, pady=10)

    result_label = tk.Label(acc_win, text='')
    result_label.grid(row=3, column=0, columnspan=2)

def login():
    username = entry3.get()
    password = entry4.get()

    if username in accounts:
        if accounts[username] == password:
            result_label.config(text='Login successful!')
        else:
            result_label.config(text='Incorrect password')
    else:
        result_label.config(text='Username not found')

# Main window
root = tk.Tk()
root.title('LOGIN')
root.geometry('400x250')

tk.Label(root, text='USERNAME:').grid(row=0, column=0, pady=5)
entry3 = tk.Entry(root)
entry3.grid(row=0, column=1, pady=5)

tk.Label(root, text='PASSWORD:').grid(row=1, column=0, pady=5)
entry4 = tk.Entry(root, show='*')
entry4.grid(row=1, column=1, pady=5)

tk.Button(root, text='Login', command=login).grid(row=2, column=0, columnspan=2, pady=10)

tk.Label(root, text='No account? Create one below:').grid(row=3, column=0, columnspan=2)

tk.Button(root, text='Create Account', command=create_account_window).grid(row=4, column=0, columnspan=2, pady=5)

result_label = tk.Label(root, text='')
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()