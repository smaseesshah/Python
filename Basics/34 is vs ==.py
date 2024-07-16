# is vs == operator if operands = constant(immutable) and value same then location also same
a = 5
b = 5
print(a is b)
print(a == b)

# if operands are mutable then location is diiferent so in this condition the 'is' will always false
a = [1,2,3]
b = [1,2,3]
print(a is b)
print(a == b) # will true bcx values are same