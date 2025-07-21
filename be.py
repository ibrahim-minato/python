import  tkinter as tk

def press(n):
    entry.insert(tk.END, str(n))

def clear():
    entry.delete(0, tk.END)
    result_label.config(text='')

window = tk.Tk()
window.title('experiment')
window.geometry('400x400')

entry = tk.Entry(window)
entry.grid(row=0, column=0, columnspan=3, padx=10,pady=10)


buttons =[
    (1,1,0),(2,1,1),(3,1,2),
    (4,2,0),(5,2,1),(6,2,2),
    (7,3,0),(8,3,1),(9,3,2)
]
for (num,row,col) in buttons:
    tk.Button(window, text=str(num), width=2, height=2,   command=lambda n=num: press(n)).grid(row=row, column=col, padx=10, pady=10)


tk.Button(window,text='clear', command=clear).grid()

result_label = tk.Label(window, text='')
result_label.grid()


window.mainloop()
