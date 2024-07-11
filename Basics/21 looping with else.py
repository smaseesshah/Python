for i in range(0,5):
    print(i)
else: #will run after checking the last condition when it is not true
    print("Loop is ended")
while True:
    i=i+1
    if i==10:
        break 
    print(i)
else: #will not execute because of the loop is not ended it is breaked (loop is run but break at mid)
    print("Loop is ended")