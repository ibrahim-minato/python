'''This program calculate the area of a circle and uses cerberus to prevent system crash'''
from cerberus import Validator

PI =3.14159

schema = {
    'radius': {'type':'float','min':0,'required':True}
}
v = Validator(schema)

radius = float(input("Enter the radius: "))

data ={'radius':radius}

Area = PI * radius**2
if v.validate(data):
    print(f'THe area of the circle is {Area}')
else:
    print(f'Input error {v.errors}')
