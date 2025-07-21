import tkinter as tk

def clear():
    entry.delete(0, tk.END)
    result_label.config(text='')

def press(n):
    if n=='=':
        cal()
    else:
        entry.insert(0,str(n))

def cal():
    try:
      expression = entry.get()
      result = eval(expression)
      entry.delete(0, tk.END)
      entry.insert(0, str(result))
      result_label.config(text=f'Result: {result}')
    except:
        result_label.config(text='Error - Invalid expression')


root = tk.Tk()
root.title('FULL CALCULATOR')
root.geometry("400x500")

tk.Label(root, text='Enter  number:',font=('Arial',12)).grid( row=0,column=0,pady=10,columnspan=4)
entry =tk.Entry(root, width=20, font=('Arial',14))
entry.grid(row=1,column=0,columnspan=4,pady=10,padx=10)

buttons = [
    (1,3,0),(2,3,1),(3,3,2),('+',3,3),
    (4,4,0),(5,4,1),(6,4,2),('-',4,3),
    (7,5,0),(8,5,1),(9,5,2),('*',5,3),
    (0,6,0),('.',6,1),('=',6,2),('/',6,3)

]

for (num , row,col) in buttons:
    tk.Button(root, text=str(num), width=2,height=2, command=lambda n=num: press(n)).grid(row=row, column=col,pady=2,padx=2)

tk.Button(root, text='clear', command=clear).grid(row=7,column=0,pady=5,padx=5)
tk.Button(root, text='calculate', command=cal).grid(row=7,column=1,pady=5,padx=5)
result_label = tk.Label(root, text='')
result_label.grid()


root.mainloop()
