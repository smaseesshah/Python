# print 1 to 20 with step 2
x = int(input("input start number > "))
y = int(input("input end number > "))
if y<=x:
    while True:
        y = int(input("the end number must be greater than start input again > "))
        if y>x:
            break
        else:
            continue
z = int(input("input step of iteration > "))
for i in range(x,y+1,z):
    print(i,end=" ")

# febonocii series
j=0
k=1
print("\nFebonocii Sequence : ",end="")
for i in range(10):
    n=j+k
    j=k
    k=n
    print(k,end=" ")

# list
l = ["\nAsees",149,20]
for item in l:
    print(item)

# string
s = "Happy COding"
for character in s:
    print(character,end=" ")

