""" List Manipulation """

a=[1,2,3]
b=a
print(a)
print(b)

a[1]=5
print(a)
print(b)


# True Copy

# 1st Method
a=[1,2,3]
b=list(a)
print(a)
print(b)

a[2]=0
print(a)
print(b)


# 2nd Method
list1=[1,2,3]
list2=list1.copy() 
print(list1)
print(list2)
list1[0]+=9
print(list1)
print(list2)


# 3rd Method
list1=[1,2,3,4]
list2=list(list1)
print(list1)
print(list2)
list1[0]+=9
print(list1)
print(list2)
