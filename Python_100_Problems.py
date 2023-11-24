#1.arthematic calaculations
a = int(input("enter a value :"))
b = int(input("enter a value :"))
sources = input("calculation_type")
if sources == "+":
    a + b
    print(a + b)
elif sources == "-":
    print(a - b)

elif sources == "*":
    print(a * b)

elif sources == "/":
    print(a / b)

elif sources == "//":
    print(a // b)
