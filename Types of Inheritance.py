#Multi-level/Hierarchal Inheritance
class Address:
    __Address:str=""
    def addAddress (self,address):
        self.__address=address
    def getAddress(self):
            return self.__address
class Employee (Address):
            __firstName:str=""
            __lastName:str=""
            __surName:str=""
            def setName (self,fName:str,lName:str,sName:str=""):
                self.__firstName=fName
                self.__surName=sName
                self.__lastName=lName
            def __nameFormat (self):
                return f'{self.__firstName} {self.__lastName} {self.__surName}'
            def getFullName(self):
                return self.__nameFormat()
class permanentEmployee(Employee):
    __sal:int = 50000
    def salcal(self):
        return 12*self.__sal
class contractEmployee(Employee):
    __hr_pay:int =4000
    def salcal(self, hrs:int):
        return f'salcal for {hrs} {self.__hr_pay*hrs}'

emp=permanentEmployee()
emp.setName(fName="Naveen",sName="S",lName="Kumar")
emp.addAddress("Kothagudem")
print(emp.getFullName())
print(emp.getAddress())
print(emp.salcal())

emp=contractEmployee()
emp.setName(fName="Naveen",sName="S",lName="Kumar")
emp.addAddress("Kothagudem")
print(emp.getFullName())
print(emp.getAddress())
print(emp.salcal(20))

#Multiple inheritance
class ClassB:
    def printData(self):
        print("Naveen")
class ClassC:
    def printData(self):
        print("Kumar")
class ClassA(ClassB,ClassC):
    pass
a=ClassA()
a.printData()

#Hybrid Inheritance
class ClassA:
    def printData(self):
        print("Kumar")
class ClassB(ClassA):
    def printData(self):
        print("Naveen S")
class ClassC(ClassA):
    def printData(self):
        print("12")
class ClassD(ClassB,ClassC):
    pass
a=ClassD()
a.printData()
