#  Write a program to check whether a number n is a palindrome (reads the same reversed).

n = int(input("Enter the value of n: "))

while n != 0:
    digit = n % 10
    n = n // 10
if n == digit:
        print("palindrome")
else:
        print("not")    

