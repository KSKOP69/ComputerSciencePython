""" 2D List """

list1=[[1,2],[6,7],[10,5]]


# Create 2D List
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
