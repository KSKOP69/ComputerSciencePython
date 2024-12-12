""" List Manipulation """

# len()
list1= [10,15,20,25,30]
print(len(list1))


# list()
list1=list()
print(list1)
str1="python"
list1=list(str1)
print(list1)


# append() method
list2=[10,15,20,25]
list2.append(30)
print(list2)

list2=[10,15,20,25]
list2.append([30,40])
print(list2)


# extend()
list1=[10,15,20]
list2=[25,30,35]
list1.extend(list2)
print(list1)


# insert()
list1=[10,20,30,40,50]
list1.insert(2,25)
print(list1)
list1.insert(5,45)
print(list1)


# count()
list1=[10,20,30,40,50,10]
print(list1.count(10))
print(list1.count(90))


# index()
list1=[10,20,30,40,50,10]
print(list1.index(30))
'print(list1.index(80))' # Error


# remove()
list1=[10,20,30,40,50,30]
list1.remove(30)
print(list1)

list2=[10,20,30,40,50,30]
'list2.remove(70)' # Error
print(list2)


# pop()
list1=[10,20,30,40,50,60]
list1.pop(3)
print(list1)

list2=[10,20,30,40,50,60]
list2.pop()
print(list2)


# reverse()
list1=[33,44,55,66,77,88,99]
list1.reverse()
print(list1)

list2=["Tiger","Lion","Deer"]
list2.reverse()
print(list2)


# sort()
list1=["Tiger","Lion","Deer","Dog","Zebra"]
list1.sort()
print(list1)

list1=[99, 88, 77, 66, 55, 44, 33]
list1.sort()
print(list1)


list1=["Tiger","Lion","Deer","Dog","Zebra"]
list1.sort(reverse=True)
print(list1)

list1=[33,44,55,66,77,88,99]
list1.sort(reverse=True)
print(list1)


# sorted()
list1=[23,45,67,34,67]
list2=sorted(list1)
print(list2)


# clear()
list1=[99, 88, 79, 62, 85, 44, 33]
list2=["Tiger","Lion","Deer","Dog","Zebra"]
list1.clear()
list2.clear()
print(list1)
print(list2)


# min(), max(), sum()
list1=[32,12,45,67,23,15]
print(min(list1))
print(max(list1))
print(sum(list1))