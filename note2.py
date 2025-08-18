import tkinter as tk

def save():
    with open('minato.txt','w') as f:
        f.write('file')
    print('tobirama.text')

def redo():
    try:
        text.edit_redo()
    except tk.TclError:
        pass



root = tk.Tk()
root.title('NOTE 2')
root.geometry('800x600')

top_bar =tk.Frame(root, bg='light blue', height=30)
top_bar.pack(fill=tk.X)

btn = tk.Button(top_bar,text='💾',width=3)
btn.pack(side=tk.LEFT,padx=5,pady=5)

btn1 = tk.Button(top_bar,text='🛟',width=3, command=save)
btn1.pack(side=tk.LEFT,padx=5,pady=5)

btn2 = tk.Button(top_bar,text='🚃',width=3)
btn2.pack(side=tk.LEFT,padx=5,pady=5)

btn3 = tk.Button(top_bar,text='♨️',width=3)
btn3.pack(side=tk.LEFT,padx=5,pady=5)

btn4 = tk.Button(top_bar,text='🛸',width=3)
btn4.pack(side=tk.LEFT,padx=5,pady=5)

text = tk.Text(root, undo=True,width=800,height=600)
text.pack()


text.bind("<Control-y>", lambda e:
redo())


root.mainloop()