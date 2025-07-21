import os
import json


def save():
    if os.path.exists('accounts.json'):
        with open('accounts.json','r') as f:
            json.load(f)
    else:
        accounts = {}

    def create_account():
        username = input('Username')
        password = input('Password')
        accounts[username] = password

        with open('accounts.json','w') as f:
            json.dump(accounts,f)
            print('Account created')

        create_account()