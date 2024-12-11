""" Statement Flow Control """

# If Statement
a=int(input("Enter a Number: "))
if a<200:
    print("The Number is Less Than 200.")


# If Else Statement
a=int(input("Enter a Number: "))
if a<200:
    print("The Number is Less Than 200.")
else:
    print("The Number is Greater Than 200.")

age=int(input("Enter your Age: "))
if age>=18:
    print("You can Vote.")
else:
    print("You cannot Vote.")


# If Elif Else Statement
num=float(input("Enter First Number: "))
num1=float(input("Enter Second Number: "))
op=input("Enter Operator: ")

if op=="+":
    print(num+num1)
elif op=="-":
    print(num-num1)
elif op=="/":
    print(num/num1)
elif op=="*":
    print(num*num1)
elif op=="%":
    print(num%num1)
elif op=="**":
    print(num**num1)
else:
    print("You have entered wrong Operator.")
