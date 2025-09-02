import tkinter as tk
import random
from PIL import Image,ImageTk


def clear():
    entry.delete(0,tk.END)
    result_label.config(text='')

def rock():
    try:
        options = ['rock','paper','scissor']
        user = entry.get()
        computer = random.choice(options)

        if user == computer:
            result_label.config(text=f'{computer} it a tie')
        elif ((user == 'rock' and computer == 'scissor') or
              (user == 'paper' and computer == 'rock') or
              (user == 'scissor' and computer == 'paper')):
            result_label.config(text=f'{computer} you win!')
        else:
            result_label.config(text=f'{computer} you lose!')
    except ValueError:
        result_label.config(text='Please enter a valid input')

root =tk.Tk()
root.title('ROCK,PAPER, SCISSOR')
root.geometry('400x200')

bg_image = Image.open('naru.png')
bg_image = bg_image.resize((500,400))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label= tk.Label(root, image=bg_photo)
bg_label.place(x=0,y=0,relwidth=1, relheight=1)



tk.Label(root,text='Please enter your choice(Rock,Paper,Scissor)').pack()
entry =tk.Entry(root)
entry.pack(pady=10)

tk.Button(root, text='Start', command=rock).pack()
tk.Button(root, text='Clear', command=clear).pack(pady=10,padx=20)

result_label = tk.Label(root,text='')
result_label.pack()

root.mainloop()




