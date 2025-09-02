import  tkinter as tk
import random

def guess():
    try:
        number=random.randint(1,100)
        num1 = int(entry.get())
        if num1==number:
            result_label.config(text='You guess corrent!, you own')
        elif num1<number:
            result_label.config(text='Too low')
        elif num1>number:
            result_label.config(text='Too high')
    except ValueError:
        result_label.config(text='Please enter a valid number')

root =tk.Tk()
root.title('GUESS THE NUMBER')
root.geometry('400x200')

tk.Label(root, text='Enter a number between 1-100').pack(padx=10,pady=10)
entry = tk.Entry(root)
entry.pack(padx=10,pady=10)

tk.Button(root, text='GO', command=guess).pack(padx=10,pady=10)

result_label = tk.Label(root, text='')
result_label.pack(padx=10,pady=10)

root.mainloop()
