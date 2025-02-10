n= int(input("""Enter which method you want to do with your string
                0)To upper case
                1)To lower case
                2)To remove all whitespaces from start and end
                3)Replace with word
                4)Split to list
                5)Capitalize
                6)Center
                7)Count
                8)Find a character
                9)To find as there is any other characters than alphanumericals
                10)To Find if there is any whitespaces present
                11)To Find if there is any other characters than whitespaces
                12)To make the string as title
                13)Swapcase
                Enter The Number of Method : """))
string = input("Enter The String : ")
# 0)upper
if (n==0):
    print(string.upper())
# 1)lower
elif (n==1):
    print(string.lower())
# 2)strip #remove character from start and end # also lstrip()and rstrip()
elif (n==2):
    print(string.strip(input("Enter The Character You Want To remove from start and end : ")))
# 3)replace
elif (n==3):
    print(string.replace(input("Enter character you want to replace in : "),input("Enter character you want to replace with : ")))
# 4)split #make a list
elif (n==4):
    print(string.split(input("Enter the character you want to split to a list : ")))
# 5)capitalize
elif (n==5):
    print(string.capitalize())
# 6)center
elif (n==6):
    print(string.center(int(input("Enter The Center index to be align : ")),input("Enter The Filling Character : ")))
# 7)count
elif (n==7):
    print(string.count(input("Enter The Characters You want to count : ")))
# 8)find
elif (n==8):
    print(string.find(input("Enter The Character You Want To find its index : ")))
# 9)isalnum
elif (n==9):
    print(string.isalnum())
# 10)isprintable
elif (n==10):
    print(string.isprintable())
# 11)isspace
elif (n==11):
    print(string.isspace())
# 12)title
elif (n==12):
    print(string.title())
# 13)swapcase
elif (n==13):
    print(string.swapcase())
else:
    print("invalid input")