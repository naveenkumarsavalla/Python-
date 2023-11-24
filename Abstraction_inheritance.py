#Abstraction with function
class Employee:
    __firstName:str="Naveen"
    __lastName:str="Kumar"
    def fullName(self):
        return self.__nameFormat(self.__firstName,self.__lastName)
    def __nameFormat(self,fName:str,lName:str):
        return f"{fName}{lName}"
emp=Employee()
emp.__firstName="ABC"
print(emp.fullName())z
print(emp.__nameFormat("Naveen","Kumar"))


#Single level Inheritance

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
emp=Employee()
emp.setName(fName="Naveen",sName="S",lName="Kumar")
emp.addAddress("Kothagudem")
print(emp.getFullName())
print(emp.getAddress())


