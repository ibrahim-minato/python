import tkinter as tk

root = tk.Tk()
root.title('Menu')
root.geometry('800x600')

man = tk.Menu(root)

new = tk.Menu(man)
new.add_command(label='Minato')
new.add_separator()
new.add_command(label='Hashirama')
new.add_separator()
new.add_command(label='Naruto')
new.add_separator()
new.add_command(label='Tobirama')
new.add_separator()
new.add_command(label='Hirusa')
new.add_separator()
new.add_command(label='Kakashi')

edit = tk.Menu(man)
edit.add_command(label='Madara')
edit.add_separator()
edit.add_command(label='Sasuke')
edit.add_separator()
edit.add_command(label='Itachi')
edit.add_separator()
edit.add_command(label='Fugaku')
edit.add_separator()
edit.add_command(label='Nagato')
edit.add_separator()
edit.add_command(label='Obito')
edit.add_separator()


man.add_cascade(label='File',menu=new )
man.add_cascade(label='Edit',menu=edit)
root.config(menu=man)

tk.Text(root,undo=True, width=800, height=600).pack()


root.mainloop()