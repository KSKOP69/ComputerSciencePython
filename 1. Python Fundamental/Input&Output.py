""" Input and Output"""

'''
The type() function in Python is used to determine the type of an object. It returns the class type of the object, which helps you understand what kind of data or object you're dealing with.

The int() function in Python is used to convert a value into an integer. It can take strings, floats, or other types of data (if convertible) and return their integer representation. It is also commonly used for type conversion.
'''
# Input
name=input("Enter your Name: ")
age=input("Enter your Age: ")
print(name, type(name))
print(age, type(age))

"Reading Numbers"

# Integers
age=int(input("Enter your Age: "))
print(age, type(age))

a=int(input("Enter a Number: "))
b=int(input("Enter a Number: "))
c=a+b
print(c, type(c))

# Float
a=float(input("Enter a Number: "))
b=float(input("Enter a Number: "))
c=a+b
print(c, type(c))




# Output
'''
Output refers to the data that a program sends to the user or another system after processing. This is typically done using functions like print() to display data in the terminal/console or by writing to files, GUIs, or network connections.

sep: A string inserted between the values (default is a space).
end: A string added after the output (default is a newline \n).
'''
print("My","Name","is","Karan","Singh")
print("My","Name","is","Karan","Singh",sep="_")

print("Hello World", end=" @ ")
print("Python Programming")