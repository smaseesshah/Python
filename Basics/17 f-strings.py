# String Formating 
# Before python 3.6
name = "Asees"
profession = "Student"
pi = 3.141523431
intro = "Hey! My Name is {0} And I am a {1} And Value of pi is {2:.2f}"
print(intro.format(name,profession,pi))

# After puthon 3.6
intro = f"Hey! My Name is {name} And I am a {profession} And Value of pi is {pi:.2f}"
print(intro)