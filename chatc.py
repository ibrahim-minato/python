import tkinter as tk

def press(num):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(num))

root =tk.Tk()
root.title('minto')
root.geometry('440x500')

display =tk.Entry(root, font=("Arial", 24), justify='right',bd=10, relief=tk.RIDGE)
display.grid(row=0, column=0, columnspan=3, pady=20,padx=10)

buttons =[
    (1,1,0), (2,1,1), (3,1,2),
    (4,2,0), (5,2,1), (6,2,2),
    (7,3,0), (8,3,1), (9,3,2),
    (0,4,1)
]
for (num, row, col) in buttons:
    tk.Button(root, text=str(num), width=5, height=2, font=('Arial',18),
              command=lambda n=num: press(n)).grid(row=row, column=col, padx=10, pady=10)

    #clear button
    tk.Button(root, text='clear', width=5, height=2, font=('Arial',18), command=lambda:
              display.delete(0, tk.END)).grid(row=4, column=0, padx=10, pady=10)

root.mainloop()