#Polimorphism
#1)Method Overloading
class calculation:
    def add(self,a:int,b:int,c:int=0):
        print(a+b+c)
cal=calculation()
cal.add(12,34,56)
cal.add(643,24,55)

# 2)Method Overriding
class Employee:
    __amt = 50000
    def sal(self):
        return self.__amt*12
class ContractEmployee(Employee):
    __hrpay=2000
    __hrs=20
    def sal(self):
        return self.__hrpay*self.__hrs
emp=ContractEmployee()
emp=Employee()
# print(emp.sal())
print(emp.sal())

# Constractor
# 1)Default Constractor
class Employee:
    def fullName(self,fName,lName):
        print(fName+lName)
emp=Employee()
emp.fullName("Naveen","Kumar")

# 2)Parameterless Constructor
class Employee:
    def __init__(self):
        pass
    def fullName(self,fName,lName):
        print(fName,lName)
emp=Employee()
emp.fullName("Naveen","Kumar")

#3)Parameterized Constructor
class Employee:
    __fname:str=""
    __lname:str=""
    def __init__(self,fName,lName):
        self.__fname=fName
        self.__lname=lName
    def fullName(self):
        print(self.__fname+" "+self.__lname)
emp=Employee("Naveen","Kumar")
emp.fullName()
