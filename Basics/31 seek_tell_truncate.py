with open ('30 file handling.txt','r') as file:
# Seek()
    file.seek(5) # specify the starting index
    print(file.read(10)) # it will print next 10 indexes after seek
# Tell()
    print(file.tell()) # prints current seeked position

# Truncate()
with open ('31 truncate.txt','w+') as file:
    file.write("Syed Muhammad Asees Shah")
    file.truncate(19) # will reduce text size to 15
with open('31 truncate.txt','r') as file:
    print(file.read())
