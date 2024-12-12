""" 2D List """

list1=[]
r=int(input("Enter Number of Row: "))
c=int(input("Enter Number of Columns: "))
for i in range(r):
    row=[]
    for j in range(c):
        elements=int(input("Enter Elements: "+str(i)+","+str(j)+":"))
        row.append(elements)
    list1.append(row)
print("List Created",list1)
print("list=[ ")
for a in range(r):
    print("\t[",end="")
    for b in range(c):
        print(list1[a][b],end="")
    print("]")
print("\t]")
