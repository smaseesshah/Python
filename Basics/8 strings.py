# Strings Syntax

str1 = 'Syed'#single cots
str2 = "Muhammad"#double cots
str3 = '''Asees Shah'''#Triple Cots(aslo for multi line)
str4 = """Syed
Muhammmad
Asees
Shah"""#Double triple cots
print(str1,str2,str3)
print(str4)
# print("This is \"Syed Muhammad Asees Shah\"")
# instead of the above we can use the following
print('This is "Syed Muhammad Asees Shah"')

# string length

print("The length of My Name is",len(str4),"Characters")

# String indeces

#positive indexes
print(str4[0])#print first character
print(str4[len(str4)-1])#print last character
#negative indexes
print(str4[-1])#print last character (i.e length-1)
print(str4[-25])#print first character (i.e length-17)
#print all by for loop
for character in str3:
    print(character,end="\t")
print("\n")

# String Slicing string[start:end:stepS](we will specify the end index as the index+1 to print before it)

print(str3[0:5])#from 0 index to 5-1 index
print(str4[5:20:2])#from 5 index upto 20-1 index but incrementing 2 characters at a time
print(str1[-4:len(str1)])#negative slicing



