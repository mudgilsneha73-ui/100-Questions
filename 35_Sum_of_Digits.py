# Write a program to find the sum of all digits of a number n.

n = int(input("Enter the value of n: "))

sum_digits = 0

while n != 0:
    digit = n % 10
    sum_digits += digit
    n = n // 10
    
print("Sum of digits = ", sum_digits)