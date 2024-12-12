""" Tuples """

a=(1,2,3,4,5,6)
print(a)

tuple1=("Eco",25,"Physics",69.5)
print(tuple1)


# Creating a Tuple
tuple3=(10,20,30,[20,30],"KSK")
print(tuple3)


# Empty Tuple
tuple4=()
tuple5=tuple()
print(tuple4)
print(tuple5)


# Single Element
tuple6=(25,) # Just add comma in the End
print(tuple6)


# Long Tuple
tuple7=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50)
print(tuple7)


# Nested Tuple
tuple8=(1,2,3,4,5,(6,7))
print(tuple8)


# Create Tuple from existing Sequence
tuple9=tuple("Hello")
print(tuple9)
a="Welcome"
tuple10=tuple(a)
print(tuple10)

tuple11=tuple(input("Enter Number: "))
print(tuple11)

tuple11=eval(input("Enter Number: ")) # Integers
print(tuple11)
