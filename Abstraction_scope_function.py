#1,Global scope(public scope)
#Ex 1:-
class Student:
    firstName:str="Naveen"
    lastName:str="Kumar"
Stu=Student()
print(Stu.firstName)

#Ex:-2
class Student:
    firstName:str="Naveen"
    lastname:str="Kumar"
    roleNumber:int="R.NO:-14"
    def fullName(self):
        return self.firstName + " " +self.lastname+ " " +self.roleNumber
Stu=Student()
print(Stu.fullName())

#2,Parcially privaite(procted)
class Student:
    _firstName:str="Naveen"
    _lastName:str="Kumar"
emp=Student()
print(emp._firstName)

#3,Strictly private

# class Student:
#     firstName:str="Naveen"
#     lastName:str="Kumar"
# emp=Student()
# print(emp.__Student)

#Global variable
def fullName():
    global fName
    lname="Naveen"
    fName="Kumar"
fullName()
print(fName)

#Abstraction
class Student:
    __firstName:str="Naveen"
    __lastName:str="Kumar"
    def fullName(self):
         return self.__firstName+" "+self.__lastName
emp=Student()
emp._lastName="ABC"
print(emp.fullName())
