#  Write a program to find the sum of all natural numbers from 1 to n
n = int(input("Enter the value os n: "))

sum = 0
for i in range(1 , n+1):
    sum = sum + i
print(f"Sum = {sum}")