class Student:
    def __init__(self,name,age,gpa):
        self.name=name
        self.age=age
        self.gpa=gpa
    @property
    def _name(self):
        return self.name
    @_name.setter
    def _name(self,name):
        self.name=name
    @_name.deleter
    def _name(self):
        self.name=None
    @property
    def _age(self):
        return self.age
    @_age.setter
    def _age(self,age):
        self.age=age
    @_age.deleter
    def _age(self):
        self.age=None
    @property
    def _gpa(self):
        return self.gpa
    @_gpa.setter
    def _gpa(self,gpa):
        self.gpa=gpa
    @_gpa.deleter
    def _gpa(self):
        self.gpa=None
# object creation and constructor calling
s = Student("Syed Muhammad Asees Shah",20,3.98)
# Getter Function calling
print(f"{s._name} is {s._age} years old and has GPA is {s._gpa}")
# Setter Function calling
s._name = "Shahab Ahmad"
s._age = 20
s._gpa = 4.00
print("After Changing through setters functions")
print(f"{s._name} is {s._age} years old and has GPA is {s._gpa}")
# Deleter Function calling
del s._name
del s._age
del s._gpa
print("After Deleting through deleters functions")
print(f"{s._name} is {s._age} years old and has GPA is {s._gpa}")