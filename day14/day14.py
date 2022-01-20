print("1-Enter command Name for  name")
print("2-Enter command Contact for  contact")
print("3-Enter command Email for email")
print("4-Enter command Addres for addres")
print("5-Enter command calc for calculator")
print("6-Enter command grd for calculating your grade")
print("7-Enter command exit for closing the bot")
for i in range(1000000):
     bot=input("Enter your commnad:")
     if(bot=="Name"):
         name=input("Enter your name:")
         print("Hey",name)    
     elif(bot=="Contact"):
         cont=input("Enter your contact number:")
         print("Your number is saved")
     elif(bot=="Email"):
         email=input("Enter your email-id:")
         print("Your email-id is saved ")
     elif(bot=="Addres"):
         ls=[]
         addr=input("Enter your addres:")
         addres=ls.append(addr)
         print("Your addres is saved")
     elif(bot=="calc"):
         a=int(input("Enter number 1:"))
         b=int(input("Enter number 2:"))
         print(f"Addition of {a} and {b} is : {a+b}")
         print(f"Subtraction of {a} and {b} is : {a-b}")
         print(f"Multiplication of {a} and {b} is {a*b}")
         print(f"Division of {a} and {b} is : {a/b}")
     elif(bot=="grd"):
         l=[]
         p=float(input("Enter marks of Physics:"))
         l.append(p)
         c=float(input("Enter marks of Chemistry:"))
         l.append(c)
         m=float(input("Enter marks of Maths:"))
         l.append(m)
         eng=float(input("Enter marks of English:"))
         l.append(eng)
         com=float(input("Enter marks of Computer:"))
         l.append(com)
         
         total=0
         for j in l:
             total+=j
         print(f"Total marks is: {total}")
         per=total/len(l)
         print(f"Your percentage is {per}")
    
        
     elif(bot=="exit"):
         break        
        
    