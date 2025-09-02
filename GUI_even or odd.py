import tkinter as tk

def even():
    try:
        number = int(entry.get())
        if (number%2)==0:
            result_label.config(text=f'{number} is an even number ')
        else:
            result_label.config(text=f'{number} is an odd number')
    except ValueError:
        result_label.config(text='Please enter a valid number')

window = tk.Tk()
window.title('EVEN OR ODD CHECKER')
window.geometry('400x200')
window.config(background='light blue')

tk.Label(window, text='Enter any number').pack()
entry = tk.Entry(window)
entry.pack()

tk.Button(window, text='check', command=even).pack()

result_label = tk.Label(window,text='')
result_label.pack()

window.mainloop()




