import tkinter as tk



def cal():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        operator = operator_var.get()

        if operator =='+':
            result =num1 + num2
        elif operator =="-":
            result = num1 - num2
        elif operator =='*':
            result = num1 * num2
        elif operator=='/':
            result = num1 / num2
        else:
            result_label.config(text='Invalid operator')
            return
        result_label.config(text=f'result: {result}')
    except ValueError:
        result_label.config(text='Please enter a valid number')


root = tk.Tk()
root.title('Simple calculator')
root.geometry('500x500')

tk.Label(root, text='Enter first number ' ).pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text='Enter second number ' ).pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text='Enter operator ' ).pack()
operator_var =tk.StringVar()
entry_operator = tk.Entry(root, textvariable=operator_var)
entry_operator.pack()

tk.Button(root, text='calculate', command=cal).pack()

result_label = tk.Label(root, text='')
result_label.pack()

root.mainloop()
