# Write a program to read two numbers and print their sum, difference, product and quotient.

a = int(input("Enter the first number : "))
b = int(input("Enter the Second number : "))

sum = a + b
difference  = a - b
product = a * b
quotient = a / b

print(f" {a} + {b} = {sum}")
print(f" {a} - {b} = {difference}")
print(f" {a} * {b} = {product}")
print(f" {a} / {b} = {quotient}")