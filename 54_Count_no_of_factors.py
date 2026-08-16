#  Write a program to count the number of factors of a number n.
n = int(input("Enter the value of n: "))

count = 0

for i in range(1,n+1):
    if n % i == 0:
        count += 1

print(count)