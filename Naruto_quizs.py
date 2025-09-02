import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

questions = [
    {'question':'who is naruto father ',
     'options':{
        'A':'Jiriya',
        'B':'Kakashi',
        'C':'Minato',
        'D':'Iruka'
     },
     'answer':'C'
    },
    {'question': 'Who is the Ghost of the Uchiha',
     'options':{
         'A': 'Madara',
         'B': 'Obito',
         'C': 'Itachi',
         'D': 'Fugaku'
     },
        'answer':'A'
     },
    {'question':'Who killed Minato and Kushina',
     'options':{
         'A': 'Obito',
         'B': 'Kurama',
         'C': 'Madara',
         'D': 'Danzo'
     },
     'answer':'B'
    },
    {'question':'Apart from Itachi who has Shisui eye',
     'options':{
         'A': 'Madara',
         'B': 'Obito',
         'C': 'Kakashi',
         'D': 'Danzo'
     },
     'answer':'D'
    },
    {'question':'Who killed Rin',
     'options':{
         'A': 'Obito',
         'B': 'Kakashi',
         'C': 'Madara',
         'D': 'Black zetsu'
     },
     'answer':'B'
    },
    {'question':'Who said that level of genjustsu would work on me',
     'options':{
         'A': 'Kurenai',
         'B': 'Kakashi',
         'C': 'Madara',
         'D': 'Itachi'
     },
     'answer':'D'
    }
]

current_question =0
score=0

def display_question():
    question_label.config(text=questions[current_question]['question'])
    for key in option_buttons:
        option_buttons[key].config(text=f'{key}. {questions[current_question]['options'][key]}')


def check_answer(selected):
    global current_question, score
    correct = questions[current_question]['answer']
    if selected == correct:
        score +=1

    current_question +=1
    if current_question < len(questions):
        display_question()
    else:
        show_result()

def show_result():
    result = f' You scored {score} out of {len(questions)}'
    messagebox.showinfo('Quiz Finished', result)
    root.destroy()

root = tk.Tk()
root.title('Naruto Quiz App')
root.geometry('500x400')
root.resizable(False,False)

bg_image = Image.open('madara.jpg')
bg_image = bg_image.resize((500,400),Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


main_frame = tk.Frame(root,bg='#000000080')
main_frame.place(relx=0.5, rely=0.5, anchor='center')


question_label = tk.Label(main_frame, text='', wraplength=400, font=('Comic Sans MS',14,'bold'),fg='orange',
                          bg='black', pady=20 )
question_label.pack()

option_buttons ={}

for key in ['A','B','C','D']:
    btn = tk.Button(main_frame, text='',width=30, font=('Comic Sans MS',12),bg='#f7d354',fg='black',command=lambda k=key:
                    check_answer(k))
    btn.pack(pady=5)
    option_buttons[key] = btn

display_question()
root.mainloop()