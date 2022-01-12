#Task1
print("Task1")
print("Printing number from -10 to -1 using for loop:")
for i in range(-10,0):
    print(i,end=" ")
    i=i+1
#Task2
r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))
matrix = []
for i in range(r):		 
	m =[]
	for j in range(c):
		m.append(int(input()))
	matrix.append(m)
for i in range(r):
	for j in range(c):
		print(matrix[i][j], end = " ")
	print()

#Task3
print("Task2")
for i in range(0,5):
    print(chr(65+i)*(i+1))
    i=i+1