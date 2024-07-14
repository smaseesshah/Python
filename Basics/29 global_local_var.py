x = 5 # global variable

def fun1():
    y = 8
    x = 10 # will create new variable and didnot modify the global
    print(f"Local y = {y}, Local x = {x}")
fun1()
print(f"Global x = {x}")
# print(y) # gives error

def fun2():
    global x # now we are using global x 
    x = 7
    print(f"Global x modified inside function is {x}")
fun2()
print(f"GLobal x after modification in function is {x}")
