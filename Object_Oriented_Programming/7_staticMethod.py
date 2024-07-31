#static method example
class Add:
    @staticmethod
    def add(*args):
        return sum(args)
print(Add.add(1,3,4,56,2,3))
