number = input('Enter a  number')
if number.isdigit():
    number =int(number)
if number > 1:
    for i in range(2,number):
        if number%i==0:
            print('not prime')
        else:
            print('prime')