l = [1,2,3,4,5,6,7,8,9]
print(list(enumerate(l,1)))#as a tuple list
s = "asees"
print(list(enumerate(s,1)))#as a tuple string

for item in enumerate(s,1):#as a tuple
    print(item)

for index,value in enumerate(l,1):#as individual index+value
    print(f"Index-{index} value = {value}")