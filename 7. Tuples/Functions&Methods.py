""" Tuples """

# len()
tuple1=(10,20,30,40)
print(len(tuple1))


# tuple()
tuple1=tuple()
print(tuple1)

str1="python"
tuple2=tuple(str1)
print(tuple2)


# count()
tuple1=(10,20,30,40,50,10,30,10,10,30,50,60,20,30,70)
print(tuple1.count(10))
print(tuple1.count(90))


# index()
tuple1=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50)
print(tuple1.index(20))
'print(tuple1.index(90))' # Error


# sorted()
tuple1=(20,10,9,5,1,2,3,4,5,6,7,8,9,10)
tuple2=sorted(tuple1)
print(tuple2)


# sorted()
tuple1=(20,10,9,5,1,2,3,4,5,6,7,8,9,10)
tuple2=sorted(tuple1, reverse=True) # Reverse
print(tuple2)


# max(), min(), sum()
tuple1=(5,6,7,8,9,10)
print(min(tuple1))
print(max(tuple1))
print(sum(tuple1))