""" Counting Loops """

'''
The range() function in Python is used to generate a sequence of numbers. It is commonly used in loops and is very efficient because it generates numbers lazily, meaning the numbers are created as needed rather than all at once.

range(start, stop, step):-
~ start (optional): The starting value of the sequence. Default is 0.
~ stop (required): The end value of the sequence (exclusive, i.e., not included in the range).
~ step (optional): The difference between each number in the sequence. Default is 1.
'''
a="Python"
for i in a:
    print(i)


# List
a=["Python",5,"KSK",25.7]
for i in a:
    print(i)


# Range Function
a=list(range(10))
print(a)

a=list(range(4,20))
print(a)

a=list(range(4,20,6))
print(a)


# Range Function with For Loop
for num in range(5):
    if num>0:
        print(num*10)

for num in range(2,5):
    print(num)

num=5
for k in range(1,11):
    print(num,"*",k,"=",num*k)


# Question:- Write a program to print the table of a number.

num=int(input("Enter a Number: "))
for k in range(1,11):
    print(num,"*",k,"=",num*k)
