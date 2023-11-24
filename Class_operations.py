# Instance Method/Concreat method
class MathOperation:
    def __init__(self):
        pass

    def add(self,a:int,b:int):
        print(a+b)
m = MathOperation()
m.add(1,2)

#Static Method
class MathOperation:
    def __init__(self):
        pass

    def add(a:int,b:int):
        print(a+b)

MathOperation.add(1,2)

# Static  Variables/class variables
class MathOperation():
    a:int = 10

    def getval(self):
        return self.a

m=MathOperation()
m.a =20
print(id(m))
print(m.getval())

MathOperation.a=30
print(id(MathOperation))
print(m.getval())

m=MathOperation()
print(m.getval())





