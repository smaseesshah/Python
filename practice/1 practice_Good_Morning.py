import time
print("----------------------Current Time is",time.strftime("%H:%M:%S"),"----------------------")
if (int(time.strftime("%H"))<12):
    print("--------------------------Good Morning!--------------------------")
elif (int(time.strftime("%H"))<18):
    print("--------------------------Good AfterNoon!------------------------")
else:
    print("--------------------------Good Evening---------------------------")
