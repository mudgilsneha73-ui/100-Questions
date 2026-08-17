#  Write a program to find the GCD (HCF) of two numbers.

m = int(input("Enter the First number: "))
n = int(input("Enter the Second number: "))

factor = 0
for i in range(1,m+1):
    if m % i == 0:
        factor_m = i
    if n % i == 0:  
        factor_n = i

        if factor_n == factor_m:
           if factor_m > factor:
               factor =  factor_m

print(factor)
