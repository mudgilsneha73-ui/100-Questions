#  Write a program to find the sum of the first and last digit of a number n

n = int(input("Enter the value of n: "))
original = n

last_digit = n % 10
while n >= 10:
    n = n // 10

first_digit = n

print("sum = ",first_digit + last_digit)
