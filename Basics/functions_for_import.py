# Default Argument Function
def greet(name,greeting="Hello,"):# greeting is default default
    print(greeting,name)
if __name__=="__main__":
    print("This will run only in the current module")
    greet("Asees") 
    greet("Asees","Hi,")#also if we provide the 2nd argument it will replace the default 
print("Others will run in all module from\n '''")
# Keyword Argument Function
def person(name,age,profession):
    print(name,"is",age,"years old and is a",profession)
person(name="Asees",profession="Student",age=20)

# Required Argument Function
def calculate_area(length, width):
    return length * width #Also a value returning function
area = calculate_area(5, 3)#we should provide the arguments in order
print("Area of rectangle:",area)

# Variable Length Argument Function
def sum_num(*numbers):
    sum=0
    for num in numbers:
        sum=sum+num
    return sum
sum = sum_num(1,2,3,4,5,6,7,8,9)
print("TOtal =",sum)

# Type Hint Function
def double_num(num:int)->int:#will recieve int value and return int value
    return num+num
print("Double of 8 =",double_num(8),"\n'''")
