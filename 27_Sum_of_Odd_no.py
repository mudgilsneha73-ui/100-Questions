#  Write a program to find the sum of all odd numbers from 1 to n.

n = int(input("Enter the valur of n: "))
total = 0
for i in range(1,n+1,2):
    total += i
print(f"Total = {total}")