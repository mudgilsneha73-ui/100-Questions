# Write a program to check whether a number is a perfect number. 

n = int(input("Enter the value of n: "))

original = n
factor = 0


for i in range(1,n):
    
    if n % i == 0:
        factor += i

if(factor == original):
    print(f"{original} is a Perfect Number.")

else:
    print(f"{original} is not a Perfect number.")