'''A calculator  with functions'''
import math

def add(*numbers):
    return sum(numbers)
def subtract(*numbers):
    result =numbers[0]
    for num in numbers[1:]:
        result -= num
    return result
def multiply(*numbers):
    return math.prod(numbers)

def power(*numbers):
    return math.pow(numbers[0],numbers[1])

def root(numbers):
    return math.sqrt(numbers)

def divide(*numbers):
    result = numbers[0]
    for num in numbers[0:]:
        if num ==0:
          return  'Error: cannot divide by zero '
        result /= num
    return result

oper = input('Enter the operators (x,-,/,+,^,sqrt): ')

num = input('Enter the numbers separated by spaces: ')
number = [float(num) for num in num.split()]

if oper =='+':
    print('The sum is: ',add(*number))
elif oper =='-':
    print('The difference is: ',subtract(*number))
elif oper=='x':
    print('The product is: ',multiply(*number))
elif oper=='sqrt':
    print('The square of the number is: ',root(*number))
elif oper=='/':
    print('The quotient is: ',divide(*number))
elif oper=='^':
    print('THe power is: ',power(*number))
else:
    print('Please enter a valid operator')
