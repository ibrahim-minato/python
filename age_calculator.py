import tkinter as tk

def clear():
    entry.delete(0,tk.END)
    entry1.delete(0, tk.END)
    result_label.config(text='')


def age():
    try:
        birth_year = int(entry.get())
        current = int(entry1.get())
        age = current - birth_year

        result_label.config(text=f'You are {age} year old')
    except ValueError:
        result_label.config(text='Please enter a valid year')

root=tk.Tk()
root.title('AGE CALCULATOR')
root.geometry('500x400')
root.config(background='light green')

main_frame = tk.Frame(root, bg='light green',padx=20, pady=20)
main_frame.grid()

tk.Label(main_frame, text='Enter year of birth', font=('Arial',18),bg='light green').grid(row=0,column=0,pady=5)
entry = tk.Entry(main_frame)
entry.grid(row=0,column=1,pady=5)

tk.Label(main_frame, text='Enter the current year',font=('Arial',18),bg='light green').grid(row=1,column=0,pady=5)
entry1 = tk.Entry(main_frame)
entry1.grid(row=1,column=1,pady=5)

tk.Button(main_frame, text='begin',font=('Arial',16), command=age).grid(row= 2,column=1,pady=10)

clear_button=tk.Button(main_frame, text='clear',font=('Arial',16),bg='light blue', command=clear)
clear_button.grid(row=2, column=0,pady=10 )

result_label = tk.Label(root, text='',bg='light green',font=('Arial',18))
result_label.grid(row=3,column=0,pady=10,columnspan=2)

root.mainloop()

