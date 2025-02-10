# <!-- Problem: Word Frequency Counter

# Write a Python program that takes a paragraph of text as input from the user and performs the following tasks:

#     Word Tokenization: Split the paragraph into individual words. You can assume that words are separated by spaces and punctuation marks.

#     Word Frequency Calculation: Count the frequency of each word in the paragraph. Ignore the case sensitivity (treat 'Word' and 'word' as the same).

#     Display the Results: Print out each word along with its frequency in alphabetical order. -->
d_txt={}
txt = input("input text : ")
txt=txt.lower()
t_txt=txt.split()
l_txt=[]
for w in t_txt:
    if ((ord(w[-1]))>96 and (ord(w[len(w)-1]))<123):
        l_txt.append(w)
    else:
        w=w[0:-1]
        l_txt.append(w)
l_txt.sort(reverse=False)
for i in range(0,len(l_txt)):
    if l_txt[i] in d_txt.keys():
        continue
    else:
        c = l_txt.count(l_txt[i])
        # print({l_txt[i]:c})
        d_txt[l_txt[i]]=c
for key,value in d_txt.items():
    print(f"The Number Of Word \"{key}\" in The Given Text is '{value}'")

