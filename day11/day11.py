#Task1
print("Task1")
l=[1,2,3,4,5,6]
for i  in range(len(l)-1,-1,-1):
    print(i,end=" ")
#Task2
print("Task2")
la = [1,2,3]
lb = [4,5,6]
print("List 1=",la)
print("List2=",lb)
lc = [i + j for i, j in zip(la, lb)]
print("The concatenated lists: ",lc)
#Task3
print("Task3")
a=[]
b=int(input("enter how many values you want to add in list:"))
print(f"Enter {b} values")
for i in range(b):
    x=int(input())
    a.append(x)
print("List is :",a)
#Task4
print("Task4")
l=[1,2,3,4,5,6,7]
print("printing list using loop:")
for i in range(len(l)):
    print(l[i], end=" ")