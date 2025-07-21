import random

while True:

    name = input('What is your name? :')
    age = int(input('How old are you? :'))

    answer = {}

    questions = [
        ('color', 'What is your favorite color? :'),
        ('food', 'What is your favorite food? :'),
        ('city', 'What city do you live? :'),
        ('shs', 'What SHS did you attended? :'),
        ('team', 'What is your favorite Scoccer team? :')
    ]
    random.shuffle(questions)

    for a, question in questions:
        answer[a] = input(question)

    print('---personal summary---')
    print(f"\nHello {name}")
    print(f'You are {age} years old, you love the color {answer["color"]}, and you enjoy eating {answer["food"]}')
    print(
        f'Life must be awesome in {answer["city"]}, you attended {answer["shs"]}, and you are a real {answer["team"]} fan ')

    save = input('Do you want to save his summary (yes/no)')
    rate = int(input('Rate the Assistant ⭐(1-5):'))
    if save == 'yes':
        with open(f'{name}.txt', 'w') as f:
            f.write(f'Name: {name}')
            f.write(f'\nAge: {age}')
            f.write(f'\nFavorite Color: {answer["color"]}')
            f.write(f'\nFavorite Food: {answer["food"]}')
            f.write(f'\nCity: {answer["city"]}')
            f.write(f'\nSHS Attended: {answer["shs"]}')
            f.write(f'\nFavorite Team: {answer["team"]}')
            f.write(f'\nSummary Rate: {rate}')
        print('summary.txt')

    again = input('Do you want to restart 🤔 (yes/no)')
    if again == 'no':
        print('Goodbye 🫡m ')
        break


