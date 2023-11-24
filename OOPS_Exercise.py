"""
Principals
1)Encapsulation
2)Abstraction
3)Inheritance
4)Polymorphism
"""
class Oneplus:
    __Brand:str=""
    def __init__(self):
        pass
    def setBrand(self,Brand):
        self.Brand=Brand
    def getBrand(self):
        return self.Brand
Brand = Oneplus()
Brand.setBrand("Oneplus")
print(Brand.getBrand())

class Series:
    def __init__(self, Brand, Series, Price):
        self.__Brand = Brand
        self.__Series = Series
        self.__Price = Price
    def getFullDetails(self) -> str:
        return f'Full Details: {self.__Brand} {self.__Series} {self.__Price}'
    def setBrand(self, Brand):
        self.__Brand = Brand
    def getPrice(self) -> str:
        return self.__Price
class OnePlus(Series):
    def __init__(self, Brand, Series, Price):
        super().__init__(Brand, Series, Price)

    def Bprice(self) -> str:
        return f'Price: {self.getPrice()}'
Brd = OnePlus("OnePlus", 10, 49999)
name = Brd.getFullDetails()
print(name)
Brd.setBrand("OnePlus")
price = Brd.Bprice()
print(price)







