# Write a program to find the sum of the series 1 + 1/2 + 1/3 + ... + 1/n 

n = int(input("Enter the Range: "))

total_sum = 0

for i in range(1, n+1):
    total_sum += 1/i 
print(total_sum)