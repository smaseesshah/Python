def factorial(n:int)->int:
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
def combination(n:int,r:int)->int:
    while True:
        if r>n:
            input("r should be less than n : ")
            if r<=n:
                break
    return factorial(n)/(factorial(r)*factorial(n-r))
def permutation(n:int,r:int)->int:
    while True:
        if r>n:
            input("r should be less than n : ")
            if r<=n:
                break
    return factorial(n)/(factorial(n-r))

while True:
    x = input("\nSelect The Option 1/2/3/4 :\n1) To Find Factorial \n2) To Find Permutation \n3) To Find Combination \n4) To Exit\n> ")
    if x=="1" or x=="2" or x=="3" or x=="4":
        x = int(x)
        if x==1:
            n = int(input("Enter Value To Find Factorial : "))
            print(f"The Factorial Of {n} is",factorial(n))
        elif x==1:
            n = int(input("Enter Value Of 'n' : "))
            r = int(input("Enter Value Of 'r' : "))
            print(f"The Permutation Of {n} and {r} is",permutation(n,r))
        elif x==1:
            n = int(input("Enter Value Of 'n' : "))
            r = int(input("Enter Value Of 'r' : "))
            print(f"The Combination Of {n} and {r} is",combination(n,r))
        else:
            print("GOOD BYEEEEEE!")
            break   
    else:
        print("Invalid Input!\nPress 1/2/3 or 4 only !")
        continue


        