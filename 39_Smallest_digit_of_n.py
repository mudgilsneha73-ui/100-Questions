# Write a program to find the smallest digit in a number n

n = int(input("Enter the value of n: "))
smallest = 9

while n != 0:

    digit = n % 10

    if digit < smallest:
        smallest = digit

    n = n // 10
    
print(f"Smallest digit = {smallest}")
