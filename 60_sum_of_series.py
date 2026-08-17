# Write a program to find the sum of the series 1^2 + 2^2 + 3^2 + ... + n^2 

n = int(input("Enter the Range: "))

total_sum = 0

for i in range(1, n+1):
    total_sum += i ** 2

print(total_sum)