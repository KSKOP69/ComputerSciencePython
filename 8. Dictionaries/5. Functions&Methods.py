""" Dictionaries """

# len()
dict1={"Mohan":95,"Ksk":25,"Ram":108,"Neha":98}
print(len(dict1))


# dict()
p1=[("Mohan",95),("Ksk",25),("Ram",108),("Neha",98)]
print(p1)
dict2=dict(p1)
print(dict2)


# get()
print(dict2.get("Ksk"))
print(dict2.get("Raman"))


# items()
print(dict2.items())


# keys()
print(dict2.keys())


# values()
print(dict2.values())


# fromkeys()
a=dict.fromkeys([2,4,6,8],100)
print(a)


# setdefault()
marks={1:350,2:42,3:420,4:69}
print(marks)
marks.setdefault(5,400)
print(marks)


# update()
dict1={"Mohan":95,"Ksk":25,"Ram":108,"Neha":98}
dict2={"Raman":109,"Jaadu":22,"Reena":110}
dict1.update(dict2)
print(dict1)


# copy()
dict1={"Mohan":95,"Ksk":25,"Ram":108,"Neha":98}
dict2=dict1.copy()
print(dict2)

dict2["Ksk"]=21
print(dict1)
print(dict2)



# clear()
dict1={"Mohan":95,"Ksk":25,"Ram":108,"Neha":98}
dict1.clear()
print(dict1)


# pop()
dict1={"Mohan":95,"Ksk":25,"Ram":108,"Neha":98}
dict1.pop("Ram")
print(dict1)


# popitem()
dict1={"Mohan":95,"Ksk":25,"Ram":108,"Neha":98}
print(dict1.popitem())


# sorted()
dict1={4:"Sachin",2:"KSK",1:"Zeus"}
dict2=sorted(dict1)
print(dict2)

dict3=sorted(dict1.values())
print(dict3)

dict2=sorted(dict1,reverse=True) # Reverse (Descending)
print(dict2)


# max(), min(), sum()
dict1={4:"Sachin",2:"KSK",1:"Zeus",10:"Mohan"}
print(min(dict1))
print(max(dict1))
print(sum(dict1))

dict1={4:40,2:20,1:10,10:100}
print(min(dict1.values()))
print(max(dict1.values()))
print(sum(dict1.values()))
