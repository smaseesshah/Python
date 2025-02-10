# in python there are no such access specifiers but we use our own
class A:
    def __init__(self,name,age,profession):
        self.__name=name # __private
        self._age=age # _protected
        self.profession=profession # default public
    def display(self):
        print(f"{self.__name}\n{self._age}\n{self.profession}")
class B(A):
    def protected_display(self):
        # print(self.__name) #can't display
        print(self._A__name) #will display
        print(self._age) #can display
obj = A("Asees",20,"Student")
print(obj.__dir__()) #prints all the data members and methods for the object
obj.display()
# print(obj.__name) #cannot access 
print(obj._A__name) # can be accessed with the name of class also for protected

objb = B("Asees",20,"Student")
objb.protected_display()