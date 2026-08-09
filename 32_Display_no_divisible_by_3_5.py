#  Write a program to display all numbers from 1 to n that are divisible by 3 or 5.

n = int(input("Enter the value of n: "))

for i in range(1,n+1):
    if(i % 3 == 0 or i % 5 == 0):
        print(i)