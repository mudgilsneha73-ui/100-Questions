# Write a program to find the value of x raised to the power y without using inbuilt power.

m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

power = 1

for i in range(1, n+1):
    power  *= m

print(power)
