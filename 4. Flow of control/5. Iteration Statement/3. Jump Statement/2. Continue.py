""" Jump Statement """

for i in range(1,10):
    if i==5:
        continue
    print(i)


# Sqaure 
while True:
    num=int(input("Enter a Number: "))
    square=num**2
    print("Sqaure of",num,"is",square)
    c=input("Press Y to Continue or Press N to Stop.")
    if c=="y":
        continue
    elif c=="n":
        print("Program Terminated.")
        break
    else:
        print("Invalid Input.")
