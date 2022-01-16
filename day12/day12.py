#Task1
print("Task1")
tup=(1,2,3,4,5,6)
for i in range(len(tup)):
    print(tup[i],end=" ")
#Task2
print("Task2")
tup=[(1,2),(1,11),(1,0),(1,33)]
print("Orignal tuple:",tup)
tup.sort(key = lambda x: x[1]) 
print("Sorted  tuple:",tup)
#Task3
print("Task3")
x,y,*z=(1,2,"Three","Four","Five")
print(x)
print(y)
print(z)