""" Dictionaries """

# Modifying Existing Item
dict1={"KSK":21,"Raj":37,"Mohan":30,"Neha":35}
print(dict1)
dict1["Neha"]=37
print(dict1)


# Add New Item
dict1["Meenal"]=34
print(dict1)


# Delete
del dict1["Raj"]
print(dict1)


# Checking for Existance of a Key
print("Mohan" in dict1)
print("Rohan" in dict1)


# Checking for Existance of a Value
print(34 in dict1.values())
print(105 in dict1.values())
