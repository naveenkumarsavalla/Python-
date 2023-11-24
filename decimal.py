#1.Integer
#implicit
num=10
print(num)
print(type(num))

#explicit
num=str(10)
print(num)
print(type(num))

#Data type/Annotation
num:int=10
print(num)
print(type(num))

#2.Float
#Implicit
num=10.10
print(num)
print(type(num))
#Explicit
num=10.10
print(num)
print(type(num))
#Data type/Annotation
num=10.10
print(num)
print(type(num))

#3.Exponential number
#Implicit
num=float(8768546267653456832476326876)
print(num)
print(type(num))
#Ex:2
num=1.2e2
print(num)
print(type(num))
#Ex:3
num=1.4e5
print(num)
print(type(num))
#Ex:4
num=1.8e12
print(num)
print(type(num))
#Ex:5
num=5.8e6
print(num)
print(type(num))

#Complex Numbers
#Implicit
a=1+2j
b=3+4j
print(a+b)
print(type(a+b))
print(a.real)
print(b.imag)
#Explicit
a=complex(1)
print(a)
#Data type/Annotation
a:complex=1
print(a)

#binery to int
#implicit
a=0b101010
print(a)
print(type(a))
#explicit
a=bin(0b101010101)
print(a)
print(type(a))
#data type/annotation
a:bin=0b101010101
print(a)
print(type(a))

#int to binery
#implicit
a=36
print(a)
print(type(a))
#explicit
a=bin(76)
print(a)
print(type(a))
#data type/annotation
a:bin=(36)
print(a)
print(type(a))

#binary to float
#implicit
a=0b10101010
print(a)
print(type(a))
#explicit
a=float(0b1010101)
print(a)
print(type(a))
#data type/annotation
a:float=0b10101010
print(a)
print(type(a))

#float to binery
a=98.30
print(a)
print(type(a))
#implicit
a=bin(56)
print(a)
print(type(a))
#data type/annotation
a:bin=56.3
print(a)
print(type(a))


