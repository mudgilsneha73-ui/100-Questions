#  Write a program to display all multiples of a number m up to n terms
n= int(input("Enter the value of n: "))
m= int(input("Enter the value of m: "))


for i in range(1 ,n+1):
    print(m * i)

