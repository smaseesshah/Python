i = (input("Enter A Number or enter Quit : ")).lower()
if (i.isnumeric() or i=="quit"):
    if i.isnumeric():
        i=int(i)
        print("You entered-",i)
    else:
        print("Quiting")
else:    
    raise ValueError("You Enter Wrong!")
