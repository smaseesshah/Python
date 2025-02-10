# LAMBDA FUNCTION 

# use as variable
square = lambda x : x*x
print(square(2))

# in function
def cube(lv,value):
    return lv(value)
print(cube(lambda x : x*x*x , 7))


