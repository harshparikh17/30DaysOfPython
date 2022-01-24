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