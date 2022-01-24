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