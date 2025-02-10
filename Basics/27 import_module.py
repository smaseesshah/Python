# import module
import math
print(math.pi) #to access its functions+variables use '.' operator

# as keyword
import math as m # this import math as a name m(we will use m instead of math)
print(m.sqrt(25))

# from keyword (to import specific functions
from math import factorial
print(factorial(7))

# * keyword (TO import all to your current namespace)
from random import *
print(randint(1,10)) # a function from random module to generate a random number

# importing local modules
import functions_for_import as f
f.greet("Asees")