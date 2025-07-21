import tkinter as tk
import random
from PIL import Image, ImageTk


def clear():
    entry.delete(0, tk.END)
    result_label.config(text='')

def guess():
    try:
        computer = random.randint(0,100)
        number = int(entry.get())
        if number >100 :
            result_label.config(text='Please enter a number less than 100')
        elif number <0:
            result_label.config(text='Please enter a number greater than 0')
        elif number ==computer:
            result_label.config(text='correct! welcome to Konoha!')
        elif number > computer:
            result_label.config(text="Too high, like jiraiya's ego")
        elif number < computer:
            result_label.config(text="Too low, like Sasuke's emotions")
    except ValueError:
        result_label.config(text='Please enter a valid number')

root = tk.Tk()
root.title('Naruto Guessing Game')
root.geometry('500x400')
root.resizable(False,False)

bg_image = Image.open('ghost.jpg')
bg_image = bg_image.resize((500,400))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label= tk.Label(root, image=bg_photo)
bg_label.place(x=0,y=0,relwidth=1, relheight=1)

main_frame = tk.Frame(root, bg='black')
main_frame.place(relx=0.5,rely=0.5, anchor='center')

tk.Label(main_frame, text='Enter your guess(1-100)', font=('Comic San MS',14,'bold'),
         fg='orange',bg='black').pack(pady=10)
entry = tk.Entry(main_frame, font=('Comic San MS',14))
entry.pack()

tk.Button(main_frame, text=' Guess', command=guess, font=('Comic San MS',12),bg='#f0c808',fg='black').pack(pady=5)
tk.Button(main_frame, text=' Clear', command=clear, font=('Comic San MS',12),bg='red',fg='white').pack(pady=5)

result_label = tk.Label(main_frame, text='', font=('Comic San MS',12), fg='white',bg='black')
result_label.pack(pady=10)

root.mainloop()

