#Task1
print("Task1")
a=int(input("Enter number:"))
if(a%2==0):
    print("Number is divisible by 2")
else:
    print("Number is not divisible by 2")
    
#Task2
print("Task2")
a=int(input("Enter your percentage"))
if(a>90):
    print("Grade::A")
elif(a>80 and a<=90):
    print("Grade::B")
elif(a>=60 and a<=80):
    print("Grade::C")
elif(a>=50 and a<60):
    print("Grade::D")
elif(a>=33 and a<50):
    print("Grade::E")
else:
    print("You are Fail!!!")
