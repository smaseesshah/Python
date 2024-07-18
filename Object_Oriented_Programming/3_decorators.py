# decorator function
def greet(func):
    def wrapped(*args):
        print("Welcome To Coding World!")
        return func(args)
    return wrapped

@greet # @ use to link the function to decorator
def sum_fun(*numbers):
    return sum(*numbers)

print(sum_fun(1,2,3,6,2,3,8,4,32,))
