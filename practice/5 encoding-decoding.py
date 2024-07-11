import random
def encode(text:str)->str:
    text_l=[]
    word_l=text.split()
    for word in word_l:
        if (len(word)<4):
            l=list(word)
            l.reverse()
            word=''.join(l)
            text_l.append(word)
        else:
            l=list(word)
            l.append(l[0])
            l.pop(0)
            for _ in range(3):
                l.insert(0, chr(random.randint(97, 122))) 
            l.reverse()
            for _ in range(3):
                l.insert(0, chr(random.randint(97, 122)))
            l.reverse()
            word="".join(l)
            text_l.append(word)
    print(text_l)
    text=" ".join(text_l)
    return text
def decode(text:str)->str:
    text_l=[]
    word_l=text.split()
    for word in word_l:
        if (len(word)<4):
            l=list(word)
            l.reverse()
            word=''.join(l)
            text_l.append(word)
        else:
            l=list(word)
            l.insert(3,l[-4])
            l=l[3:-4]
            word="".join(l)
            text_l.append(word)
    text=" ".join(text_l)
    return text

while True:
    n=input("\nEnter:\n1 To Encode A Text File : \n2 To Decode A Text File : \n3 To Quit\n>")
    if n=="1":    
        text=input("Enter Text To Encode : ")
        print("Encoded Text : ",encode(text))
    elif n=="2":
        text=input("Enter Text To Decode : ")
        print("Decoded Text : ",decode(text))
    elif n=="3":
        break
    else:
        print("Invalid Input !")

    