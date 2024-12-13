""" Dictionaries """

employee={"Ajey":{"Age":25,"Salary":20000}, "Neha":{"Age":35,"Salary":5000}}
for i in employee:
    print("Employee",i,":")
    print("Age",employee[i]["Age"])
    print("Salary",employee[i]["Salary"])
