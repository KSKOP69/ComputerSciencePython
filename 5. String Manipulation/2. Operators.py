""" String Manipulation """

# Basic Operators #

# String Concatenation
a="Tea"
b="pot"
print(a+b)

a,b=2,3
print(a+b)

'print("2"+3)' #Wrong will throw Error.


# String Replication
a,b=3,"Hello !"
print(a*b)

a,b=3,"2"
print(a*b)

'print("3"*"2")'  #Wrong will throw Error.



# Membership Operators #
print("H" in "Hello")
print("Del" in "India")

print("H" not in "Hello")
print("123" not in "Japan")



# Comparison Operators #
print("a" == "a")
print("a" != "abcd")

print("a" < "A")
print("ABC" > "AB")
print("abc" < "ABCD")


print(ord("A"))
print(ord("a"))

print(chr(97))
print(chr(65))
