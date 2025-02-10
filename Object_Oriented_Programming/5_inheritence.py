# parent class
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"The Person name is {self.name} and is {self.age} years old")
class Student:
    def __init__(self,name,age,roll_no,gpa):
        self.roll_no=roll_no
        self.gpa=gpa
        Person.__init__(self,name,age)
    def student_info(self):
        Person.info(self)
        print(f"Roll Of Student is {self.roll_no} And GPA = {self.gpa}")
s1 = Student("Syed Muhammad Asees Shah",20,149,3.98)
s1.student_info()