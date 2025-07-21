import json
import os
import sys

if os.path.exists("accounts.json"):
    with open('accounts.json','r') as f:
        accounts = json.load(f)
else:
     accounts = {}

def create_account():
    username = input('username: ')
    password = input('password: ')
    accounts[username] =password

    with open('accounts.json','w') as f:
        json.dump(accounts, f)
        print('Account saved!')


username = input('Enter Username: ')
password = input('Enter your password: ')

try:
    if username and password == accounts[username]:
            print('You have sucessfuly login')
    else:
        print('incorrect password')
except KeyError:
    print('Username not found')
        
    create = input('Do you to create an account? (yes/no): ')
    if create =='yes':
         create_account()
    else:
        sys.exit()
    
   