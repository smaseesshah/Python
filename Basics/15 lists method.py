List1 = [1,2,3,4,5,6,7]
List2 = ["Asees","Shah","Programmer","Ethical Hacker"]
List3 = []
str1 = "This is Syed Muhammmad ASees shah"

# List Methods

# 1) append() Method
print(f"List Before Append : {List1}")
List1.append(8) #it will add 8 to the last of the list1 
print(f"List After Appending Element {List1[len(List1)-1]} : {List1}")
#also by for loop we can intitialize a complete list by our own 
n = int(input("Enter The Number Of Elements You Want To Add To List : "))
for i in range(0,n):
    e = (input(f"Enter The Element-{i+1} : "))
    if e.isdigit():
        List3.append(int(e))
    else:
        List3.append(e)
print(f"New List : {List3}")

# 2) insert() Method use to insert element in a list at a specific index
print(f"Before inserting Element in List : {List2}")
List2.insert(2,"Student Of Computer Science")
print(f"After Adding at index 2 List : {List2}")

# 3) extend() Method
List4 = [9,10,11]
List1.extend(List4)
print(f"After Extending List with {List4} : {List1}")

# 4) reverse() Method
List2.reverse()
print(f"after reversing the list : {List2}")

# 5) sort() Method
List2.sort()
print(f"After Ascending List : {List2}")
List2.sort(reverse=True)
print(f"After Descending List : {List2}")

# 6) copy() Method
List5 = List4.copy()
print(f"After Copying {List4} To New List : {List5}")
List5.extend([12,13])
print(f"Changing List {List5} will Not Change {List4}")

# 7) remove() Method
print(f"Before Removing 1 From {List1}")
List1.remove(1)
print(f"After Removing 1 From {List1}")

# 8) pop() Method
print(f"Before Removing index 5 element From {List1}")
List1.pop(5)
print(f"After Removing index 5 element From {List1}")

# 9) List Concatenation
List6 = List1+List2+List3+List4+List5
print(f"After Adding All The List Together : {List6}")
List7 = List4*3
print(f"After Multiplying List {List4} By 3 : {List7}")