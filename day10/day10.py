#Task1
print("Task1")
m=int(input("Enter the number upto u want table")) 

for i in range(1,m+1):
    
    for j in range(1,11):
        c=i*j
        print(c,end="  ")
    print("\n") 
#Task2
print("Task2")
rows = 5
columns = 3

print("Rectangle Star Pattern")

for i in range (rows):
    j = 0
    while(j < columns):
        print('*', end = '  ')
        j = j + 1
    i = i + 1
    print("")