# 12. Write a program to read a number and check whether it is positive, negative or zero.

n = int(input("Enter the Number : "))

if(n == 0):
    print(f"{n} = Zero")
elif(n > 0):
    print(f"{n} is Positive")
else:
    print(f"{n} is Negative")