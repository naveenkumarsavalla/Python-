n=int(input("Enter the no of Rows:"))
for i in range (1,n+1):
    print(" "* (n-i),end="")
    print("* "*i)

n=int(input("Enter the no of Rows:"))
for i in range(1,n+1):
    print(""*(n-1),end="")
    print("* "*i)

n=int(input("Enter the no of Rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*i)

n=int(input("Enter the no of Rows:"))
x=0
for i in range(0,n):
    for j in range(0,x):
        print(" ",end="")
    x=x+1
    for k in range (0,n):
        print(" * ",end="")
    n=n-1
    print("\r")

n=int(input("Enter the no of Rows:"))
a=1
end=2
for k in range(n):
    for l in range(1,end):
        print(a,end="")
        a=a+1
    print("")
    end=end+1

