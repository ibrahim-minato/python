#!/usr/bin/env python3
# encoding: utf-8

'''THis program is a simple notebook
it use tkinter to create the inteface
you type what you want and if you click on save as it will as the filename
the save updates the saved file. it uses simpledialog to ask for the filename'''

import tkinter as tk
from tkinter import filedialog
import os


# The is the save function is uses simpledialog to ask filename
def save():
    filename = filedialog.asksaveasfilename(
        title='save file as...',
        defaultextension='.txt',
        filetypes=[('Text', '*.txt'), ('All', '*.*')])
    if filename:
        with open(filename, 'w') as f:
            f.write(tell.get('1.0', tk.END))


def update():
    with open('file.txt', 'a') as f:
        f.write(tell.get('1.0', tk.END))


root = tk.Tk()
root.title('Textbook')
root.geometry('800x600')


def view():
    open_path = filedialog.askopenfilename(
        title='Open file ...',
        defaultextension='.txt',
        filetypes=[('Text', '*.txt'), ('Python', '*.py'), ('All', '*.*')])
    if open_path:
        with open(open_path, 'r') as f:
            content = f.read()
            tell.delete('1.0', tk.END)
            tell.insert('1.0', content)
            print(content)


tell = tk.Text(root, width=5000, height=60, undo=True)
tell.pack()

man = tk.Menu(root)
drop = tk.Menu(man)
drop.add_command(label='save as', command=save)
drop.add_command(label='save', command=update)
drop.add_command(label='Open as', command=view)

man.add_cascade(label='file', menu=drop)
root.config(menu=man)

root.mainloop()