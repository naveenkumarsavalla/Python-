"""
swap num formula
a = a+b
b = a-b
a = a-b
"""
a=1
b=2
a=a+b
a=a-b
print(a,b)

#Ex:-

a=2
b=4
a=a*b
a=a/b
print(a,b)

a=2
b=4
a=a*b
a=a+b
print(a,b)

a=2
b=4
a=a-b
a=a*b
print(a,b)

a=2
b=4
a=a/b
a=a*b
print(a,b)

#swap temp variables

a=1
b=2
temp=a
a=b
b=temp
temp=a
print(a,b)

#Fibanoic series
"""
a=a+b
b=a-b
print(a,b)
"""
a=10
d=4
b=0
c=1
while c<=5:
    print(b)
    d=d+b
    b=d-b
    c+=1

#Ex:-

a=12
b=15
c=16
while b<=16:
    print(c)
    a=a+b
    b=a-c
    c+=1
