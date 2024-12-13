""" Dictionaries """

address={"KSK":"Delhi","Raj":"Kanpur","Mohan":"Kerala"}
print(address)

rn={"KSK":"21","Raj":"37","Mohan":"30"}
print(rn)


# Create Dict
student={}
for i in range(1,5):
    name=input("Enter your Name: ")
    rn=input("Enter your Roll No.: ")
    student.update({name:rn})
print("Dict After Updates.")
print(student)


# Accessing Dict
rn={"KSK":"21","Aditya":"2","Neha":"39"}
print(rn["Aditya"])
'print(rn["Raamu"])' # Error
