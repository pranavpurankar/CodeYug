"""
Enumerate is the builtin function in the python and it can be accessed by 
using "enumerate" function. We can directly convert the data to the json
but best practices is to use the dictonary and then transfer it to json
"""
#Imported json module to convert data to json.
#Always follow good practices 

import json

#Create a list of the different sports

sport = ['cricket','kabbadi','tenni','basketball','badminton']

for pos, ele in enumerate(sport,start=2):
    print(f'{pos}:{ele}')
    print(type(pos))

# Conversion to the dictonary
print("\nConvert the enumerate list to dict")

cricketer = ['virat','hardik','kartik','arjun','sachin']

data=dict(list(enumerate(cricketer,1)))

print(f"Conversion in dictonary key value pair:\n{data}")

print("\nExample of data serialization: ")
'''
Now we have to transfer this data to the java application so we need to do
serialization.
'''
family = ['pranav','shreyash','prafull','archana']

data = dict(list(enumerate(family,start=1)))
f = open('data.json','w')
json.dump(data,f)

f.close()

#The json file is created in the working directory
f = open('data.json','r')
data1 = json.load(f)
print(data1,indent=4)
f.close()
