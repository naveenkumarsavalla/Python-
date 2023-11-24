#pyremid pattern
n=int(input("Enter The Number of rows: "))
for i in range(1,n+1):
	print("*"*i)

#num pattern
n=int(input ("enter the number of rows: "))
for i in range (1, n+1):
    for j in range (1, i+1):
        print(i,end="")
    print()

#star pattern
n=int(input ("enter the number of rows: "))
for i in range (1, n+1):
    print(" " * (n-i),end="")
    print(" * " * i)
