# Write a program to replace all zeros in a number n with the digit 5

n = int(input("Enter the value of n: "))

original = n
new_number = 0

while n != 0:
    digit = n % 10
 
    if digit == 0:
        digit = 5

    new_number = new_number * 10 + digit
    n = n // 10

# Reverse again because digits were processed from right to left.
result = 0

while new_number != 0:
    digit = new_number % 10
    result = result * 10 + digit
    new_number = new_number // 10

print(result)