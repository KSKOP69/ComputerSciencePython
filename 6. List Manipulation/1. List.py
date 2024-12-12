""" List Manipulation """

# Empty List
list1=[]
list2=list()
print(list2)


# Long List
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,
         28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
print(numbers[5])


# Nested List
list3=[[1,2],["Delhi", "India"],[8,"Python"]]
print(list3)
print(list3[2])


# Creating a List from Existing Sequence
list4=list("Hello")
print(list4)

a="Karan Singh"
print(list(a))

list5=list(input("Enter Elements of List: "))
print(list5)


# eval() function in Python is used to evaluate a valid Python expression or code represented as a string. It interprets the string as Python code and executes it, returning the result of the evaluation.
list5=eval(input("Enter Elements of List: "))
print(list5)

# Uses of eval() Function
ak=eval("25*5")
print(ak)


# Accessing List
a=[5,10,15,20,25,30]
print(a[2])

list6=["Delhi","Mumbai","Chennai",25]
print(list6[2])
print(list6[-4])


# Changes in List
list7=["Red","Green","Blue","Black","Pink"]
list7[-3]="Orange"
print(list7)