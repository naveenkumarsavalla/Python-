# # Number Pyramed
# n=int(input("Enter the number of Rows:"))
# def print_number_pattern():
#     num = 1
#     spaces = 10
#     for i in range(10):
#         print(" " * spaces, end="")
#         for j in range(i + 1):
#             print(num, end=" ")
#             num += 1
#         print()
#         spaces -= 1
# print_number_pattern()

# # Prime Number Pyramid
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def generate_prime_triangle(rows):
#     current_number = 1
#     for i in range(1, rows + 1):
#         for j in range(1, i + 1):
#             while not is_prime(current_number):
#                 current_number += 1
#             print(current_number, end=" ")
#             current_number += 1
#         print()
# generate_prime_triangle(5)

# # fibonocii
# n=int(input("Enter the Number of Rows:"))
# def fibonocii(n):
#     if n<=1:
#         return n
#     else:
#         return fibonocii(n-1)+fibonocii(n-2)
# for i in range(1,n+1):
#     print(fibonocii(i))

# fib_recursive
n=int(input("Enter the Number of Values:"))
lst=[]
def fib_recursive(n, a, b, i):
   if i<=n:
     lst.append(b)
     a = a + b
     b = a - b
     i += 1
     fib_recursive(n, a, b, i )
   else:
       print(lst)
fib_recursive(a=1, b=0, i=1)
