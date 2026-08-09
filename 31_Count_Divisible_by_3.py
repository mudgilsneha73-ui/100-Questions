#  Write a program to count how many numbers from 1 to n are divisible by 3
n = int(input("Enter the value of n: "))
count = 0
for i in range(1,n+1):
    if(i % 3 == 0):
        count = count + 1
print(count)