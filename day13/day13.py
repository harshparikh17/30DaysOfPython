#Task1
print("Task1")
keys = ["Hey", "Welcome", "Harsh"]
values = [1, 4, 5]

print ("Key list is : ",keys)
print ("Value list is : ",values)

res = dict(zip(keys,values))

print ("Dictionary is : " ,res)

#Task2
print("Task2")
dict1 = {'a': 1, 'b':2}
dict2 = {'d':3, 'c':4}
dict3={**dict1,**dict2}
print("Merged dictionary is:",dict3)
#Task3
print("Task3")
set1 = {10, 20, 30}
set2 = {20, 40, 50}

set1.difference_update(set2)
print(set1)