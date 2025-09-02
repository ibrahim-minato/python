'''This a naryto base age calculator it only ask for year of birth
and it uses the current year '''
import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk


def  calculator():
    try:
        birth_year = int(entry.get())
        current = datetime.now().year
        age =  current - birth_year
        result_label.config(text=f' You are are {age} year old')
    except ValueError:
        result_label.config(text='Please enter a valid year')

def clear():
    entry.delete(0, 'end')
    result_label.config(text='')


app = tk.Tk()
app.title('Naruto Themed Age Calculator')
app.geometry('400x400')
app.resizable(False,False)

bg_image = Image.open('naru.png')
bg_image = bg_image.resize((400,400))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label= tk.Label(app, image=bg_photo)
bg_label.place(x=0,y=0,relwidth=1, relheight=1)

heading = tk.Label(app, text='Age Calculator', font=('Comic San MS' ,24),bg='black',fg='orange')
heading.pack(pady=20)

entry = tk.Entry(app, width=200,font=('Arial',16), justify='center')
entry.pack(pady=10)

result_label =tk.Label(app, text='', font=('Comic San MS',16))
result_label.pack(pady=10)

button_frame = tk.Frame(app)
button_frame.pack(pady=20)

calc_button = tk.Button(button_frame, text='Calculate', command=calculator,font=('Comic San MS',12),bg='#f0c808',fg='black')
calc_button.grid(row=0, column=0, padx=10)

clear_button =tk.Button(button_frame,text='Clear',command=clear,font=('Comic San MS',12),bg='red',fg='white')
clear_button.grid(row=0, column=1, padx=10)

app.mainloop()