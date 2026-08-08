#  Write a program to find the sum of all even numbers from 1 to n

n = int(input("Enter th vaue of n:"))
sum = 0
for i in range(2,n+1,2):
    sum += i
print(sum)
