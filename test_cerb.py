from cerberus import Validator

schema = {
      'name': {'type':'string','required':True},
      'age': {'type':'integer','min':18,'required':True}
}
v = Validator(schema)

data = {'name':'Minato','age':20}
if v.validate(data):
      print('valid data')
else:
      print('invalid data:',v.errors)