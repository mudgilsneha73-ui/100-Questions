#  Write a program to check whether a number n is a palindrome (reads the same reversed).

n = int(input("Enter the value of n: "))

original = n
reverse = 0 

while n != 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("Palindrome")

else:
    print("Not Palindrome")