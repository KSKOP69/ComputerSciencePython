""" Python Identity Operators """

'''
The id() function in Python is a built-in function that returns the unique identifier for a given object. This identifier is an integer that is guaranteed to be unique and constant for the object during its lifetime.
'''

a=5
b=5
c='5'

# is 
print(a is b)
print(a is c)

# is not
print(a is not b)
print(a is not c)

"Checking id"
print(id(a))
print(id(b))
print(id(c))