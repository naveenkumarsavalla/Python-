#Append
list=["Naveen",1,True]
print(list)

lst:list=[]
lst.append("Naveen")
print(lst)

#Insert
a=["Naveen","Chanty","Ananth"]
a.insert(1,"Srikanth")
print(a)

#Count
a=["Naveen","Chanty","Ananth"]
print(a.count("Chanty"))
print(a.count("Srikanth"))

b=["Naveen","Chanty","Ananth"]
if(b.count("Srikanth")>0):
   print(b.index("Srikanth"))

#Update
a=["Naveen","Chanty","Ananth","Naveen"]
a[3]=("Naveen Kumar")
print(a)

#Extend
a=["Naveen","Chanty","Ananth"]
a1=["Srikanth","Gopi","Narendra"]
a.extend(a1)
print(a)
print(a1)

#Delete
#1)Remove
b=["Naveen","Chanty","Ananth"]
b.remove("Ananth")
print(b)

#2)Pop with index
a=["Naveen","Chanty","Ananth"]
a.pop(1)
print(a)

#3)Pop without index
a=["Naveen","Chanty","Ananth"]
a.pop()
print(a)
