#String_concatenation
#Operator over loading
x = "Naveen"
y = "Kumar"
print(x+ " " +y)

#f'string/interpolation
x="Naveen"
y="Kumar"
fullname=f"{x} {y}"
print(fullname)

#String name
x = "Naveen"
y = "Kumar"
lst = (x,y)
print(" ".join(lst))

#insert the "full name:"
#Operator over loading
x="Naveen"
y="Kumar"
print("Full name :", x + " " + y)

#f'string/interpolation
x="Naveen"
y="Kumar"
fullname=f"Full name : {x} {y}"
print(fullname)

#String name
x = "Naveen"
y = "Kumar"
lst = (x,y)
print("Full name :"," ".join(lst))

#string split/ slicin/ dividing/ partition
#1.Split
email="naveen@gmail.com"
print(email.split("@"))

#2.split lines
Address:str= """ H.no 5-484
    Narasimhapuram
    mulakalapally
    bhadradri kithagudem
    telangana
    pin 507316
    """
print(Address)

#3.Partation
email="n@naveen@gmail.com"
print(email.partition("@"))

#4.Rpartition
email="n@naveen@gmail.com"
print(email.rpartition("@"))
