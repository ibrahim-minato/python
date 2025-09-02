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
         'D': 'Fugako'
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
    {'question':'Apart from Itachi who has Shiuia eye',
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
         'D': 'Black zasu'
     },
     'answer':'B'
    },
    {'question':'Who said that level of genjustsu would work on me',
     'options':{
         'A': 'Kuramia',
         'B': 'Kakashi',
         'C': 'Madara',
         'D': 'Itachi'
     },
     'answer':'D'
    }
]

score =0

for index, question in  enumerate(questions, start=1):
        print(f'\nQuestion {index}:{question['question']}')

        for key, value in question['options'].items():
                 print(f'{key}.{value}')
        ans= input('Your answer(A,B,C,D): ').upper()

        if ans == question['answer']:
            print('correct!')
            score +=1
        else:
            print(f' incorrect. The answer was {question['answer']}')

print('\n Quiz complete!')
print(f'Your score is {score}/{len(questions)}')
percentage = (score /len(questions)) *100
print(f'percentage: {percentage:.2f}%')

if percentage ==100:
    print('Excellent! Your are a true otaku!')
elif percentage >=60:
    print('You are Good')
else:
    print("Slow you don't watch naruto " )

