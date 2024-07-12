a = 100
b = 200
print("a is greater") if a>b else print("a=b") if a==b else print("b is greater")

c=a+b if (a%2==0 and b%2==0) else b-a
print(c)