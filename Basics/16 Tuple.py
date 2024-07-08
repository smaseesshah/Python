# Tuple is like an immutable array
tup1 = (1,2,3,4,5,6,7,8,9)
# it contain any type of data
tup2 = ("mango",1,"banana",2,"apple",3)

# TO access
print(tup1[0])
print(tup1[1])
print(tup1[2])
print(tup1[3])

# Also By For Loop
for e in tup2:
    print(e)#it will start from index 0 upto index length-1 of tuple

# To print elements of tuple in range
print(tup1[1:8:2])  #start from index 1 upto 8-1 and jump 2 elements
for i in range(0,len(tup1),1):  #range(start:stop+1:step)
    print(tup1[i])

# To check an object is present in tuple or not
if "mango" in tup2:
    print(True)
else:
    print(False)
if "asees" in tup1:
    print(True)
else:
    print(False)

# Multi Dimensional tuple
tup3 = ((1,"Asees",2),(3,"Syed",4,"ended")) # 2D

# TO access
print(tup3[0][0]) # 1st element
print(tup3[0][1]) # 2nd element
print(tup3[1][1])
print(tup3[1][2])

# Also by for loop
for item in tup3:
    print(item)   #it will print the rows not the item inside items
    for i in item:
        print(i) # it will print all elements inside

# Tuple Concatenation
tup4 = tup1+tup2+tup3
print(f"After Concatenating all The Tuples : {tup4}")
tup5 = tup1*3
print(f"After Multiplying tuple {tup1} by 3 : {tup5}")