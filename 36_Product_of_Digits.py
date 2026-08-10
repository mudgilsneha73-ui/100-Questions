# Write a program to find the product of all digits of a number n

n = int(input("Enter the vale of n: "))
product_digits = 1
while n != 0:
    digits = n % 10 
    product_digits *= digits
    n = n // 10

print(f"Product = {product_digits}")

