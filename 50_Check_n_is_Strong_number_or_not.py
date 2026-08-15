# Write a program to check whether a number is a strong number.

n = int(input("Enter the value of n: "))

original = n
total = 0

while n != 0:
    digit = n % 10

    factorial = 1

    for i in range(1, digit + 1):
        factorial = factorial * i

    total += factorial
    n = n // 10

if total == original:
    print(f"{original} is a Strong Number.")
else:
    print(f"{original} is not a Strong Number.")