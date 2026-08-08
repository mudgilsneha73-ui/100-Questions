#  Write a program to find the product of all natural numbers from 1 to n (factorial of n).

n = int(input("Enter the value of n "))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(f"factorial = {fact}")
