import tkinter as tk

def login():
    try:
        passcode = 1122
        user='minato'
        name = entry.get()
        pin = int(entry1.get())
        if user==name and passcode==pin:
            result_label.config(text=f'You have successfully login!,{name} welcome')
    except ValueError:
        result_label.config(text='Please enter a valid username and passcode')


root=tk.Tk()
root.title('Minato')
root.geometry('500x500')

tk.Label(root, text='Enter username', font=('Arial',18)).pack()
entry =tk.Entry(root)
entry.pack(padx=10,pady=10)

tk.Label(root, text='Enter your passcode', font=('Arial',18)).pack()
entry1 = tk.Entry(root)
entry1.pack(padx=10,pady=10)
tk.Button(root, text='login', font=('Arial',16), command=login).pack()

result_label = tk.Label(root, text='')
result_label.pack()

root.mainloop()


