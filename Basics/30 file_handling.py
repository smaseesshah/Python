import os
# FILE HANDLING

# creating a file
if not os.path.exists('30 file handling.txt'):
    file = open('30 file handling.txt','x')
    file.close()

# writing a file (it deletes all the data present in it)
file = open('30 file handling.txt','w') # it also creates a file if not exist
file.write("This is Syed Muhammad Asees Shah\n")
# also we can write several lines in it like;
list_ = ['student\n','university of peshawar\n']
file.writelines(list_)
file.close()

# appending to a file (it append other lines to end of the existing)
file = open('30 file handling.txt','a')
file.writelines(['We append\n','another\n','also another\n'])
file.close()

# reading a file (it gives error if file not exist)
file = open('30 file handling.txt','r')
print(file.read()) # it print the overall contents in file
file.close()
file = open('30 file handling.txt','r')
list__ =file.readlines() # it print a list of each line in file (also can use for loop)
print(list__)
file.close()

# with keyword (we can use the with statement to handle file without closing it)
with open ('30 file handling.txt','r') as file:
    for line in file.readlines():
        print(line.strip())
