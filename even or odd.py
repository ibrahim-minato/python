'''This is a program to check if a number is even or odd'''
number = input('Enter the number: ')
if number.isdigit():
    number = int(number)
if number/2==0:
    print(f'{number} is ann odd number')
else:
    print(f'{number} is an even number')