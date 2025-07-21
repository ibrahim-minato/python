import tkinter as tk

root = tk.Tk()
root.title('Note1')
root.geometry('800x600')

tk.Text(root, undo=True, width=800,height=600).pack()



root.mainloop()