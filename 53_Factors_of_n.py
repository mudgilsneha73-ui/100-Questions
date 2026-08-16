#  Write a program to find all factors (divisors) of a number n.
n = int(input("Enter the value of n: "))

for i in range(1 ,n + 1):
    if n % i == 0:
        print(f"Factors of {n} = {i} ")