#Task1
print("Task1")
p=int(input("Enter principle amount: "))
r=float(input("Enter intrest rate: "))
t=float(input("Enter time in years:"))
ci=p*(pow((1+r/100),t))
print(f"Compound Intrest is: {ci}")
#Task2
print("Task2")
m=float(input("Enter marks of Mathematics:"))
p=float(input("Enter marks of Physics:"))
c=float(input("Enter marks of Chemistry:"))
com=float(input("Enter marks of Computer Science:"))
e=float(input("Enter marks of English:"))
per=float((m+p+c+com+e)/5)
print(f"Your Percentage = {per}")
#Task3
print("Task3")
a="Harsh Parikh"
print(f"Frist letter of string {a} is {a[0]}")
print(f"Middle letter of string {a} is {a[6]}")
print(f"Last letter of string {a} is {a[-1]}")