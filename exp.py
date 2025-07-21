import tkinter as tk

root =tk.Tk()
root.title('minato')
root.geometry('300x400')

display_var =tk.StringVar()
display_var.set('0')

def button():
    current = display_var



tk.Button(root, text='1', command='1').grid(row=0,column=0,pady=5)
tk.Button(root, text='2').grid(row=0,column=1,pady=5)
tk.Button(root, text='3').grid(row=0,column=2,pady=5)
tk.Button(root, text='+').grid(row=0,column=3,pady=5)

tk.Button(root, text='4').grid(row=1,column=0,pady=5)
tk.Button(root, text='5').grid(row=1,column=1,pady=5)
tk.Button(root, text='6').grid(row=1,column=2,pady=5)
tk.Button(root, text='-').grid(row=1,column=3,pady=5)

tk.Button(root, text='7').grid(row=2,column=0,pady=5)
tk.Button(root, text='8').grid(row=2,column=1,pady=5)
tk.Button(root, text='9').grid(row=2,column=2,pady=5)
tk.Button(root, text='x').grid(row=2,column=3,pady=5)

tk.Button(root, text='0').grid(row=3,column=0,pady=5)
tk.Button(root, text='.').grid(row=3,column=1,pady=5)
tk.Button(root, text='=').grid(row=3,column=2,pady=5)
tk.Button(root, text='/').grid(row=3,column=3,pady=5)

result_label = tk.Label(root,text='')
result_label.grid()

root.mainloop()