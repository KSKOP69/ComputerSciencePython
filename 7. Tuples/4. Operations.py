""" Tuples """

# Concatenation
tuple1=(1,3,5,7,9)
tuple2=(2,4,6,8,0)
tuple3=tuple1+tuple2
print(tuple3)

tuple4=("Red","Black")
tuple5=("Blue","Green")
tuple6=tuple4+tuple5
print(tuple6)


# Replication
tuple1=(1,3)
print(tuple1*3)


# Slicing
tup=("Red","Green","Blue","Cyan","Magenta","Black","Yellow")
print(tup[2:6])
print(tup[:5])
print(tup[0:7:3]) # Index
print(tup[-1:-5:-2]) # Negative Index
print(tup[::3]) # Both Index Missing


# Comparing
tuple1=(1,2,3)
tuple2=(1,(2,3))
tuple3=(1,2,3)
print(tuple1==tuple2)
print(tuple1==tuple3)
'print(tuple1<tuple2)' # Error
print(tuple1<tuple3)


# Unpacking
t1=(10,"KSK",25)
a,b,c=t1
print(a)
print(b)
print(c)


# Delete
tup1=(1,6,0,"Hello")
del tup1
'print(tup1)' # Error 