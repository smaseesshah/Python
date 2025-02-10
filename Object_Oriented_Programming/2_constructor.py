# Constructor
class Mobile:
    # for constructor we use __init__ method
    # default Constructor
    # def __init__(self):
    #     pass
    # parameterized constructor (Python Does Not Support Method Overloading)
    def __init__(self,brand_name,mobile_model):
        self.brand_name=brand_name
        self.mobile_model=mobile_model
    def mobile_info(self):
        print(f"This Mobile Brand is '{self.brand_name}' And Model is '{self.mobile_model}'")

mbl1 = Mobile("Xiaomi Redmi","Note 12")
mbl2 = Mobile("Iphone","X")
mbl1.mobile_info()
mbl2.mobile_info()