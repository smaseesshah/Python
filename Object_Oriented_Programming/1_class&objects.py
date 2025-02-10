# Creating a class
class Person:
    # Data Members
    name = "Syed Muhammad Asees Shah"
    profession = "Student"
    # Member Functions
    def info(self): # self refers to this object
        print(f"{self.name} is a {self.profession}")

p1 = Person()
p1.info() # print default info

p2 = Person()
p2.name="Shahab"
p2.profession="Pharmacist"
p2.info() # info of person 2
