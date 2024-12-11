""" Conditional Loops """

# Square of 1st Five Nautral Numbers
n=1
while n<6:
    print("Sqaure of",n,"is",n*n)
    n+=1
print("Over !!!")

# 1st Five Natural Numbers
count=1
while count<=5:
    print("1st Natural Number: ",count)
    count+=1
print("Done !!!")

# Calculate Factorial
num=int(input("Enter a Number: "))
fact=1
a=1
while a<=num:
    fact*=a
    a+=1
print("The Factorial of",num,"is",fact)
