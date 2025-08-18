import  tkinter as tk


root = tk.Tk()
root.geometry('500x400')
root.title('minato')

new=tk.Frame(root,)
new.pack(expand=True)

name =['minato','madara','tobirama','sasuke']

select = tk.StringVar()
select.set(name[0])

menu = tk.OptionMenu(new, select,*name)
menu.pack()

root.mainloop() 