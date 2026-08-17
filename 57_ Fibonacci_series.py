#  Write a program to display the first n terms of the Fibonacci series.

n = int(input("Enter the value of n: "))

sum = 0
first_number = 0
second_number = 1
for i in range(1, n+1):
    sum = first_number + second_number
    first_number = second_number
    second_number = sum
    print(sum)

