# list is like an array 
List = [1,2,3,4,5,6,7,8,9]
# unlike c++ it contain any type of data
List2 = ["mango",1,"banana",2,"apple",3]

# TO access
print(list[0])
print(list[1])
print(list[2])
print(list[3])

# Also By For Loop
for e in List2:
    print(e)#it will start from index 0 upto index length-1 of list

# To print elements of list in range
print(List[1:8:2])  #start from index 1 upto 8-1 and jump 2 elements
for i in range(0,len(List),1):  #range(start:stop+1:step)
    print(List[i])

# To check an object is present in list or not
if "mango" in List2:
    print(True)
else:
    print(False)
if "asees" in List:
    print(True)
else:
    print(False)

# Multi Dimensional List
List3 = [[1,"Asees",2],[3,"Syed",4,"ended"]] # 2D

# TO access
print(List3[0][0]) # 1st element
print(List3[0][1]) # 2nd element
print(List3[1][1])
print(List3[1][2])

# Also by for loop
for item in List3:
    print(item)   #it will print the rows not the item inside items
    for i in item:
        print(i) # it will print all elements inside

# List Comprehension
List4 = [i**2 for i in List]
print(List4)
List5 = [i for i in range(0,11) if i%2!=0]  #odd list upto 10
print(List5)
List6 = [i for i in range(0,11) if i%2==0]  #even list upto 10
print(List6)

# list input
n = int(input("Enter Size Of List : "))
List7 = []

