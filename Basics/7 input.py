# input in python (by default String)
name = input("Enter Your Name : ")

# For all other (except string) input we will typecast it
# integer input
age = int(input("Enter Your Age : "))

# Float input
temp = float(input("Enter The Current Temperature in Your Area : "))

# List input
li = list(input("Enter a List : "))

# Tuple input
tup = tuple(input("Enter a Tuple : "))

# Dict will be study later

#output
print("Your Name is",name)
print("You are",age,"years old")
print("The Current Temperature in Your Area is",temp,"celcius")
print("List : ",li)
print("Tuple : ",tup)