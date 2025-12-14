""" String Manipulation """

name="Karan"
for k in name:
    print(k,"-")


# Question:- Reverse the String
string=input("Enter a String: ")
print(f"The {string} in Reverse Order is: ")
length=len(string)
print(length)
for a in range(-1,-length-1,-1):
    print(string[a])
