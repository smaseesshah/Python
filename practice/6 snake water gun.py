from random import randint
while True:
    try:
        x = int(input("Enter:\n1 for SNAKE\n2 for WATER\n3 for GUN\n4 to CLOSE GAME\n>"))
    except:
        print("Invalid input!\nEnter Only 1/2/3 or 4\n")
        continue
    y = randint(1,3)
    match x:
        case 1:
            if y == 1:
                print("PLAYER = Snake & COMPUTER = Snake")
                print("YOU DRAW!\n")
                continue
            elif y == 2:
                print("PLAYER = Snake & COMPUTER = Water")
                print("YOU WIN!\n")
                continue
            else:
                print("PLAYER = Snake & COMPUTER = Gun")
                print("YOU LOSE!\n")
                continue
        case 2:
            if y == 1:
                print("PLAYER = Water & COMPUTER = Snake")
                print("YOU LOSE!\n")
                continue
            elif y == 2:
                print("PLAYER = Water & COMPUTER = Water")
                print("YOU DRAW!\n")
                continue
            else:
                print("PLAYER = Water & COMPUTER = Gun")
                print("YOU WIN!\n")
                continue
        case 3:
            if y == 1:
                print("PLAYER = GUN & COMPUTER = Snake")
                print("YOU WIN!\n")
                continue
            elif y == 2:
                print("PLAYER = GUN & COMPUTER = Water")
                print("YOU LOSE!\n")
                continue
            else:
                print("PLAYER = GUN & COMPUTER = Gun")
                print("YOU DRAW!\n")
                continue
        case _:
            break