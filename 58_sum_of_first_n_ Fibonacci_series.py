# Write a program to find the sum of the first n terms of the Fibonacci series.
n = int(input("Enter the Range: "))

nexg = 0
first_number = 0
second_number = 1
total = 0

for i in range(1, n+1):
    total += first_number
    next = first_number + second_number
    first_number = second_number
    second_number = next
   

print(total)
