# Explicit Type Casting

a="Asees"
b="12"
c=1.22
d='A'
e=(("a",1),("b",2))
f=97

print(int(b))#stirng to int
print(int(c))#float to int
print("\n")
print(float(f))#int to float
print(str(f))#int to string
print("\n")
print(tuple(a))#string to tuple
print(set(a))#string to set
print(list(a))#string to list
print("\n")
print(dict(e))#tuple to dictionary
print("\n")
print(chr(f))#ascii to character
print(ord(d))#character to ascii
print("\n")
print(hex(f))#int to hex string
print(oct(f))#int to oct string