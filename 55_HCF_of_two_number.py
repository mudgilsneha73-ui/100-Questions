#  Write a program to find the GCD (HCF) of two numbers.

m = int(input("Enter the First number: "))
n = int(input("Enter the Second number: "))

factor = 0
for i in range(1,m+1):
    if m % i == 0 and n % i == 0:  
         if i > factor:
            factor = i 
print(factor)
