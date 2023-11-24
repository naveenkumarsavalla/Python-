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

#Palindrome
a = input("enter the value :")
reverse_a=a[::-1]
if a==reverse_a:
    print("value is palindrome")
else:
    print("value is not palindrome")
# print(reverse_a)

# Prime Number
a = int(input("enter the number :"))
if a < 2:
    print("number is not prime")
else:
    prime=True
    for i in range(2,int(a*0.5)+1):
        if a%2==0:
            prime=False
if prime:
    print("number is  the prime ")
else:
    print("number is not prime")

#Prime series
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_prime_series(n):
    prime_series = []
    for i in range(2, n + 1):
        if is_prime(i):
            prime_series.append(i)
    return prime_series

# Example: Print prime numbers up to 20
n = 20
result = print_prime_series(n)
print(f"Prime series up to {n}: {result}")

#Reverse string
original_string = "Naveen"
reverse_string = ''.join(reversed(original_string))
print(original_string)
print(reverse_string)

# Reverse Number
number = int(input("Enter a Number:"))
reverse_number = int(str(number)[::-1])
print("Reverse of the number",reverse_number)

# Check Alphabet
character = input("Enter a character:")

if character.isalpha():
    print(f"{character} is an alphabet.")
else:
    print(f"{character} is not an alphabet.")

# Count total characters in a string
str = input("Enter a string:")
total_characters = len(str)
print(f"Total characters in the string :{total_characters}")

# count Vowels in string
input_string=input("Enter a string:")
vowels = "aeiouAEIOU"
count=0
for char in input_string:
    if char in vowels:
        count+=1
print(f"Total vowelsin the string:{count}")

# Count constant in a string
input_string = input("Enter a string:")
vowels="aeiouAEIOU"
consonant_count = 0

for char in input_string:
    if char.isalpha() and char not in vowels:
        consonant_count +=1
print(f"Total consonant in the string: {consonant_count}")

#start practice
n = int(input("enter the number of rows: "))
for i in range(1, n+1):
    print("*"*i)

# Number Pattren
# n = int(input("Enter no of Rows:"))
# for i in range(1,n+1):

rows = 5
current_number = 1

for i in range(1, rows + 1):
    # Print spaces before the numbers
    for j in range(rows - i):
        print(" ", end=" ")

    # Print the numbers for the current row
    for k in range(1, i * 2):
        print(current_number, end=" ")
        current_number += 1

    print()
# Print Numbers by using while loop
numbers=[int(x) for x in input("Enter a list of numbers:").split()]
sum_of_numbers=0
index=0

while index < len(numbers):
    sum_of_numbers +=numbers[index]
    index +=1
print(f"Sum of numbers in the list:{sum_of_numbers}")

# Print Numbers by using for loop
numbers = [int(x) for x in input("Enter a list of numbers:").split()]
sum_of_numbers = 0

for num in numbers:
    sum_of_numbers +=num
print(f"sum of numbers in the list:{sum_of_numbers}")


n=int(input("Enter the number of rows:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()
    # With out Speace
n=int(input("Enter the number of Rows:"))
for i in range(n):
    for j in range (n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()

# Inverted Pyramed
n=int(input("Enter the Number of rows:"))
for i in range(0,n):
    for j in range(0,n-i):
        print("* ",end="")
    print()
# 2
n=int(input("Enter the number of Rows:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()

# Number Pyramed
n=int(input("Enter the number of Rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# Inverted Number Pyramed
n= int(input("Enter the Number of Rows:"))

for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

