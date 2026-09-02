#  Write a program to check whether a number is an automorphic number.
 
n= int(input("Enter the value of n: "))

original = n
n = n * n
count = 0

temp = original

while temp != 0:
    count += 1 
    temp = temp // 10

power  = 10 ** count

if n % power == original:
    print("Automorphic number ")
else:
    print("Not Automorphic number")                                