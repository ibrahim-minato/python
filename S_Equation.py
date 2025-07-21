import tkinter as tk

def equation():
    try:
         a = int(a_entry.get())
         b = int(b_entry.get())
         c = int(c_entry.get())
         a1 = int(a1_entry.get())
         b1 = int(b1_entry.get())
         c1 = int(c1_entry.get())
         main =(b1*a)-(a1*b)
         x_deter =(c*b1)-(c1*b)
         y_deter =(a*c1)-(a1*c)
         x =x_deter/main
         y =y_deter/main

         result_label.config(text=f'X = {x} and Y = {y}')
    except ValueError:
        result_label.config(text='Please enter a valid equation')

window = tk.Tk()
window.title('STIMULATOUS EQUATION')
window.geometry('552x250')

tk.Label(window, text='Enter the equation').grid(row=0, column=0, columnspan=3, pady=10)
a_entry = tk.Entry(window)
a_entry.grid(row=1, column=0,padx=5,pady=5)


b_entry = tk.Entry(window)
b_entry.grid(row=1, column=1,padx=5,pady=5)


c_entry = tk.Entry(window)
c_entry.grid(row=1, column=2,padx=5,pady=5)


a1_entry = tk.Entry(window)
a1_entry.grid(row=2, column=0,padx=5,pady=5)

b1_entry = tk.Entry(window)
b1_entry.grid(row=2, column=1,padx=5,pady=5)

c1_entry = tk.Entry(window)
c1_entry.grid(row=2, column=2,padx=5,pady=5)

tk.Button(window,text='start', command=equation).grid(row=4, column=0, columnspan=3, pady=10)

result_label = tk.Label(window, text='')
result_label.grid(row=5, column=0, columnspan=3, pady=10 )

window.mainloop()





