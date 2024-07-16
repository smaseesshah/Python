import math
listt = [4,2,5,8,6,3,7]

# MAP (apply a function to all of iterators and return it)
print(list(map(lambda x : math.factorial(x),listt))) # take factorial of listt and return it

# FILTER (filter items through a condition)
print(list(filter(lambda x : True if x%2==0 else False , listt))) # return only even numbers

# REDUCE (reduce item to one through function)
from functools import reduce
print(int(reduce(lambda x,y:x*y , listt)))
