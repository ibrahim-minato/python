import tkinter as tk


def hello():
    result_label.config(text='hello am naruto')


root = tk.Tk()
root.title('minato')
root.geometry('400x400')

tk.Button(root,text='now',command=hello).pack()

result_label = tk.Label(root,text='')
result_label.pack()

root.mainloop()
