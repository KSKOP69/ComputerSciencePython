""" Jump Statement """

num=0
for num in range(10):
    num += 1
    if num ==8:
        break
    print("Num has Value",num)
print("encountered break!! Out of Loop")


# Infinite Loop
"""
a=0
while a<=10:
    print(a)
"""

a=0
while a<=10:
    print(a)
    a+=1
    if a==10:
        break

# Sqaure 
while True:
    num=int(input("Enter a Number: "))
    square=num**2
    print("Sqaure of",num,"is",square)
    c=input("Press N to Stop.")
    if c=="n":
        break
