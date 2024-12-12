""" List Manipulation """

list1=["Red","Green","Blue","Cyan","Magenta","Black","Yellow"]
print(list1[2:6])
print(list1[2:7])
print(list1[7:2])
print(list1[:5])
print(list1[-5:])


# Slicing with Step Size
print(list1[0:6:2])

# Slicing with Negative Indexes
print(list1[-6:-2])

# Both Missing
print(list1[::2])

# Negative Step Size
print(list1[::-1])


# List Modification
list1=["one","two","three"]
list1[0:2]=[1,2]
print(list1)

list2=["one","two","three"]
list2[0:2]=["2"]
print(list2)

list1=[1,2,3]
list1[2:]="345"
print(list1)

list1=[1,2,3]
list1[2:]=[3,4,5]
print(list1)
