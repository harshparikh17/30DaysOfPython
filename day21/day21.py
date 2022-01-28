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



#Task1
print("Task1")
f=open("new.txt","a")
a=input("Enter your name \n")
b=input("Enter your email\n")
c=input("Enter your contact\n")
f.write(f"Name={a} \n")
f.write(f"Email={b} \n")
f.write(f"Contact={c} \n")
f.close()
#Task2

f=open("new.txt","r")
print(f.read())
f.close()
#Task3
f=open("new.txt","a")
a=input("Enter your name \n")
b=input("Enter your email\n")
c=input("Enter your contact\n")
f.write(f"Name={a} \n")
f.write(f"Email={b} \n")
f.write(f"Contact={c} \n")
a=input("Enter your name \n")
b=input("Enter your email\n")
c=input("Enter your contact\n")
f.write(f"Name={a} \n")
f.write(f"Email={b} \n")
f.write(f"Contact={c} \n")
f.close()
f=open("new.txt","r")
print(f.read())
f.close()



#Task1
import json
 

a={
    "Name": "Harsh Parikh",
    "Contact" : "1234567890",
    "Email": "harsh@gmail.com"
}
with open("sample.json","w") as p:
    json.dump(a,p)
a_dictionary = {"d": 4}

with open("sample.json", "r+") as file:
    data = json.load(file)
    data.update(a_dictionary)
    file.seek(0)
    json.dump(data, file)
    
    
    
#Task1
from datetime import datetime
tm=datetime.now()
print(tm)
#Task2
import os
print(os.name)
os.mkdir("d:\\newdir")  
print(os.getcwd()) 
os.rmdir("d:\\newdir") 
#Task3
import random
import string
characters = string.ascii_letters + string.digits 
password = ''.join(random.choice(characters) for i in range(8))
print("Random password is:", password)