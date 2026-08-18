# Write a program to find the sum of the series 1 + 2 + 3 + ... + n

n = int(input("Enter the Range: "))

total_sum = 0 

for i in range(1, n+1):
    total_sum  += i
print(total_sum)