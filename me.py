import tkinter as tk

root = tk.Tk()
root.title('custom')
root.geometry('500x400')
root.config(bg='#2e2e2e')

menu_btn = tk.Button(root, text='MENU',width=100, height=1,bg='#3b82f6',fg='white')
menu_btn.place(relx=0.5,rely=0.5,anchor="center")


root.mainloop()