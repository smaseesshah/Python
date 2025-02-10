# Sets
superset=set()
set1 = {1,2,3,4,5,6,6,5}
set2 = {4,5,6,7,8,9}
set3 = {1,2,3}
set4 = {"asees","set",1,3,6}
set5 = set() # to define an empty set
superset.update(set1,set2,set3,set4,set5) # add all the sets to superset
print(superset)

# Sets Methods

# 1) Union
print(f"Union of set : {set1} and set : {set2}")
# print(set1.union(set2)) #1-9
set1.update(set2)     #To Save the union values in set 1
print(f"Set = {set1}")

# 2) Intersection
print(f"INtersection of set : {set1} and set : {set2}")
# print(set2.intersection(set1)) #4-9
set2.intersection_update(set1)    #To Save the Intersection values in set 1
print(f"Set = {set2}")

# 3) Symmetric Difference AUB - A intersection B
print(f"Symmetric Difference of set : {set1} and set : {set2}")
# print(set1.symmetric_difference(set2)) 
set1.symmetric_difference_update(set2) #To Save The Symmetric Differnce values in set1
print(f"Set = {set1}")

# 4) Difference (Present in A But Not in B) A-B
print(f"Difference of set : {set1} and set : {set2}")
# print(set1.difference(set2)) 
set1.difference_update(set2) #To Save The Differnce values in set1
print(f"Set = {set1}")

# 5) TO check disjoint
print(f"As set : {set1} is disjoint of set : {set2}")
print(set1.isdisjoint(set2))
print(f"As set : {set1} is disjoint of set : {set3}")
print(set1.isdisjoint(set3))

# 6) To check Super And Subset
print(f"As set : {superset} is superset of set : {set4}")
print(superset.issuperset(set4))
print(f"As set : {set1} is subset of set : {set4}")
print(set1.issubset(set3))

# 7) Add items to list
n = int(input("Enter How Many Items You Want To Add To Set : "))
for i in range(0,n):
    set3.add(input(f"Enter Item-{i+1} : "))
print(set3)

# 8) Update (Use To Add Items in Range)
new_set = set()
new_set.update(set1,set3)
print(new_set)

# 9) Remove/Discard
set4.remove("asees") #give error when the specified element is not available
set1.discard(6) # does not gives error
print(f"Set-4 = {set4}")
print(f"Set-1 = {set1}")

# 10) del/clear
del new_set # delete the set entirely
superset.clear() # remain an empty set
