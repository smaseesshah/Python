# practice on for loops

#Count Vowels in a String
st=input("Enter String to count how many vowels are there : ")
st=st.lower()
count = 0
for ch in st:
    if (ch=='a' or ch=='e' or ch=='i' or ch =='o' or ch=='u'):
        count = count + 1
print("Total Number Of Vowels are",count)

#Reverse a List
li=st.split(" ")
print(li)
for i in range(len(li)-1,-1,-1):
    print(li[i],end=" ")
