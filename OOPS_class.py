#OPPS class append
class Employee:
    firstName:str="Naveen"
    lastName:str="Kumar"
    def fullName(self):
        return self.firstName+" "+self.lastName
emp = Employee()
print(emp.fullName())

#Ex:-1
class Employee:
    firstName:str="Naveen"
    lastName:str="Kumar"
    EmployeeID:str="ID:157212043"
    def fullName(self):
        return self.firstName+" "+self.lastName+" "+self.EmployeeID
emp = Employee ()
print(emp.fullName())


#OOPS FIBseries in class
class fibseries:
    def fibEx(self):
        n=10
        a=2
        b=3
        i=1
        lst=[]
        while i<=n:
            lst.append(b)
            a=a+b
            b=a-b
            i+=1
            print(lst)
fib = fibseries()
fib.fibEx()
