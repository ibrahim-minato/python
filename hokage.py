import tkinter as tk

root = tk.Tk()
root.title('Naruto theme')
root.geometry('400x300')
root.config(bg='#FF8300')

label = tk.Label(root, text='Welcome Konoha!', font=('Helvetica',16), fg='white', bg='#FF8300')
label.pack(pady=20)

button =tk.Button(root, text='Believe it',font=('Helvetica',16), bg='black',fg='#FF8300')
button.pack(pady=10)

root.mainloop()