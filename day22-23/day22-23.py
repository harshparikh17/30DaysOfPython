def checkage(x):
    if(x<18):
        raise Exception("You are not allowed to vote")
try:
    age=int(input("Enter your age:"))
    checkage(age)
except:
    print("Age must be 18 or greater !!!")
    
            
#Task2
print("Enter two values")

try:
    a=int(input())
    b=int(input())
    c=a/b
    print("Division is:",c)
except ZeroDivisionError:
    print("Can't divide by zero!!!!")
    
except ValueError:
    print("Please Enter valid value")
except :
    print("Please check your program")
print("Program end")