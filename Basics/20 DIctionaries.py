# Dictionaries in Python
dict1 = {1:"asees",2:"syed",3:"shah",4:["Python","C++","Linux"]}
dict2 = {} #empty dictionary
dict2["apple"] = "fruit"
dict2["toyota"] = "car company"
dict2["pencil"] = "object"
print(dict2)


# Accessing
# single values
print(dict1[1]) # By Key Name
print(dict1.get(2)) # Same but gives no error

# Multiple values
print(dict1.keys()) # To Print All Keys
print(dict1.values()) # TO Print ALl Values
for key in dict1.keys(): 
    print("Keys : ",key)
for value in dict1.values():
    print("Values : ",value)
for key in dict1.keys():
    print(f"The value corresponding with key {key} is {dict1[key]}")
print(dict1.items()) # To Print All Key Value Pairs as a tuple inside
for key,value in dict1.items():
    print(key,"->",value)

# Methods

# 1) Update
dict2.update(dict1) # add all items in dict1 to dict2
print(dict2)

# 2) Clear
dict2.clear() #remove all items and remain only the empty dictionary
print(dict2)

# 3) Pop
dict1.pop(2) #remove the specified key
print(dict1)

# 4) Pop item
dict1.popitem() #delete the last key value
print(dict1)

# 5) del
del dict1[3] # remove a key value
print(dict1)
del dict1 # delete an entire dictionary
# print(dict1) #error giving

# 6) To input a dictionary
k = int(input("Enter How many keys do you want to add : "))
for i in range(0,k):
    key = input(f"Input key-{i+1} Name : ")
    value = input(f"Input Value of key-{key} : ")
    dict2[key]=value
print(dict2)

