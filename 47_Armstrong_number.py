# Write a program to check whether a number is an Armstrong number.

n = int(input("Enter the value of n: "))

original = n
count = 0

# Count the number of digits
while n != 0:
    digit = n % 10
    count += 1
    n = n // 10

# Use a copy because n is now 0
temp = original
total = 0

# Calculate sum of each digit raised to count.
while temp != 0:
    digit = temp % 10
    total += digit ** count
    temp = temp // 10

# Compare the sum with original number
if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

