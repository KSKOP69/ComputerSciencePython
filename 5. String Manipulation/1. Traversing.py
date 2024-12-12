""" String Manipulation """

name="Karan"
for k in name:
    print(k,"-")


# Question:- Reverse the String
string=input("Enter a String: ")
print(f"The {string} in Reverse Order is: ")
lenght=len(string)
print(lenght)
for a in range(-1,-lenght-1,-1):
    print(string[a])
