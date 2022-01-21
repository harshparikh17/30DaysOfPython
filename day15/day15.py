#Task1
print("Task1")
def typ(a):
    
    return type(a)

c=int(input("Enter any number:"))
print(typ(c))

#Task2
print("Task2")
def sqr(a):
    return (a**2)
sq=int(input("Enter number you want to square:"))
print("square of a numbe is :",sqr(sq))
#Task3
print("Task3")
def mul(a,i):
    if(i>10):
        return
    print(f"{a}*{i}={a*i}")
    return mul(a,i+1)
m=int(input("Enter the number you want table"))
mul(m,1)