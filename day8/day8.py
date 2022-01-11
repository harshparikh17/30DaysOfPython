#Task1
print("Task1")
print("Even number upto 100")
for i in range(101):
    print(i, end=" ")
    i=i+2
#Task2
print("Task2")
a=int(input("Enter a number:"))
rev=0
while(a>0):
    rem=a%10
    rev=(rev*10)+rem
    a=a//10
print("Reverse of number is:",rev)
#Task3
print("Task3")
for i in range(1,11):
    
    for j in range(1,11):
        print(i*j,end="  ")
    print("\n")